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

## Open — **SIX items, reconciled against disk 2026-10-10 by looking, ages to 2026-10-10**

**2026-10-10 — THE HEAD WAS TAKEN AS WRITTEN, AND THE RULE CHOSE THE DAY'S FIRST JOB FOR THE FIFTH
CONSECUTIVE RUN — ON A BOARD WHERE THE TIEBREAK TIED.** The displacement line, in one sentence: **this run
took item 1 — the gating assertions' HOME, 6 days, four displacements — and displaced item 6 a fifth time,
item 7 a third, item 5 a first, and the 10-08 forward question once.** What is new is that **nothing chose
it by judgment and the published tiebreak did not reach it either.** Items 1 and 6 were tied at **six days
AND at four displacements**, so *among items past threshold the oldest goes first* did not discriminate —
the first time the 10-05 tiebreak has failed to select. **Broken by going to the raising commits' own
timestamps rather than to their dates:** item 1 was raised by `0024344` at **11:00:51Z** (the 10-04 daily,
whose forward question it is) and item 6 by `84881d6` at **11:42:47Z** (the 10-04 weekly) — **41 minutes
and 56 seconds apart.** Age at finer granularity is still age, so this is the existing rule read at the
resolution the artefacts actually record, not a new rule. **Recorded as the tiebreak's third amendment
candidate for the 2026-10-11 review**, which already owed this board two answers and now owes three.

**AND THE TIE EXISTS BECAUSE OF THE 10-09 FAILURE, which is worth more than the tie.** Items 1 and 6 were
*not* tied on 10-08: item 1 was the board's youngest past threshold and item 6 was its oldest, and the
10-06 and 10-07 notes both predicted in writing that item 1 would be **starved** by the clause meant to
stop starvation. **A run that produced nothing aged every item equally and ended that starvation by
accident.** Displacements move only when a run *chooses*; ages move on the wall clock. The 10-09 run chose
nothing, so it displaced nothing and aged everything — and that alone converted a predicted starvation into
a tie. *The clause the tiebreak's author could not fix was repaired by a failure, which is not a mechanism
anyone should rely on and is exactly why the review still owes it an answer.*

**Item 1 is CLOSED**, and **it was wrong about its own subject.** It asked which gating assertion is wired
where it cannot observe what it asserts: **none of the 29 are.** All read `dist` or the repo root, both of
which exist in the `build` job where all 29 run. **The wrong home belongs to the BRIDGE** — only the
`verify` byte-compare promotes a claim about `dist` into a claim about the publication, and it compares
**six files of 257 (2.3%)**, two of 120 pages, with **zero of the 133 assets a page loads** — including the
**34 fonts that shipped two days earlier** and were confirmed at the origin this morning **by hand**.
`qa_bridge_coverage`, standing assertion **32**, **ruling #93**, 29 of 32 gating, proved **13 ways** with
the bite first. **Fifth for five on the one-queue rule, and the fourth consecutive closure whose real scope
was found by doing the work rather than by specifying it harder.**

**Count line: SIX open, one closed today (item 1).** Counted by reading the rows today: six. Six rather
than four because **two new items were opened** (items 9 and 10, below).

**THE RESTRAINT TEST'S ONE NUMBER: the oldest open item is now item 6 at 6 days**, up from 4 on 10-08 and
down from the 28 the test was set against on 10-04. The 10-08 note's complaint stands and is now
demonstrated rather than predicted: **the number is dominated by how recently the last item was raised**,
it rose by two days this week purely because a run failed, and at this range it is not discriminating. The
2026-10-11 review owes that an answer alongside the tie above.

**2026-10-08 — THE HEAD WAS TAKEN AS WRITTEN, AND THE RULE CHOSE THE DAY'S FIRST JOB FOR THE FOURTH
CONSECUTIVE RUN.** The displacement line, in one sentence: **this run took item 4 — self-hosted fonts, 20
days, three displacements, the oldest item past the three-displacement threshold — and displaced item 1 (the
gating assertions' HOME) a fourth time, item 6 a fourth, and the 10-07 forward question once on its first
morning.** Nothing was argued and nothing was chosen: the 10-05 tiebreak says *among items past threshold
the oldest goes first*, item 3 closed yesterday, and item 4 was next by age with no second candidate to
weigh. **Item 4 is CLOSED**: 34 woff2 faces and their five OFL notices self-hosted under
`web/public/fonts/`, the two `preconnect`s and the `fonts.googleapis.com` stylesheet removed from
`Base.astro`, guarded by **`qa_third_party_origins`, standing assertion 31, 28 of 31 gating**, proved 19
ways with the bite first. *Four for four on the one-queue rule, and all four times it produced the item
nobody would have remembered — item 1 at 18 days, item 2 at 29, item 3 at 24, item 4 at 20.*

**THIS IS THE FIRST TIME THE RULE HAS SENT A [WD] ITEM FIRST, and that is the more interesting half.** The
first three closures were all **[AE]** — instruments — which is exactly what a reader would predict of a
queue whose head is refilled by the daily forward question. Item 4 changes **served bytes on 120 pages**,
which the split assigns to the Web Developer *even when an assertion found it*, and it reached the head by
age alone. **A rule that only ever surfaces one role's work is a rule nobody has tested**; this one has now
been tested.

**AND THE 09-18 AUDIT'S OWN REASON FOR DEFERRING IT WAS RE-READ RATHER THAN INHERITED.** That note filed
this as a P1 and said *"deliberately not done in this run"* because a font migration touches the rendering
of every page in both editions and should not ride along with a deploy repair. **That reasoning is still
correct and it argues for today rather than against it:** three days from the wave flip, the choice was
between landing it now with two clean deploys ahead of the gate, or landing it *in or after* the flip
commit — which is the bundling the audit warned about, with the stakes multiplied by six pieces. The
restraint was about *what else is in the commit*, never about the calendar.

**What twenty days of specifying it never produced, again, was the scope.** The P1 said *"subset woff2
files"*. Google's css2 response is not five fonts; it is **73 `@font-face` blocks over 34 files**, carved
into `unicode-range` subsets. Hand-writing five `@font-face` rules — the obvious reading of the item, and
what every vendor's documentation shows — would have shipped **the entire Arabic face to every English
reader** and been a performance regression dressed as a privacy fix. So the bundle is a **mirror**,
generated by `agents/tools/build_font_bundle.py` from the exact URL the layout carried, and the rendering
cannot drift from what it replaced. *Third consecutive closure whose real scope was found by doing the work
and not by specifying it harder.*

**The measurement the 09-18 audit said was impossible is now taken.** That note's point 2 was that
assertion 18 *"measures the font **this runner** resolved. It cannot measure the reader's."* Self-hosting
makes those the same file, so a served Arabic page was loaded with **every host blackholed at the resolver
except our own loopback** — the reader whose network cannot reach a font vendor — and **15 faces load, all
five families, Amiri joining ratio 0.428.** With the bundle removed: **0 faces, and both Arabic families
collapse to one identical 0.571.** That second column is the state every reader behind a blocked
`fonts.gstatic.com` was in, on every page, from 2026-05-25 until this morning. **Ruling #92** came out of
the same probe: `document.fonts.check('16px Amiri')` returns **true** in both columns.

**Count line: FIVE open, one closed today (item 4), one closed 2026-10-07, one 2026-10-06, one 2026-10-05 —
four in four days.** Counted by reading the rows today: five. Five rather than four because **one new item
was opened** (item 8, below) — the first time a closure and an opening have landed on the same run.

**THE RESTRAINT TEST'S ONE NUMBER, MEASURED RATHER THAN IMPRESSED: the oldest open item is now item 6 at
4 days, down from 19 yesterday and from the 28 the test was set against on 10-04.** That is the largest
single-day fall the board has recorded, and it is an artefact worth naming rather than celebrating: it fell
because the four oldest items were closed in four days, so **the number the 2026-10-25 test measures is now
dominated by how recently the last item was raised.** At 4 days the test is passing so comfortably that it
has stopped discriminating — a queue of five fresh items would score better than a queue of one 30-day
item, which is the wrong ranking. **The 2026-10-11 review owes that an answer, and it is the second
question on this board the tiebreak's own author did not foresee** (the first being item 1's, below, still
unanswered).

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
| 5 | **FIVE dead citations on four PUBLISHED pieces** — hard 404s confirmed on two reads: `ei-ie.org` (Lebanon), `men.gov.ma` ×2 (Morocco), `osym.gov.tr` (Türkiye), `unicef.org.uk` (Rohingya). Both languages each, so **eight live pages**. | **[WD]** + Editor | **2026-10-05** | **5 days** | **1** — displaced 2026-10-10 by item 1's rule | The first complete census of all 343 outbound promises (`agents/growth/2026-10-05-the-first-complete-census-of-our-outbound-promises.md`), affordable for the first time because #88 gave the sweep a ceiling. **Deliberately not fixed in the run that found it:** these are **served bytes on published pieces**, which the split assigns to the Web Developer even when an assertion found it, and the disposition is **editorial** per #41 — *supersede, don't resurrect* — needing a replacement register read in served text or a dated 404 annotation. Rushing five annotation rewrites into the tail of a run six days before a wave flip is how a correction becomes the next defect. | nothing — but it is the only open item a **reader** can currently see |
| 6 | **`agents/stats/history.jsonl` has 102 rows for 89 dates** — ten dates carry two snapshots and one (09-14) carries four. | **[AE]** | **2026-10-04** (weekly) | **6 days — THE BOARD'S OLDEST** | **5** — displaced again 2026-10-10 by item 1's rule, after TYING item 1 on both age and displacement count and losing on the raising commits' timestamps by 41 minutes | Counted today: 102 lines, 89 distinct `as_of` values. The duplicated dates are exactly the days with more than one run, so the file is a faithful per-run log and not corrupt — **but the CHARTER's stated purpose for it is *"so week-over-week deltas accumulate"***, and any consumer taking "the row seven back" gets the wrong answer on ten of 89 dates. Nothing consumes it yet, which is the only reason it has never bitten; the Substack metrics read is what will consume it. **Not fixed here on purpose:** `madar_stats.py` is the Assertions Engineer's and the right answer (last-write-wins per date, or an explicit `run_seq`) is a design call, not a patch. This review also **declined to run `--log` a third time today** rather than add an eleventh duplicate for a corpus that has not changed. | nothing yet — it blocks the first week-over-week read |
| 7 | **The published oracle has no auditor** — `qa_served_manifest`'s emit half reads `dist`, its check half compares the **origin's manifest** against a **local build**, and the one comparison never made is the **origin's manifest against the origin's own pages**. A manifest that rode along with a deploy while describing a different tree would silently rebase every later answer with every exit code reading clean. **MEASURED BY HAND TODAY AND IT PASSES: 120 of 120 pages, both hashes, zero differences, identical page sets** — the first time this operation has ever checked a published oracle against the thing it is an oracle for. **But the audit covers 120 of the manifest's 216 claimed entries.** Its **95 asset hashes** and its **404 entry** are claimed and unverified, because the origin seed walks sitemap URLs only; that is 44% of the file unaudited, and the two-normalisation gap between the CI manifest (240) and the origin seed (238) is exactly the 404's, checked rather than assumed. **The instrument is what is owed** — a gated `--audit-origin` that does this without a human remembering to. | **[AE]** | **2026-10-06** (the daily's forward question) | **4 days** | **3** — displaced 2026-10-07 by item 3's rule, 2026-10-08 by item 4's and 2026-10-10 by item 1's. **Now AT the three-displacement threshold**, where the 10-05 tiebreak ranks it by age against items 6 and 9 — and item 1's closure removed the corner of the triangle it shares with items 7 and 8, so the 10-11 review should decide whether 7 and 8 are one item. | **Answered by hand, not by an instrument**, which is the 09-13 defect carried deliberately for one day: a green that cost a human's attention. | nothing yet — but it is the baseline every future cross-deploy answer rebases on |
| 8 | **`qa_served_manifest --check` has no honest home before the commit** — it compares a **git-derived** `<lastmod>` against a **working-tree** build, and the resolver cannot see an uncommitted file. So on **any** chrome edit it reports *silent content change* on every page, which is an artefact of the commit not existing yet and not a finding. Measured today: 119 of 120 pages flagged, every one a false positive, cleared by committing and re-running. **It has been invisible for exactly as long as it has existed**, because 10-06 and 10-07 both touched no `CHROME_GLOBS` file and both read 0/0 — and both runs reported that 0/0 in the QA log as *bounding the commit*, a reading the instrument cannot support in general. **This is open item 1's question in its other direction: not a check in the wrong home passing forever, but a check in the wrong MOMENT failing on every real change.** The fix is a home (post-commit, pre-push) or a guard that refuses to run against a dirty tree in the paths the resolver reads. | **[AE]** | **2026-10-08** (the daily's QA sweep) | **2 days** | **1** — displaced 2026-10-10 by item 1's rule | Measured, both ways, today: pre-commit 119 flagged; post-commit 0 flagged, 119 dates moved. | nothing — but two QA logs already contain a conclusion drawn from it |
| 9 | **The mandated reading list has no budget and took a whole run** — **ruling #94.** The 2026-10-09 run was not dark: it ran, spent $3.05 and 2.47M read tokens, and **failed on `usage_limit_reached` at turn 31 inside STEP 1**, dying on `RUNBOOK.md` before it reached any of the five standing functions. Measured from git, the six mandated artefacts went **119 KB (2026-09-14) to 357 KB (2026-10-08)** — 3x in 26 days, monotonic — because the operation's rules require every run to **append to the files every run must read first.** Mechanism: inline nesting instead of reference. **One reduction taken on 2026-10-10** (`CLAUDE.md` 22,559 to 16,140 bytes, **-28%**, the ruling-range audit trail archived because assertion 30 had made it redundant three days earlier). **What is owed:** the same treatment for the guidebook's `Series integrity` paragraph and for the Edition 05 ledger, which is 185 KB of which `CLAUDE.md` itself says only the Log and the newest reconciliation block are state. | **[AE]** + Manager | **2026-10-10** (state verification) | **0 days** | 0 | Measured both ways: the failure from the Actions API (`api_error: usage_limit_reached`, 429, 31 turns), the growth from `git show` at one commit per week. | **nothing red — it blocks the next run that is unlucky.** It has already cost one entire day. |
| 10 | **Four webfont families and 502 KB on an article page** — measured 2026-10-10 in headless Chrome against the built pages, not modelled: EN article **7 woff2 / 501,864 bytes**, EN home 12 / 778,376, AR home 11 / 705,600, against a 2,792,392-byte bundle on disk. The `unicode-range` mirror is working exactly as the 10-08 closure argued — it saves a first-time English reader **~2.29 MB** against the five-rule implementation — **and 502 KB is still heavy for the page 118 of our 120 URLs are.** The reductions are real (subset to our own corpus's glyph inventory rather than mirroring Google's generic slices; or drop a family) and **both are served bytes and a Designer judgment**, which is why this run measured and did not act. Specification is the growth note, which carries the method and the baseline. | **[WD]** + Designer | **2026-10-10** (growth) | **0 days** | 0 | `agents/growth/2026-10-10-what-a-reader-actually-downloads-for-our-typefaces.md` — observed network fetches, with the loopback-vs-origin caveat stated. | nothing — but it is the second open item a **reader** can feel, beside item 5 |

## Closed

| Item | Raised | Closed | By |
|---|---|---|---|
| **The gating assertions' HOME** (was open item 1) — of the assertions that gate the deploy, which are wired somewhere that cannot observe the thing they assert? | **2026-10-04** (the daily's forward question) | **2026-10-10** | **Saturday's daily run, as its first work, before the content lane and before anything new** — reaching the head at **6 days** and four displacements by the three-displacement clause, and then by a tiebreak that **tied**: items 1 and 6 matched on both age and displacement count, the 10-05 rule (*oldest past threshold goes first*) did not discriminate for the first time, and the tie was broken on the raising commits' own timestamps — `0024344` at 11:00:51Z against `84881d6` at 11:42:47Z, **41m56s apart on 2026-10-04**. **The item was wrong about its own subject, and the measurement is what says so.** Enumerated tool by tool: **none** of the 29 gating assertions is blind to what it asserts — all read `dist` or the repo root, both present in the `build` job where all 29 run, and the two named suspects (`qa_feed_enclosures`, `qa_feed_direction`) are innocent. **The wrong home belongs to the BRIDGE.** Every one of the 29 concludes something about `dist`; a reader is served the origin; and the only thing that carries a conclusion across is the `verify` byte-compare, which compares **sitemap-0.xml plus a five-file sample — six files of 257, 2.3%** — two of 120 pages and, of 137 assets, only both feeds and both sitemaps. **Everything a page loads is confirmed zero times: 46 stills, 40 share cards, 34 woff2 fonts, two stylesheets, one script.** The fonts landed 2026-10-08 as the largest single addition to the served surface in this publication's history and **not one is inside the bridge**; one was confirmed at the origin this morning **by hand**, which is the 2026-09-13 defect. `qa_bridge_coverage.py`, standing assertion **32**, **ruling #93**, 29 of 32 gating. It **measures** the ratio and deliberately does not assert a floor — widening the bridge is an edit to `.github/workflows/**` this identity cannot write, and a floor above today's reality would red every build until a patch nobody can apply lands. It **asserts** what is reachable: members exist in `dist`, every `.html` member is a page the sitemap claims, and the bridge **spans both editions and both feeds**, because a bridge that silently lost its Arabic half would byte-compare the English half and pass forever. **Proved 13 ways with the bite first (#74), on copies in /tmp** — five bites (Arabic page dropped, Arabic feed dropped, a member the build does not produce, `404.html` as an unlisted `.html` member, the probe drifting to `sitemap-7.xml`), two control negatives (a `cmp` injected into the **build** job must not widen the bridge; the untouched workflow reads CLEAN) and five failure-to-check guards, all exit 3, because **a bridge that cannot be found is not a bridge of width zero**. **And the harness found the tool overcounting while the control printed the right total.** The first parser credited every `for f in` list in the verify job; that job has **two**, and the second is the feed-cache step, which `curl -I`s for an `ETag` and compares nothing. Both parsers print **6** on the real tree because the two lists overlap exactly on the feeds — the right number for the wrong reason — and only bite 2, aimed at a file named in *both* loops, could discriminate. **A control that returns the expected number cannot distinguish a correct derivation from an incorrect one.** **The remedy is already published:** `served-manifest.json`, 256 entries, live at the origin — a 257-file bridge for one `curl`. Staged at `agents/patches/2026-10-10-verify-bridge-via-served-manifest.md`, self-contained, needing no checkout and no tool that does not exist. |
| **Self-hosted fonts** (was open item 4) — two third-party origins requested by the layout on every page, against the privacy posture | **2026-09-18** (`growth/2026-09-18-third-party-surface-audit.md`, *"Filed as a P1 to the Web Developer"*) — this cell read *carried, P1* **with no date until 2026-10-07**, in the single column this file's own restraint test is scored on | **2026-10-08** | **Thursday's daily run, as its first work, before the content lane and before anything new** — reaching the head by the **three-displacement clause** and the **10-05 tiebreak** (*oldest past threshold goes first*) at **20 days**, with no second candidate to weigh once item 3 closed. **The first [WD] item the one-queue rule has ever sent first**, and therefore the first test that the rule surfaces *served bytes* and not only instruments. `qa_third_party_origins.py`, standing assertion **31**, 28 of 31 gating. **What the specification never produced was the scope:** it said *"subset woff2 files"*, and the css2 response the layout carried is **73 `@font-face` blocks over 34 files** carved into `unicode-range` subsets — so the five hand-written `@font-face` rules the item implies would have shipped the **whole Arabic face to every English reader**, a performance regression dressed as a privacy fix. The bundle is therefore a **mirror**, generated by `build_font_bundle.py` from that exact URL, with the same families, styles, weights, ranges and `font-display`; `url()` is relative so the site's base string keeps its single home in `withBase`. All five families are OFL-1.1 and each upstream notice is served verbatim beside the faces it covers, copied from the repository the files came from rather than paraphrased — and deliberately **not** added to sitemap `customPages`, the same disposition the served manifest got on 10-06, because the 08-17 orphan rule is about pages a reader should find. **Proved 19 ways with the bite first (#74), on a copy of `dist` in `/tmp`:** the first bite is the markup removed from `Base.astro` this morning rather than an invented one, and it names **both** vendor origins; then a `<script src>` tracker, an `<img>` pixel, a `<style>` `@import`, a `style=""` `url()`, an `<iframe>`, a **protocol-relative** `//host` preload, a multi-URL `srcset` descriptor and an SVG `<use xlink:href>`. **Four control-negatives matter as much as the nine bites** — an external `<a href>` citation, the `wa.me`/`x.com` share rail, a `rel=alternate` declaration and a third-party `og:image` must all stay **silent**, because this publication points at ~180 external origins on purpose and a check that failed on those would be switched off inside a week. Three failure-to-check guards (exit 2 empty, exit 2 missing, **exit 3 nothing-to-classify**), and **guard 3 failed on its first draft and the failure was the finding**: renaming `<link` left the home page's eleven `<img>` stills and one `<script src>` still classifying clean, so the injection never reached the condition — *a guard proved by an injection that does not reach its condition is not a proved guard*, #74 pointed at a harness. **And the measurement the 09-18 audit said was impossible is now on file**, because self-hosting makes *the runner's font* and *the reader's font* the same file: with every host blackholed except our own loopback, **15 faces load across all five families** (Amiri joining ratio 0.428, Cairo 0.612); with the bundle removed, **0 faces load and both Arabic families collapse to one identical 0.571**. That second column is where every reader behind a blocked `fonts.gstatic.com` has been since 2026-05-25. **Ruling #92** came out of the same probe. |
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