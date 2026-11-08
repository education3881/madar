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
from datetime import datetime, timedelta, timezone
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
        c = re.search(r'^\s*-\s*cron:\s*["\']([^"\']+)["\']', text, re.M)
        return (
            path,
            int(t.group(1)) if t else None,
            int(n.group(1)) if n else None,
            c.group(1).strip() if c else None,
        )
    return (candidates[0] if candidates else None, None, None, None)


def cron_delay(cron: str, started):
    """Minutes between the run's cron instant and its actual start.

    Added 2026-10-18 under ruling #107. The schedule was the one bound in this
    operation nobody had ever measured: `madar-daily.yml`'s own header says, in
    writing, that if a run is *still hours late on this offset the delay is not
    contention* and the planning assumption must change -- a trigger with a
    condition, a consequence and **nobody named to evaluate it**. Measured over
    all 38 scheduled runs since the 2026-09-15 offset change: every one started
    between **4h14m and 7h42m** after its cron, median 5h37m, and no artefact of
    the operation said so. **Re-measured at the 2026-11-01 weekly review, which
    the CHARTER names as this column's owner: 54 runs now, band 4h14m to 7h43m,
    median 5h34m, still zero inside four hours.** The band and the median did
    not move; the POPULATION did, by sixteen, and this literal had not been
    re-read in fourteen days -- a hardcoded figure in the instrument built
    because recording a number is not measuring it (#124's shape, one desk
    over). The number is now printed by the run itself on every
    call, because recording a median in a document is the error #105 is about.

    Only minute-and-hour crons are read -- `23 4 * * *` and `23 5 * * 0`, which
    are the two this repository has. A field this parser cannot read returns
    None and the line prints as unread rather than as zero.
    """
    parts = cron.split()
    if len(parts) != 5 or not parts[0].isdigit() or not parts[1].isdigit():
        return None, None
    minute, hour = int(parts[0]), int(parts[1])
    fire = started.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if fire > started:
        fire -= timedelta(days=1)
    # THE DAY-OF-WEEK FIELD, and the first draft dropped it. `23 5 * * 0` is
    # the weekly, and rolling back a DAY from a Tuesday start would have named
    # a Monday 05:23 that is not a cron instant at all -- a delay figure that
    # is wrong rather than unread, which is the one output this tool must not
    # produce (it REFUSES rather than remembering, by design). Found by a bite
    # on a start instant three hours before the cron hour, not by reading the
    # code. Cron weekdays are 0=Sunday; Python's weekday() is 0=Monday.
    if parts[4].isdigit():
        want = int(parts[4]) % 7
        while (fire.weekday() + 1) % 7 != want:
            fire -= timedelta(days=1)
    return fire, (started - fire).total_seconds() / 60.0


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


TURNS_REGISTER = Path("agents/stats/run-turns.jsonl")

# THE CRON BAND IS A MEASUREMENT AND WAS BEING KEPT AS PROSE, in two homes, for
# the third week running. The CHARTER's cadence table names the weekly review as
# this column's owner; the 2026-11-01 review re-measured it (54 runs, 4.2–7.7 h,
# median 5.6 h), moved both homes, and recorded that *the band did not move in
# sixteen further runs, which is the strongest form the falsification has taken*
# — and it was broken the NEXT DAY, by the 2026-11-02 run at 8.15 h. Seven days
# later both homes were stale again. So the band is now DERIVED from a register
# the same way #136 derives the turn base rate, and for the same reason: a
# literal is a measurement that has stopped being taken.
#
# IT IS A DIFFERENT POPULATION FROM THE TURN REGISTER AND IS KEPT SEPARATE
# DELIBERATELY. The band is *every scheduled run since the 2026-09-15 cron
# offset change* — 62 today, read from `gh run list`, which is cheap. The turn
# register holds the 47 whose agent-step logs could still be read. Pooling them
# would silently narrow the band to the runs whose logs survived, and a
# population that shrinks because evidence expired is #111's lesson: a gap
# because we were budgeted is an observation about us, not about the world.
BAND_REGISTER = Path("agents/stats/cron-band.json")
OFFSET_CHANGE = "2026-09-15"


def read_band(root: Path, workflow: str | None):
    path = root / BAND_REGISTER
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except ValueError:
        return None
    if workflow and workflow in data.get("per_workflow", {}):
        return data["per_workflow"][workflow] | {"measured_at": data.get("measured_at")}
    return data.get("all") | {"measured_at": data.get("measured_at")} if data.get("all") else None

# THE TURN AXIS IS DARK FROM INSIDE A RUN AND LIT FROM OUTSIDE ONE (ruling #136).
#
# #105 found half this envelope observable and said the other half was not. That
# was right about THIS run and wrong about every previous one. A completed run's
# agent step writes a final result record into its own Actions log carrying
# `"num_turns": N` and `"subtype"`, and that log is readable with the
# `actions: read` grant the job already holds — so the number this run cannot
# know about itself is on record for all 47 runs before it. Same move as #128:
# no run can observe its own publication, so each run observes the previous
# one's. Here no run can count its own turns, so each run reads the ones behind
# it.
#
# WHAT THIS BUYS AND WHAT IT DOES NOT. It does not tell a run its position; a
# base rate is not a measurement of you. It tells a run the SHAPE of the cap it
# is working inside, which is what a planning decision actually needs and what
# `UNMEASURABLE` withheld for 21 days while three runs died at it.
#
# COST, because this is called at every function close. The read is free: the
# register is a file. Only `--observe-turns` touches the network, and it is
# BUDGETED — one log zip is ~4 MB, so a run tops the register up by a few and
# never backfills. Same split as #89 and #111: the expensive half writes the
# chain of memory, the cheap half reads it.
def read_turns(root: Path, workflow: str | None):
    path = root / TURNS_REGISTER
    rows = []
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except ValueError:
                continue
    if workflow:
        rows = [r for r in rows if r.get("workflow") == workflow]
    return [r for r in rows if isinstance(r.get("num_turns"), int)]


def turn_base_rate(rows, cap, timeout_minutes=None):
    """What the cap has done to the runs on record. Never a claim about this one.

    EVERY FIGURE HERE IS DERIVED FROM `rows`, and that sentence is the whole
    discipline of this tool rather than a nicety. The first draft of this
    function printed `the clock has never killed a run; this axis has killed
    three` and `35 to 50 min of 90 unspent` as PROSE — two literals true of the
    47 runs on record on 2026-11-08 — and a synthetic two-row register in the
    proof harness printed `1 hit the cap` directly above `this axis has killed
    three`. That is precisely the defect the 2026-11-01 review found in this
    same file: *a hardcoded literal inside `run_envelope.py`, the instrument
    built on the principle that recording a number is not measuring it.* Found
    by the bite, one reading after writing it.
    """
    if not rows:
        return None
    vals = sorted(r["num_turns"] for r in rows)
    n = len(vals)
    med = vals[n // 2] if n % 2 else (vals[n // 2 - 1] + vals[n // 2]) / 2
    at_cap = [r for r in rows if cap is not None and r["num_turns"] >= cap]
    near = [r for r in rows if cap is not None and cap - 10 <= r["num_turns"] < cap]
    # How much wall clock the cap-killed runs had left, derived from their own
    # recorded durations against the timeout parsed from the workflow file.
    spare = [timeout_minutes - r["duration_min"]
             for r in at_cap
             if timeout_minutes and isinstance(r.get("duration_min"), int)]
    # Did the measurable axis ever end a run? A row whose duration reached the
    # timeout is a clock kill. Derived, so it can become true without an edit.
    clock_kills = [r["date"] for r in rows
                   if timeout_minutes and isinstance(r.get("duration_min"), int)
                   and r["duration_min"] >= timeout_minutes]
    return {
        "n": n, "median": med, "max": vals[-1], "min": vals[0],
        "at_cap": len(at_cap), "within_10": len(near),
        "at_cap_dates": [r["date"] for r in at_cap],
        "at_cap_spare_min": (min(spare), max(spare)) if spare else None,
        "clock_kills": clock_kills,
        "longest_run_min": max((r["duration_min"] for r in rows
                                if isinstance(r.get("duration_min"), int)),
                               default=None),
    }


def write_band(root: Path) -> None:
    """Re-measure the cron band from `gh run list` and write it to disk.

    Cheap — a run list, not a log — so it runs on every `--observe-turns` call
    and the default read stays offline. The cron minute for each workflow is
    parsed from the workflow file, never copied, so a cron change moves this
    measurement by itself.
    """
    import subprocess
    out = {"measured_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
           "offset_change": OFFSET_CHANGE, "per_workflow": {}}
    pooled = []
    for wf in ("madar-daily.yml", "madar-weekly.yml"):
        wf_path, _, _, cron = parse_budget(root, wf)
        if not cron:
            continue
        parts = cron.split()
        try:
            cm, ch = int(parts[0]), int(parts[1])
        except (IndexError, ValueError):
            continue
        try:
            raw = subprocess.run(
                ["gh", "run", "list", "--workflow", wf, "--limit", "100",
                 "--json", "databaseId,createdAt,event"],
                capture_output=True, text=True, timeout=120, check=True).stdout
        except Exception:                              # noqa: BLE001
            continue
        late = []
        for r in json.loads(raw):
            if r.get("event") != "schedule":
                continue
            if r["createdAt"][:10] < OFFSET_CHANGE:
                continue
            st = _parse_iso(r["createdAt"])
            fire = st.replace(hour=ch, minute=cm, second=0, microsecond=0)
            if fire > st:
                fire -= timedelta(days=1)
            late.append(((st - fire).total_seconds() / 3600.0, r["createdAt"][:10]))
        if not late:
            continue
        late.sort()
        vals = [x[0] for x in late]
        n = len(vals)
        out["per_workflow"][wf] = {
            "cron": cron, "n": n,
            "min_h": round(vals[0], 2), "max_h": round(vals[-1], 2),
            "median_h": round(vals[n // 2] if n % 2
                              else (vals[n // 2 - 1] + vals[n // 2]) / 2, 2),
            "inside_four_hours": sum(1 for v in vals if v < 4.0),
            "earliest_date": late[0][1], "latest_date": late[-1][1],
        }
        pooled.extend(late)
    if pooled:
        pooled.sort()
        vals = [x[0] for x in pooled]
        n = len(vals)
        out["all"] = {"n": n, "min_h": round(vals[0], 2), "max_h": round(vals[-1], 2),
                      "median_h": round(vals[n // 2] if n % 2
                                        else (vals[n // 2 - 1] + vals[n // 2]) / 2, 2),
                      "inside_four_hours": sum(1 for v in vals if v < 4.0),
                      "earliest_date": pooled[0][1], "latest_date": pooled[-1][1]}
        (root / BAND_REGISTER).write_text(
            json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"  cron band re-measured ...... {n} scheduled run(s) since "
              f"{OFFSET_CHANGE}: {out['all']['min_h']:g}–{out['all']['max_h']:g} h, "
              f"median {out['all']['median_h']:g} h, "
              f"{out['all']['inside_four_hours']} inside four hours "
              f"→ {BAND_REGISTER}")


def observe_turns(root: Path, budget: int) -> int:
    """Top the register up from the Actions logs of runs it does not hold.

    The only network half of this tool. It asks `gh` for completed runs of both
    scheduled workflows, skips every run already on record, and for at most
    `budget` of the remainder downloads the run log and reads `num_turns` and
    `subtype` out of the agent step's final result record. The log member is
    named for the job (`0_run.txt` for the daily, `0_review.txt` for the
    weekly), so the extractor reads whichever member is present rather than
    assuming one — the first cut of this measurement assumed `0_run.txt` and
    silently returned NA for all seven weekly runs, which looked exactly like
    seven runs that had never reported a turn count.
    """
    import subprocess
    path = root / TURNS_REGISTER
    have = {r["run_id"] for r in read_turns(root, None) if "run_id" in r}
    wanted = []
    for wf in ("madar-daily.yml", "madar-weekly.yml"):
        try:
            out = subprocess.run(
                ["gh", "run", "list", "--workflow", wf, "--limit", "20",
                 "--json", "databaseId,conclusion,createdAt,status"],
                capture_output=True, text=True, timeout=120, check=True).stdout
        except Exception as exc:                       # noqa: BLE001
            print(f"REFUSED run_envelope --observe-turns — `gh run list` for "
                  f"{wf} failed: {exc}")
            return 4
        for r in json.loads(out):
            if r.get("status") == "completed" and r["databaseId"] not in have:
                wanted.append((r["createdAt"][:10], r["databaseId"],
                               r.get("conclusion"), wf))
    wanted.sort(reverse=True)
    if not wanted:
        print("OK run_envelope --observe-turns — the register already holds "
              f"every completed run `gh` reports ({len(have)} on record).")
        # The band is re-measured even when no turn row is owed: its population
        # is every scheduled run, not every run whose log survived, so it moves
        # on days this register does not.
        write_band(root)
        return 0
    print(f"run_envelope --observe-turns — {len(wanted)} run(s) not on record, "
          f"fetching at most {budget} (a log is ~4 MB, so no run backfills)")
    added = 0
    for date, rid, concl, wf in wanted[:max(0, budget)]:
        try:
            blob = subprocess.run(
                ["gh", "api", f"repos/{{owner}}/{{repo}}/actions/runs/{rid}/logs"],
                capture_output=True, timeout=300, check=True).stdout
            import io, zipfile
            zf = zipfile.ZipFile(io.BytesIO(blob))
            member = next((m for m in zf.namelist()
                           if m.endswith(("0_run.txt", "0_review.txt"))), None)
            if member is None:
                print(f"  {date} run {rid} — no agent-step log member; SKIPPED")
                continue
            text = zf.read(member).decode("utf-8", "replace")
            turns = re.findall(r'"num_turns":\s*(\d+)', text)
            sub = re.findall(r'"subtype":\s*"([a-z_]+)"', text)
            dur = re.findall(r'"duration_ms":\s*(\d+)', text)
            if not turns:
                print(f"  {date} run {rid} — no num_turns in the log; SKIPPED")
                continue
            row = {"date": date, "run_id": rid, "workflow": wf,
                   "conclusion": concl, "num_turns": int(turns[-1]),
                   "duration_min": int(dur[-1]) // 60000 if dur else None,
                   "subtype": sub[-1] if sub else None,
                   "observed_at": datetime.now(timezone.utc)
                                  .replace(microsecond=0).isoformat(),
                   "observed_by": "run_envelope --observe-turns"}
            with path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(row, ensure_ascii=False) + "\n")
            added += 1
            print(f"  {date} run {rid} — num_turns {row['num_turns']}, "
                  f"{row['subtype']}, {row['duration_min']} min")
        except Exception as exc:                       # noqa: BLE001
            print(f"  {date} run {rid} — fetch failed, left unrecorded: {exc}")
    print(f"  appended ................... {added} row(s) to {TURNS_REGISTER}")
    write_band(root)
    if len(wanted) > budget:
        print(f"  still owed ................. {len(wanted) - budget} run(s), "
              "which the next call picks up. A register topped up across runs "
              "is #111's pacing: a gap because we were budgeted is an "
              "observation about us, not about the world.")
    return 0


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
    ap.add_argument("--observe-turns", action="store_true",
                    help="network: top the turn register up from the Actions "
                         "log of runs it does not yet hold (budgeted)")
    ap.add_argument("--observe-budget", type=int, default=3,
                    help="how many run logs --observe-turns may fetch in one "
                         "call; a log is ~4 MB, so no run backfills")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    wf_path, timeout_minutes, max_turns, cron = parse_budget(root, args.workflow)

    if args.observe_turns:
        return observe_turns(root, args.observe_budget)

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

    # Scoped to THIS workflow, because the two have different shapes — the
    # weekly review's median is 112 turns and the daily's is 140 — and a base
    # rate pooled across both would be a number about neither.
    rate = turn_base_rate(read_turns(root, wf_path.name), max_turns,
                          timeout_minutes)

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
        "turn_axis": "UNMEASURABLE FOR THIS RUN",
        "turn_base_rate": rate,
        "verdict": "BANK NOW" if breached else "room remains",
    }

    if args.json:
        print(json.dumps(record, ensure_ascii=False, indent=2))
    else:
        head = "BANK NOW" if breached else "OK"
        print(f"{head} run_envelope — wall clock, the measurable half of the envelope")
        print(f"  budget parsed from ......... {record['workflow']}")
        print(f"  run started ................ {record['started_at']}  ({how})")
        if cron:
            fire, late = cron_delay(cron, started)
            if late is None:
                print(f"  cron ....................... '{cron}' — not a fixed "
                      "hour-and-minute this parser reads, so the delay is UNREAD")
            else:
                print(f"  cron ....................... {cron}  →  "
                      f"{fire.strftime('%H:%M')}Z, so this run began "
                      f"{late/60:.1f} h late")
                band = read_band(root, None)
                if band is None:
                    print("    The band this is ordinary against is UNREAD: no cron-band")
                    print("    register on disk. Run `--observe-turns` to measure it (#136).")
                else:
                    print(f"    Normal, measured, and nobody's fault: all {band['n']} scheduled runs")
                    print(f"    since the {OFFSET_CHANGE} offset change began {band['min_h']:g} to "
                          f"{band['max_h']:g} h after their")
                    print(f"    cron (median {band['median_h']:g} h, "
                          f"{band['inside_four_hours']} of {band['n']} inside four hours), "
                          f"measured from the")
                    print(f"    run list rather than recorded in prose — last re-measured "
                          f"{(band.get('measured_at') or '?')[:10]}.")
                    print("    A delay in this band is ordinary and is NOT evidence of a missed")
                    print("    run (#107). It does mean the day starts in the Dubai afternoon,")
                    print("    which is what the CHARTER's cadence table says.")
        print(f"  now ........................ {record['now']}")
        print(f"  elapsed .................... {elapsed:.1f} of {timeout_minutes} min")
        print(f"  remaining .................. {remaining:.1f} min "
              f"(reserve {args.reserve_minutes:g})")
        print(f"  job is killed at ........... {record['deadline_utc']}")
        print()
        print(f"  TURN AXIS .................. UNMEASURABLE FOR THIS RUN. The cap is "
              f"--max-turns {max_turns if max_turns is not None else '<not found>'}, "
              f"parsed from the")
        print("    same file, and nothing inside the agent step counts turns — no file,")
        print("    no variable, no API field. That is a fact about THIS run only.")
        if rate is None:
            print("    And the base rate is UNREAD: no turn register on disk. Run")
            print("    `run_envelope.py . --observe-turns` to start one (#136).")
        else:
            print(f"    MEASURED ON THE {rate['n']} RUNS BEFORE IT, from their own Actions")
            print(f"    logs (#136): median {rate['median']:g}, range {rate['min']}–{rate['max']}, "
                  f"and {rate['at_cap']} hit the cap")
            if rate["at_cap_dates"]:
                print(f"      and DIED there — {', '.join(rate['at_cap_dates'])}")
                if rate["at_cap_spare_min"]:
                    lo, hi = rate["at_cap_spare_min"]
                    print(f"      with {lo:g} to {hi:g} min of {timeout_minutes:g} "
                          "wall clock UNSPENT on each.")
            print(f"    {rate['within_10']} more finished within 10 turns of it.")
            if rate["clock_kills"]:
                print(f"    The clock has ended {len(rate['clock_kills'])} run(s) "
                      f"({', '.join(rate['clock_kills'])}); this axis has ended "
                      f"{rate['at_cap']}.")
            elif rate["longest_run_min"] is None:
                # A register can hold turn counts and no durations; the clock
                # claim is then UNREAD rather than false. Found by the bite,
                # whose synthetic rows carried no `duration_min` and crashed
                # the formatter — a tool that dies on a thin register is a tool
                # that stops being called.
                print("    Whether the clock has ever ended a run is UNREAD: no row on")
                print(f"    record carries a duration. This axis has ended {rate['at_cap']}.")
            else:
                print(f"    The clock has ended NO run on record — the longest ran "
                      f"{rate['longest_run_min']:g} of")
                print(f"    {timeout_minutes:g} min — and this axis has ended "
                      f"{rate['at_cap']}.")
            print("    A base rate is NOT your position; it is the shape of the cap you")
            print("    are working inside, which is what `UNMEASURABLE` withheld.")
        print("    Commit at the close of every standing function (#96) regardless of")
        print("    what either number says.")
        if breached:
            print()
            print("  The reserve is reached. Close the current function, commit and")
            print("  push it, then write the brief against work already on origin.")

    return 3 if breached else 0


if __name__ == "__main__":
    sys.exit(main())
