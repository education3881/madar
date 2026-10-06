#!/usr/bin/env python3
"""qa_served_manifest — a page whose RENDERED CONTENT changed must say so in its
date, and a date that moved must have a changed byte behind it.

WHY (Manager, 2026-10-06 — standing-queue item 2, raised 2026-09-06, named
twelve times, done zero. The oldest item on the board at 29 days, reached today
by the one-queue rule's displacement clause and its 10-05 tiebreak: among items
past the three-displacement threshold, the OLDEST goes first.)
-----------------------------------------------------------------------------
Every instrument this operation owns derives *change* from **source
provenance** — git history over `CONTENT_DIRS` and `CHROME_GLOBS`. The truth of
"did this page change" lives in the **served bytes**, which only the deploy
pipeline ever sees. The 09-06 weekly review wrote the gap down and called the
answer "an output-bounded lastmod (per-URL content hash across deploys)", and
then nobody built it for twenty-nine days.

`qa_lastmod` bounds ONE direction: no `<lastmod>` newer than its own per-URL
ceiling. That is the leak direction — a date that moved when nothing served
changed (9886987 on 08-30, 642fef2 on 09-02, both held drafts dating live
pages). The direction it cannot bound, and the reason the queue item exists:

    a page whose served bytes CHANGED and whose date says they did NOT.

After a deploy, `origin == build` by construction, so the `verify` job's
byte-compare cannot see it either: that job answers *did my deploy land*, and
this question is **across deploys**. Nothing in the pipeline holds state from
one deploy to the next. That is why the manifest is emitted INTO `dist` — the
published artefact becomes the memory, fetched back from the origin on the next
build. There is no other place to keep it that is not provenance again.

THE DEFECT IS NOT HYPOTHETICAL. MEASURED 2026-10-06, NOT ASSERTED.
------------------------------------------------------------------
`sitemapLastmod.mjs` lists four `CHROME_GLOBS` — layouts, components, lib,
pages — and deliberately excludes `web/src/styles`, with a stated reason:
*"presentation is excluded, rendered content is included."* The reason is
defensible for lastmod semantics. Its consequence was never checked.

Astro serves the stylesheet as a **content-hashed filename**
(`/madar/_astro/style.DBd_Pbzi.css`), so the hash is printed into the `<head>`
of every page that links it. Probed on the real tree today by changing one
character in `global.css` (`max-width: 100%` -> `99%`):

    served bytes changed on 120 of 121 HTML pages
    <lastmod> values moved:                      0

One character, 120 pages, zero dates, and not one check in the operation could
see it. The injection was confirmed to have changed the artefact before the
measurement was believed (#74) and the tree was reverted in the same run.

So the unbounded direction is reachable by editing one file, it fires on the
whole corpus at once, and it has exactly one *declared* legitimate source. Which
is the opening this instrument needs: declare that source and the rest of the
surface becomes a clean assertion.

TWO HASHES PER PAGE, AND THAT IS THE WHOLE DESIGN
-------------------------------------------------
  * `bytes_sha`   — sha256 of the served bytes, exactly as a reader receives
                    them. The honest record of the artefact.
  * `content_sha` — sha256 of the same bytes with the build's own
                    content-hashed asset filenames collapsed
                    (`/_astro/style.CTkyS1Kw.css` -> `/_astro/style.__.css`).
                    The record of what the page SAYS.

Measured on the same probe: raw 120 differ, normalised **0** differ. A
presentation-only change is therefore mechanically separable from a rendered
content change, which means the three cases that look identical today can be
told apart without a judgment call:

  1. `content_sha` changed and `lastmod` did NOT move      -> FAIL (exit 1).
     The page's rendered content changed and the sitemap tells every crawler it
     did not. Unambiguous, no declared exception, and invisible to every other
     instrument we own. This is the assertion.

  2. `bytes_sha` changed, `content_sha` did not, no date   -> REPORTED, counted.
     The resolver's own declared exclusion (a stylesheet edit), now VISIBLE and
     COUNTED instead of invisible. Not a failure: the tool asserts the
     resolver's stated intent rather than overruling it.

  3. `lastmod` moved and `content_sha` did NOT change      -> REPORTED, counted.
     The 09-04 over-reporting shape: all 119 dates moved for a `Base.astro`
     change that altered the served output of one page. The 09-06 review called
     this "a design question for the Web Developer, not a defect", so it is
     printed as a number every run and never as a build failure. **The number is
     the point** — the design question has been named twelve times and has never
     once had a measurement attached to it.

The normalisation is deliberately NARROW — only the build's own `_astro`
css/js hashes. A wider normaliser would hide real changes, which is the 09-14
trap on the input side (an assertion scoped wider than the thing it checks finds
the right string for the wrong reason). And because a normaliser that silently
matches nothing is a silent pass, the tool FAILS TO CHECK (exit 2) if `_astro`
assets exist in `dist` and zero substitutions were applied.

WHAT THIS CANNOT DO, STATED SO IT DOES NOT READ AS COVERED
----------------------------------------------------------
The manifest is generated by the same build whose output it describes. If a
build is wrong, the manifest is wrong consistently and the comparison passes. It
compares ACROSS deploys and can never validate a single build in isolation. The
instrument's seed is therefore taken from the ORIGIN's real served bytes
(`--seed-from-origin`), not from a local build, so the first baseline is derived
from reality rather than from the thing it is meant to check (#36).

A KNOWN FUTURE BITE, WITH A DATE
--------------------------------
`SiteFooter.astro` computes `new Date().getFullYear()` at build time. On
2027-01-01 the first deploy will change the served bytes of every page with no
commit touching any source file and no date moving anywhere. That is case 1, on
the whole corpus, from the calendar. It is written here so that when it fires it
is recognised as predicted rather than diagnosed from scratch.

EXIT CODES
----------
  0  every rendered-content change is dated; cases 2 and 3 reported if present
  1  SILENT CONTENT CHANGE — bytes say the page changed, the date says it did not
  2  FAILURE TO CHECK — no dist, no sitemap, the page/URL join could not be
     confirmed, the normaliser matched nothing, the origin was unreachable, or
     the budget truncated the sweep. Never reported as "no drift" (08-16).
  3  NO BASELINE at the origin yet. The first deploy carrying this tool seeds
     it; the deploy after that is the first real comparison. Loud and distinct,
     because "nothing to compare" is the silent-pass trap's favourite costume.

USAGE
-----
  python3 agents/tools/qa_served_manifest.py --emit [dist]
  python3 agents/tools/qa_served_manifest.py --describe [dist]
  python3 agents/tools/qa_served_manifest.py --check [dist] [--baseline PATH]
  python3 agents/tools/qa_served_manifest.py --seed-from-origin PATH [dist]
                                             [--budget SECONDS]

WHERE IT IS WIRED, AND WHY THE HALVES DIFFER (the 09-13 rule)
-------------------------------------------------------------
`--emit` is gated from `web/package.json`'s `postbuild`, because if it ever
fails to run, the chain of memory breaks and the NEXT build has no baseline. It
reads only `dist`, needs no network, and its output is asserted by `qa_census`
against the sitemap's own URL set, so a manifest that quietly stops describing
some pages fails the build rather than narrowing in silence.

`--check` is NOT gated, and the home it wants is **not** the `verify` job.
Verify downloads the exact artifact `deploy-pages` published and compares it to
the origin, so by the time it runs, origin == artifact by construction and the
manifest would be compared against itself. The question is *across* deploys, so
the only moment it can be asked is in the **build job, after `npm run build`,
against the still-current origin** — before this build replaces it.

Two reasons it stays out of the gate, and the second is the load-bearing one:

  * It reads the ORIGIN. A briefly unreachable github.io must not red a deploy,
    and must never be downgraded to a pass either — which is what exit 2 is for.
    Same stance the workflow already takes on `qa_live_drift`.
  * **Its counts are a function of deploy latency, not of the commit.** On a
    staged-but-undeployed morning the origin's manifest is older than HEAD, so
    the comparison spans several commits and the case-2/case-3 numbers describe
    the gap rather than the change. That is exactly right for a daily
    measurement and wrong for a gate.

So this identity cannot wire it where it belongs (`.github/workflows/**` is
refused), and per RUNBOOK clause (4) of the 09-14 rule the reason lives in this
header and the one-line patch is staged at `agents/patches/`. Same shape as
`qa_feed_validators` (#63), for the same reason, named here rather than left to
be inferred from a count. Until that patch lands the check is HAND-RUN in every
daily run — which is the 09-13 defect by name, carried deliberately and with a
staged patch rather than a promise.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

# STDLIB ONLY, AND THAT IS A GATE REQUIREMENT RATHER THAN A PREFERENCE.
# `--emit` is wired into `postbuild`, so it runs on every build and a failed
# import reds the deploy. The first draft of this file imported `requests` at
# module level and exited 2 when it was missing — which would have made a step
# that needs NO NETWORK AT ALL fail on an image lacking a third-party package.
# `requests` is used by exactly one tool in this directory (`qa_live_drift`) and
# that tool is deliberately NOT gated; CLAUDE.md states the assertions are
# "Python 3, no deps" except the four that need a headless Chrome. A gated
# assertion must not be the first to break that. So the origin is read with
# `urllib`, the same way `qa_sources_alive` reads third-party hosts.

SCHEMA = "madar-served-manifest/1"
MANIFEST_NAME = "served-manifest.json"
PER_REQUEST_TIMEOUT = 20

# The build's own content-hashed asset filenames. Narrow on purpose: see the
# header. `style.CTkyS1Kw.css` -> `style.__.css`.
ASSET_HASH_RX = re.compile(rb"(/_astro/[A-Za-z0-9_\-]+?)\.[A-Za-z0-9_\-]{8}\.(css|js)\b")

# ---- the total ceiling, per ruling #88 -------------------------------------
# Same design as qa_sources_alive: the deadline is owned by the MAIN thread and
# the socket by a daemon worker, because a clock checked *between* units can
# only bound the loop and never the request in flight. Default 0 = unbounded.
_DEADLINE: float | None = None


def _budget_left() -> float:
    return float("inf") if _DEADLINE is None else _DEADLINE - time.monotonic()


def _attempt_timeout() -> float:
    left = _budget_left()
    if left == float("inf"):
        return float(PER_REQUEST_TIMEOUT)
    return max(0.5, min(float(PER_REQUEST_TIMEOUT), left))


# ---- hashing ---------------------------------------------------------------

def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def hash_page(raw: bytes) -> tuple[str, str, int]:
    """(bytes_sha, content_sha, substitutions_applied)."""
    norm, n = ASSET_HASH_RX.subn(rb"\1.__.\2", raw)
    return sha(raw), sha(norm), n


# ---- the sitemap, and the join ---------------------------------------------

def sitemap_map(xml: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for m in re.finditer(r"<url>(.*?)</url>", xml, re.S):
        block = m.group(1)
        loc = re.search(r"<loc>(.*?)</loc>", block)
        mod = re.search(r"<lastmod>(.*?)</lastmod>", block)
        if loc:
            out[loc.group(1).strip()] = mod.group(1).strip() if mod else ""
    return out


def site_prefix(urls: list[str]) -> str:
    """The site root, derived from the sitemap rather than hardcoded (#36).

    The shortest <loc> is the home page, and every other URL hangs off it.
    Derived because a constant copied into a fourth file is the defect #75 was
    filed about.
    """
    if not urls:
        return ""
    return min(urls, key=len).rstrip("/")


def url_for(dist: Path, page: Path, prefix: str) -> str:
    rel = page.relative_to(dist).as_posix()
    if rel == "index.html":
        return prefix + "/"
    if rel.endswith("/index.html"):
        return prefix + "/" + rel[: -len("index.html")]
    return prefix + "/" + rel


# ---- building the manifest -------------------------------------------------

def head_commit() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        # Absent, not wrong. The manifest is still a valid baseline without it;
        # it just cannot tell you which deploy it came from.
        return "unknown"


def build_manifest(dist: Path) -> tuple[dict | None, int]:
    """(manifest, exit_code). exit_code 2 means the manifest must not be trusted."""
    sm = dist / "sitemap-0.xml"
    if not sm.exists():
        print(f"FAIL(2): no sitemap-0.xml in {dist} — a manifest with no dates to "
              "join against is not a baseline.")
        return None, 2

    smap = sitemap_map(sm.read_text())
    if not smap:
        print("FAIL(2): the sitemap parsed to zero URLs. An assertion that finds "
              "nothing to check has failed, not passed.")
        return None, 2
    prefix = site_prefix(list(smap))

    pages: dict[str, dict] = {}
    unrouted: dict[str, dict] = {}
    subs = 0
    for p in sorted(dist.rglob("*.html")):
        raw = p.read_bytes()
        b, c, n = hash_page(raw)
        subs += n
        entry = {"bytes_sha": b, "content_sha": c, "bytes": len(raw),
                 "file": p.relative_to(dist).as_posix()}
        u = url_for(dist, p, prefix)
        if u in smap:
            entry["lastmod"] = smap[u]
            pages[u] = entry
        else:
            entry["lastmod"] = None
            unrouted[u] = entry

    # THE JOIN IS ASSERTED, NOT ASSUMED. A sitemap URL with no built file means
    # the mapping is wrong, and a baseline built on a wrong mapping is worse
    # than none: it would report a page as unchanged forever (#14's trap on the
    # input side — the instrument must be proved before it is trusted, #35).
    missing = sorted(set(smap) - set(pages))
    if missing:
        print(f"FAIL(2): {len(missing)} sitemap URL(s) have no built HTML file — "
              "the page/URL join is wrong, so every hash in this manifest would "
              "be filed against the wrong name:")
        for u in missing[:10]:
            print(f"  ? {u}")
        return None, 2

    # A normaliser that matched nothing is a silent pass (09-14 trap 1). If the
    # build emits hashed assets at all, the substitution MUST have fired.
    if any((dist / "_astro").glob("*.css")) and subs == 0:
        print("FAIL(2): dist/_astro carries hashed stylesheets and the asset-hash "
              "normaliser applied ZERO substitutions. content_sha would equal "
              "bytes_sha everywhere and case 2 would be indistinguishable from "
              "case 1 — a check reading its own answer off the wrong field.")
        return None, 2

    assets: dict[str, dict] = {}
    for p in sorted(dist.rglob("*")):
        if not p.is_file() or p.suffix == ".html":
            continue
        rel = p.relative_to(dist).as_posix()
        if rel == MANIFEST_NAME:
            continue
        raw = p.read_bytes()
        assets[rel] = {"bytes_sha": sha(raw), "bytes": len(raw)}

    return {
        "schema": SCHEMA,
        "source": "build",
        "site": prefix,
        "commit": head_commit(),
        "generated_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "normalisations_applied": subs,
        "pages": pages,
        "unrouted": unrouted,
        "assets": assets,
    }, 0


# ---- seeding from the origin's real bytes ----------------------------------

def fetch(url: str) -> bytes | None:
    """The raw bytes the origin serves at this URL, or None.

    Raw BYTES, never decoded text: the whole instrument hashes what a reader
    receives, and a decode-then-reencode round trip is not guaranteed to be the
    identity. Returning text here would make every hash a hash of our own
    transcoding.
    """
    req = urllib.request.Request(url, headers={"User-Agent": "madar-qa-served-manifest"})
    try:
        with urllib.request.urlopen(req, timeout=_attempt_timeout()) as r:
            return r.read() if r.status == 200 else None
    except (urllib.error.URLError, urllib.error.HTTPError, OSError, ValueError):
        return None


def seed_from_origin(dist: Path, out_path: Path) -> int:
    """Build a baseline from what the ORIGIN actually serves.

    The seed must not come from a local build: the instrument exists to judge
    builds, and a baseline taken from one is the 09-14 masking trap at the
    level of the whole tool.
    """
    sm = dist / "sitemap-0.xml"
    if not sm.exists():
        print(f"FAIL(2): no local sitemap in {dist} to learn the URL set from.")
        return 2
    prefix = site_prefix(list(sitemap_map(sm.read_text())))
    if not prefix:
        print("FAIL(2): could not derive the site prefix from the local sitemap.")
        return 2

    live_xml = fetch(f"{prefix}/sitemap-0.xml")
    if live_xml is None:
        print(f"FAIL(2): could not fetch {prefix}/sitemap-0.xml — an unreachable "
              "origin is a failure to seed, never an empty baseline.")
        return 2
    smap = sitemap_map(live_xml.decode("utf-8", "replace"))
    if not smap:
        print("FAIL(2): the origin's sitemap parsed to zero URLs.")
        return 2

    pages: dict[str, dict] = {}
    unreached: list[str] = []
    subs = 0
    result: dict[str, bytes | None] = {}
    todo = sorted(smap)

    def _sweep() -> None:
        for u in todo:
            if _budget_left() <= 0:
                return
            result[u] = fetch(u)

    print(f"seeding from the origin: {len(todo)} URL(s)"
          + (f" · total ceiling {_DEADLINE and 'set'}" if _DEADLINE else " · no ceiling"),
          flush=True)
    t = threading.Thread(target=_sweep, daemon=True)
    t.start()
    while t.is_alive():
        left = _budget_left()
        if left <= 0:
            break
        t.join(timeout=min(1.0, left) if left != float("inf") else 1.0)

    for u in todo:
        raw = result.get(u)
        if raw is None:
            unreached.append(u)
            continue
        b, c, n = hash_page(raw)
        subs += n
        pages[u] = {"bytes_sha": b, "content_sha": c, "bytes": len(raw),
                    "lastmod": smap[u], "file": None}

    if unreached:
        # Truncation is louder than failure (#88). A seed with holes would
        # report those pages as "new" forever, which reads like a pass.
        print(f"FAIL(2): {len(unreached)} of {len(todo)} URL(s) were never read — "
              "a baseline with holes reports those pages as new forever:")
        for u in unreached[:10]:
            print(f"  ! {u}")
        return 2

    manifest = {
        "schema": SCHEMA,
        "source": "origin",
        "site": prefix,
        "commit": "origin-observed",
        "generated_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "normalisations_applied": subs,
        "pages": pages,
        "unrouted": {},
        "assets": {},   # an origin seed covers pages only, and says so.
    }
    out_path.write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n")
    print(f"SEEDED from the origin: {len(pages)} page(s), {subs} asset-hash "
          f"normalisation(s) applied -> {out_path}")
    return 0


# ---- the comparison --------------------------------------------------------

def compare(base: dict, cur: dict) -> int:
    bp, cp = base.get("pages", {}), cur.get("pages", {})
    shared = sorted(set(bp) & set(cp))
    if not shared:
        print("FAIL(2): the baseline and the build share zero URLs. Nothing was "
              "compared, which is not the same as nothing having changed.")
        return 2

    silent: list[tuple[str, str, str]] = []      # case 1 — the assertion
    presentation: list[str] = []                 # case 2 — declared exclusion
    unbacked: list[str] = []                     # case 3 — the design question
    dated: list[str] = []                        # content changed AND dated

    for u in shared:
        b, c = bp[u], cp[u]
        content_moved = b["content_sha"] != c["content_sha"]
        bytes_moved = b["bytes_sha"] != c["bytes_sha"]
        date_moved = (b.get("lastmod") or "") != (c.get("lastmod") or "")
        if content_moved and not date_moved:
            silent.append((u, b.get("lastmod") or "—", c.get("lastmod") or "—"))
        elif content_moved and date_moved:
            dated.append(u)
        elif bytes_moved and not date_moved:
            presentation.append(u)
        elif date_moved:
            unbacked.append(u)

    added = sorted(set(cp) - set(bp))
    removed = sorted(set(bp) - set(cp))

    print(f"baseline: {base.get('source')} · commit {str(base.get('commit'))[:12]} "
          f"· {len(bp)} page(s) · generated {base.get('generated_at_utc')}")
    print(f"build:    {cur.get('source')} · commit {str(cur.get('commit'))[:12]} "
          f"· {len(cp)} page(s)")
    print(f"compared: {len(shared)} page(s) present in both\n")

    if added:
        print(f"NEW: {len(added)} page(s) built that the baseline does not carry "
              "(a new page legitimately has no prior hash):")
        for u in added[:10]:
            print(f"  + {u}")
    if removed:
        print(f"GONE: {len(removed)} page(s) in the baseline no longer built:")
        for u in removed[:10]:
            print(f"  - {u}")

    if dated:
        print(f"\nOK — {len(dated)} page(s) whose rendered content changed AND "
              "whose date moved. This is what a correct change looks like.")
        for u in dated[:10]:
            print(f"  ~ {u}")

    if presentation:
        print(f"\nPRESENTATION-ONLY ({len(presentation)}): served bytes changed, "
              "rendered content identical, no date moved.")
        print("  This is `sitemapLastmod.mjs` excluding `web/src/styles` on "
              "purpose — presentation is excluded, rendered content is included.")
        print("  Reported rather than failed: the tool asserts the resolver's "
              "stated intent, it does not overrule it. Before today this set was")
        print("  invisible, which is why a stylesheet edit and a corpus-wide "
              "rendering bug looked exactly alike.")
        for u in presentation[:6]:
            print(f"  = {u}")
        if len(presentation) > 6:
            print(f"  … and {len(presentation) - 6} more")

    if unbacked:
        print(f"\nUNBACKED DATES ({len(unbacked)}): <lastmod> moved and the "
              "rendered content is byte-identical.")
        print("  The 09-04 shape: a provenance-derived date moving for pages "
              "whose output did not change. The 09-06 review ruled this a design")
        print("  question for the Web Developer, not a defect — so it is a "
              "number here and never a build failure. The number is the point:")
        print(f"  this deploy would tell crawlers {len(unbacked)} page(s) changed "
              "with nothing behind it.")
        for u in unbacked[:6]:
            print(f"  ! {u}")
        if len(unbacked) > 6:
            print(f"  … and {len(unbacked) - 6} more")

    if silent:
        print(f"\nSILENT CONTENT CHANGE ({len(silent)}) — THE ASSERTION, AND IT "
              "FAILED:")
        print("  These pages' rendered content changed and their <lastmod> did "
              "not move. Every crawler is being told nothing happened here.")
        print("  No other instrument in this operation can see this; it is the "
              "one direction qa_lastmod's ceiling cannot bound and the one the")
        print("  verify byte-compare cannot either, because after a deploy "
              "origin == build by construction.")
        for u, ob, nb in silent[:12]:
            print(f"  X {u}  date unchanged at {ob}")
        if len(silent) > 12:
            print(f"  … and {len(silent) - 12} more")
        print(f"\nFAIL(1): {len(silent)} page(s) changed what they say and kept "
              "their date.")
        return 1

    print(f"\nCLEAN — every rendered-content change carries a moved date. "
          f"{len(shared)} page(s) compared · {len(dated)} changed and dated · "
          f"{len(presentation)} presentation-only · {len(unbacked)} unbacked "
          f"date(s) · {len(added)} new · {len(removed)} gone.")
    return 0


# ---- main ------------------------------------------------------------------

def main() -> int:
    global _DEADLINE
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("dist", nargs="?", default="web/dist")
    ap.add_argument("--emit", action="store_true",
                    help="write dist/served-manifest.json from this build")
    ap.add_argument("--describe", action="store_true",
                    help="print the manifest's counts and write nothing. This is "
                         "what qa_census reads: an observer that writes is an "
                         "observer whose own side effects it cannot see.")
    ap.add_argument("--check", action="store_true",
                    help="compare this build against the origin's manifest")
    ap.add_argument("--baseline", default=None,
                    help="compare against a manifest FILE instead of the origin")
    ap.add_argument("--seed-from-origin", default=None, metavar="PATH",
                    help="write a baseline from the origin's REAL served bytes")
    ap.add_argument("--budget", type=float, default=0,
                    help="total wall-clock ceiling in seconds for origin reads "
                         "(ruling #88). 0 = unbounded, so existing invocations "
                         "behave exactly as they did.")
    args = ap.parse_args()

    dist = Path(args.dist)
    if not dist.is_dir():
        print(f"FAIL(2): dist not found at {dist} — nothing to describe is not a pass.")
        return 2

    if args.budget and args.budget > 0:
        _DEADLINE = time.monotonic() + args.budget

    if args.seed_from_origin:
        return seed_from_origin(dist, Path(args.seed_from_origin))

    manifest, code = build_manifest(dist)
    if code or manifest is None:
        return code or 2

    if args.describe:
        print(f"qa_served_manifest: {len(manifest['pages'])} routed page(s) · "
              f"{len(manifest['unrouted'])} served-not-routed · "
              f"{len(manifest['assets'])} asset(s) · "
              f"{manifest['normalisations_applied']} normalisation(s)")
        return 0

    if args.emit:
        out = dist / MANIFEST_NAME
        out.write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n")
        print(f"qa_served_manifest — emitted {out.relative_to(dist)}: "
              f"{len(manifest['pages'])} routed page(s), "
              f"{len(manifest['unrouted'])} served-not-routed, "
              f"{len(manifest['assets'])} asset(s), "
              f"{manifest['normalisations_applied']} asset-hash "
              "normalisation(s) applied.")
        print("  The published artefact is now the memory: the next build fetches "
              "this file back from the origin and compares against it. Emitting "
              "is gated because a gap in the chain leaves the next build blind.")
        return 0

    if not args.check:
        print("Nothing asked. Use --emit, --check or --seed-from-origin.")
        return 2

    if args.baseline:
        bp = Path(args.baseline)
        if not bp.exists():
            print(f"FAIL(2): baseline {bp} does not exist.")
            return 2
        base = json.loads(bp.read_text())
    else:
        url = f"{manifest['site']}/{MANIFEST_NAME}"
        raw = fetch(url)
        if raw is None:
            print(f"NO BASELINE(3): {url} is not served.")
            print("  Either this is the first deploy carrying the tool — in which "
                  "case this deploy SEEDS the baseline and the next one is the "
                  "first real comparison — or the origin is unreachable.")
            print("  Reported as its own exit code rather than as a pass, because "
                  "'nothing to compare' is the silent-pass trap's favourite "
                  "costume (08-16).")
            return 3
        try:
            base = json.loads(raw)
        except json.JSONDecodeError:
            print(f"FAIL(2): {url} is served but is not JSON — the baseline is "
                  "corrupt and a corrupt baseline is not an empty one.")
            return 2

    if base.get("schema") != SCHEMA:
        print(f"FAIL(2): baseline schema {base.get('schema')!r} != {SCHEMA!r}. "
              "Comparing across schema versions would invent findings.")
        return 2

    return compare(base, manifest)


if __name__ == "__main__":
    sys.exit(main())
