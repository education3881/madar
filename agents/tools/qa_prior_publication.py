#!/usr/bin/env python3
"""qa_prior_publication — the publication nobody in this operation has ever watched.

Standing assertion 42. Raised as standing-queue **item 31** on 2026-10-21 as the daily's
forward question and taken from the OPEN head on 2026-11-05 at **15 days**, the oldest row
on the board.

WHAT THE ITEM ASKED
-------------------
*Which of this operation's claims are checked only by the NEXT run's goodwill?*

Every instrument this operation owns runs inside the agent step, and the deploy runs after
that step ends. **So no run has ever observed its own publication.** Ruling #71 handles the
consequence in prose — *every brief carries the previous run's deploy ID, its conclusion and
a `qa_live_drift` result* — and **nothing fails when that sentence is not honoured.** On
2026-10-20 a run finished green, pushed five commits, wrote its brief, and its deploy failed
seven minutes later; the origin then served the 10-19 build for two days. The only reason
anybody knows is that the next run happened to look. Queue item 77 is the same shape with a
second cause: `madar-daily.yml`'s publish step carries `if: success()`, so a run that
overruns banks its work and publishes none of it, and **the resulting strand is invisible in
`git log` by construction** — the commits are all there, in order, with nothing recording
that no deploy ever carried them.

WHAT THIS TOOL DOES, AND THE SPLIT IS LOAD-BEARING
--------------------------------------------------
`--observe` (NETWORK, gates nothing)
    Asks the Actions API for the most recent `astro-pages.yml` run — its id, status,
    conclusion and head SHA — reads the tip of `origin/main` out of the local clone, and
    computes the **strand**: the commits on `main` that no successful deploy has carried.
    Appends one row per call to `agents/stats/publication-observations.jsonl`.
    It gates nothing for the reason #111 and #112 both state: an outage at somebody else's
    API must not stop this publication deploying. If the API does not answer, **no row is
    written** and the exit is 2 — a row that records a failure because we were rate-limited
    is an observation about us rather than about the publication (#111).

`--check` (OFFLINE, deterministic, GATED from `postbuild`)
    Asserts that the register is well-formed, internally re-derivable from this repository's
    own git history, and coherent over time. The point of gating this half is #89's: a
    register nobody is forced to keep stops describing the thing it was built to describe,
    and it does so in silence.

    Limb 1 — SCHEMA. Every row carries the nine required fields, `observed_at` parses as an
             ISO instant, and every SHA field is 40 hex characters or empty.
    Limb 2 — PROVENANCE. For every row whose two SHAs are objects this repository contains,
             `strand_len` must equal `git rev-list --count <deployed>..<tip>`. A row that
             cannot be re-derived from git is a fabricated observation. Rows whose SHAs this
             clone does not hold are PRINTED as unverifiable with their count, never failed:
             a rewritten history must not red a build forever.
    Limb 3 — THE NEWEST ROW IS VERIFIABLE. The newest observation was written by the most
             recent observing run against this same repository, so its SHAs are necessarily
             here. This is the non-vacuity guard, and it is derived rather than counted
             (queue item 67): the guard is *the newest row*, not *N rows*.
    Limb 4 — MONOTONICITY. Ordered by `observed_at`, the deployed SHA never regresses: each
             verifiable row's deployed SHA is an ancestor of, or equal to, the next one's. A
             register that walks backwards is describing something other than one origin.
    Limb 5 — THE DUTY, enforced where it is owed and skipped where it is not. Limbs 1-4 all
             stay green for a run that observes nothing: the rows a previous run wrote stay
             well-formed and re-derivable forever, which is item 31's own defect one level
             out — *a register whose upkeep is checked only by the next run's goodwill.* So
             inside the **daily** run the register must carry a row written by **this**
             `GITHUB_RUN_ID`, and a daily run that builds without observing reds its own
             build with the command it should have run. In the **deploy** job the limb is
             SKIPPED with its reason printed, because the deploy owes no observation and
             must never red for the daily run's silence — that scoping is proved by running
             the same failing tree under `GITHUB_WORKFLOW=Deploy…` and watching it pass.

WHAT IT PRINTS AND DELIBERATELY DOES NOT ASSERT
-----------------------------------------------
The current strand length and the previous deploy's conclusion are printed on every run and
**asserted by nothing**, and the reason is not #93's floor-above-reality. It is sharper and
it belongs in the record:

    **An assertion whose only repair path runs through the artefact it blocks cannot be
    gated.** A red prior deploy is repaired by pushing a commit; a push is made by a run
    whose build is green; so a gate that reds on a red prior deploy forbids the one action
    that would clear it. The 10-21 run would have been unable to build, unable to push, and
    therefore unable to recover the 10-20 strand — the gate would have converted a one-day
    publication gap into a permanent one.

So the strand is a **printed number with a named owner**: the brief reads it (#71), and the
number now exists in a file instead of in whichever run remembers to look.

EXITS
-----
0 = pass · 1 = a limb failed · 2 = cannot measure (no API, no git, no register) ·
4 = refused (bad arguments)

Proved both ways per #35 on the real register, restored byte-identical afterwards: **five bites
red** (a dropped field, a falsified `strand_len`, a newest row naming a SHA this repository does
not hold, a register walked backwards, and a register whose newest row was written by somebody
else's run) and **four controls green** (the register as written; two rows walking forwards; an
old row with a foreign SHA and a sound newest row, which must stay green and print 1
unverifiable; and bite 5's own tree read from the deploy job, which must pass). Every injection
was asserted to have changed the file before the check was run on it.

**Bite 1 was caught twice on its first run** — the schema limb and the provenance limb both
reported it, because provenance read the missing `strand_len` as `None`. *A defect two limbs
catch proves neither of them necessary*, so provenance now declines a row the schema has
already failed, and bite 1 isolates.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REGISTER = Path("agents/stats/publication-observations.jsonl")
DEPLOY_WORKFLOW = "astro-pages.yml"
REQUIRED = (
    "observed_at",
    "observer_run_id",
    "observer_workflow",
    "deploy_run_id",
    "deploy_status",
    "deploy_conclusion",
    "deployed_sha",
    "origin_tip_sha",
    "strand_len",
)
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")


def git(root: Path, *args: str, check: bool = False):
    try:
        out = subprocess.run(
            ["git", "-C", str(root), *args],
            capture_output=True, text=True, timeout=60,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if out.returncode != 0 and check:
        return None
    return out


def has_object(root: Path, sha: str) -> bool:
    if not SHA_RE.match(sha or ""):
        return False
    out = git(root, "cat-file", "-e", f"{sha}^{{commit}}")
    return bool(out) and out.returncode == 0


def rev_count(root: Path, a: str, b: str):
    out = git(root, "rev-list", "--count", f"{a}..{b}")
    if not out or out.returncode != 0:
        return None
    try:
        return int(out.stdout.strip())
    except ValueError:
        return None


def is_ancestor(root: Path, a: str, b: str) -> bool:
    out = git(root, "merge-base", "--is-ancestor", a, b)
    return bool(out) and out.returncode == 0


def load_rows(path: Path):
    rows, broken = [], []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            broken.append((n, f"not JSON ({exc.msg})"))
            continue
        if not isinstance(obj, dict):
            broken.append((n, "not a JSON object"))
            continue
        obj["_line"] = n
        rows.append(obj)
    return rows, broken


# ---------------------------------------------------------------- observe (network)

def gh_api(path: str, jq: str | None = None):
    cmd = ["gh", "api", path]
    if jq:
        cmd += ["--jq", jq]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None, f"gh api did not answer ({exc.__class__.__name__})"
    if out.returncode != 0:
        return None, f"gh api exit {out.returncode}: {out.stderr.strip()[:140]}"
    return out.stdout.strip(), None


def observe(root: Path, write: bool) -> int:
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not repo:
        print("CANNOT MEASURE qa_prior_publication --observe — no GITHUB_REPOSITORY in the")
        print("  environment, so there is no Actions API to ask. This half is network and")
        print("  gates nothing; the gated half is --check.")
        return 2
    raw, err = gh_api(
        f"repos/{repo}/actions/workflows/{DEPLOY_WORKFLOW}/runs?per_page=20",
        ".workflow_runs | map({id, status, conclusion, head_sha, created_at})",
    )
    if err:
        print(f"CANNOT MEASURE qa_prior_publication --observe — {err}")
        print("  No row written. A row that records a failure because we were throttled is")
        print("  an observation about us, not about the publication (#111).")
        return 2
    try:
        runs = json.loads(raw)
    except json.JSONDecodeError:
        print("CANNOT MEASURE qa_prior_publication --observe — the API answer did not parse")
        return 2
    if not runs:
        print(f"CANNOT MEASURE — the API reports no runs of {DEPLOY_WORKFLOW} at all")
        return 2

    latest = runs[0]
    last_good = next(
        (r for r in runs if r.get("conclusion") == "success"), None
    )
    tip_out = git(root, "rev-parse", "origin/main")
    tip = tip_out.stdout.strip() if tip_out and tip_out.returncode == 0 else ""
    deployed = (last_good or {}).get("head_sha", "") or ""

    strand, strand_shas = None, []
    if tip and deployed and has_object(root, tip) and has_object(root, deployed):
        strand = rev_count(root, deployed, tip)
        out = git(root, "log", "--format=%h %s", f"{deployed}..{tip}")
        if out and out.returncode == 0:
            strand_shas = [l.split(" ", 1)[0] for l in out.stdout.splitlines()]

    row = {
        "observed_at": _now(),
        "observer_run_id": os.environ.get("GITHUB_RUN_ID", ""),
        "observer_workflow": os.environ.get("GITHUB_WORKFLOW", "local"),
        "deploy_run_id": str(latest.get("id", "")),
        "deploy_status": latest.get("status") or "",
        "deploy_conclusion": latest.get("conclusion") or "",
        "deployed_sha": deployed,
        "origin_tip_sha": tip,
        "strand_len": strand if strand is not None else -1,
    }

    print("OK qa_prior_publication --observe — the previous publication, read rather than assumed")
    print(f"  latest {DEPLOY_WORKFLOW} run .. {row['deploy_run_id']}"
          f"  status {row['deploy_status'] or '?'}"
          f"  conclusion {row['deploy_conclusion'] or '(none yet)'}")
    print(f"  head of that run ........... {latest.get('head_sha','')[:12]}")
    print(f"  last SUCCESSFUL deploy ..... {deployed[:12] or '(none in the last 20 runs)'}")
    print(f"  tip of origin/main ......... {tip[:12] or '(unknown)'}")
    if strand is None:
        print("  strand ..................... UNMEASURABLE (a SHA is not in this clone)")
    elif strand == 0:
        print("  strand ..................... 0 — the origin is serving the tip")
    else:
        print(f"  strand ..................... {strand} commit(s) on main that NO successful")
        print("    deploy has carried, which is the number that is invisible in git log:")
        for sha in strand_shas[:10]:
            print(f"      {sha}")
        if len(strand_shas) > 10:
            print(f"      … and {len(strand_shas) - 10} more")
    print("  PRINTED AND NOT ASSERTED. An assertion whose only repair path runs through the")
    print("    artefact it blocks cannot be gated: a red prior deploy is repaired by a push,")
    print("    a push is made by a run whose build is green, so gating this would forbid the")
    print("    one action that clears it. The brief reads this number (#71); the gate does not.")

    if write:
        path = root / REGISTER
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(f"  appended ................... {REGISTER}")
    return 0


def _now() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------- check (offline, gated)

def check(root: Path) -> int:
    path = root / REGISTER
    if not path.exists():
        print(f"FAIL qa_prior_publication --check — {REGISTER} does not exist.")
        print("  The register is the operation's only record of whether a run's work was ever")
        print("  published. Run `python3 agents/tools/qa_prior_publication.py . --observe`.")
        return 1
    if git(root, "rev-parse", "--git-dir") is None:
        print("CANNOT MEASURE qa_prior_publication --check — no git here, and every limb is a")
        print("  claim about this repository's own history.")
        return 2

    rows, broken = load_rows(path)
    failures = list(broken and [f"line {n}: {why}" for n, why in broken] or [])

    # Limb 1 — schema
    for row in rows:
        missing = [k for k in REQUIRED if k not in row]
        if missing:
            failures.append(f"line {row['_line']}: missing field(s) {', '.join(missing)}")
            continue
        if not ISO_RE.match(str(row["observed_at"])):
            failures.append(f"line {row['_line']}: observed_at is not an ISO instant")
        for key in ("deployed_sha", "origin_tip_sha"):
            val = str(row[key])
            if val and not SHA_RE.match(val):
                failures.append(f"line {row['_line']}: {key} is not a 40-hex SHA")
        if not isinstance(row["strand_len"], int):
            failures.append(f"line {row['_line']}: strand_len is not an integer")

    if not rows:
        print(f"FAIL qa_prior_publication --check — {REGISTER} holds no rows.")
        print("  An empty register passes every other limb vacuously, which is the 08-09")
        print("  inversion: a green light wired to nothing.")
        return 1

    # Limb 2 — provenance, on the rows this clone can re-derive
    verifiable, unverifiable = [], []
    for row in rows:
        if any(k not in row for k in REQUIRED):
            # Limb 1 already owns this row. A defect two limbs report proves neither of
            # them necessary, so provenance declines a row the schema has already failed.
            continue
        dep, tip = str(row.get("deployed_sha", "")), str(row.get("origin_tip_sha", ""))
        if has_object(root, dep) and has_object(root, tip):
            verifiable.append(row)
            want = rev_count(root, dep, tip)
            got = row.get("strand_len")
            if want is None:
                unverifiable.append(row)
                verifiable.pop()
            elif got != want:
                failures.append(
                    f"line {row['_line']}: strand_len says {got}, git says {want} "
                    f"for {dep[:9]}..{tip[:9]} — the row is not re-derivable"
                )
        else:
            unverifiable.append(row)

    # Limb 3 — the newest row must be verifiable
    newest = max(rows, key=lambda r: (str(r.get("observed_at", "")), r["_line"]))
    if newest in unverifiable:
        failures.append(
            f"line {newest['_line']}: the NEWEST row names a SHA this repository does not "
            "hold. The newest observation was written against this tree, so this is a "
            "fabricated or foreign row, not a history rewrite."
        )

    # Limb 4 — monotonicity of the deployed SHA
    ordered = sorted(verifiable, key=lambda r: (str(r["observed_at"]), r["_line"]))
    for a, b in zip(ordered, ordered[1:]):
        sa, sb = str(a["deployed_sha"]), str(b["deployed_sha"])
        if sa == sb:
            continue
        if not is_ancestor(root, sa, sb):
            failures.append(
                f"line {b['_line']}: the deployed SHA walks BACKWARDS — {sb[:9]} is not a "
                f"descendant of line {a['_line']}'s {sa[:9]}"
            )

    # Limb 5 — the duty, enforced where it is owed and SKIPPED where it is not.
    # A duty is not a gate (queue item 60), and limbs 1-4 would all stay green for a run
    # that never observed anything: the rows a previous run wrote remain well-formed and
    # re-derivable forever. So inside the DAILY run — the one identity that owes the
    # observation — the register must carry a row written by THIS run.
    workflow = os.environ.get("GITHUB_WORKFLOW", "")
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    limb5 = None
    if run_id and "daily" in workflow.lower():
        if any(str(r.get("observer_run_id", "")) == run_id for r in rows):
            limb5 = f"met — run {run_id} observed before it built"
        else:
            failures.append(
                f"the daily run {run_id} has built without observing the previous "
                "publication. Run `python3 agents/tools/qa_prior_publication.py . "
                "--observe` and build again."
            )
            limb5 = f"NOT met — no row written by run {run_id}"
    elif run_id:
        limb5 = (f"skipped — {workflow or 'this workflow'} does not owe the observation; "
                 "the daily run does, and the deploy job must not red for its silence")
    else:
        limb5 = "skipped — not inside a GitHub Actions run, so no run owes anything here"

    label = "FAIL" if failures else "OK"
    print(f"{label} qa_prior_publication --check — the publication register, offline half")
    print(f"  rows ....................... {len(rows)}")
    print(f"  re-derived from git ........ {len(verifiable)}")
    print(f"  unverifiable in this clone . {len(unverifiable)}  "
          "(printed, never failed: a rewritten history must not red a build forever)")
    print(f"  newest observation ......... {newest.get('observed_at','?')} "
          f"by run {newest.get('observer_run_id','?') or 'local'}")
    strand = newest.get("strand_len")
    concl = newest.get("deploy_conclusion") or "(none)"
    print(f"  it recorded ................ deploy {newest.get('deploy_run_id','?')} "
          f"{concl}, strand {strand}")
    print(f"  this run's own duty ........ {limb5}")
    print("  PRINTED AND NOT ASSERTED: the strand and the prior conclusion. An assertion")
    print("    whose only repair path runs through the artefact it blocks cannot be gated —")
    print("    a red prior deploy is cleared by a push, and a push needs a green build.")
    if failures:
        print(f"  {len(failures)} failure(s):")
        for f in failures[:20]:
            print(f"    - {f}")
        if len(failures) > 20:
            print(f"    … and {len(failures) - 20} more")
        return 1
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(add_help=True, description=__doc__.splitlines()[0])
    ap.add_argument("root", help="repository root (this gate is never handed dist)")
    ap.add_argument("--observe", action="store_true",
                    help="network half: ask the Actions API and append a row (gates nothing)")
    ap.add_argument("--check", action="store_true",
                    help="offline half: assert the register (the default, and the gated one)")
    ap.add_argument("--no-write", action="store_true",
                    help="with --observe, print the reading and append nothing")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"REFUSED — {root} is not a directory")
        return 4
    if args.observe and args.check:
        print("REFUSED — the two halves are different modes and are run separately (#89)")
        return 4
    if args.observe:
        return observe(root, write=not args.no_write)
    return check(root)


if __name__ == "__main__":
    sys.exit(main())
