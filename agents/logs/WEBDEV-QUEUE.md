# Web Developer — the standing queue

**Opened 2026-09-20 at the weekly review.** Reconciled at every weekly review; items are
added by whichever run raises them, and closed by whichever run lands them.

**2026-09-27: the trigger this file was written to make checkable FIRED, and the Web
Developer role is split.** Items marked **[AE]** below are now owned by the **Assertions
Engineer** (`agents/12_assertions_engineer.md`); items marked **[WD]** stay with the Web
Developer. The file keeps one name and one table on purpose — a queue with two homes is the
defect this file exists to fix, and it very nearly happened to the patch queue this week
(see the foot of this file).

## Why this file exists

The 2026-09-20 review went looking for a capability gap and found a **bookkeeping** one.
Five open Web Developer items were live at the time, and every one of them was recorded in
a *different* artefact — one in a QA log, one in the edition ledger, one in a weekly
review, one in a daily brief, one in a growth note. Nothing anywhere held the list. That is
the guidebook drift the same review had just spent an hour repairing, one desk over: **work
filed by the run that finds it and consolidated by nobody.**

It matters for a decision, not just for tidiness. The team-expansion trigger is *a
capability gap that daily runs have hit repeatedly*, and a queue nobody can see cannot be
shown to be growing faster than it is cleared. This file made the split-the-role question
answerable by looking rather than by arguing — **and one week later it answered it.**

**The rule: an item raised for the Web Developer is written here in the same run that
raises it.** An item that lives only in a QA log is not queued; it is mentioned.

## Open — **FIVE items, reconciled against disk 2026-10-04 by looking, ages to 2026-10-04**

**Count line, because this file had none and the 09-20 finding that opened it was about a list with
five homes and no count: five open, one closed this week, oldest 28 days.** Reconcile against the rows
below at every weekly review, never against the previous week's number (#57).

**THIS FILE IS NOW THE OPERATION'S ONE QUEUE AND ITS HEAD IS BINDING** (RUNBOOK rule, 2026-10-04). The
previous run's **forward question enters at the head** — it is the freshest thing the operation knows
and it belongs first. **An item displaced from the head three times goes first regardless**, and the
run writes one line in the QA log naming which head it took and what it displaced. Displacement counts
are in the table and are the only number here that moves daily.

| # | Item | Owner | Raised | Age | Displaced | Verified how | Blocks |
|---|---|---|---|---|---|---|---|
| 1 | **`qa_sources_alive` bounded and schedulable** — a *total* ceiling, demonstrated against the full held set. | **[AE]** | 2026-09-16 | **18 days** | **3** — bet part B (09-27), then six consecutive runs | Read the file today: a per-URL `TIMEOUT` and `flush=True` are present; **no total ceiling exists** — `--help` offers `--root --sample --seed --held-only --json --collect-only` and nothing bounding. The 10-03 split gave the *parse* half a gate (`--collect-only`, network-free, proved by poisoning the socket module) and left the *probing* half unbounded, which is the half the ledger schedules. Mitigated but not closed: the full sweep has now run to completion twice (09-30, and 10-03 over 59 URLs). | **YES — the wave flip.** Seven days out. **Head of the queue by the displacement rule.** |
| 2 | **The output-bounded served-bytes manifest** — a per-URL content hash emitted into `dist` and compared against the origin's copy on the next build. The honest answer to the one direction `qa_lastmod` cannot bound: a page whose bytes changed and whose date says they did not. | **[AE]** | 2026-09-06 (weekly) | **28 days** | **11** | No manifest tool in `agents/tools/` — 28 tools listed, none of them this. **Named eleven times** (09-06, 09-18, 09-19, 09-20, 09-22, 09-23, 09-24, 09-25, 09-26, 09-27, and here) and **mentioned zero times in all seven of this week's QA logs**, which is the measurement that produced the one-queue rule. The throwaway version **found ruling #58 on its first run** and is strictly stronger than `qa_live_drift`, which reported CLEAN at that same moment. It exists, in `/tmp`, unowned. | nothing — and it is still the strongest instrument this operation has ever written |
| 3 | **The derived-register assertion** — compute the guidebook's `#1–#N` range, §1's row count **and the shape of every §3 row** from the files on disk. | **[AE]** | 2026-09-13 (weekly) | **21 days** | **4** | No tool reads `INDEX.md` — grepped all 28, zero hits. **Its urgency went back UP this week and the evidence is specific:** the 10-04 consolidation found **five of the last eight §3 rows malformed** — three columns in a four-column table, rulings #80 through #84, their long-form files unreachable from the canonical register — and **every row count and every range check ever run on that table passed on all five.** A hand reconciliation that counts rows cannot see a row with the wrong number of cells. `len(row.split("|")) == 6` is one line and would have caught it the day it shipped. | nothing — but it is now the only queue item with a *demonstrated* miss behind it |
| 4 | **Self-hosted fonts** — two third-party origins requested by the layout on every page, against the privacy posture. | **[WD]** | carried, P1 | — | **2** | Confirmed live in today's build: `fonts.googleapis.com` and `fonts.gstatic.com` on **120 of 121** served pages, printed by name by `qa_chrome_links`. The privacy claim in the statistics panel is scoped by construction and stays honest either way. | nothing — but the privacy claim is the only claim the publication makes about itself |
| 5 | **`agents/stats/history.jsonl` has 102 rows for 89 dates** — ten dates carry two snapshots and one (09-14) carries four. | **[AE]** | **2026-10-04** (weekly) | **0 days** | 0 | Counted today: 102 lines, 89 distinct `as_of` values. The duplicated dates are exactly the days with more than one run, so the file is a faithful per-run log and not corrupt — **but the CHARTER's stated purpose for it is *"so week-over-week deltas accumulate"***, and any consumer taking "the row seven back" gets the wrong answer on ten of 89 dates. Nothing consumes it yet, which is the only reason it has never bitten; the Substack metrics read is what will consume it. **Not fixed here on purpose:** `madar_stats.py` is the Assertions Engineer's and the right answer (last-write-wins per date, or an explicit `run_seq`) is a design call, not a patch. This review also **declined to run `--log` a third time today** rather than add an eleventh duplicate for a corpus that has not changed. | nothing yet — it blocks the first week-over-week read |

## Closed

| Item | Raised | Closed | By |
|---|---|---|---|
| **The feed's Arabic-direction assertion** — `direction: rtl` on AR feed item descriptions, read from the **resolved** value in headless Chrome (#55), never from our markup | 2026-08-18, re-named 09-20 | **2026-09-28** | **Monday's daily run, as its first work, before the content lane** — `qa_feed_direction`, standing assertion 26, wired to `postbuild` and declared to `qa_census` in the same commit, proved seven ways. It found **43 of 232 feed fields inheriting the reader's base direction**. Item 5 on the 09-27 list and item 1 of the Assertions Engineer's first-week brief, **40 days owed and closed on day one of the role** — and the only part of the 09-27 growth bet that landed. **This row was not written until the 2026-10-04 review**, so this file sat for seven days showing the item as open at "40 days" while the tool was shipped, gating and green — *the defect the file's own rule exists to stop (an item lands, and the queue hears about it at the next reconciliation), in the week the file was handed to a dedicated owner.* |
| Feed links and enclosures resolve from outside our origin | 2026-08-18 | **2026-09-20** | weekly review — 78/78 links, 76/76 enclosures, 76/76 declared `length` exact against the origin (`agents/growth/2026-09-20-the-feed-proved-from-outside.md`) |
| `qa_sources_alive` hangs with no output (**P1 limb only**) | 2026-09-16 | **2026-09-27** | daily run — diagnosed as block-buffered stdout, not a slow sweep; `flush=True` + per-URL timeout. The eleven-day P1 was a reporting defect in the reporter. Design limb stays open as item 2. |

## The trigger — checked by looking, 2026-09-27, and it FIRED

Recorded at the 2026-09-20 review, where team expansion was held for the eighth
consecutive week:

> **If at the 2026-09-27 weekly review this queue still stands at four or more open items
> with three or more of them older than three runs — and the daily runs have cleared fewer
> than two in the week — the Web Developer role is split**, site/build from assertions, and
> the new persona is scaffolded under the existing one per the CHARTER's ladder.

| Condition | Threshold | Actual 2026-09-27 | Fired |
|---|---|---|---|
| Open items | ≥ 4 | **4** (items 1, 3, 4, 5 — item 2's P1 limb closed, design limb open) | **yes** |
| Older than three runs | ≥ 3 | **4** — 21 days, 14 days, 40 days, and one carried | **yes** |
| Cleared in the week | < 2 | **1** (item 2's P1 limb) | **yes** |

Three conditions, three fired, **on the strictest available reading** — counting item 2 as
cleared, which is the reading least favourable to splitting the role.

**And the reason is not the count.** The role shipped **four new standing assertions in
seven days** (`qa_date_identity` 09-22, `qa_packet_figures` 09-23, `qa_feed_validators`
09-24, `qa_chrome_links` 09-26) and diagnosed a red deploy that turned out to be a wrong
check on a healthy publication. That is not a saturated role; it is a role at peak. **Three
of those four came from the daily forward question, one from a red deploy, and none from
this queue or from the week's growth bet** — which asked for exactly one assertion, item 5,
and did not get it for the fortieth day.

The constraint is **two queues competing for one desk**, and only one of them has teeth:
the RUNBOOK requires the next run to test the previous run's forward question *before
adding anything new*, while the weekly bet carries no such clause. A role cannot arbitrate
between its own priorities. That is what the second role is for, and it is why the split is
along *instrument versus product* rather than along *new work versus old work*.

~~**Restraint test, dated:** if by the **2026-10-25** review the Assertions Engineer has not
cleared at least three inherited items, and the standing-assertion count has grown faster
than this queue has shrunk, the split addressed the wrong constraint and the role folds
back.~~ — **REPLACED 2026-10-04, after one week, and the reason is that this operation's own
rule about bets applies to its own restraint tests.**

**Why it was replaced, stated against myself because I wrote it.** The 09-27 review ruled, in
the same document, that *a bet whose outcome the operation does not own is a request, not a
bet.* This test fails that standard twice.

- **Its second limb punishes the role's charter.** *"The standing-assertion count has grown
  faster than this queue has shrunk"* — read against the role's first week, that is **+3
  assertions against −1 queue item**, so the limb fires. But all three assertions came out of
  forward questions that **bit** (#73, #75, #79 and onward), and the one cleared item was the
  **oldest and most-owed thing on the board**, closed on day one of the role. The role's own
  persona says *you do not add an assertion to make the count go up.* A test that converts
  assertion count into a score — and a negative one — contradicts the file it is written in and
  would fail a role having its best possible week.
- **Its first limb includes an item the split assigns elsewhere.** Item 2, the served-bytes
  manifest, is marked **[AE]** and its deliverable is *a manifest emitted into `dist`* — a
  served byte, which the split's own standing exception assigns to the **Web Developer**
  (*"a fix that changes served bytes is the Web Developer's, even when an assertion found
  it"*). And the three staged patches are blocked on a credential **no persona holds** (issue
  #7). *Counting items the role may not finish is the same error as counting a bet the
  operation cannot read.*

**The replacement test, dated 2026-10-25, and it is one number.** The split exists to make the
queue get **reached**. So:

1. **The age of the oldest open item on this queue is LOWER on 2026-10-25 than the 28 days it
   reads today.** One number, owned entirely by the role, moved only by doing the thing the
   role was created to do. Assertion count is not in it, in either direction.
2. **The one-queue rule's displacement line appears in every QA log in the window** — *which
   head did this run take, and what did it displace.* A displacement nobody writes down is how
   an item named ten times becomes an item named eleven times.
3. **If the oldest age has climbed instead, the split addressed the wrong constraint** and the
   role folds back — and the fallback is already known: put the queue head into the RUNBOOK's
   binding forward-question slot by force, which is the 2026-10-04 one-queue rule without the
   persona.

Recorded here so it is checkable by looking, exactly as the trigger above was — and the whole
point of re-writing it at week one rather than discovering at week four that it was unmeasurable
is that **a test is an instrument, and an instrument is proved before it is trusted (#35).**

## Footnote — the patch queue nearly repeated this file's own defect

Found while reconciling today: **blocked patches live in two directories.**
`agents/patches/` holds two `.patch` files and a README; `agents/tools/patches/` holds one
`.md`. `CLAUDE.md` names the second; **issue #7 names the first.** Two homes, one queue,
one week after this file was opened to stop precisely that. Consolidated today into
`agents/patches/` (the older home, the one the founder-facing issue names) with an index;
`agents/tools/patches/` now carries a pointer only. **The general shape, for the third
time in eight days: a list with two homes has no count, and a thing with no count cannot be
caught drifting.**
