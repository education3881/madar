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

## Open — reconciled against disk 2026-09-27, by looking

| # | Item | Owner | Raised | Age at 09-27 | Verified how | Blocks |
|---|---|---|---|---|---|---|
| 1 | **The output-bounded served-bytes manifest** — a per-URL content hash emitted into `dist` and compared against the origin's copy on the next build. The honest answer to the one direction `qa_lastmod` cannot bound: a page whose bytes changed and whose date says they did not. | **[AE]** | 2026-09-06 (weekly) | **21 days** | No manifest tool in `agents/tools/`. Named ten times now. The throwaway version **found ruling #58 on its first run** and is strictly stronger than `qa_live_drift`, which reported CLEAN at the same moment. It exists, in `/tmp`, unowned. | nothing — but it is the strongest instrument this operation has ever written and it is still not in the repository |
| 2 | **`qa_sources_alive` bounded and schedulable** — the P1 is closed; the design item is not. | **[AE]** | 2026-09-16 (QA log, P1) | **11 days** | **P1 CLOSED 2026-09-27**: the 40-minute 09-16 hang was **block-buffered stdout**, not a slow sweep — `flush=True` and a per-URL timeout are in the file, verified by reading it. What remains is the *bound*: the ledger makes this the last step before the flip commit and nothing yet proves a total ceiling. | **YES — the wave flip.** An un-observable step at the worst possible moment is now an *observable* step of unproven duration. |
| 3 | **The derived-register assertion** — compute the guidebook's `#1–#N` range and Section 1's row count from the files on disk, so the INDEX header stops being hand-maintained. | **[AE]** | 2026-09-13 (weekly) | **14 days** | No tool in `agents/tools/` reads `INDEX.md` — grepped, zero hits. | nothing, and its urgency **fell** this week: see below |
| 4 | **Self-hosted fonts** — two third-party origins requested by the layout on every page, against the privacy posture. | **[WD]** | carried, P1 | — | Confirmed live in today's build: `fonts.googleapis.com` and `fonts.gstatic.com` on **120 of 121** served pages, printed by name by `qa_chrome_links`. | nothing — but the privacy claim is the only one the publication makes about itself |
| 5 | **The feed's Arabic-direction assertion** — assert `direction: rtl` on AR feed item descriptions from the **resolved** value in a rendering engine (#55), not from our markup. | **[AE]** | 2026-08-18, re-named 09-20 | **40 days** | No tool asserts feed item direction — grepped every `qa_*.py`. **It was part A of the 09-20 growth bet and did not ship.** | nothing — and it is now the **first item** on the Assertions Engineer's first-week brief |

**Item 3 stays on the list, and this week made it more interesting rather than less.** The
2026-09-27 consolidation found the ruling register **already true** for the first time in
four weeks — range, heading, series line and §1 count all correct, confirmed by counting
71 and 66 rows and resolving every long-form reference against 102 files on disk. So the
assertion that would have caught the drift was not needed, because a **RUNBOOK rule** moved
the cheapest part of the maintenance onto the faster clock and seven consecutive runs
executed it. That is the better fix and it is working. It does not retire the item: a rule
executed by hand seven times is still a rule executed by hand, and the two leaks it did
have (09-23, 09-25) were both caught by a human counting rows.

## Closed

| Item | Raised | Closed | By |
|---|---|---|---|
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

**Restraint test, dated:** if by the **2026-10-25** review the Assertions Engineer has not
cleared at least three inherited items, and the standing-assertion count has grown faster
than this queue has shrunk, the split addressed the wrong constraint and the role folds
back. Recorded here so it is checkable by looking, exactly as this trigger was.

## Footnote — the patch queue nearly repeated this file's own defect

Found while reconciling today: **blocked patches live in two directories.**
`agents/patches/` holds two `.patch` files and a README; `agents/tools/patches/` holds one
`.md`. `CLAUDE.md` names the second; **issue #7 names the first.** Two homes, one queue,
one week after this file was opened to stop precisely that. Consolidated today into
`agents/patches/` (the older home, the one the founder-facing issue names) with an index;
`agents/tools/patches/` now carries a pointer only. **The general shape, for the third
time in eight days: a list with two homes has no count, and a thing with no count cannot be
caught drifting.**
