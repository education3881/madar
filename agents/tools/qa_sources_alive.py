#!/usr/bin/env python3
"""
qa_sources_alive — do the outbound promises still resolve?

WHY THIS EXISTS (Growth, 2026-09-10; carried from the 2026-09-06 forward list)
-----------------------------------------------------------------------------
Ten standing assertions guard this site and every one of them checks that a
link is *rendered*. `qa_body_links` (#10) proves each `sources[].url` an
article declares is actually emitted as an anchor on its built page. None of
them — not one — checks that the thing at the other end still answers.

That gap sits directly on top of this publication's only differentiating
claim. Madar's entire argument for being worth returning to is that every
figure stands on a named primary source the reader can open. A rotted source
link does not degrade the piece a little; it converts the piece's central
promise into a 404 in front of the exact reader who cared enough to click.
This is a RETURN-RATE instrument, not a traffic one: the reader who follows a
source is the reader who was going to come back.

It is also the check with the shortest shelf life. The Sudan recon (08-31)
found **two of seven registers changed serving state in eighteen days** — one
walled, one unreachable — with zero figures going false. Serving state drifts
faster than facts do, and always in the direction the reader experiences.

DESIGN — deliberately NOT a deploy gate
---------------------------------------
1. **Never blocks a build.** The far side of these links belongs to UNESCO,
   UNICEF, ministries and journals. A GPE outage at 09:00 must not stop us
   publishing. Run weekly, read the report, act editorially.
2. **Sampled, not exhaustive** (`--sample`). ~570 promises against institutional
   hosts is a rude amount of traffic to send on a schedule.
3. **#20 applies: never declare rot on one read.** Anything that fails is
   re-fetched once, GET after HEAD, before it is reported — and even then it is
   reported as *what we received*, never as "dead". A 403 from a bot wall is
   not a dead source; it is a source we cannot see, which is a different fact
   and gets a different bucket (#38's habit: name the disagreement).
4. **Held pieces included, and flagged separately.** The Edition 05 pairs are
   held; their sources are exactly the ones worth checking BEFORE the wave
   flips, when a fix is still free.
5. **Silent pass is a failure** (08-16 trap). Zero URLs found to check exits
   non-zero.

Exit codes: 0 = ran and reported (whatever it found). 2 = the sweep itself is
broken (no URLs, unreadable content). It never exits non-zero for a dead link;
that is an editorial finding, not a build defect.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import queue
import random
import re
import socket
import ssl
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone

CONTENT_DIRS = ("web/src/content/articles", "web/src/content/articles-ar")
UA = "Mozilla/5.0 (compatible; MadarSourceCheck/1.0; +https://education3881.github.io/madar/)"
TIMEOUT = 20

# ---- THE TOTAL CEILING (--budget), added 2026-10-05, standing-queue item 1 ----
# Eighteen days open, displaced three times, and the only queue item that blocks
# the Edition 05 flip. The ask was never "make it faster"; it was **make it
# schedulable** — the ledger names the full held sweep as the last step before
# the flip commit, and a step whose duration cannot be stated cannot be placed
# in a sequence.
#
# What was actually unbounded, measured rather than asserted (2026-10-05): a
# per-URL TIMEOUT and flush=True were both present, and neither bounds the
# SWEEP. 59 held-cited URLs x HEAD+GET, with the TLS path adding a second
# HEAD+GET inside _still_served, is 4 x 20s x 59 = **79 minutes** of socket
# budget. And 79 minutes is itself the optimistic reading: `timeout=` on a
# urllib request is a *per-socket-operation* deadline, not a per-request one, so
# a host dribbling one byte every 19 seconds holds the connection open forever
# and the true worst case is **unbounded**. That is the 2026-09-16 P1's own
# shape — a sweep that ran 40 minutes and was filed as having no output — with
# the reporting half fixed and the scheduling half untouched.
#
# The ceiling is enforced in the MAIN THREAD against a monotonic deadline, with
# the probe loop on a daemon worker. This matters and is the whole design: a
# clock checked *between* URLs can only ever bound the loop, never the request
# in flight, so it inherits exactly the unboundedness it was added to remove.
# The main thread owns the deadline, the worker owns the socket, and a daemon
# thread does not hold interpreter exit — so a wedged read is abandoned rather
# than waited on. The ceiling is therefore a real wall-clock bound, not an
# intention.
#
# Three properties kept deliberately:
#   * **Still sequential.** One worker, same order, same traffic profile. Going
#     parallel would make it fast AND rude, and sending 59 concurrent requests
#     at UNESCO is a different decision from bounding our own run.
#   * **Truncation is LOUD.** Unreached URLs land in their own `unchecked`
#     bucket and are named individually. A partial sweep that reads like a
#     complete one is the 08-16 silent-pass trap with a clock attached — and it
#     would fail in the one direction that matters, by reporting a held source
#     as fine when it was never opened.
#   * **Default 0 = unbounded**, so every existing invocation behaves exactly as
#     it did yesterday. The ceiling is opt-in; what the flip gains is the
#     ability to ASK for one.
_DEADLINE: float | None = None


def _budget_left() -> float:
    """Seconds until the sweep must be done. inf when no ceiling was asked for."""
    if _DEADLINE is None:
        return float("inf")
    return _DEADLINE - time.monotonic()


def _attempt_timeout() -> float:
    """Clamp a single socket attempt to what is left of the total budget.

    Without this the worker can spend the entire tail of the budget inside one
    20s read and return nothing, so the last URLs are unchecked for no reason
    other than arithmetic. The 0.5s floor keeps a nearly-expired budget from
    issuing requests that cannot possibly complete.
    """
    left = _budget_left()
    if left == float("inf"):
        return float(TIMEOUT)
    return max(0.5, min(float(TIMEOUT), left))

URL_RE = re.compile(r'^\s+url:\s*"([^"]+)"\s*$', re.M)
APPROVED_RE = re.compile(r"^approved:\s*(true|false)\s*$", re.M)


def frontmatter(text: str) -> str:
    """The frontmatter BLOCK — the opening fence to the first fence that starts a LINE.

    This line read `text.split("---", 2)[1]` from this file's first commit
    (2026-09-10) until 2026-10-03, and it was wrong in the way ruling #81 is
    wrong: it stopped early and it stopped earliest on the most heavily
    annotated pieces. `---` is not a delimiter in this corpus, it is a
    SUBSTRING — one source URL contains it
    (`...schooljaar-2025---2026-vastgesteld`), so the split cut that pair's
    frontmatter at 3,182 of 4,646 characters, mid-URL, and the sweep then
    collected 678 of the corpus's 684 source promises. **The URL that broke the
    parser was the first of the three it stopped checking.** Measured, not
    reasoned: the three lost per language were the ministry newsletter that
    contains the hyphens, the PO-Raad 2030 page and the Tweede Kamer motion.

    A fence is a line. Matching it as one costs nothing and is the only reading
    that is true of YAML. (#81's family, third mechanism in three days: a
    bounded read on 10-01, a naive split in a scratch script on 10-02, and this
    — the same split, shipped, in the one content-reading tool that neither
    gates the build nor is read by qa_census.)
    """
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    return text[3:end if end != -1 else len(text)]


def collect(root: str) -> dict[str, dict]:
    """slug+lang -> {url: [(slug, held)]}; returns url -> list of citing pieces."""
    by_url: dict[str, list[tuple[str, bool]]] = {}
    for d in CONTENT_DIRS:
        path = os.path.join(root, d)
        for f in sorted(glob.glob(os.path.join(path, "*.md"))):
            text = open(f, encoding="utf-8").read()
            head = frontmatter(text)
            m = APPROVED_RE.search(head)
            # content.config.ts: `approved` is z.boolean().default(false), so an
            # ABSENT flag is HELD. This read `bool(m and ...)` — absent meant
            # NOT held, the opposite of the schema and of qa_census, which
            # mirrors it. Latent today because every one of the 88 files carries
            # the key; it stops being latent the moment a parser cannot reach
            # it, which is exactly the bug above. A held piece whose
            # frontmatter contains `---` would have been classified approved and
            # dropped from `--held-only` — the mode the Edition 05 ledger names
            # as the LAST step before the flip commit.
            held = (m.group(1) == "false") if m else True
            slug = os.path.basename(f)[:-3]
            lang = "ar" if d.endswith("-ar") else "en"
            for url in URL_RE.findall(head):
                by_url.setdefault(url, []).append((f"{slug} [{lang}]", held))
    return by_url


def _to_uri(url: str) -> str:
    """IRI -> URI. A non-ASCII URL cannot be put on the wire as written.

    Found 2026-10-05 by the FIRST complete sweep of the corpus (343 URLs), which
    the total ceiling of ruling #88 is what made affordable. Two URLs came back
    `unreachable · UnicodeEncodeError` — and that is not a fact about either
    host. `urllib` must hand the request line to a socket as ASCII, so a path
    containing Arabic raises before a single byte is sent. **Both documents are
    served**: percent-encoded, `mehe.gov.lb` answers HEAD 200 and `almodon.com`
    answers GET 200.

    **This is ruling #80 with a new mechanism, and a worse property.** #80 was
    *the certificate is fine and only Python sees a problem*; this is *the URL is
    fine and only Python cannot write it down*. In both, *the tool's own
    limitation was reported as a fact about the source* — and here it would have
    been reported in the one register that matters, since `qa_sources_alive`'s
    findings are editorial advice about whether a citation still stands.

    The worse property: **the blindness is language-correlated.** Both of the
    corpus's two non-ASCII URLs are **Arabic-language registers**, and both were
    mis-reported — 2 of 2, 100%. A source-health instrument that fails precisely
    on Arabic paths is not randomly wrong; it is systematically blind to the
    registers one of our two editions is built on, which for a publication whose
    Arabic is *composed from the sources* rather than translated is the single
    worst place for an instrument to be blind.

    No new ruling number was minted for this. It is a **second instance of #80**,
    recorded as evidence in that ruling's file, because the operation does not
    number a lesson twice for arriving by a different road.
    """
    try:
        url.encode("ascii")
        return url
    except UnicodeEncodeError:
        sp = urllib.parse.urlsplit(url)
        host = sp.netloc
        if any(ord(c) > 127 for c in host):
            try:
                host = host.encode("idna").decode("ascii")
            except Exception:  # noqa: BLE001 - malformed host, leave it to fail honestly
                host = urllib.parse.quote(host, safe=":@")
        # safe includes '%' so an already-percent-encoded segment is not
        # double-encoded into '%25..' — mixed raw/encoded paths are real.
        safe = "/%:@!$&'()*+,;=~"
        return urllib.parse.urlunsplit((
            sp.scheme, host,
            urllib.parse.quote(sp.path, safe=safe),
            urllib.parse.quote(sp.query, safe=safe + "?"),
            sp.fragment,
        ))


def _root_cause(exc: BaseException) -> BaseException:
    """Walk to the innermost reason. URLError wraps the thing that actually failed."""
    seen = set()
    cur = exc
    while True:
        nxt = getattr(cur, "reason", None)
        if not isinstance(nxt, BaseException) or id(nxt) in seen:
            return cur
        seen.add(id(cur))
        cur = nxt


def _still_served(url: str) -> str:
    """For a TLS failure only: does the DOCUMENT still exist behind the bad certificate?

    This is the whole point of the `tls` bucket. A browser shows an interstitial
    and a determined reader clicks through to a live document; a dead host has
    nothing behind it. Those are opposite editorial dispositions and the old
    code printed the same string for both.
    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    for method in ("HEAD", "GET"):
        if _budget_left() <= 0:
            return " · not probed further (sweep budget exhausted)"
        try:
            req = urllib.request.Request(_to_uri(url), method=method,
                                         headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=_attempt_timeout(), context=ctx) as r:
                if 200 <= r.status < 300:
                    return f" · document still served ({r.status})"
        except urllib.error.HTTPError as e:
            if method == "GET":
                return f" · behind it: HTTP {e.code}"
        except Exception:  # noqa: BLE001
            continue
    return " · and nothing served behind it"


def classify(exc: BaseException, url: str, tmo: float | None = None) -> tuple[str, str]:
    """Name the LAYER that failed, not merely that something did.

    Added 2026-09-27, against a live defect rather than an injected one: the
    certificate for `mineduc.gov.rw` expired on 2026-09-23 while the ministry
    went on serving every document. The old code reported that, and a hostname
    that does not resolve at all, as the identical string `unreachable ·
    URLError` — so the sweep ran, stayed green-lit, and its own output could not
    carry the one fact the editorial decision turns on. A bucket set is an
    enumeration like any other, and a check cannot report a distinction its
    buckets cannot hold.
    """
    root = _root_cause(exc)
    if isinstance(root, ssl.SSLCertVerificationError):
        why = (root.verify_message or "certificate rejected").strip()
        # A verification failure is not one failure mode, and the two it
        # usually is are opposite facts about the READER (added 2026-10-01,
        # ruling #80, against a live defect in this tool's own advice).
        #
        #   * The certificate is bad — expired, wrong hostname, self-signed.
        #     Every mainstream browser shows a full-page interstitial.
        #   * The certificate is FINE and the host simply does not send the
        #     issuing intermediate, publishing it instead at the CA Issuers
        #     address printed inside the leaf. Clients that follow that
        #     address — Chrome, Edge, Safari — complete the chain and show the
        #     reader nothing at all. Python, curl and openssl(1) do not, so
        #     this sweep fails where a reader succeeds.
        #
        # Measured on 2026-10-01 against the four `parliament.gov.zm` URLs in
        # the held Zambia pair, which this bucket had reported for three weeks
        # as unreachable, then refused, then "invalid certificate": the host
        # sends exactly one certificate; that certificate is valid 26 May 2026
        # to 10 December 2026; and `openssl verify -untrusted <AIA cert> leaf`
        # returns OK once the intermediate is fetched from the address the leaf
        # itself names. The document, the certificate and the reader were all
        # fine. Only this tool was not.
        chain_only = ("unable to get local issuer certificate" in why
                      or "unable to verify the first certificate" in why)
        return ("tls-chain" if chain_only else "tls",
                f"cert: {why}{_still_served(url)}")
    if isinstance(root, ssl.SSLError):
        return "tls", f"tls: {root.reason or type(root).__name__}{_still_served(url)}"
    if isinstance(root, socket.gaierror):
        return "dns", "name does not resolve"
    if isinstance(root, ConnectionRefusedError):
        return "refused", "connection refused at :443"
    if isinstance(root, ConnectionResetError):
        return "refused", "connection reset"
    if isinstance(root, (TimeoutError, socket.timeout)):
        # Report the timeout that ACTUALLY applied, not the module default. Under
        # a total ceiling the last attempts are clamped to whatever is left, and
        # printing "no response in 20s" for a read that was given 2.4s would be
        # this tool telling an editorial decision something false about a source.
        waited = TIMEOUT if tmo is None else tmo
        return "timeout", f"no response in {waited:g}s"
    return "unreachable", type(root).__name__


def probe(url: str) -> tuple[str, str]:
    """Return (bucket, detail). #20: HEAD, then GET on anything not clean."""
    def attempt(method: str, tmo: float):
        req = urllib.request.Request(_to_uri(url), method=method, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=tmo) as r:
            return r.status, r.geturl()

    tmo = float(TIMEOUT)
    for method in ("HEAD", "GET"):
        tmo = _attempt_timeout()
        try:
            status, final = attempt(method, tmo)
            if 200 <= status < 300:
                # Compare against the URI we actually SENT, not the IRI we hold.
                # Otherwise every non-ASCII URL reports a redirect to its own
                # percent-encoded self — a redirect that did not happen, printed
                # into a report whose readers act on it editorially.
                moved = "" if final.rstrip("/") == _to_uri(url).rstrip("/") else f" -> {final}"
                return "ok", f"{status}{moved}"
        except urllib.error.HTTPError as e:
            if method == "GET":
                # 401/403/429 from an institutional host is a wall we cannot see
                # through, NOT evidence the source is gone. Different bucket.
                bucket = "walled" if e.code in (401, 403, 429, 451) else "error"
                return bucket, f"HTTP {e.code}"
        except Exception as e:  # noqa: BLE001 - network reality is varied
            if method == "GET":
                return classify(e, url, tmo)
    return "error", "no response"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--sample", type=int, default=60, help="0 = every URL")
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--held-only", action="store_true")
    ap.add_argument("--json", dest="json_out", default=None)
    ap.add_argument("--collect-only", action="store_true",
                    help="parse the corpus, print the population, touch no "
                         "network. This is the half of this tool that is cheap, "
                         "deterministic and safe to gate (ruling #85).")
    ap.add_argument("--budget", type=float, default=0,
                    help="TOTAL wall-clock ceiling for the sweep, in seconds. "
                         "0 = unbounded (the default, and the behaviour of every "
                         "invocation before 2026-10-05). URLs not reached inside "
                         "the budget are reported as `unchecked` and named, never "
                         "silently dropped.")
    ap.add_argument("--require-complete", action="store_true",
                    help="exit 2 if the budget truncated the sweep. This is the "
                         "flag the wave flip uses: at the flip the question is "
                         "not 'what did we manage to read' but 'was the whole "
                         "held set read', and those must not share an exit code.")
    args = ap.parse_args()

    by_url = collect(args.root)
    if not by_url:
        print("qa_sources_alive: FAILED — found 0 source URLs. A sweep that finds "
              "nothing to check has failed, not passed.", file=sys.stderr)
        return 2

    total = len(by_url)

    # ---- the collection half, separable from the probing half (ruling #85) ----
    # This tool is correctly out of CI because PROBING third-party hosts must
    # never red our build. The exemption was granted to the whole tool, and so
    # its PARSER — which touches no network, costs milliseconds and reads the
    # same frontmatter five gating assertions read — went un-gated and
    # un-censused for 23 days, which is where ruling #81's family was living.
    # A tool exempted for the cost of its ACTION is not exempted for the cost
    # of its INPUT. qa_census reads this line.
    if args.collect_only:
        citations = sum(len(v) for v in by_url.values())
        held_urls = sum(1 for u in by_url if any(h for _, h in by_url[u]))
        files = sum(len(glob.glob(os.path.join(args.root, d, "*.md")))
                    for d in CONTENT_DIRS)
        print("qa_sources_alive: collect-only — %d citation(s), %d distinct URL(s), "
              "%d cited by a held piece, %d content file(s); no network touched."
              % (citations, total, held_urls, files))
        return 0
    urls = sorted(by_url)
    if args.held_only:
        urls = [u for u in urls if any(h for _, h in by_url[u])]
    pool = urls
    if args.sample and args.sample < len(pool):
        pool = random.Random(args.seed).sample(pool, args.sample)

    global _DEADLINE
    started = time.monotonic()
    if args.budget and args.budget > 0:
        _DEADLINE = started + args.budget

    print(f"qa_sources_alive — {total} distinct source URLs declared across the corpus; "
          f"checking {len(pool)}"
          + (" (held pieces only)" if args.held_only else "")
          + (f" · total ceiling {args.budget:g}s" if _DEADLINE else " · no ceiling")
          + f" · {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print()

    # The worker probes; the MAIN THREAD owns the clock. See the ceiling note at
    # the head of this file for why the deadline cannot live in the probe loop.
    done: "queue.Queue[tuple[str, str, str] | None]" = queue.Queue()

    def _sweep() -> None:
        for u in pool:
            if _budget_left() <= 0:
                break
            b, d = probe(u)
            done.put((u, b, d))
        done.put(None)

    threading.Thread(target=_sweep, daemon=True).start()

    buckets: Counter[str] = Counter()
    findings = []
    checked: list[str] = []
    while len(checked) < len(pool):
        left = _budget_left()
        if left <= 0:
            break
        try:
            item = done.get(timeout=None if left == float("inf") else left)
        except queue.Empty:
            break
        if item is None:
            break
        url, bucket, detail = item
        checked.append(url)
        buckets[bucket] += 1
        citing = by_url[url]
        held = any(h for _, h in citing)
        if bucket != "ok":
            findings.append({
                "url": url, "bucket": bucket, "detail": detail,
                "held": held, "cited_by": [s for s, _ in citing],
            })
        flag = "HELD" if held else "    "
        # flush=True because of the 2026-09-16 P1: this sweep ran 40 minutes with
        # "no output" and was filed as printing only at the end. It always printed
        # per URL. Redirected to a file, stdout is block-buffered, so nothing
        # reached the file until the process exited. The tool was observable; the
        # pipe was not. One keyword, and the step is watchable at the wave flip.
        print(f"  [{bucket:<11}] {flag} {detail:<44} {url[:96]}", flush=True)

    # Everything the budget did not reach. Named, bucketed and counted — a URL
    # we never opened must never be summarised alongside the ones that answered.
    unchecked = [u for u in pool if u not in set(checked)]
    for u in unchecked:
        citing = by_url[u]
        held = any(h for _, h in citing)
        buckets["unchecked"] += 1
        findings.append({
            "url": u, "bucket": "unchecked",
            "detail": "never opened — sweep budget exhausted",
            "held": held, "cited_by": [s for s, _ in citing],
        })
        print(f"  [{'unchecked':<11}] {'HELD' if held else '    '} "
              f"{'never opened — sweep budget exhausted':<44} {u[:96]}", flush=True)

    elapsed = time.monotonic() - started
    print()
    print("  " + " · ".join(f"{k}: {v}" for k, v in sorted(buckets.items())))
    print(f"  checked {len(checked)} of {len(pool)} in {elapsed:.1f}s"
          + (f" · ceiling {args.budget:g}s" if _DEADLINE else "")
          + (f" · TRUNCATED, {len(unchecked)} never opened" if unchecked else " · complete"))
    print()
    if findings:
        print("FINDINGS — none of these is a build defect; each is an editorial decision:")
        for f in findings:
            note = {
                "walled": "a wall, not a death — cite as fetched-on-date (#41), consider a first-party twin",
                "tls": "the CERTIFICATE is bad — expired, wrong hostname or self-signed — so "
                       "every mainstream browser shows a full-page interstitial and the "
                       "annotation says so as a dated observation (#76); if the document is "
                       "still served, the citation stands",
                "tls-chain": "the certificate is probably FINE and the host is not sending its "
                             "issuing intermediate. MEASURE BEFORE WRITING ANYTHING: fetch the "
                             "issuer from the CA Issuers address printed in the leaf and "
                             "re-verify. If the chain then completes, a browser that follows "
                             "that address — Chrome, Edge, Safari — meets NO warning, and an "
                             "annotation claiming an interstitial would be false. This sweep "
                             "fails here because Python does not chase AIA; the reader is not "
                             "Python (#80)",
                "dns": "the name itself is gone — supersede, don't resurrect (#41)",
                "refused": "a refusal is not a 404 (#54) — re-probe from a second client on a "
                           "different day before any disposition",
                "timeout": "one slow read is not a death (#20) — re-probe before any disposition",
                "unreachable": "re-read before the next flip; supersede, don't resurrect (#41)",
                "error": "re-read before the next flip",
                "unchecked": "NOT A FINDING ABOUT THE SOURCE — a finding about this "
                             "run. The budget ran out before this URL was opened, so "
                             "nothing is known about it either way. Raise --budget or "
                             "narrow the pool; do not read this as a pass",
            }.get(f["bucket"], "re-read before the next flip")
            print(f"  ✗ {f['bucket']} ({f['detail']}) {'[HELD PIECE]' if f['held'] else ''}")
            print(f"      {f['url']}")
            print(f"      cited by: {', '.join(f['cited_by'])}")
            print(f"      → {note}")
    else:
        print("Every sampled promise answered.")

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump({"checked": len(checked), "pool": len(pool), "total": total,
                       "elapsed_s": round(elapsed, 1),
                       "budget_s": args.budget or None,
                       "truncated": bool(unchecked),
                       "unchecked": unchecked,
                       "buckets": dict(buckets), "findings": findings}, fh, indent=2)

    if unchecked and args.require_complete:
        print(f"qa_sources_alive: FAILED — --require-complete was asked for and the "
              f"sweep was truncated at {len(checked)} of {len(pool)}. "
              f"{len(unchecked)} promise(s) were never opened.", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
