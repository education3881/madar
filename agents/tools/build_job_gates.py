#!/usr/bin/env python3
"""
build_job_gates — run the gates a LOCAL build cannot reach, derived from the
workflow file rather than copied out of it.

WHY THIS EXISTS (2026-10-21, after the 10-20 deploy went red)
-------------------------------------------------------------
Thirty-two of the thirty-five standing assertions gate the deploy, and they
live in two homes: **twelve** are steps in `astro-pages.yml`'s build job and
**twenty** are chained from `postbuild` in `web/package.json`. A run on this
machine executes `npm run build`, which runs the twenty. **It does not run the
twelve, and nothing on the runner says so.**

On 2026-10-20 that cost the operation a day of publication. The growth function
gave the forty browse pages `isPartOf` and `publisher` pointers without
spreading `publisherNodes()`, every browse page shipped two dangling `@id`s,
and `qa_jsonld` — a build-job step — failed the deploy. The run built four
times, called the gates green, pushed five commits and finished. The origin did
not move for two days. **A local "all gates green" was 20 of 32 and read
exactly like 32 of 32.**

`CLAUDE.md` has always said to run the others by hand — *"and the other eleven
that run as build steps"* — which is a list in prose, maintained by nobody, and
it says eleven where the file has twelve.

WHAT THIS IS, AND WHAT IT IS NOT
--------------------------------
It is a **runner**, not an assertion: the count of standing assertions globs
`qa_*.py`, and this file asserts nothing of its own. It parses the workflow,
extracts every `qa_*.py` invocation in the `build` job with its real arguments,
runs each one, and reports. Derived, never copied — so it cannot tell you about
eleven gates when there are twelve.

**It IS wired into `postbuild`, from the afternoon of the day it was written**
— standing-queue item 30, opened and closed in one run. It was a runner for
about an hour, and a runner somebody must remember is precisely the shape
2026-09-13 named as *a habit, not a gate*. The cost that argued against wiring
it was assumed and then measured: **all twelve run in 1.88 s**, and a full
`npm run build` with all thirty-two gates takes **32 s**. The twelve do now run
twice in CI, once as workflow steps and once here, and two seconds is not a
reason to let a local build mean something different from a deploy.

**Proved by re-injecting the defect that caused the gap:** removing
`...publisherNodes()` from `collectionJsonLd` again — the exact 2026-10-20
regression — now turns `npm run build` red at exit 1 on this machine, where on
2026-10-20 it exited 0 four times in a row. Restored, the build is green.

It adds ONE entry to `postbuild` and no assertion to the count: `qa_patch_queue`
globs `qa_*.py` in both homes, so the register still reads 35 / 12 / 20 /
**32 of 35**, which is correct — these twelve always gated the deploy. What
changed is where they can be *reached*.

Usage:  python3 agents/tools/build_job_gates.py [repo-root] [--dist web/dist]
Exit:   0 all green · 1 one or more gates failed · 2 cannot parse the workflow
"""
from __future__ import annotations

import pathlib
import re
import shlex
import subprocess
import sys

WORKFLOW = pathlib.Path(".github/workflows/astro-pages.yml")
INVOCATION = re.compile(r"python3\s+(agents/tools/qa_[a-z0-9_]+\.py[^\n&|]*)")


def gates_in_build_job(root: pathlib.Path) -> list[str]:
    text = (root / WORKFLOW).read_text(encoding="utf-8")
    # Everything up to the next top-level job key is the build job; the deploy
    # and verify jobs run no qa_* step today, and if they ever do this slice is
    # what keeps them out of a list about the BUILD job.
    start = text.find("\n  build:")
    end = text.find("\n  deploy:", start if start >= 0 else 0)
    body = text[start if start >= 0 else 0 : end if end > 0 else len(text)]
    seen, out = set(), []
    for match in INVOCATION.findall(body):
        cmd = match.strip()
        if cmd not in seen:
            seen.add(cmd)
            out.append(cmd)
    return out


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    root = pathlib.Path(args[0]).resolve() if args else pathlib.Path.cwd()
    if not (root / WORKFLOW).exists():
        print(f"CANNOT MEASURE build_job_gates — no {WORKFLOW} under {root}")
        return 2
    gates = gates_in_build_job(root)
    if not gates:
        print("CANNOT MEASURE build_job_gates — parsed the workflow and found no qa_* build step")
        return 2

    print(f"build_job_gates — {len(gates)} gate(s) parsed out of {WORKFLOW}, not copied from prose")
    failures = []
    for cmd in gates:
        parts = ["python3"] + shlex.split(cmd)
        name = shlex.split(cmd)[0].rsplit("/", 1)[-1][:-3]
        proc = subprocess.run(parts, cwd=root, capture_output=True, text=True)
        tail = [l for l in (proc.stdout or proc.stderr or "").strip().split("\n") if l.strip()]
        print(f"  {'ok  ' if proc.returncode == 0 else 'FAIL'} {name:<24} exit {proc.returncode}"
              f"   {tail[-1][:88] if tail else ''}")
        if proc.returncode != 0:
            failures.append((name, tail[-12:]))

    if failures:
        for name, tail in failures:
            print(f"\n--- {name} ---")
            for line in tail:
                print(f"  {line}")
        print(f"\nFAIL build_job_gates — {len(failures)} of {len(gates)} build-job gate(s) red. "
              f"Before 2026-10-21 these did not run under `npm run build` at all, and a defect here "
              f"reached the deploy past a green local build.")
        return 1
    print(f"CLEAN build_job_gates — all {len(gates)} build-job gates green against this tree's dist, "
          f"so the local gate set is the deploy's gate set rather than two-thirds of it.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
