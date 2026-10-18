#!/usr/bin/env python3
"""
run_envelope — report where THIS run stands against the envelope that binds it.

Not an assertion. It fails no build and it is deliberately not named `qa_*`: the
assertion count is globbed from `qa_*.py` (`qa_patch_queue`), and an instrument
that reports a position rather than judging an artefact is not a thirty-third
standing assertion. Second non-assertion instrument in `agents/tools/`, after
`lastmod_tree_guard.py`.

WHY (standing-queue item 11, raised 2026-10-11, taken 2026-10-18 at 7 days and
six displacements — the oldest item past the three-displacement threshold)
---------------------------------------------------------------------------
The item is titled *the run envelope is invisible to the run it binds*, and it
recorded its own actionable half as **applied**: `CLAUDE.md` now carries both
numbers, and the RUNBOOK requires a commit at the close of every standing
function (#96). The half it could not take was a workflow write, staged at
`agents/patches/2026-10-11-run-envelope-and-checkpoints.md`.

**That accounting was wrong on one of the two axes, and this file is the
correction.** The envelope has two bounds and they are not symmetric:

  --max-turns 180      a TURN bound. Nothing the agent step can read counts
                       turns. There is no file, no variable and no API field.
                       Genuinely dark from in here.

  timeout-minutes: 90  a WALL-CLOCK bound. The run's own start instant is
                       readable with the credential this identity already
                       holds — `actions: read` is granted in the same job
                       block that sets the timeout — and the current instant
                       is readable from the runner's clock. Measured on
                       2026-10-18 on the first attempt:
                         run_started_at 2026-10-18T08:53:10Z, answered in
                         under a second by
                         `gh api repos/{owner}/{repo}/actions/runs/$GITHUB_RUN_ID`.

So **half the envelope was measurable from inside the whole time, and no run in
the five since 10-11 ever looked** — because recording the two numbers in
`CLAUDE.md` read as closing the gap. It did not. A number in prose tells a run
what the limit IS; it does not tell the run WHERE IT STANDS against it. A
constant is not a measurement, and the distance between them is the entire
defect this file closes (ruling #105).

THE ASYMMETRY IS PRINTED, NOT HIDDEN
------------------------------------
This instrument reports one axis and the other stays dark. That is exactly the
shape of the silent-pass trap the enumeration family keeps finding: a green on
the axis you can see, read as a green on the thing. So every report prints the
turn axis as **UNMEASURABLE**, with the reason, in the same block as the
minutes. A run that reads `62 minutes left` must not be able to come away
believing its envelope is safe — on 2026-10-11 the run that lost a whole day's
work to `error_max_turns` had, by this instrument's reckoning, ample minutes.

THE BUDGET IS PARSED, NEVER COPIED
----------------------------------
`timeout-minutes` and `--max-turns` are read out of `.github/workflows/*.yml`
on every invocation. Copying either into this file would make it their next
home and this tool the next entry in the drift family the 09-27 amendment is
about (*where else does this number live? grep for it, do not remember it*).
`CLAUDE.md` carries them as prose for a reader; this file refuses to.

If the budget cannot be parsed, the instrument **refuses** rather than falling
back on a remembered 90 — exit 4, the same code and the same reason as
`lastmod_tree_guard`: an unsupportable number printed calmly is how two QA logs
came to contain a conclusion drawn from a 0/0.

THE RESERVE IS A JUDGMENT, AND IT IS MADE CHECKABLE
---------------------------------------------------
`--reserve-minutes` defaults to **15**. That is a judgment, not a measurement:
it is the room the closing function needs to write the brief, the manager
status and the stats panel and get them onto `origin`, plus the ~40 seconds the
job's own post-agent steps take (the brief summary and the deploy dispatch).
Nothing had ever measured it, because nothing had ever measured any run's
wall clock at all.

`--log` is how it stops being a judgment. It appends one line per call to
`agents/stats/run-envelope.jsonl` with the run id, the label passed, and the
elapsed minutes — so the cost of each standing function accumulates as a
population, and a later run can set the reserve from its own history instead of
from this paragraph. Same shape as `madar_stats.py --log`, and the same reason.

EXIT CODES
----------
  0  measured, and more than the reserve remains
  3  measured, and the reserve is reached or breached — BANK NOW
  2  cannot measure (not inside Actions, no run id, or the API did not answer)
  4  REFUSED — the budget is not parseable from the workflow file; no guess

3 rather than 1 for the low-margin case on purpose: 1 is the drift/failure code
everywhere else in this directory, and a run approaching its own ceiling has
found no defect. Nothing is wrong with the publication; the run is simply
nearly over.

USAGE
-----
  python3 agents/tools/run_envelope.py .
  python3 agents/tools/run_envelope.py . --log --label "quality"
  python3 agents/tools/run_envelope.py . --reserve-minutes 20
  python3 agents/tools/run_envelope.py . --started-at 2026-10-18T08:53:10Z   # proof harness
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKFLOW_DIR = Path(".github/workflows")
LOG_PATH = Path("agents/stats/run-envelope.jsonl")

# The two workflows that carry an agent step, keyed by the `name:` they declare,
# because GITHUB_WORKFLOW holds the declared name and not the file path.
AGENT_WORKFLOWS = ("madar-daily.yml", "madar-weekly.yml")


def parse_budget(root: Path, workflow: str | None):
    """Read timeout-minutes and --max-turns out of the workflow file itself.

    Returns (path, timeout_minutes, max_turns). Any of the last two may be None,
    which the caller treats as a refusal rather than as a default.
    """
    candidates = []
    if workflow:
        candidates = [root / WORKFLOW_DIR / workflow]
    else:
        declared = os.environ.get("GITHUB_WORKFLOW", "")
        for name in AGENT_WORKFLOWS:
            p = root / WORKFLOW_DIR / name
            if not p.is_file():
                continue
            text = p.read_text(encoding="utf-8")
            m = re.search(r"^name:\s*(.+)$", text, re.M)
            if declared and m and m.group(1).strip() == declared.strip():
                candidates = [p]
                break
            candidates.append(p)
        # No GITHUB_WORKFLOW (a hand run): the daily is the right default, and
        # the choice is printed so a weekly run cannot read a daily's budget
        # without noticing.
        if len(candidates) > 1:
            candidates = candidates[:1]

    for path in candidates:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        t = re.search(r"^\s*timeout-minutes:\s*(\d+)\s*$", text, re.M)
        n = re.search(r"--max-turns\s+(\d+)", text)
        return (
            path,
            int(t.group(1)) if t else None,
            int(n.group(1)) if n else None,
        )
    return (candidates[0] if candidates else None, None, None)


def run_started_at(override: str | None):
    """The run's own start instant. Returns (datetime, how) or (None, why)."""
    if override:
        return _parse_iso(override), "passed with --started-at"

    run_id = os.environ.get("GITHUB_RUN_ID")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not run_id or not repo:
        return None, "not inside a GitHub Actions run (no GITHUB_RUN_ID/REPOSITORY)"

    try:
        out = subprocess.run(
            ["gh", "api", f"repos/{repo}/actions/runs/{run_id}",
             "--jq", ".run_started_at"],
            capture_output=True, text=True, timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None, f"gh api did not answer ({exc.__class__.__name__})"
    if out.returncode != 0:
        return None, f"gh api exit {out.returncode}: {out.stderr.strip()[:120]}"
    stamp = out.stdout.strip()
    if not stamp or stamp == "null":
        return None, "the API answered with no run_started_at"
    return _parse_iso(stamp), f"gh api, run {run_id}"


def _parse_iso(stamp: str):
    s = stamp.strip().replace("Z", "+00:00")
    dt = datetime.fromisoformat(s)
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def main() -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("root", nargs="?", default=".", help="repository root")
    ap.add_argument("--workflow", default=None,
                    help="workflow file name under .github/workflows/")
    ap.add_argument("--reserve-minutes", type=float, default=15.0)
    ap.add_argument("--started-at", default=None,
                    help="override the run's start instant (proof harness)")
    ap.add_argument("--label", default="",
                    help="what the run has just finished, for the log line")
    ap.add_argument("--log", action="store_true",
                    help="append a line to agents/stats/run-envelope.jsonl")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    wf_path, timeout_minutes, max_turns = parse_budget(root, args.workflow)

    if timeout_minutes is None:
        shown = wf_path.relative_to(root) if wf_path and wf_path.is_file() else (
            args.workflow or "<none found>")
        print(f"REFUSED run_envelope — no `timeout-minutes:` parseable from {shown}.")
        print("  The budget is parsed from the workflow file on every run and never")
        print("  copied into this tool, so there is nothing to fall back to. A")
        print("  remembered 90 would be an unsupportable number printed calmly,")
        print("  which is the defect lastmod_tree_guard exists to refuse.")
        return 4

    started, how = run_started_at(args.started_at)
    if started is None:
        print(f"CANNOT MEASURE run_envelope — {how}.")
        print(f"  budget (parsed from {wf_path.relative_to(root)}): "
              f"timeout-minutes {timeout_minutes}, --max-turns "
              f"{max_turns if max_turns is not None else 'not found'}")
        print("  The wall-clock axis needs the run's own start instant. Without it")
        print("  BOTH axes are dark, and this instrument says so rather than")
        print("  reporting the one number it still has.")
        return 2

    now = datetime.now(timezone.utc)
    elapsed = (now - started).total_seconds() / 60.0
    remaining = timeout_minutes - elapsed
    deadline = started.timestamp() + timeout_minutes * 60
    breached = remaining <= args.reserve_minutes

    if args.log:
        log = root / LOG_PATH
        log.parent.mkdir(parents=True, exist_ok=True)
        with log.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps({
                "run_id": os.environ.get("GITHUB_RUN_ID", ""),
                "workflow": wf_path.name,
                "label": args.label,
                "at": now.replace(microsecond=0).isoformat(),
                "elapsed_minutes": round(elapsed, 2),
                "timeout_minutes": timeout_minutes,
                "remaining_minutes": round(remaining, 2),
            }, ensure_ascii=False) + "\n")

    record = {
        "workflow": str(wf_path.relative_to(root)),
        "started_at": started.replace(microsecond=0).isoformat(),
        "started_from": how,
        "now": now.replace(microsecond=0).isoformat(),
        "elapsed_minutes": round(elapsed, 2),
        "timeout_minutes": timeout_minutes,
        "remaining_minutes": round(remaining, 2),
        "reserve_minutes": args.reserve_minutes,
        "deadline_utc": datetime.fromtimestamp(deadline, timezone.utc)
                                .replace(microsecond=0).isoformat(),
        "max_turns": max_turns,
        "turn_axis": "UNMEASURABLE",
        "verdict": "BANK NOW" if breached else "room remains",
    }

    if args.json:
        print(json.dumps(record, ensure_ascii=False, indent=2))
    else:
        head = "BANK NOW" if breached else "OK"
        print(f"{head} run_envelope — wall clock, the measurable half of the envelope")
        print(f"  budget parsed from ......... {record['workflow']}")
        print(f"  run started ................ {record['started_at']}  ({how})")
        print(f"  now ........................ {record['now']}")
        print(f"  elapsed .................... {elapsed:.1f} of {timeout_minutes} min")
        print(f"  remaining .................. {remaining:.1f} min "
              f"(reserve {args.reserve_minutes:g})")
        print(f"  job is killed at ........... {record['deadline_utc']}")
        print()
        print(f"  TURN AXIS .................. UNMEASURABLE. The cap is "
              f"--max-turns {max_turns if max_turns is not None else '<not found>'}, "
              f"parsed from the same")
        print("    file, and nothing inside the agent step counts turns — no file, no")
        print("    variable, no API field. A healthy wall clock is NOT a healthy")
        print("    envelope: the run that lost 10-11 to error_max_turns had minutes")
        print("    to spare. Commit at the close of every standing function (#96)")
        print("    regardless of what the number above says.")
        if breached:
            print()
            print("  The reserve is reached. Close the current function, commit and")
            print("  push it, then write the brief against work already on origin.")

    return 3 if breached else 0


if __name__ == "__main__":
    sys.exit(main())
