#!/usr/bin/env python3
"""
qa_dist_input.py — standing assertion #16: the artefact under audit is the
artefact the run thinks it is.

WHY (2026-09-15)
----------------
Every standing assertion this operation owns answers the question "is the built
output correct?" None of them has ever answered the question that comes before
it: "WHICH built output am I reading?"

Found today, by accident, while going after the 09-14 forward question. The
standing pass was run from the repository root in the form CLAUDE.md documents:

    python3 agents/tools/qa_jsonld.py web/dist

It printed:

    qa_jsonld: pages 67 · nodes 0 · dereferenced 0 promises to dist
    CLEAN — every JSON-LD promise parses, agrees with its page, and
    dereferences to dist.

The same tool, run against the same build from a directory where it could not
guess wrong, printed `pages 120 · nodes 308 · dereferenced 608`. Two facts
compose into the green:

  1. `qa_jsonld` is the one assertion of the fourteen that does not read
     `sys.argv[1]`. It calls a `find_dist()` helper that searches
     `web/dist`, then `dist`, then a path relative to its own file. The path
     handed to it on the command line was accepted by the shell, ignored by
     the program, and never mentioned again.

  2. `web/dist` in the founder's working tree was a build from **2026-07-29**
     — 48 days old, 67 pages against today's 120, no `browse/` surface at all,
     and zero `application/ld+json` blocks, because it predates the 08-23 work
     that introduced them. It is `.gitignore`d, correctly, which is exactly why
     it never appeared in `git status` and nobody knew it was there.

So the check found nothing to check and called that a pass — the silent-pass
trap named in the 2026-08-16 rule and never before caught in our own toolkit —
and the reason it found nothing is that it was reading a directory from seven
weeks earlier while reporting on today's.

This is the third distinct way an assertion can be green and worthless, and the
operation now has one rule for each:

    scope   — a green check is scoped to what it enumerates   (08-16 → 09-06)
    oracle  — prove the bite as carefully as the control       (#35, 09-14)
    INPUT   — an assertion names the artefact it read          (this file)

WHAT THIS CHECK ENUMERATES
--------------------------
1. **Identity.** It resolves the dist path to an absolute path and PRINTS it.
   A QA log that carries this line cannot later be read as a claim about a
   directory the run never opened.

2. **Freshness.** The newest byte in `dist` must be no older than the newest
   byte under the source surfaces that produce it (`web/src`, `web/public`,
   `web/astro.config.mjs`, `web/package.json`, `web/src/lib`). A dist older
   than its own inputs is a stale artefact, and every assertion downstream of
   it is reporting on a site that no longer exists.

3. **Non-vacuity.** The dist must contain at least one built page and a
   sitemap. A check run against an empty or half-written directory must fail
   loudly rather than sweep zero files and exit 0.

WHAT IT DELIBERATELY DOES NOT DO
--------------------------------
It does not compare dist against git, and it does not try to decide whether the
dist matches HEAD. Uncommitted source edits are the normal state of a run in
progress; the honest invariant is *the build is not older than its inputs*, not
*the build matches a commit*. The commit-level question is already answered,
better, by the `verify` job's byte-compare against the live origin (#39).

PROVED BOTH WAYS per ruling #35, and per the 2026-09-14 rule that the bite is
proved as carefully as the control (assert the injection changed the artefact
before running the check on it):

  CONTROL (must be silent): today's freshly built 120-page dist — PASS.
  BITE 1 (must fire): the 2026-07-29 dist still in the working tree, with a
    source file demonstrably newer than every byte in it — FAIL, naming the
    dist's age and the source file that outran it.
  BITE 2 (must fire): an empty directory — FAIL on non-vacuity, not a silent
    sweep of zero pages.

Exit 0 clean; exit 1 with named defects; exit 2 on a usage error.
"""
import os
import sys
import time
from pathlib import Path

# The source surfaces whose edits a build is supposed to pick up. A dist older
# than the newest of these is stale by definition.
SOURCE_SURFACES = (
    "src",
    "public",
    "astro.config.mjs",
    "package.json",
)


def newest(paths):
    """(mtime, path) of the newest regular file under any of `paths`, or None."""
    best = None
    for root in paths:
        if root.is_file():
            cand = (root.stat().st_mtime, root)
            if best is None or cand[0] > best[0]:
                best = cand
            continue
        if not root.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", ".astro")]
            for name in filenames:
                p = Path(dirpath) / name
                try:
                    m = p.stat().st_mtime
                except OSError:
                    continue
                if best is None or m > best[0]:
                    best = (m, p)
    return best


def stamp(t):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))


def main(argv):
    dist = Path(argv[1] if len(argv) > 1 else "web/dist").resolve()

    # 1. IDENTITY — print it before anything can go wrong, so even a failure
    #    run leaves the path in the log.
    print("qa_dist_input: auditing %s" % dist)

    if not dist.is_dir():
        print("FAIL — no such directory. Nothing downstream of this can mean anything.")
        return 1

    # 2. NON-VACUITY
    pages = sorted(dist.rglob("index.html"))
    sitemap = dist / "sitemap-0.xml"
    print("qa_dist_input: %d built page(s); sitemap-0.xml %s"
          % (len(pages), "present" if sitemap.exists() else "ABSENT"))
    if not pages:
        print("FAIL — the directory contains no built page. An assertion that "
              "sweeps zero files and exits 0 is a green light wired to nothing.")
        return 1
    if not sitemap.exists():
        print("FAIL — no sitemap-0.xml. This is not a completed Astro build.")
        return 1

    # 3. FRESHNESS
    web = dist.parent if dist.name == "dist" else dist.parents[0]
    sources = [web / s for s in SOURCE_SURFACES]
    src_newest = newest(sources)
    dist_newest = newest([dist])

    if src_newest is None:
        print("qa_dist_input: no source surface found beside the dist (%s) — "
              "freshness not assessable, identity and non-vacuity pass." % web)
        print("CLEAN (partial) — the dist is real and non-empty; freshness unchecked.")
        return 0

    s_m, s_p = src_newest
    d_m, d_p = dist_newest
    print("qa_dist_input: newest source %s  (%s)" % (stamp(s_m), s_p))
    print("qa_dist_input: newest built   %s  (%s)" % (stamp(d_m), d_p))

    if d_m < s_m:
        gap = s_m - d_m
        if gap >= 86400:
            how = "%.1f day(s)" % (gap / 86400.0)
        elif gap >= 3600:
            how = "%.1f hour(s)" % (gap / 3600.0)
        else:
            how = "%d minute(s)" % max(1, round(gap / 60.0))
        print("FAIL — the build is OLDER than its own inputs by %s. "
              "Every assertion pointed at this directory is reporting on a site "
              "that no longer exists." % how)
        print("  stale build :  %s  (%s)" % (stamp(d_m), d_p))
        print("  outrun by   :  %s  (%s)" % (stamp(s_m), s_p))
        return 1

    print("CLEAN — the dist is real, non-empty, and no older than the sources "
          "that produce it. The other assertions may be trusted to be reading "
          "today's site.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
