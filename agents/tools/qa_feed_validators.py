#!/usr/bin/env python3
"""
qa_feed_validators — standing assertion 24: a polling reader can revalidate the
feeds cheaply, and the origin serves ONE set of bytes under however many
validators it happens to mint.

WHY (Manager, 2026-09-24 — the 09-23 deploy went red and the check was wrong)
-----------------------------------------------------------------------------
The `verify` job has carried an inline step, "Feed cache validators work for a
polling reader", since the feeds shipped. It does this:

    HEAD  /madar/ar/rss.xml            -> read the ETag
    GET   /madar/ar/rss.xml  If-None-Match: <that ETag>
    assert the status is 304

On 2026-09-23 it returned 200 and failed the deploy. The byte-compare in the
same job had already passed on all five files: the origin was serving exactly
the artefact we built. Nothing was wrong with the publication.

WHAT IS ACTUALLY HAPPENING. GitHub Pages serves from Fastly over anycast, and
the Pages origin unpacks each deploy onto more than one replica. nginx mints
`ETag: "<hex-mtime>-<hex-size>"`. The replicas unpacked the 09-23 artefact one
second apart, so the same URL has two permanent validators:

    "6ab3a42c-920e"   and   "6ab3a42d-920e"
     ^^^^^^^^ mtime         ^^^^^^^^ mtime+1s
              ^^^^ size               ^^^^ identical size

The two requests the step makes are independent, so they land on independently
chosen edges. When the conditional GET reaches an edge holding the OTHER
replica's validator, that edge has never seen the ETag it was handed, and a 200
with the full body is the only correct answer it can give. The step reads that
as "validator not honored".

This was measured, not inferred — 12 probe pairs on 2026-09-24, ~23 hours after
the deploy, every one of them unambiguous:

    every 304: the response's own ETag == the ETag sent
    every 200: the response's own ETag != the ETag sent, differing ONLY in the
               mtime limb, never in the size limb

The origin never once refused a validator it actually held. And because the two
mtimes were still being served a day later, this is not propagation settling —
it is a permanent two-valued validator, which makes the old step a coin flip on
every deploy, forever. It passed on 09-21 and 09-22 by luck.

THE FIX, AND WHY IT IS THE HONEST INSTRUMENT RATHER THAN A TOLERANCE. The first
draft of this check kept the two independent requests and merely forgave the
mismatch: read the ETag off the 200, and call it a defect only when the returned
ETag equals the one sent (the edge held the validator and refused it anyway).
That discriminator is sound and is kept below as A3. But it made A4 — "at least
one probe revalidated" — a 1-in-64 coin flip on six probes, which is a smaller
flake, not the absence of one. Proving the bite exposed it: the fanout control
FAILED on first run.

The real instrument was in the question itself. A polling reader does not open a
new connection for every request; it keeps one. And a TCP connection terminates
at exactly ONE Fastly edge, which holds exactly ONE replica's validator. So do
what the reader does: open one connection, GET, read the ETag, and revalidate
ON THE SAME CONNECTION. Measured against the live origin on 2026-09-24, three
trials, two different validators across them:

    trial0  etag "6ab3a42d-920e"  node kpao1770082-PAO  conditional GET -> 304
    trial1  etag "6ab3a42c-920e"  node sjc1000110-SJC   conditional GET -> 304
    trial2  etag "6ab3a42d-920e"  node kpao1770071-PAO  conditional GET -> 304

Deterministic, and it makes the assertion strictly STRONGER than the step it
replaces: every in-connection revalidation must be 304, not merely one of them.
The fanout is still visible across connections, where it belongs — as reported
colour, and as the input to A2.

And that is the second thing asking bought. If an origin can serve two validators
for one URL, the question nobody had asked is whether it also serves two BODIES —
a far worse defect than the one that went red, and one the old step could not
have seen, because it never fetched a body. So this check fetches the body on
every probe and hashes it: many validators are tolerated, many bodies are not.
That axis has never been asserted by anything we own.

Ruling #63 (`agents/guidebook/2026-09-24-a-validator-is-not-the-content.md`):
an identifier minted by the server that stores a file is a property of the
STORAGE, not of the file. Same family as #57 (equal counts are not an agreement)
and #60 (a date is not a moment) — three ways of saying that two things printing
different strings are not thereby different things.

WHAT THIS CHECKS (each probe is one keep-alive connection: GET, then
revalidate on that same connection)
  A1  every GET carries both an ETag and a Last-Modified
  A2  every response body for a URL is byte-identical (hash equality), however
      many distinct validators the origin mints for it       <- the new axis
  A3  no revalidation returns 200 while carrying back the SAME ETag it was
      handed — that, and only that, is "validator ignored"
  A4  EVERY in-connection revalidation is honored with a 304

WHY THIS IS NOT GATED ON THE DEPLOY. It reads the ORIGIN, so it joins
`qa_live_drift` (the verify job's byte-compare is strictly stronger) and
`qa_sources_alive` (someone else's 404 is not our build's failure) as the third
assertion that does not gate, with its reason stated — per the 2026-09-13 rule
that an unwired assertion carries its reason at the point the others are listed.
The gate it belongs in is the `verify` job's inline step, and the patch for that
step is written and staged at `agents/tools/patches/` — it cannot be pushed by
this identity, which is refused write access to `.github/workflows/**`
(issue #7, and the probe was re-run today and still refused).

PROVED BOTH WAYS, per ruling #35, against a local origin that assigns a replica
PER CONNECTION, the way Fastly does — and the fanout control is the one that
matters, because it is the real 09-23 condition and the check MUST stay silent
on it:
  CONTROL  honest origin, one validator, honors If-None-Match       -> exit 0
  CONTROL  FANOUT: two validators, identical bodies (the real 09-23)-> exit 0
  CONTROL  the live origin itself                                   -> exit 0
  BITE     validator ignored: 200 carrying back the SAME ETag       -> exit 1
  BITE     two validators AND two DIFFERENT BODIES                  -> exit 1
  BITE     no ETag header at all                                    -> exit 1
  BITE     never honored: a fresh validator on every response       -> exit 1

The fanout control failed on its first run and the failure was real — see THE FIX
above. A bite that fails to bite reads like a pass; a control that fails is the
cheaper half of the same lesson, and this one rewrote the check.

Exit codes: 0 pass · 1 assertion failed · 2 could not read the origin
"""

import argparse
import hashlib
import http.client
import ssl
import sys
import urllib.parse

BASE = "https://education3881.github.io/madar"
FEEDS = ["rss.xml", "ar/rss.xml"]
UA = "madar-qa-feed-validators/1.0 (+https://education3881.github.io/madar)"


def connect(base):
    """A single keep-alive connection — which pins exactly one edge, and so
    exactly one replica's validator. This is what a polling reader holds."""
    u = urllib.parse.urlsplit(base)
    if u.scheme == "https":
        return http.client.HTTPSConnection(
            u.netloc, timeout=30, context=ssl.create_default_context()
        )
    return http.client.HTTPConnection(u.netloc, timeout=30)


def one_probe(base, feed):
    """GET then revalidate ON THE SAME CONNECTION. Returns one observation."""
    path = urllib.parse.urlsplit(base).path.rstrip("/") + "/" + feed
    conn = connect(base)
    try:
        conn.request("GET", path, headers={"User-Agent": UA})
        r = conn.getresponse()
        body = r.read()
        if r.status != 200:
            return {"error": f"GET returned {r.status}"}
        row = {
            "etag": r.getheader("ETag"),
            "last_modified": r.getheader("Last-Modified"),
            "sha256": hashlib.sha256(body).hexdigest(),
            "bytes": len(body),
            "served_by": (r.getheader("X-Served-By") or "?").split(",")[-1].strip(),
        }
        if row["etag"]:
            conn.request(
                "GET", path, headers={"User-Agent": UA, "If-None-Match": row["etag"]}
            )
            r2 = conn.getresponse()
            r2.read()
            row["cond_status"] = r2.status
            row["cond_etag"] = r2.getheader("ETag")
        return row
    finally:
        conn.close()


def probe(base, feed, attempts):
    """One feed, N independent connections. Returns observations."""
    return f"{base}/{feed}", [one_probe(base, feed) for _ in range(attempts)]


def check_feed(feed, url, obs, out):
    """Apply A1-A4 to one feed's observations. Returns a list of failure strings."""
    fails = []
    errs = [o["error"] for o in obs if "error" in o]
    if errs:
        fails.append(f"{feed}: origin unreadable — {errs[0]}")
        return fails
    if not obs:
        fails.append(f"{feed}: no observations")
        return fails

    # A1 — validators are present at all.
    if any(not o["etag"] for o in obs):
        fails.append(f"{feed}: serves no ETag — readers cannot poll cheaply")
    if any(not o["last_modified"] for o in obs):
        fails.append(f"{feed}: serves no Last-Modified")

    # A2 — many validators are tolerated; many bodies are not.
    hashes = {o["sha256"] for o in obs}
    etags = {o["etag"] for o in obs if o["etag"]}
    if len(hashes) > 1:
        sizes = sorted({o["bytes"] for o in obs})
        fails.append(
            f"{feed}: the origin serves {len(hashes)} DIFFERENT BODIES for one URL "
            f"(sizes {sizes}) — replicas are out of step, not merely out of clock"
        )

    # A3 — the discriminator, kept as the precise name for the real defect.
    for o in obs:
        if o.get("cond_status") == 200 and o.get("cond_etag") == o["etag"]:
            fails.append(
                f"{feed}: revalidation returned 200 carrying back the SAME ETag "
                f"{o['etag']} it was handed — validator ignored"
            )
            break

    # A4 — every in-connection revalidation must be honored. Same edge, same
    # validator: a 200 here has no innocent explanation.
    honored = [o for o in obs if o.get("cond_status") == 304]
    if len(honored) != len(obs):
        fails.append(
            f"{feed}: {len(obs) - len(honored)} of {len(obs)} in-connection "
            f"revalidations were not honored with a 304"
        )

    pops = {o["served_by"] for o in obs}
    out.append(
        f"  {feed}: {len(obs)} connections · {len(etags)} distinct validator(s) "
        f"across {len(pops)} edge(s) · {len(hashes)} "
        f"{'body' if len(hashes) == 1 else 'bodies'} ({obs[0]['bytes']} bytes) · "
        f"{len(honored)}/{len(obs)} revalidated 304"
    )
    for e in sorted(etags):
        out.append(f"      ETag {e}")
    return fails


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--base", default=BASE, help="origin base URL")
    ap.add_argument("--attempts", type=int, default=6, help="probe pairs per feed")
    ap.add_argument("--feeds", nargs="*", default=FEEDS)
    args = ap.parse_args()

    print(f"qa_feed_validators — {args.base}")
    fails, out = [], []
    for feed in args.feeds:
        try:
            url, obs = probe(args.base, feed, args.attempts)
        except Exception as exc:  # noqa: BLE001 — an unreadable origin is exit 2
            print(f"COULD NOT READ: {feed}: {exc}")
            return 2
        fails += check_feed(feed, url, obs, out)
    print("\n".join(out))

    if fails:
        print(f"\nFAIL — {len(fails)} assertion(s):")
        for f in fails:
            print(f"  - {f}")
        return 1
    print("\nPASS — feeds revalidate, and every validator names the same bytes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
