#!/usr/bin/env python3
"""
lastmod_tree_guard — refuse to compare a GIT-DERIVED date against a
WORKING-TREE build.

Not an assertion. A precondition shared by the two instruments that compare a
`<lastmod>` to something, which is why it is deliberately not named `qa_*`: the
assertion count is globbed from `qa_*.py` (`qa_patch_queue`), and a precondition
that cannot fail a build on its own is not a thirty-third standing assertion.

WHY (standing-queue item 8, raised 2026-10-08, taken 2026-10-15 at 7 days and
four displacements — the oldest item past the three-displacement threshold)
---------------------------------------------------------------------------
`web/src/lib/sitemapLastmod.mjs` resolves every `<lastmod>` from **git history**
over its own `CHROME_GLOBS` and `CONTENT_DIRS`. A build run against a dirty
working tree therefore emits dates that describe **the last commit**, while the
bytes it emits describe **the files on disk**. Any instrument that compares the
two is, in that state, comparing two different moments and calling the
difference a finding.

Measured, both directions, both instruments:

  2026-10-08  `qa_served_manifest --check`, uncommitted chrome edit:
              119 of 120 pages reported as *silent content change* —
              every one a FALSE POSITIVE. Cleared by committing and re-running.

  2026-10-14  `qa_live_drift`, uncommitted content edit (eight article files):
              `CLEAN — 134 URLs, 0 lastmod drift` while eight files on disk
              had changed — a FALSE NEGATIVE. Rebuilt after the commit it
              reported `DRIFT(53)`, correctly.

The false negative is the worse half, and it is the reason this is a refusal
rather than a warning: **the loud version gets investigated.** A wrong number
printed in red is read by the next run; `CLEAN` is read by nobody, ever again.
Two QA logs already contain a conclusion drawn from a 0/0 this instrument could
not support (10-06 and 10-07, both reporting `0/0` as *bounding the commit*).

WHAT IT REFUSES, AND WHAT IT DELIBERATELY DOES NOT
--------------------------------------------------
The defect is a property of the **date axis**, not of either whole tool. So:

  - `qa_served_manifest --check` refuses entirely. Every one of its four
    buckets keys on `date_moved`, so there is nothing left to report.
  - `qa_live_drift` refuses **the lastmod axis only** and still reports the URL
    set and the sampled heads, which compare served bytes to served bytes and
    need no provenance at all. Throwing away two working axes to punish a third
    would be its own silent-pass trap: a check too blunt to run is a check that
    stops being run.

A refusal is NOT a finding and NOT a failure to reach the origin, and it must
be distinguishable from both — the whole defect was an unsupportable number
being read as one of the two. Hence a fourth exit code, **4 = REFUSED**, beside
`1` (drift found), `2` (could not check) and, in `qa_served_manifest`, `3` (no
baseline served).

WHERE THE PATH LIST COMES FROM, AND WHY IT IS NOT WRITTEN HERE
--------------------------------------------------------------
`CHROME_GLOBS` and `CONTENT_DIRS` are **parsed out of the resolver** on every
run. Copying them into this file would make it the resolver's second home and
this guard the next entry in the drift family the 09-27 amendment is about:
*when you write a rule that fixes a drift by enumerating the places to touch,
the enumeration is now the drift's new home — grep for it, do not remember it.*
If the resolver grows a fifth chrome glob, a copy here would quietly stop
guarding it, which is precisely the shape of defect this file exists to close.

A parse that yields nothing is a FAILURE, never an empty guard (08-16 silent-
pass trap): an unreadable resolver means the guard cannot establish support,
and cannot-establish is refused exactly like dirty.

HELD FILES ARE CLASSIFIED, NOT COUNTED (the resolver's own semantics)
--------------------------------------------------------------------
A held file (`approved: false`, ruling #18) contributes no date anywhere — the
resolver says so and 2026-09-06 made it binding. So a dirty held draft cannot
make the date axis unsupportable, and refusing on one would make the guard fire
on every drafting day, which is how a guard gets switched off. Held dirty paths
are printed and excluded, with the reason in the output, the same way
`qa_third_party_origins` prints `<a href>` and asserts nothing about it.

A file is date-relevant if it is approved in the **working tree** or in **HEAD**:
a flip in either direction changes what the resolver may read.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

RESOLVER = "web/src/lib/sitemapLastmod.mjs"
REFUSED = 4


class GuardUnavailable(RuntimeError):
    """The guard could not establish support. Refused, never assumed clean."""


def _git(root: Path, *args: str) -> str:
    out = subprocess.run(["git", "-C", str(root), *args],
                         capture_output=True, text=True)
    if out.returncode != 0:
        raise GuardUnavailable(
            f"git {' '.join(args)} failed in {root}: "
            f"{(out.stderr or out.stdout).strip().splitlines()[:1]}")
    return out.stdout


def resolver_paths(root: Path) -> tuple[list[str], list[str]]:
    """(chrome_globs, content_dirs), parsed from the resolver. Never copied."""
    src = root / RESOLVER
    if not src.exists():
        raise GuardUnavailable(f"{RESOLVER} not found under {root}")
    text = src.read_text()

    def arr(name: str) -> list[str]:
        m = re.search(rf"const\s+{name}\s*=\s*\[(.*?)\]", text, re.S)
        if not m:
            return []
        return re.findall(r"['\"]([^'\"]+)['\"]", m.group(1))

    chrome, content = arr("CHROME_GLOBS"), arr("CONTENT_DIRS")
    if not chrome or not content:
        raise GuardUnavailable(
            f"parsed {len(chrome)} chrome glob(s) and {len(content)} content "
            f"dir(s) from {RESOLVER} — a guard that enumerates nothing guards "
            "nothing, so this is a refusal and not an empty pass.")
    return chrome, content


def _approved(blob: str | None) -> bool:
    if not blob:
        return False
    m = re.search(r"^approved:\s*(true|false)\s*$", blob, re.M)
    return bool(m and m.group(1) == "true")


def _head_blob(root: Path, rel: str) -> str | None:
    out = subprocess.run(["git", "-C", str(root), "show", f"HEAD:{rel}"],
                         capture_output=True, text=True)
    return out.stdout if out.returncode == 0 else None


def dirty_paths(root: Path) -> list[str]:
    """Every path git reports as not matching HEAD, including untracked."""
    raw = _git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all",
               "--no-renames")
    fields = [f for f in raw.split("\0") if f]
    return [f[3:] for f in fields if len(f) > 3]


def report(root: Path) -> dict:
    """Classify the working tree against the resolver's own read paths."""
    chrome, content = resolver_paths(root)
    relevant: list[tuple[str, str]] = []
    held: list[str] = []

    for rel in dirty_paths(root):
        if any(rel == g or rel.startswith(g.rstrip("/") + "/") for g in chrome):
            relevant.append((rel, "chrome — dates every page that includes it"))
            continue
        if any(rel.startswith(d.rstrip("/") + "/") for d in content):
            if not rel.endswith(".md"):
                continue
            wt = (root / rel)
            now = _approved(wt.read_text()) if wt.exists() else False
            was = _approved(_head_blob(root, rel))
            if now or was:
                relevant.append((rel, "approved content — dates its own page"))
            else:
                held.append(rel)
    return {"chrome_globs": chrome, "content_dirs": content,
            "relevant": relevant, "held": held}


def _print_report(rep: dict, axis: str) -> None:
    rel, held = rep["relevant"], rep["held"]
    print(f"REFUSED({REFUSED}): {axis} compares a GIT-DERIVED <lastmod> against "
          "a WORKING-TREE build, and the tree is dirty in "
          f"{len(rel)} path(s) the resolver reads.")
    print("  The dates this build emitted describe HEAD. The bytes it emitted "
          "describe disk. A difference between them is an artefact of the "
          "commit not existing yet, not a finding (standing-queue item 8).")
    for p, why in rel[:12]:
        print(f"  ! {p}  ({why})")
    if len(rel) > 12:
        print(f"  … and {len(rel) - 12} more")
    if held:
        print(f"  {len(held)} dirty held draft(s) EXCLUDED — a held file "
              "contributes no date anywhere (ruling #18, 2026-09-06), so it "
              "cannot make this axis unsupportable:")
        for p in held[:4]:
            print(f"    - {p}")
    print("  The honest home for this comparison is POST-COMMIT, PRE-PUSH. "
          "Commit the work — ruling #96 asks for a commit at the close of "
          "every standing function anyway — and run it again.")
    print(f"  Reported as exit {REFUSED}, which is neither drift (1) nor a "
          "failure to reach the origin (2): a refusal to form a verdict is its "
          "own outcome, and the defect this guard closes was exactly an "
          "unsupportable number being read as one of the other two.")


def check(root: Path, axis: str) -> int | None:
    """None = the comparison is supportable. REFUSED = it is not, and said so."""
    try:
        rep = report(root)
    except GuardUnavailable as e:
        print(f"REFUSED({REFUSED}): the date axis of {axis} cannot be shown to "
              f"be supportable — {e}")
        print("  Cannot-establish is refused exactly like dirty. An instrument "
              "that cannot check its own precondition has not passed it.")
        return REFUSED
    if not rep["relevant"]:
        if rep["held"]:
            print(f"lastmod_tree_guard: clean in the resolver's read paths "
                  f"({len(rep['chrome_globs'])} chrome glob(s), "
                  f"{len(rep['content_dirs'])} content dir(s)) · "
                  f"{len(rep['held'])} dirty held draft(s) excluded by design.")
        return None
    _print_report(rep, axis)
    return REFUSED


if __name__ == "__main__":
    import sys
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    code = check(root, "a standalone guard run")
    if code is None:
        print("lastmod_tree_guard: SUPPORTABLE — a git-derived date may be "
              "compared against this build.")
    sys.exit(code or 0)
