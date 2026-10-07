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

## Open — **FIVE items, reconciled against disk 2026-10-07 by looking, ages to 2026-10-07**

**2026-10-07 — THE HEAD WAS TAKEN AS WRITTEN, AND THE RULE CHOSE THE DAY'S FIRST JOB FOR THE THIRD
CONSECUTIVE RUN.** The displacement line, in one sentence: **this run took item 3 — the derived-register
assertion, 24 days, six displacements, the oldest item past the three-displacement threshold with an age on
the board — and displaced item 1 (the gating assertions' HOME) a third time and the 10-06 forward question
once on its first morning.** Nothing was argued: the 10-05 tiebreak says *among items past threshold the
oldest goes first*, item 2 closed yesterday, and item 3 was next by age with no second candidate to weigh.
**Item 3 is CLOSED**: `qa_register_shape`, standing assertion 30, **ruling #90**, proved 28 ways with the
bite first. *Three for three on the one-queue rule, and all three times it produced the item nobody would
have remembered — item 1 at 18 days, item 2 at 29, item 3 at 24.*

**The scope it closed on is 13× the scope it was specified at.** Item 3 said *`INDEX.md`*; the 10-06 run
generalised it in writing to every hand-maintained table and ran it over 7 files, 34 tables, 255 rows. The
real population is **717 files, 432 tables, 2,885 rows** — the hand-run had covered **7.9% of the tables**,
and the other 92% held **three malformed rows the hand-run could never have seen**, two of them the *same
row* in the Zambia and Sierra Leone verification verdicts, blanking the **AR column** of the one table in
each whose purpose is to show both editions checked, for 29 and 28 days.

**And the new assertion found a SIXTH home for a moving number on its first run** — the families list's
quotable ratio, *twenty-six of eighty-eight rulings* against a true twenty-seven of eighty-nine. **Named as
a defect by the 10-04 consolidation, honoured on 10-05, dropped again on 10-06 by the run that moved the
count line three sentences above it.** So the conditional fifth home has two halves in one bullet and only
the *uncheckable* one had an owner. That is **ruling #90**.

**Item 1 is now AT the three-displacement threshold**, which the 10-06 note predicted in writing and flagged
as the tiebreak's untested case: at three displacements it is ranked by age against items 3, 4 and 6, and it
is the youngest of those, **so the tiebreak would still not send it first.** Item 3 has now left the board,
which removes one competitor but not the shape. **This is the one outcome the tiebreak was not designed for
and the 2026-10-11 review owes it an answer rather than another restatement.**

**Count line: FIVE open, one closed today (item 3), one closed 2026-10-06, one closed 2026-10-05 — three in
three days.** Counted by reading the rows today: five.

**AND THE RESTRAINT TEST'S ONE NUMBER WAS BRIEFLY UNMEASURABLE, WHICH IS WORTH MORE THAN THE REPAIR.** After
three days of closing the board's oldest items, the new oldest was **item 4, whose `Raised` cell read
*"carried, P1"* and whose `Age` cell read *"—"*.* The 2026-10-25 test is *the age of the oldest open item is
lower than the 28 days it read on 10-04* — a single number, and this morning the row holding it had no date
to compute it from. **Found by looking rather than by arithmetic**, and fixed by going to the source: item 4
was filed as a P1 on **2026-09-18**, in `agents/growth/2026-09-18-third-party-surface-audit.md` (*"Filed as a
P1 to the Web Developer"*), so its age is **19 days** and the test is measurable again. **The general shape
is this file's own founding defect one turn in:** it was opened because five items had five homes and no
count — and it then carried, for nineteen days, a row with no date, in the single column its own restraint
test is scored on. *A queue that records ages cannot be caught missing one unless something counts them.*
**Oldest open item today: 19 days, down from 28 on 10-04.** The test is currently passing and that is now a
measurement rather than an impression.

**2026-10-06 — THE HEAD WAS TAKEN AS WRITTEN, AND THE RULE CHOSE THE DAY'S FIRST JOB FOR THE SECOND
CONSECUTIVE RUN.** The displacement line this file's restraint test requires, in one sentence:
**this run took item 2 — the served-bytes manifest, 29 days, twelve namings — and displaced item 1
(the gating assertions' HOME) a second time and item 3 (the derived-register assertion) a sixth.**
Nothing was argued. The 10-05 tiebreak said *among items past the three-displacement threshold the
oldest goes first*, item 2 was the oldest past threshold, and the 10-05 log had already named it in
writing as today's head — so the selection was made yesterday by rule and merely executed today.
**Item 2 is CLOSED**: `qa_served_manifest`, standing assertion 29, **ruling #89**, proved eight ways
with the bite first. *Two for two on the one-queue rule, and both times it produced the item nobody
would have remembered — item 1 on Monday at 18 days, item 2 today at 29.*

**And item 3 was displaced for the sixth time while its own subject bit this run.** Yesterday's forward
question was *this operation has no instrument that reads its own artefacts' SHAPE*, which is item 3's
territory; it was not built, and the one-line check was run by hand instead — over **every** table in
`INDEX.md` rather than over the section being edited, 21 tables and 189 rows, and it **caught this run's
own §1 row at five fields against a six-column header.** Eighteenth instance in three days of a defect
repaired seventeen times. A hand-run check that bites on its author is the strongest argument item 3 has
ever had, and it is recorded here rather than in a log nobody re-reads.

**Count line, because this file had none and the 09-20 finding that opened it was about a list with
five homes and no count: FIVE open, one closed today (item 2), one closed 2026-10-05, oldest 23 days.**

**Row numbers are deliberately NOT compacted when an item closes.** The open rows below read 1, 3, 4, 5, 6 — item 2 is in the Closed table, not missing. Renumbering would silently invalidate every *item N* reference in five weeks of QA logs, briefs, the CHARTER's restraint test and this file's own trigger table, which is the drift this file exists to stop rather than to cause.
Five rather than six because item 2 closed and nothing new was opened — the first net reduction the
board has recorded on a daily run. Reconcile against the rows below at every weekly review, never
against the previous week's number (#57). **Counted by reading the rows today: five.**

**2026-10-05 — THE ONE-QUEUE RULE WORKED ON ITS FIRST MONDAY, and this line is the proof it asks for.**
The 10-04 weekly named the daily's forward question as Monday's head *and wrote down that taking it would
displace item 1 a fourth time, so item 1 goes first by rule.* **Today's run took item 1 and closed it** —
18 days open, three displacements, the flip's only queue dependency — **before adding anything new.**
The forward question it displaces enters at the head below with its displacement count at **one**. Nobody
remembered item 1; the rule produced it. *That is the arbitration a single role could not perform for
itself, and it is the first evidence for the 2026-10-25 restraint test: the oldest open age moved 28 → 29
only because the clock moved, and item 1 left the board entirely.*

**THIS FILE IS NOW THE OPERATION'S ONE QUEUE AND ITS HEAD IS BINDING** (RUNBOOK rule, 2026-10-04). The
previous run's **forward question enters at the head** — it is the freshest thing the operation knows
and it belongs first. **An item displaced from the head three times goes first regardless**, and the
run writes one line in the QA log naming which head it took and what it displaced. Displacement counts
are in the table and are the only number here that moves daily.

**TIEBREAK, added 2026-10-05 on the rule's first Monday, because executing it exposed the gap.** The
displacement clause says *an item displaced three times goes first regardless* — and this morning it
selected **three** items at once (item 1 at three, item 2 at eleven, item 3 at four). *"Regardless"*
with three candidates and no ordering is not a rule; it is the run choosing by judgment, which is the
exact thing the clause was written to remove. **Among items past the three-displacement threshold, the
OLDEST goes first** — age, not displacement count, because age is what the 2026-10-25 restraint test
measures and a rule should move the number it will be judged by. Today's run took **item 1** rather than
the oldest, and the reason is recorded rather than smoothed over: the 10-04 log had named item 1 in
writing as Monday's head *before* this gap was visible, and it also blocks the flip six days out, which
is the only Blocks cell on the board reading YES. **Tomorrow the tiebreak binds with nothing to argue:
item 2, the served-bytes manifest, 29 days and twelve namings, is the oldest past threshold and goes
first.** It has now been named twelve times and done zero; if it is displaced a thirteenth, the one-queue
rule has failed in the specific way its own author predicted, and the 2026-10-11 review says so plainly
rather than restating the rule a third time.

| # | Item | Owner | Raised | Age | Displaced | Verified how | Blocks |
|---|---|---|---|---|---|---|---|
| 1 | **The gating assertions' HOME** — of the **27** that gate the deploy, which are wired somewhere that cannot observe the thing they assert? Twelve run where `dist` and the origin both exist; **fifteen** run inside the build and exit before anything is published — and assertion 30 made it fifteen today, so this item's own number moved underneath it again. **This item's subject was hit head-on by today's work and it changed the design:** `qa_served_manifest --check` was going to be staged for the `verify` job until the question *can that home observe what this asserts* was asked — verify compares the artifact it just published against the origin, so origin == artifact by construction and the check would have compared the manifest against itself, **passing forever**. It is staged for the `build` job instead. One assertion saved from exactly the defect this item names, by asking this item's question without building this item. `qa_feed_enclosures` and `qa_feed_direction` are suspect by their own names. **A check in the wrong home passes forever.** | **[AE]** | 2026-10-04 (the daily's forward question) | **2 days** | **3 — AT THE THRESHOLD** — displaced 2026-10-05 by item 1's rule, 2026-10-06 by item 2's, and 2026-10-07 by item 3's, **all three predicted in writing the day before.** It is now past the three-displacement threshold itself, where the 10-05 tiebreak ranks it **by age** against items 4, 6 and 7 — and at 3 days it is the youngest, **so the clause that exists to stop starvation would still not send it first.** The 10-06 note predicted exactly this and called it the tiebreak's untested case; item 3 closing removes a competitor and not the shape. **The 2026-10-11 review owes this an answer, not a restatement.** | Not yet tested. Entered at the head per the one-queue rule and displaced once on its first morning, **by rule and with the displacement written down in advance** — which is the mechanism working, not failing. | nothing yet — but it is the sharpest thing the operation currently knows |
| 4 | **Self-hosted fonts** — two third-party origins requested by the layout on every page, against the privacy posture. | **[WD]** | **2026-09-18** (`growth/2026-09-18-third-party-surface-audit.md`, *"Filed as a P1 to the Web Developer"*) — **this cell read *carried, P1* with no date until 2026-10-07**, see the note above | **19 days** | **3** | Confirmed live in today's build: `fonts.googleapis.com` and `fonts.gstatic.com` on **120 of 121** served pages, printed by name by `qa_chrome_links`. The privacy claim in the statistics panel is scoped by construction and stays honest either way. | nothing — but the privacy claim is the only claim the publication makes about itself |
| 5 | **FIVE dead citations on four PUBLISHED pieces** — hard 404s confirmed on two reads: `ei-ie.org` (Lebanon), `men.gov.ma` ×2 (Morocco), `osym.gov.tr` (Türkiye), `unicef.org.uk` (Rohingya). Both languages each, so **eight live pages**. | **[WD]** + Editor | **2026-10-05** | **2 days** | 0 | The first complete census of all 343 outbound promises (`agents/growth/2026-10-05-the-first-complete-census-of-our-outbound-promises.md`), affordable for the first time because #88 gave the sweep a ceiling. **Deliberately not fixed in the run that found it:** these are **served bytes on published pieces**, which the split assigns to the Web Developer even when an assertion found it, and the disposition is **editorial** per #41 — *supersede, don't resurrect* — needing a replacement register read in served text or a dated 404 annotation. Rushing five annotation rewrites into the tail of a run six days before a wave flip is how a correction becomes the next defect. | nothing — but it is the only open item a **reader** can currently see |
| 6 | **`agents/stats/history.jsonl` has 102 rows for 89 dates** — ten dates carry two snapshots and one (09-14) carries four. | **[AE]** | **2026-10-04** (weekly) | **3 days** | **3** — displaced again 2026-10-07 by item 3's rule | Counted today: 102 lines, 89 distinct `as_of` values. The duplicated dates are exactly the days with more than one run, so the file is a faithful per-run log and not corrupt — **but the CHARTER's stated purpose for it is *"so week-over-week deltas accumulate"***, and any consumer taking "the row seven back" gets the wrong answer on ten of 89 dates. Nothing consumes it yet, which is the only reason it has never bitten; the Substack metrics read is what will consume it. **Not fixed here on purpose:** `madar_stats.py` is the Assertions Engineer's and the right answer (last-write-wins per date, or an explicit `run_seq`) is a design call, not a patch. This review also **declined to run `--log` a third time today** rather than add an eleventh duplicate for a corpus that has not changed. | nothing yet — it blocks the first week-over-week read |
| 7 | **The published oracle has no auditor** — `qa_served_manifest`'s emit half reads `dist`, its check half compares the **origin's manifest** against a **local build**, and the one comparison never made is the **origin's manifest against the origin's own pages**. A manifest that rode along with a deploy while describing a different tree would silently rebase every later answer with every exit code reading clean. **MEASURED BY HAND TODAY AND IT PASSES: 120 of 120 pages, both hashes, zero differences, identical page sets** — the first time this operation has ever checked a published oracle against the thing it is an oracle for. **But the audit covers 120 of the manifest's 216 claimed entries.** Its **95 asset hashes** and its **404 entry** are claimed and unverified, because the origin seed walks sitemap URLs only; that is 44% of the file unaudited, and the two-normalisation gap between the CI manifest (240) and the origin seed (238) is exactly the 404's, checked rather than assumed. **The instrument is what is owed** — a gated `--audit-origin` that does this without a human remembering to. | **[AE]** | **2026-10-06** (the daily's forward question) | **1 day** | **1** — displaced 2026-10-07 by item 3's three-displacement rule, on its first morning, with the displacement predicted by the rule rather than chosen. | **Answered by hand, not by an instrument**, which is the 09-13 defect carried deliberately for one day: a green that cost a human's attention. | nothing yet — but it is the baseline every future cross-deploy answer rebases on |

## Closed

| Item | Raised | Closed | By |
|---|---|---|---|
| **The derived-register assertion** (was open item 3) — compute the guidebook's `#1–#N` range, §1's row count and **the shape of every row in every hand-maintained markdown table** from the files on disk | 2026-09-13 (weekly) | **2026-10-07** | **Wednesday's daily run, as its first work, before the content lane and before anything new** — reaching the head by the **three-displacement clause** at six displacements and the **10-05 tiebreak** (*oldest past threshold goes first*) at **24 days**, with no second candidate to weigh once item 2 closed. `qa_register_shape.py`, standing assertion **30**, **ruling #90**. **What 24 days of specifying it never produced was the scope.** The item said `INDEX.md`; the 10-06 run generalised it in writing and ran it over 7 files, 34 tables, 255 rows. The real population is **717 files, 432 tables, 2,885 data rows** — the hand-run had covered **7.9% of the tables**, and the other 92% held **three malformed rows**: an Egypt recon row three cells wide in a four-column table since its first write **51 days** earlier, and **the same row in both the Zambia and Sierra Leone verification verdicts**, two cells in a three-column EN/AR table, blanking the **AR column** of the one table in each verdict whose purpose is to show both editions checked, for 29 and 28 days. *Two verdicts, two drafters, one row is a property of the template, not a slip* — and both judgments were **re-measured** before the missing cell was written rather than copied from the cell beside it. **The register limb makes the 2026-09-20 four-count rule a gate**: §3's range, §3's heading, §1's count line *in both its word and numeral forms*, and `CLAUDE.md`'s non-negotiables are all derived from §3's own rows, so the home that stood thirteen rulings stale for seven days is now a build failure. **And on its first run it found a SIXTH home** — the families list's quotable ratio, *twenty-six of eighty-eight rulings* against a true twenty-seven of eighty-nine, a home the 10-04 consolidation named, the 10-05 run honoured and the 10-06 run dropped while moving the count line three sentences above it. **Proved 28 ways with the bite first (#74), on a copy of the tree in `/tmp`** so a failed experiment cannot leave a mutation behind. **Three things the measurement decided rather than the design:** fenced code must be skipped (a shell `\|\|` in our own patch queue is not a one-cell row — **and this very row failed the new gate on its first write for quoting those two pipes unescaped, which is the second consecutive day that the row documenting this check has been the row the check catches**); continuation blocks inherit a header across prose but **not across a heading**, which was found by the headerless-row bite *passing*; and the ratio check had to be scoped to the families **list** rather than to §3, because §3 contains its own history and quotes every superseded ratio on purpose. **The harness itself went stale within the hour** — it hardcoded `#89` and `85 rows`, all four range bites broke when the ruling they prove moved the numbers, and the #74 guard printed *INJECTION DID NOT CHANGE THE FILE* four times instead of reading them as passes; it now derives every value from the tree. |
| **The output-bounded served-bytes manifest** (was open item 2) — a per-URL content hash emitted into `dist` and compared against the origin's copy on the next build | 2026-09-06 (weekly) | **2026-10-06** | **Tuesday's daily run, as its first work, before the content lane and before anything new** — reaching the head by the **three-displacement clause** and the **10-05 tiebreak** (*oldest past threshold goes first*) at **29 days and twelve namings**, with the selection made in writing the day before so nothing was chosen by judgment. `qa_served_manifest.py`, standing assertion 29, **ruling #89**. **What the five weeks of naming never produced was the design, and the design is two hashes rather than one:** `bytes_sha` (the served bytes as a reader gets them) and `content_sha` (the same bytes with the build's own `_astro` content-hashed filenames collapsed). Measured, not assumed — a one-character edit to `global.css` changes raw bytes on **120 of 121** pages and normalised content on **0**, so a presentation-only change is *mechanically* separable from a rendered-content change, which is what makes this an assertion instead of an alarm. Three states that were indistinguishable because all three were invisible: **content changed + date did not → FAIL**; bytes changed, content did not → *reported* (the resolver's declared `web/src/styles` exclusion, now visible); date moved, content did not → *reported* (the 09-04 shape, ruled a design question, **and now carrying a number for the first time**). **The bite is real rather than injected:** one `<title>` in `design-assets/wordmark/madar-wordmark.svg` — inlined into every page by three build-time readers, and in **neither** `CHROME_GLOBS` **nor** the resolver's git pathspec — changes what **117 of 120** served pages say and moves **zero** dates. Proved **eight** ways with the bite first (#74): control silent against an origin-derived baseline (**120/120 byte-identical to the origin**, where `qa_live_drift` samples four heads), control restored by reverting, the wordmark bite at exit 1, both report-branches at exit 0, and three failure-to-check guards — no baseline (exit 3, today's real state), a sitemap URL with no built file, and the normaliser matching nothing while hashed assets exist. **`--emit` is gated from `postbuild`** and `qa_census` asserts its routed-page count against the sitemap's own `<loc>` set, so the baseline cannot narrow in silence. **`--check` has no gated home this identity can write** — and the home it wanted was wrong, see open item 1 — so it is staged at `agents/patches/2026-10-06-build-served-manifest-check.md` and hand-run daily until that lands, which is the 09-13 defect carried deliberately with a patch instead of a promise. |
| **`qa_sources_alive` bounded and schedulable** — a *total* ceiling, demonstrated against the full held set | 2026-09-16 | **2026-10-05** | **Monday's daily run, as its first work, before the content lane and before anything new** — reaching the head by the **three-displacement clause** rather than by anyone remembering it, which is the one-queue rule's first live test and it passed. `--budget SECONDS` (total wall-clock) + `--require-complete`, **ruling #88**. What was actually unbounded, measured not asserted: the per-URL `TIMEOUT` and `flush=True` were both already there and neither bounds a *sweep* — 59 held URLs × 4 attempts × 20s is **79 minutes**, and unbounded in truth because `timeout=` is per **socket operation**. Enforced in the **main thread** against a monotonic deadline with a **daemon worker** on the socket, because a clock checked *between* units inherits exactly the unboundedness it was added to remove. Proved both ways and the bite proved first (#74): the unbounded sweep against a black-hole host was **killed at 45s having done 1 of 6**; with `--budget 25` it returned in **25.0s**, named all six `unchecked`, and exited **2** under `--require-complete`; the healthy control completed 6 of 6 and the mixed control reported the 3 that answered as answered. **Against the real population: 59 of 59 held URLs in 153.2s under a 300s ceiling, complete, exit 0.** The flip step is now specified with a measured figure instead of a hope. |
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