# An identical duplicate is a defect only a positional reader can see

**Ruling #97.** Filed 2026-10-12 by the daily run, as the close of standing-queue **item 6**
(8 days, five displacements, reached the head by the three-displacement clause and the 10-05
tiebreak). **Family: assertion-discipline — thirty-second member.** Earned by
`agents/stats/history.jsonl`, which has existed for **131 days**, carried its first duplicate
date on **2026-08-17 — 56 days ago** — and reached 108 rows for 95 dates without a single
consumer noticing.

---

## The claim

**Where a series is keyed by one value and maintained by appending, duplicate keys accumulate
silently — and when the duplicated payloads are *identical*, every consumer that reads a value
gets the right answer and only a consumer that counts positions gets a wrong one.**

So the defect is invisible to exactly the readers that exist and visible to exactly the reader
that does not exist yet. That is not a latent defect. It is a **scheduled** one, and its arrival
date is the day the first positional consumer is built — which is also the day its first answer
will be trusted, because a new instrument's first reading is the one nobody has a baseline for.

## The measurement

`agents/stats/history.jsonl` is written by `madar_stats.py --log`, once per run, and the CHARTER
states its purpose in one clause: *"so week-over-week deltas accumulate."* A week-over-week delta
is **the row seven back** — a positional read.

Counted on 2026-10-12, before any edit:

| | |
|---|---|
| Rows | **108** |
| Distinct `as_of` dates | **95** |
| Dates carrying more than one row | **10** |
| Dates whose duplicate rows are **byte-identical** | **9 of 10** |
| Worst date | **2026-09-14, four rows** |
| Dates on which "the row seven back" lands on the wrong day | **10 of 95** |

**Nine of ten is the whole ruling.** Those nine duplications record nothing: the corpus had not
changed between the two snapshots, so the second row is a fact about the *operation* having run
twice, not about the publication. A file that answers *what was true on date D* answers it
correctly on all 95 dates even while it is wrong. Only `len()`, `rows[-7]` and `zip(rows,
rows[1:])` can tell.

And the tenth date is what says last-write-wins is correct rather than convenient: on 2026-09-14
the four rows are not identical — `ar_total` moves 41 → 42 between the third and the fourth,
because the ruler piece's Arabic twin landed during the day. **The last snapshot of a day is that
day's closing state**, which is what a daily series is for.

## Why the obvious fix is the wrong one

The queue item was raised as *ten dates carry two snapshots*, which reads as a data problem and
invites a de-duplication pass. A de-duplication pass restores the population and leaves the next
duplicate free to arrive tomorrow.

It also would not have prevented these. **Four of the ten duplicated dates are Sundays** — the
weekly-review day, when a daily and a weekly both snapshot — and the other six are weekdays. *Two
runs in one day is a cause and not the cause.* The fix has to be a property of the **write**: the
row for a date is **replaced**, never appended beside. Then the cause stops mattering.

## What was done

- `--log` now reads the whole series, drops any row carrying today's date, appends the new row,
  and rewrites atomically in date order. Running it three times in one day leaves one row.
- `--dedupe` applies the same resolution to the existing series, **as an instrument rather than
  by hand**, because the RUNBOOK's second amendment (2026-10-04, limb two) says a point-of-filing
  rule fixes a count's future and leaves a step discontinuity where it was written. Reconciled
  backward in the same commit: **108 → 95 rows, all 95 dates surviving, nothing invented.**
- Both modes **refuse to write** if any line of the series fails to parse or carries no `as_of`,
  and exit 2 leaving the file untouched. Both modes rewrite the file; a rewrite that silently
  dropped a line it could not read would destroy the series it exists to keep.
- The date key moved from `date.today()` (the runner, UTC) to the operation's calendar
  (Asia/Dubai, a fixed UTC+4 — the emirate has never observed daylight saving, so the offset is
  exact and needs no tzdata). `date.today()` *meant* the operation's calendar while the runs
  happened on a Dubai desktop and silently became UTC at the 2026-09-14 cloud cutover; every run
  on file has fallen in the 10:30–12:30 UTC window, so no row is affected and the key now means
  what the series says it means.

**Proved eleven ways, bite first (#74), on a copy in `/tmp`:** the old tool appending two rows for
one date (the defect reproduced before the fix was trusted); the new tool idempotent across three
runs; all 108 other rows byte-identical afterwards; order preserved; `--dedupe` keeping the *last*
row of 2026-09-14 and every kept row traceable to an original; `--dedupe` idempotent on a second
pass; three refuse-to-write guards reaching their condition and leaving the file unchanged; the
calendar key proved against a 21:30Z probe where UTC and Dubai disagree; and the HTML panel the
brief pastes **byte-identical before and after**, because the point of the change was the series,
not the artefact.

## The general form

*Ask of every accumulating artefact: which consumer would notice if this were wrong?* If the
answer is only a consumer that does not exist yet, the artefact is not being checked — it is
being **believed**, and the belief will be cashed on the first day it matters.

Kin, and the reason this sits in assertion-discipline rather than in the enumeration family: the
enumeration rules ask *what can today's sweep not structurally see?* and are answered by widening
the sweep. This one is narrower and harsher — a one-line sweep could have seen it on any of the
56 days since the first duplicate, and there was no sweep, because **nothing counts a file nobody
consumes.** Same shape as the
operation's own repeated finding that *a list with two homes has no count*: here it is one file
with two definitions — a per-run log and a per-date series — and no count to catch them
disagreeing.

Related: **#89** (the served manifest: a chain of memory breaks silently if a write stops
happening), **#92** (a predicate that falls back cannot fail), **#95** (a shortfall indicts the
method before the population), **#57** (count against the population, never against yesterday's
number).
