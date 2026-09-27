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
import random
import re
import socket
import ssl
import sys
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone

CONTENT_DIRS = ("web/src/content/articles", "web/src/content/articles-ar")
UA = "Mozilla/5.0 (compatible; MadarSourceCheck/1.0; +https://education3881.github.io/madar/)"
TIMEOUT = 20

URL_RE = re.compile(r'^\s+url:\s*"([^"]+)"\s*$', re.M)
APPROVED_RE = re.compile(r"^approved:\s*(true|false)\s*$", re.M)


def collect(root: str) -> dict[str, dict]:
    """slug+lang -> {url: [(slug, held)]}; returns url -> list of citing pieces."""
    by_url: dict[str, list[tuple[str, bool]]] = {}
    for d in CONTENT_DIRS:
        path = os.path.join(root, d)
        for f in sorted(glob.glob(os.path.join(path, "*.md"))):
            text = open(f, encoding="utf-8").read()
            head = text.split("---", 2)[1] if text.startswith("---") else text
            m = APPROVED_RE.search(head)
            held = bool(m and m.group(1) == "false")
            slug = os.path.basename(f)[:-3]
            lang = "ar" if d.endswith("-ar") else "en"
            for url in URL_RE.findall(head):
                by_url.setdefault(url, []).append((f"{slug} [{lang}]", held))
    return by_url


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
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as r:
                if 200 <= r.status < 300:
                    return f" · document still served ({r.status})"
        except urllib.error.HTTPError as e:
            if method == "GET":
                return f" · behind it: HTTP {e.code}"
        except Exception:  # noqa: BLE001
            continue
    return " · and nothing served behind it"


def classify(exc: BaseException, url: str) -> tuple[str, str]:
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
        return "tls", f"cert: {why}{_still_served(url)}"
    if isinstance(root, ssl.SSLError):
        return "tls", f"tls: {root.reason or type(root).__name__}{_still_served(url)}"
    if isinstance(root, socket.gaierror):
        return "dns", "name does not resolve"
    if isinstance(root, ConnectionRefusedError):
        return "refused", "connection refused at :443"
    if isinstance(root, ConnectionResetError):
        return "refused", "connection reset"
    if isinstance(root, (TimeoutError, socket.timeout)):
        return "timeout", f"no response in {TIMEOUT}s"
    return "unreachable", type(root).__name__


def probe(url: str) -> tuple[str, str]:
    """Return (bucket, detail). #20: HEAD, then GET on anything not clean."""
    def attempt(method: str):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, r.geturl()

    for method in ("HEAD", "GET"):
        try:
            status, final = attempt(method)
            if 200 <= status < 300:
                moved = "" if final.rstrip("/") == url.rstrip("/") else f" -> {final}"
                return "ok", f"{status}{moved}"
        except urllib.error.HTTPError as e:
            if method == "GET":
                # 401/403/429 from an institutional host is a wall we cannot see
                # through, NOT evidence the source is gone. Different bucket.
                bucket = "walled" if e.code in (401, 403, 429, 451) else "error"
                return bucket, f"HTTP {e.code}"
        except Exception as e:  # noqa: BLE001 - network reality is varied
            if method == "GET":
                return classify(e, url)
    return "error", "no response"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--sample", type=int, default=60, help="0 = every URL")
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--held-only", action="store_true")
    ap.add_argument("--json", dest="json_out", default=None)
    args = ap.parse_args()

    by_url = collect(args.root)
    if not by_url:
        print("qa_sources_alive: FAILED — found 0 source URLs. A sweep that finds "
              "nothing to check has failed, not passed.", file=sys.stderr)
        return 2

    total = len(by_url)
    urls = sorted(by_url)
    if args.held_only:
        urls = [u for u in urls if any(h for _, h in by_url[u])]
    pool = urls
    if args.sample and args.sample < len(pool):
        pool = random.Random(args.seed).sample(pool, args.sample)

    print(f"qa_sources_alive — {total} distinct source URLs declared across the corpus; "
          f"checking {len(pool)}"
          + (" (held pieces only)" if args.held_only else "")
          + f" · {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print()

    buckets: Counter[str] = Counter()
    findings = []
    for url in pool:
        bucket, detail = probe(url)
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

    print()
    print("  " + " · ".join(f"{k}: {v}" for k, v in sorted(buckets.items())))
    print()
    if findings:
        print("FINDINGS — none of these is a build defect; each is an editorial decision:")
        for f in findings:
            note = {
                "walled": "a wall, not a death — cite as fetched-on-date (#41), consider a first-party twin",
                "tls": "the HOST is broken, not necessarily the document — if it is still served, "
                       "the citation stands and the annotation states the certificate's state; "
                       "a reader meets a browser interstitial either way, so say so",
                "dns": "the name itself is gone — supersede, don't resurrect (#41)",
                "refused": "a refusal is not a 404 (#54) — re-probe from a second client on a "
                           "different day before any disposition",
                "timeout": "one slow read is not a death (#20) — re-probe before any disposition",
                "unreachable": "re-read before the next flip; supersede, don't resurrect (#41)",
                "error": "re-read before the next flip",
            }.get(f["bucket"], "re-read before the next flip")
            print(f"  ✗ {f['bucket']} ({f['detail']}) {'[HELD PIECE]' if f['held'] else ''}")
            print(f"      {f['url']}")
            print(f"      cited by: {', '.join(f['cited_by'])}")
            print(f"      → {note}")
    else:
        print("Every sampled promise answered.")

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump({"checked": len(pool), "total": total,
                       "buckets": dict(buckets), "findings": findings}, fh, indent=2)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
