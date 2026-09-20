# Web Developer — the standing queue

**Opened 2026-09-20 at the weekly review.** Reconciled at every weekly review; items are
added by whichever run raises them, and closed by whichever run lands them.

## Why this file exists

The 2026-09-20 review went looking for a capability gap and found a **bookkeeping** one.
Five open Web Developer items were live at the time, and every one of them was recorded in
a *different* artefact — one in a QA log, one in the edition ledger, one in a weekly
review, one in a daily brief, one in a growth note. Nothing anywhere held the list. That is
the guidebook drift the same review had just spent an hour repairing, one desk over: **work
filed by the run that finds it and consolidated by nobody.**

It matters for a decision, not just for tidiness. The team-expansion trigger is *a
capability gap that daily runs have hit repeatedly*, and a queue nobody can see cannot be
shown to be growing faster than it is cleared. This file makes the split-the-role question
answerable by looking rather than by arguing.

**The rule: an item raised for the Web Developer is written here in the same run that
raises it.** An item that lives only in a QA log is not queued; it is mentioned.

## Open

| # | Item | Raised | Age at 09-20 | Why it is not done yet | Blocks |
|---|---|---|---|---|---|
| 1 | **The output-bounded served-bytes manifest** — a per-URL content hash emitted into `dist` and compared against the origin's copy on the next build. The honest answer to the one direction `qa_lastmod` cannot bound: a page whose bytes changed and whose date says they did not. | 2026-09-06 (weekly) | **14 days** | Named as a design question on 09-06, re-named 09-18, 09-19, 09-20. The throwaway version written to diagnose the 09-19 red deploy **found ruling #58 on its first run** and is strictly stronger than `qa_live_drift`, which reported CLEAN at the same moment. It exists, in `/tmp`, unowned. | nothing — but it is the strongest instrument this operation has ever written and it is not in the repository |
| 2 | **`qa_sources_alive` is unschedulable** — `--held-only --sample 0` ran 40 minutes with no output and no JSON on 09-16, because it prints only after the final URL and four refusing hosts burn the whole budget. Needs a per-URL timeout, incremental output, and a bounded total. | 2026-09-16 (QA log, P1) | **4 days** | Not picked up; every run since has had a louder lane. | **YES — the wave flip.** The ledger makes this sweep the last step before the flip commit, which currently makes it an unbounded, un-observable step at the worst possible moment. |
| 3 | **The derived-register assertion** — compute the guidebook's `#1–#N` range and Section 1's row count from the files on disk, so the INDEX header stops being hand-maintained. | 2026-09-13 (weekly) | **7 days** | Routed, not built. | nothing, but see below |
| 4 | **Self-hosted fonts** | carried, P1 | — | third-party font origin on every page, against the privacy posture | nothing |
| 5 | **The feed's Arabic-direction question** — assert `direction: rtl` on AR feed item descriptions from the **resolved** value in a rendering engine (#55), not from our markup. | 2026-08-18, re-named 2026-09-20 | **33 days** | Named as needing "a client we do not own"; the cloud runner's headless Chrome is that client. | nothing — and it is **this week's growth bet** |

**Item 3 is the queue's own joke and is left in deliberately.** The assertion that would
have caught the ten-ruling register drift was routed a week before the drift was found, and
was not built, and the drift was found by hand. It is not the highest-value item on this
list and it should not jump the queue; it is here because a queue that quietly drops the
embarrassing item is not a queue.

## Closed

| Item | Raised | Closed | By |
|---|---|---|---|
| Feed links and enclosures resolve from outside our origin | 2026-08-18 | **2026-09-20** | weekly review — 78/78 links, 76/76 enclosures, 76/76 declared `length` exact against the origin (`agents/growth/2026-09-20-the-feed-proved-from-outside.md`) |

## The trigger this file exists to make checkable

Recorded at the 2026-09-20 review, where team expansion was **held for the eighth
consecutive week**:

> **If at the 2026-09-27 weekly review this queue still stands at four or more open items
> with three or more of them older than three runs — and the daily runs have cleared fewer
> than two in the week — the Web Developer role is split**, site/build from assertions, and
> the new persona is scaffolded under the existing one per the CHARTER's ladder.

It did **not** fire today, on a deliberately strict reading: the role produced **seven new
standing assertions in seven days** and five of the week's ten rulings came out of that
work. A role writing a ruling a day is at peak, not saturated. What is growing is the
queue, not the incapacity — and the correct first response to a queue nobody wrote down is
to write it down and look again in a week.
