# A concurrency group binds only the runners inside it

**Filed:** 2026-09-29, desktop runner · **Status:** candidate — for the weekly review to adopt into
`/agents/guidebook` with a register number, or to reject. Not filed into the register by this run,
because a second runner writing to the register is the defect this note is about.

## The observation

`madar-weekly.yml` shares the `madar-autonomous-run` concurrency group with `madar-daily.yml`
deliberately. Its own comment gives the reason: *"On a Sunday both are due within an hour of each
other, and two agents editing the guidebook index at the same time is exactly how the 2026-08-23
near-clobber happened."*

That reasoning is correct and the fix works — **for the two runners inside the group.** It has no
reach over a runner scheduled on a different surface. A Cowork scheduled task firing against a
desktop checkout is not a GitHub Actions job, holds no lease on that group, and cannot be serialised
by it. Against such a runner a concurrency group is not a weak guard; it is not a guard at all.

**The only available control on a runner outside the group is to retire it.**

## The corollary that cost fifteen days

**A cadence is not a runner.** The 2026-09-14 migration retired the desktop cadence *as written in
the repository* — it moved the schedule into `madar-daily.yml` and the commit message declares both
dependencies ended. The schedule written **outside** the repository was never named in that
migration, and nothing in the repository can name it. It kept firing for fifteen days and produced
two complete duplicate days (09-25, 09-28), uncommitted, one of them colliding at an identical path
with the canonical brief.

Generalised: **a migration is only complete over the surfaces it can enumerate.** When work moves
from surface A to surface B, the migration's own record lives on B and is structurally blind to what
is still scheduled on A. The check is not "is the new runner running" — it is "who else is still
scheduled to do this, and on what surface".

## Why no instrument caught it

Every gap-check in this operation asks whether the day's work **happened**. None asks whether it
happened **once**. A doubled day passes every one of them: the commits are there, the brief is there,
the deploy is green. The duplicate is only visible in the working tree of a machine no assertion
runs on.

The cheapest detector, if the runner is kept: a brief that carries a number must fail when its number
already exists on `origin`.

## Second ruling, same root

**`--log` is a write.** The brief template instructs *every run* to call
`madar_stats.py --log`, which appends a dated snapshot to `agents/stats/history.jsonl` — a series
whose entire purpose is week-over-week deltas. Reissued to a second runner on the same date, that
instruction produces a duplicate row and silently corrupts every delta computed across it.

**An instruction that mutates shared state is not safely reissued to a second executor.** Any such
instruction must name which runner owns the mutation. This run called the script without `--log`,
which is why today's series is still one row per day.

## Test that would have caught both

Before a run writes anything, have it answer in writing: *what else is scheduled to do this work
today, and on what surface?* The answer is one `curl` against the Actions API and one look at the
task list. On 2026-09-29 that question, asked at 11:14Z, would have returned "a run is in progress,
started 10:44:03Z" — and stopped this run before it read a single article.
