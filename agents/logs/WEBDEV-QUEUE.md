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

## Open — **TWENTY-ONE items in THREE BUCKETS, reconciled against disk 2026-10-27**

**2026-10-27 — THE HEAD WAS TAKEN AS WRITTEN, AND IT IS THE SECOND SERVED DEFECT EVER TO TAKE ONE.** The
displacement line, in one sentence: **this run took item 27 — *twenty-five founder-facing artefacts render
broken, seven of them catastrophically*, raised 2026-10-19, 8 days, the oldest row in the DEFECT bucket —
and displaced items 33 and 35 inside that bucket, and items 21, 26, 28, 29, 31, 34, 36, 37, 38, 39, 40, 41,
42, 43 and 44 in OPEN, including item 43, yesterday's forward question, on its first morning.** The two
BLOCKED rows (22, 32) are out of the ordering entirely and were not displaced.

**Twenty-first selection in twenty-two daily runs made by the rule rather than by judgment, and the second
under #116.** Under the retired ordering the head this morning would have been **item 21** at 10 days, and
item 27 would have waited behind five questions while three reader-facing and founder-facing falsehoods
stood. **Item 43 was displaced on the morning after it was raised — the eleventh consecutive day a fresh
forward question lost its slot — and then was closed anyway**, by the growth function rather than from the
head, which is the first time a displaced forward question has been taken in the same run that displaced it.

**Item 27 is CLOSED at 8 days, and for the twenty-first consecutive closure the specification was not the
scope: it named TWO mechanisms and there were THREE.** All 25 artefacts repaired, **136 of 136 now render
with nothing overflowing**, the `OVERFLOW_BASELINE` is emptied and **limb B of standing assertion 33 is
promoted from measured to ASSERTED** — the floor now sits at today's reality rather than above it, which is
#93's own condition. The third mechanism is in the one review on the list, which carries no `li { display:
grid }` at all: a prose sentence inside a `<td class="n">`, `white-space: nowrap`, taking the table's
min-content 19px past its section. **Ruling #118** is what the repair earned: the intended layout survived
only in the selector that matched nothing (`.push` unstyled in seven briefs while `.push-block` sat complete
beside it; `.container` complete in two briefs whose `<main>` had been deleted), and the actual defect
survived only in git — **a bite rebuilt by hand from a correct diagnosis restored one half of a two-part
mechanism, changed the artefact, and exited 0.**

**Also repaired, found by looking at the output rather than by the probe (the 2026-08-23 rule):
`2026-08-16` and `2026-08-17` had no `<main class="container">` at all** and rendered edge to edge. Those
are the two briefs the RUNBOOK's founder-facing perimeter rule was written about on 2026-08-23. **The rule
was written, the perimeter was asserted, and the two artefacts that earned it stood broken for 65 days.**

**Count line: TWENTY-ONE open — TWO DEFECT, SIXTEEN OPEN, THREE BLOCKED. TWO closed today** (item 27 from
the DEFECT head at 8 days; item 43 by the growth function at 1 day), **THREE opened** — item 45 (Class A of
item 43's enumeration, BLOCKED on founder issue #13, and **the first row this board has carried that changes
bucket by itself on a stated date**), item 46 (nothing gates the derived `copyrightYear`, the sibling of item
44) and item 47 (**the day's forward question**). Counted by reading the rows below after removing items 27
and 43 in the same commit as their closure, per the 10-24 rule: twenty-one. **The board is UP ONE.**

**Rates, carried and moved by today:** raised 15 + 3 + 3 · closed 10 + 1 + 2 · board 20 → 21 · the 28-day
breach date stands at **2026-11-25** and today's two-for-three does not move it back.

## Superseded count line — **NINETEEN items in THREE BUCKETS, reconciled against disk 2026-10-26**

**2026-10-26 — THE HEAD WAS TAKEN AS WRITTEN, AND IT IS THE FIRST SERVED DEFECT EVER TO TAKE ONE.** The
displacement line, in one sentence: **this run took item 25 — *78 future-dated claims are SERVED and nothing has
ever re-read one*, raised 2026-10-18, 8 days, the oldest row in the DEFECT bucket — and displaced items 27, 33
and 35 inside that bucket, and items 21, 26, 28, 29, 31, 34, 36, 37, 38, 39, 40 and 41 in OPEN, including item 41,
yesterday's forward question, on its first morning.** The two BLOCKED rows (22, 32) are out of the ordering
entirely and were not displaced, because #116 took them out of it.

**Twentieth selection in twenty-one daily runs made by the rule rather than by judgment — and the first under
#116, which is the only reason this item was reachable.** Under the retired ordering the head this morning would
have been **item 21** at 9 days, and item 25 would have waited behind four questions while four served defects
stood. The 10-25 weekly review predicted exactly this and wrote it down: *in nineteen rule-made selections not one
head has been a served defect, because a defect our instruments found yesterday is by construction newer than
every question they asked last week.* One day later the new bucket reached one. **Item 41 was displaced on the
morning after it was raised, which is the tenth consecutive day a fresh forward question lost its slot — and for
the first time it lost to a reader-facing falsehood rather than to a clock.**

**Item 25 is CLOSED, and for the twentieth consecutive closure the specification was not the scope — this time
the specification's UNIT was the thing that was wrong, and it was wrong in the direction of being uncloseable.**
Item 25 asked for *a date that has not yet arrived*, 78 of them in EN. **That population needs no correction and
shrinks by itself as the calendar moves**: the bytes are right, the reader is not misled, and it can never reach
zero because every piece this publication will ever ship cites a dated plan. The population that is **wrong now**
is its complement — a date that HAS arrived carrying a verb that still points past it. **Ruling #117**, standing
queue's own head: **18 EN strong-future claims on arrived dates, 13 of them SHIELDED** by a quotation (and
'correcting' the Zambia one would break #112), by reported speech, or by a target already resolved — leaving
**5 unshielded EN sentences on 4 pieces plus 4 AR, all nine repaired in this run's first commit.** The repair is
the Edition 05 standing prohibition applied to tense, *announced ≠ measured*: each claim restated as the
register's dated announcement, which cannot expire. **And the pair disagreed once, in the direction that matters**
— `rak-iqra` EN said *will run*, the Arabic said the bare imperfect `يعمل`, unmarked for tense and still true,
because Arabic futurity is an **optional bound prefix** `سـ` homographic with the first letter of ordinary nouns.

**Count line: TWENTY open — THREE DEFECT, FIFTEEN OPEN, TWO BLOCKED. ONE closed today (item 25 from the
DEFECT head, at 8 days), THREE opened** — item 42 (the measured half of item 25: four registers whose dates have
now passed, re-read for what actually happened, because an announcement correctly labelled as an announcement is
**not** a measurement) and item 43 (**the day's forward question**) and item 44 (raised by the growth
function in the run that created its subject: nothing gates the `dateModified` it added to all 88 article
pages). Counted by reading the rows below after removing item 25's row in the same commit as its closure, per
the 10-24 rule: twenty. **The board is UP TWO** — one closed, three opened.

**Rates, carried from the 2026-10-25 review and moved by today:** raised 15 + 3 · closed 10 + 1 · board 18 → 20
· the 28-day breach date the review computed is **2026-11-25**, and today's one-for-three does not move it
forward — a board growing faster than it closes is the review's own finding, printed here rather than smoothed.

## Superseded count line — **EIGHTEEN items in THREE BUCKETS, reconciled against disk 2026-10-25 at the weekly review**

**2026-10-25, WEEKLY REVIEW — THE ORDERING IS REPLACED, AND THE TWO NUMBERS THIS FILE HAND-KEPT ARE DELETED
(RULING #116).** The rule that has chosen nineteen of the last twenty heads worked on the number it was set
on — the oldest item is **8 days** against the **28** it stood at on 2026-10-04 — and three things measured
here say what it needs is a different ordering rather than more discipline.

**(i) The tiebreak had four rungs and one real one.** Over **all eighteen open rows the displacement count
equalled the age in days, exactly.** That is an identity, not a coincidence: one head selection per day, no
dark day since 10-04, so every day that ages an item also displaces it. Which is why **this morning's
selection reached the 10-16 fourth rung for the first time** — items 20 and 21 tied at 8 days, the 10-11
ANSWER 1 narrowing was applied to separate them and returned a tie at seven displacements each, and it had
to. *A second key that is a copy of the first cannot break a tie the first did not break.*

**(ii) The one real key could not see a byte that is currently false, and could not see a wall.** Four rows
name artefacts that are **wrong now** — item 25 (78 future-dated served claims), item 27 (25 broken
founder-facing artefacts), item 33 (three misquoted citations), item 35 (**4 of 15 acronym expansions with no
evidence**, re-measured during this review and unchanged since 10-23, one of them on the piece that earned
#101). **In nineteen rule-made selections, not one head has been a served defect**, because a defect found
yesterday is by construction newer than every question asked last week. And two rows cannot be closed by
anybody here — on the retired rule **item 22 took the head on 2026-10-27** holding a patch that needs issue
#7's permission, open **35 days**.

**(iii) *Nothing reaches 28 days* was arithmetic nobody did.** Measured 10-19 → 10-25: **15 raised, 10
closed, board 13 → 18**; raise 2.14/day, closure 1.43/day. Under oldest-first the oldest age converges on
board ÷ closure rate, so it reaches 28 days on **2026-11-25**. **The closure rate holds that ceiling. The
threshold only decided who waits.**

**What changed, in four lines.** Every row carries **one** time cell, `Raised`; age is `today − Raised`,
computed by the run that needs it, and **the Age and Displaced columns are deleted** — they were two copies
of one number derivable from a date three cells to their left (#75), and **fifteen of eighteen arrived at
this review stale under a header rewritten that morning claiming *ages to 2026-10-25***, which is limb 3 of
the 10-04 second amendment for the fourth time in eight days. The tiebreak is **two rungs: age, then raise
order**. Rows are bucketed **BLOCKED · DEFECT · OPEN** by the run that raises them, and **the head is the
oldest DEFECT if any DEFECT is open, otherwise the oldest OPEN.** The three-displacement threshold is
retired, having been a second name for age throughout its life.

**Rates, printed here every review from today (#116 clause 5):** **raised 15 · closed 10 · net +5 · board
13 → 18 · 28-day breach 2026-11-25.**

**Count line: EIGHTEEN open — FOUR DEFECT, TWELVE OPEN, TWO BLOCKED.** Counted by reading the rows below
after bucketing them; the board is unchanged in size by this review, which closed no item and raised none.
The daily run's own count line for 2026-10-25 is immediately below, demoted rather than deleted, because it
is the exhibit.

## Superseded count line — EIGHTEEN open, reconciled against disk 2026-10-25 **by the daily run**, "ages to 2026-10-25" — **and fifteen of the eighteen rows disagreed with that claim by one to three days (ruling #116, filed at the weekly review the same afternoon)**

**2026-10-25 — THE HEAD WAS TAKEN AS WRITTEN, AND FOR THE FIRST TIME THE TIEBREAK NEEDED ITS LAST RUNG.**
The displacement line, in one sentence: **this run took item 20 — *four webfont families and 521,408 bytes
on an ENGLISH article*, 8 days, seven displacements — and displaced item 21 an eighth, items 22, 25 and 26
a seventh each, items 27 and 28 a sixth each, item 29 a fifth, items 31 and 32 a fourth each, items 33 and
34 a third each, items 35, 36 and 37 a second each, and item 38 a first.**

**Ten items stood at or past the three-displacement threshold (20, 21, 22, 25, 26, 27, 28, 29, 31, 32)**
and the 10-05 tiebreak discriminated at **8, 8, 7, 7, 7, 6, 6, 5, 4 and 4** — which **TIED items 20 and
21 at 8 days**. The 10-11 ANSWER 1 narrowing did not separate them either: both carry **seven**
displacements. So the ladder went to the **10-16 fourth level**, the one its author called *the last the
artefacts can support* — **both rows were raised by the same commit, `330b936`, the 10-17 daily**, one from
the growth function and one as that day's forward question, and item numbers are assigned in raise order,
so **item 20 goes first.** This is the first selection to reach that rung since it was adopted on 10-16.
**Nineteenth selection in twenty daily runs made by the rule rather than by judgment.** The 10-24 status
queued **item 38** for this morning and clause (2) overruled it, for the **ninth** consecutive day on which
a fresh forward question lost to the threshold clause.

**Item 20 is CLOSED, and for the nineteenth consecutive closure the specification was not the scope** —
this time the item contained a sentence that was simply false. It declines the subset reduction because
it would break *"a byte-for-byte mirror … which is the property `qa_third_party_origins` … rest[s] on"*;
that assertion asserts **origin and nothing else**, contains no hash and no byte comparison, and the
mirror is a design choice in `build_font_bundle.py`'s header held by no gate. *Item 26's question pointed
at a queue item's reason for not acting.* (The subset stays declined on the correct ground: a subset over
today's 44 pieces is the 2026-06-07 hand-maintained-artefact defect with an invisible failure mode.)

What the measurement found instead: **a woff2 in `dist` is not a byte anybody has received**, and all
thirty-eight standing assertions read bytes that EXIST. **Standing assertion 39, `qa_font_payload`**,
ruling **#115**: 39 assertions, 24 postbuild, **36 of 39 gating**, all derived by `qa_patch_queue`.
Two `<em>` tags were slanting Arabic on both home pages — **131,100 bytes to paint 29 characters** — and
the stylesheet had already said *Arabic is not slanted* twice, both times per component. One rule took the
**Arabic home page from 426,728 to 295,628, −30.7%**. *And bite 2, the real 2026-10-17 defect restored,
DID NOT BITE*: the Arabic strapline ends in a full stop and U+002E is inside every Latin subset, so those
146,872 bytes were never a dead fetch but a fetch justified by the cheapest glyph in the file.

**AND THE GATE'S OWN STATED LIMITATION ARRIVED THE SAME DAY.** Its header says the six-page set is a
sample and a defect living outside it is outside the gate. The afternoon's corpus census found
`amiri-italic-400-arabic.woff2` still fetched by **twelve Arabic article pages**, from
`.body-main :global(em) { font-style: italic }` in the Arabic template, which outranks `global.css` at
equal specificity — 686 slanted characters of quoted Arabic on the Iraq piece alone. Fixed in the Arabic
template; **AR corpus 21,349,860 → 19,776,660, exactly 12 × 131,100.** *A sampled gate is not a weaker
gate; it is a gate with a population it has not been shown.*

**Count line: EIGHTEEN open, ONE closed today (item 20 from the head, at 8 days), THREE opened** — item
39 (item 20's Designer half: drop a family, and what replaces italic emphasis in Arabic now the slant is
gone, both now carrying census numbers), item 40 (the 89 painted Arabic runs whose own stack names no
bundled Arabic family), and item 41 (**the day's forward question**). Counted by reading the rows below,
after removing item 20's row in the same commit as its closure, per the rule the 10-24 run wrote:
eighteen. **The board is UP TWO** — one closed, three opened — after one flat day.

**THE RESTRAINT TEST'S ONE NUMBER (10-11, ANSWER 2) — READ TODAY, ON THE DATE IT WAS SET FOR.** The age of
the oldest item that has been displaced at least once: **8 days (item 21)**, against the **28 days** the
test was set at on 2026-10-04. It is **down 20**, and the Assertions Engineer's dated restraint test is
passed on its own terms, assertion count excluded in both directions as the test requires. **The
CHARTER's standing trigger — *no new persona is considered before 2026-10-25* — is now live**, and the
consideration itself belongs to the weekly review, not to this daily: the daily's job was to read the
number on the date, and the number is 8.

## Superseded count line — SIXTEEN open, reconciled against disk 2026-10-24, ages to 2026-10-24

**2026-10-24 — THE HEAD WAS TAKEN AS WRITTEN, AND THE COUNT LINE ABOVE IT WAS WRONG BY ONE.** The
displacement line, in one sentence: **this run took item 19 — *which of our annotations assert something
their own URL does not support?*, 8 days, seven displacements, the board's oldest item past the
three-displacement threshold and taken outright on age — and displaced items 20 and 21 a seventh each,
items 22, 25 and 26 a sixth each, items 27 and 28 a fifth each, item 29 a fourth, items 31 and 32 a third
each, items 33 and 34 a second each, and items 35, 36 and 37 a first each.**

**Nine items stood at or past the three-displacement threshold (19, 20, 21, 22, 25, 26, 27, 28, 29)** and
the 10-05 tiebreak discriminated at **8 days against 7, 7, 6, 6, 6, 5, 5 and 4**, so nothing tied, the
displacement counts were never compared and the 10-11 and 10-16 levels were never reached. **Eighteenth
selection in nineteen daily runs made by the rule rather than by judgment.** The 10-23 status queued
**item 37** for this morning and clause (2) overruled it, for the **eighth** consecutive day on which a
fresh forward question lost to the threshold clause.

**THE COUNT LINE THIS FILE CARRIED YESTERDAY WAS WRONG, AND IT IS THIS FILE'S OWN DEFECT CLASS.** The
10-23 line read **FIFTEEN open** and said in the same paragraph *"the board is UP TWO"* against a 10-22
line reading **FOURTEEN** — 14 + 2 = 16 — and claimed *"counted by reading the rows below: fifteen"*, while
reading the rows below gives **SEVENTEEN**, because **item 18's row was never removed when item 18 closed
on 10-22.** Three numbers for one board in one screen: 15 in the prose, 16 in the delta, 17 in the table.
**The true figure on arrival this morning was SIXTEEN.** This is **#57** — *count against the population,
never against yesterday's number* — in the one artefact the one-queue rule makes binding, five days after
#106 found the same shape in the ruling register's family counts, and the mechanism is the same: a row
that outlives its item makes the table uncountable, so the only cheap check available silently stops
agreeing with anything. Item 18's row is removed here. **Standing rule, and it costs one line: the run
that closes an item deletes its row in the same commit as the Closed entry.**

**Item 19 is CLOSED, and for the eighteenth consecutive closure the specification was not the scope** —
this time the word was **URL**. Read literally the item needs a classifier to sort *claim* from
*description* before it can ask anything, and #113 is one-day-old evidence of what a classifier buys on a
prose boundary. It is unnecessary: **a digit is an exact boundary the artefact supplies**, so the question
narrows to *is this number anywhere our own figure discipline can reach it?* **Standing assertion 38,
`qa_annotation_figures`**, ruling **#114**: 38 assertions, 23 postbuild, **35 of 38 gating**, all derived
by `qa_patch_queue`. Measured: **2,033 annotation quantities, 423 in no body of either edition, across 40
of 44 pieces.** *And the first bite did not bite* — it changed the file outside the brackets the check
read and exited 0 like a passing control, which is how the item's own wording was found to be hiding 43%
of its subject.

**Count line: SIXTEEN open, ONE closed today (item 19 from the head, at 8 days), ONE opened** — item 38
(the day's forward question: assertion 38 measures the part of the ruler made of digits, and item 19's own
founding instance is in the other part — an annotation's non-numeric prose asserts a rename, a mandate, a
named human, a hedge, and nothing reads any of them). Counted by reading the rows below, after removing
the row that should have gone on 10-22 **and the row of the item this run itself closed, which is the
new rule binding the run that wrote it**: sixteen. **The board is FLAT** — one closed, one opened — and it
is flat for the first time in nine days.

**THE RESTRAINT TEST'S ONE NUMBER (10-11, ANSWER 2) — the age of the oldest item that has been displaced
at least once: it reads 7 days (items 20 and 21), DOWN from 8.** Closing item 19 moved it, because item 19
*was* the oldest displaced item. It is 7 against the 28 the test was set at, and **the reading that
matters is TOMORROW, Sunday 2026-10-25** — the day the Assertions Engineer's dated restraint test is read
and the day the CHARTER's standing trigger says no new persona may be considered before.

## Superseded count line — FIFTEEN claimed, SIXTEEN true, reconciled against disk 2026-10-23, ages to 2026-10-23

**2026-10-23 — THE HEAD WAS TAKEN AS WRITTEN, AND AN ITEM TWO RUNS HAD DECLARED UNACTIONABLE WAS THE
ONE THAT CLOSED.** The displacement line, in one sentence: **this run took item 17 — *a named
institution expanded in a body the piece's own annotations never carry*, 8 days, five displacements,
the board's oldest item past the three-displacement threshold and taken outright on age — and
displaced item 19 a seventh, items 20 and 21 a sixth each, items 22, 25 and 26 a fifth each, items 27
and 28 a fourth each, item 29 a third, items 31 and 32 a second each, and items 33 and 34 a first
each.**

**Nine items stood at or past the three-displacement threshold (17, 19, 20, 21, 22, 25, 26, 27, 28)**
and the 10-05 tiebreak discriminated at **8 days against 7, 6, 6, 5, 5, 5, 4 and 4**, so nothing tied,
the displacement counts were never compared and the 10-11 and 10-16 levels were never reached.
**Seventeenth selection in eighteen daily runs made by the rule rather than by judgment.** The 10-22
status queued **item 34** for this morning and clause (2) overruled it, for the **seventh**
consecutive day on which a fresh forward question lost to the threshold clause.

**Item 17 is CLOSED, and for the seventeenth consecutive closure the specification was not the scope
— this time the item had been declared UNACTIONABLE AS SPECIFIED on 10-17 and it was.** The question
as written (*can a name-boundary assertion be built?*) has the answer two runs gave it: no, and the
10-16 negative result stands — two detectors over one population returned 3 and 46. **What was never
asked is whether the artefact supplies a boundary the check does not have to guess**, and it does
whenever the name carries an acronym. **Standing assertion 37, `qa_acronym_evidence`**, ruling
**#113**: 37 assertions, 22 postbuild, **34 of 37 gating**, all derived by `qa_patch_queue`.
*An item is unactionable as specified for exactly as long as nobody re-specifies it, and three runs
read the 10-17 amendment as a verdict on the subject rather than on the sentence.*

**Count line: FIFTEEN open, ONE closed today (item 17 from the head, at 8 days), THREE opened** — item
35 (the four unevidenced acronym expansions the instrument found in *our* served prose — `KJSEA`,
`PSLE`, `TMIS`, `J-PAL` — handed over rather than fixed, because a fix that changes served bytes is
the Web Developer's even when an assertion found it, and because two of the four registers cannot be
read from this runner and #101 clause 1 demands the register's own wording) and item 36 (the day's
forward question: every name instrument this operation owns is anchored on a Latin token, so the
Arabic edition — the edition #101 makes the control precisely because it is FORCED to read the
register — is the one edition none of them can see into, and that is now true of #101's names, #112's
quotations and #113's acronyms alike) and item 37 (**the day's forward question**, raised by the
content function rather than by the QA sweep: the morning's new gate was run on the afternoon's own
draft and could not see its live case — 123 acronym tokens in the EN corpus, **15 anchored, 12.2%**).
Counted by reading the rows below: fifteen. **The board is UP TWO**, and the second opening came from
turning a new instrument on the operation's own work in progress rather than from a sweep.

**THE RESTRAINT TEST'S ONE NUMBER (10-11, ANSWER 2) — the age of the oldest item that has been
displaced at least once: it reads 7 days (item 19), DOWN from 8.** Closing item 17 moved it, because
item 17 *was* the oldest displaced item and item 19 was raised a day later. It is 7 against the 28
the test was set at, and **the reading that matters is this Sunday, 2026-10-25** — two days away.

## Superseded count line — FOURTEEN items, reconciled against disk 2026-10-22, ages to 2026-10-22

**2026-10-22 — THE HEAD WAS TAKEN AS WRITTEN, AND THE TIE WENT TO THE DISPLACEMENT COUNT.** The
displacement line, in one sentence: **this run took item 18 — *a 200 is not the document we cited*, 7
days, six displacements, tied with item 17 as the board's oldest past the three-displacement threshold
and taken on displacement count — and displaced item 17 a fifth, item 19 a sixth, items 20 and 21 a
fifth each, items 22, 25 and 26 a fourth each, items 27 and 28 a third each, item 29 a second, and
items 31 and 32 a first each.**

**Eight items stood at or past the three-displacement threshold (17, 18, 19, 20, 21, 22, 25, 26)** and
the 10-05 tiebreak discriminated at **7 days against 7, 6, 5, 5, 4, 4 and 4**, which **tied items 17
and 18**, both raised 2026-10-15. The tie went to the next level, **displacement count, 6 against 4**,
per the 10-11 ANSWER 1 narrowing (*the finer clock is reached only when the displacement counts also
tie*), so the 10-16 fourth level was never needed. **Sixteenth selection in seventeen daily runs made
by the rule rather than by judgment.** The 10-21 status queued **item 31** for this morning and clause
(2) overruled it, for the **sixth** consecutive day on which a fresh forward question lost to the
threshold clause.

**Item 18 is CLOSED, and for the sixteenth consecutive closure the specification was not the scope** —
this time about where the token comes from. The item specified *a distinctive string from the
annotation*; the finding is that **the annotations already carry 529 of them, inside quotation marks**,
and that nothing needed inventing. **Standing assertion 36, `qa_citation_identity`**, ruling **#112**:
36 assertions, 21 postbuild, **33 of 36 gating**, all derived by `qa_patch_queue`.

**Count line: FOURTEEN open, ONE closed today (item 18 from the head, at 7 days), TWO opened** — item
33 (the three served-page citation defects the instrument found in *our* prose, plus one soft-dead
citation to dispose of under #100, handed over rather than fixed because a fix that changes served
bytes is the Web Developer's even when an assertion found it) and item 34 (the day's forward question:
the instrument could compare only 90 of 218 registers and the 80 it declined are disproportionately
the primary sources this publication's method rests on, so every reachability rate we own may be a
rate over the documents our clients happen to be able to open). Counted by reading the rows below:
fourteen. **The board is UP ONE.**

**THE RESTRAINT TEST'S ONE NUMBER (10-11, ANSWER 2) — the age of the oldest item that has been
displaced at least once: it reads 7 days (item 17), UP from 6.** Closing item 18 could not hold it,
because item 17 was raised the same day and is now the oldest displaced item on the board. It is 7
against the 28 the test was set at, and **the reading that matters is this Sunday, 2026-10-25** — three
days away.

## Superseded count line — THIRTEEN items, reconciled against disk 2026-10-21, ages to 2026-10-21

**2026-10-21 — THE HEAD WAS TAKEN AS WRITTEN, AND THE DAY'S LARGEST FINDING CAME FROM STATE
VERIFICATION RATHER THAN FROM THE HEAD.** The displacement line, in one sentence: **this run took item
15 — *which of our published CLAIMS can no longer be re-verified by anybody, including us?*, 7 days,
six displacements, the board's oldest item past the three-displacement threshold — and displaced item
17 a fourth, item 18 a sixth, item 19 a fifth, items 20 and 21 a fourth each, items 22, 25 and 26 a
third each, items 27 and 28 a second each, and item 29 a first on its first morning.**

**Six items stood at or past the three-displacement threshold (15, 17, 18, 19, 20, 21)** and the 10-05
tiebreak discriminated at **7 days against 6, 6, 5, 4 and 4**, so the displacement counts were never
compared and the 10-16 fourth level was never reached. **Fifteenth selection in sixteen daily runs made
by the rule rather than by judgment.** The 10-20 status queued item 29 for this morning and clause (2)
overruled it, for the fifth consecutive day on which a fresh forward question lost to the threshold
clause.

**Item 15 is CLOSED, and for the fifteenth consecutive closure the specification was not the scope** —
this time by one word. It asked whether a register is openable *today, **by us***; the finding is that
*by us* was the wrong half. **Standing assertion 35, `qa_claim_registers`**, ruling **#111**: 35
assertions, 20 postbuild, **32 of 35 gating**, all derived by `qa_patch_queue`.

**AND THE RUN OPENED THE DAY ON A RED DEPLOY, which is why the board is up by two rather than up by
one.** `39404252315` failed on 2026-10-20 at the `qa_jsonld` build step — **80 dangling JSON-LD `@id`s**
from the 10-20 growth commit — so `deploy` and `verify` were skipped and **the origin served the 10-19
build for two days** while five commits sat on `main`. Repaired and pushed inside eleven minutes. What
it exposed is **item 30**: `npm run build` runs **twenty of the thirty-two** gating assertions, the
other twelve are workflow steps a local run cannot reach, and a green postbuild reads exactly like a
green deploy. Today closed the *reachable* half (`npm run gates`, derived from the workflow, which found
CLAUDE.md's prose claiming eleven) and left the *gating* half open, because a runner somebody must
remember is 2026-09-13's *a habit, not a gate*.

**Count line: FOURTEEN open, ONE closed today (item 15 from the head, at 7 days), THREE opened** —
item 30 (the twelve unreachable gates, raised by the P0 repair), item 31 (the day's forward question:
every instrument runs inside the agent step and the deploy runs after it, so no run has ever observed
its own publication, and ruling #71's requirement is prose that nothing fails on), and item 32 (the 40
registers that exist in one copy, which is an *action* this run deliberately did not take because it is
an outbound write to somebody else's service). Counted by reading the rows below: fourteen. **The board
is UP TWO**, and the reason is worth naming rather than smoothing: **one of today's three openings came
from a defect found in state verification, not from the head** — the first time in sixteen runs that
the board grew because of something the run arrived to rather than something it chose.

**ADDENDUM, same run, 2026-10-21 afternoon — ITEM 30 IS CLOSED, about an hour after it opened, and
the count line above is amended rather than rewritten.** The reason it was opened rather than closed on
the spot was a cost nobody had measured: wiring the twelve into `postbuild` means each runs twice in CI.
**Measured instead of assumed (the 10-19 addendum's habit): all twelve run in 1.88 s, and a full
`npm run build` with all thirty-two gates takes 32 s.** Two seconds is not a reason to let a local build
mean something different from a deploy. One entry added to `postbuild` — the runner, which derives the
list from the workflow — so `qa_patch_queue` still reads **35 / 12 / 20 / 32 of 35**, correctly: these
twelve always gated the deploy and what changed is where they can be *reached*. **Proved by re-injecting
the exact 10-20 regression**: removing `...publisherNodes()` from `collectionJsonLd` now turns
`npm run build` **red at exit 1** on this machine, where on 10-20 it exited 0 four times running.
Restored, green. **So the board is THIRTEEN open, ONE closed from the head (15) and ONE closed from the
day's own P0 (30), TWO opened (31, 32) — UP ONE, not up two.**


**THE RESTRAINT TEST'S ONE NUMBER (10-11, ANSWER 2) — the age of the oldest item that has been
displaced at least once: it reads 6 days (items 17 and 18), unchanged from yesterday.** Closing item 15
could not move it below 6, because 17 and 18 were filed the day after it. It is 6 against the 28 the
test was set at, and **the reading that matters is this Sunday, 2026-10-25**, when the 09-27 split is
read against it — four days away.

## Superseded count line — TWELVE items, reconciled against disk 2026-10-20, ages to 2026-10-20

**2026-10-20 — THE HEAD WAS TAKEN AS WRITTEN, AND IT WAS NOT THE HEAD YESTERDAY PLANNED.** The
manager status of 10-19 queued **item 28** — its own forward question — for this morning. **The rule
outranks the plan**: clause (2) sends an item past three displacements first regardless, and clause
(1)'s freshness never reaches the front of a board that has five. The displacement line, in one
sentence: **this run took item 14 — *which of this publication's claims are properties of a
COMPOSITION rather than of a file?*, 7 days, seven displacements, tied for the board's oldest past
the threshold — and displaced item 15 a sixth, item 17 a third, item 18 a fifth, item 19 a fourth,
items 20 and 21 a third each, item 22 a second, items 25 and 26 a second each, and items 27 and 28 a
first each.**

**Five items stood at or past the three-displacement threshold (13, 14, 15, 18, 19)** and the 10-05
tiebreak discriminated at **7 days against 7, 6, 5 and 4** — which **tied items 13 and 14**, both
raised 2026-10-13. The tie went to the next level, **displacement count, 7 against 6**, per the
10-11 ANSWER 1 narrowing (*the finer clock is reached only when the displacement counts also tie*),
so the 10-16 fourth level was never needed. **Fourteenth selection in fifteen daily runs made by the
rule rather than by judgment.**

**Items 14 AND 13 are both CLOSED, by one instrument — and for the fourteenth consecutive closure
the specification was not the scope.** Item 14 asked whether the *build* can ask a composition
question at all. The answer is a **boundary**, filed as ruling **#109**: sort composition defects by
who assembles, and the **build** (inlined fragments into one cascade) and a **consumer** (the
JSON-LD graph, two feeds, an hreflang cluster) are both in the **served bytes**, while only the
**layout engine** needs a render. So **a static check states the collision and never the
consequence** — and the collision is the right thing to gate, because it is true before anyone has
looked. **Standing assertion 34, `qa_composition`**, gated from `postbuild`: 34 assertions, 19
postbuild, **31 of 34 gating**, all derived by `qa_patch_queue`.

**Item 13 closed without the browser it specified.** Its property — each inlined cover's kicker fill
is its own registry accent — is limb 2, **licensed by limb 1 and withheld when limb 1 fails**,
because a declared value is the computed value exactly when nothing else can match the element. A
cheap check licensed by a cheaper one, with the licence machine-checked rather than commented.
Control green, **three bites red**, each injection asserted to have changed the artefact first.

**Count line: TWELVE open, TWO closed today (items 14 and 13, both from the head, both at 7 days),
ONE opened (item 29 — the day's forward question: three of the four composition surfaces measured
clean today have no gate behind them, and the run that filed a ruling saying the build CAN ask them
gated only the cheapest).** Counted by reading the rows below: twelve. **The board is DOWN ONE, the
second net reduction since 2026-10-05 and the second in two days.** It is down for a reason worth
naming: **two items closed and only one opened, because the two closures shared one answer.** Item
13 was a defect with a gate owed and the gate was built; item 14 was a question, and a question's
answer is normally two more questions — this one produced a boundary that disposed of both.

**THE RESTRAINT TEST'S ONE NUMBER (10-11, ANSWER 2) — the age of the oldest item that has been
displaced at least once: it reads 6 days (item 15, six displacements), DOWN from 7.** Closing items
13 and 14 moved it, which is the first time this number has fallen since it was set. It is 6 against
the 28 the test was set at, and **the reading that matters is this Sunday, 2026-10-25**, when the
09-27 split is read against it.

## Superseded count line — THIRTEEN items, reconciled against disk 2026-10-19, ages to 2026-10-19

**2026-10-19 — THE HEAD WAS TAKEN AS WRITTEN, AND THE TIEBREAK DID NOT NEED ITS LATER LEVELS.** The
displacement line, in one sentence: **this run took item 12 — no founder-facing artefact has ever been
checked for LAYOUT, 7 days, seven displacements, the board's oldest item past the three-displacement
threshold — and displaced items 13 and 14 a seventh each, item 15 a fifth, item 17 a second, item 18 a
fourth, item 19 a third, items 20 and 21 a second each, and items 22, 23, 25 and 26 a first each.**
**Items 25 and 26 are the weekly review's own bet, parts A and B, displaced on their first morning** —
which is the one-queue rule working rather than failing: clause (4) made the bet an item like any other
precisely so it would queue by the same rule as everything else, and clause (2) outranks freshness.

**Six items stood at or past the three-displacement threshold (12, 13, 14, 15, 18, 19)** and the 10-05
tiebreak discriminated at **7 days against 6, 6, 5, 4 and 3**, so the displacement counts were never
compared and the 10-16 fourth level was never reached. **Thirteenth selection in fourteen daily runs made
by the rule rather than by judgment.**

**Item 12 is CLOSED, and for the THIRTEENTH consecutive closure the specification was not the scope.**
The item specified *every founder-facing artefact renders its own footer* plus *no element overflows its
container*. **Counted before implementing: 113 of 127 artefacts carry a `<footer>` element, and the newest
brief and newest review are both among the fourteen that do not.** An assertion written to the item's
letter would have failed on correct artefacts and been switched off inside a week (#35), so the property
asserted is the template-agnostic one the 10-12 defect actually violated — **the document renders to its
own end**, measured against each file's own source. 127 of 127 clean, floor 90%, thinnest real margin
98.8%. **And the second half does not gate, which is the day's ruling (#108):** the overflow probe found
**25 broken artefacts** including **seven documents up to 34,254 px wider than the viewport**, and when
the same shape was injected fresh it **did not bite** — Chrome never grows `scrollWidth` for inline text
in an `overflow: visible` block. A check that cannot be shown to fail on the defect it exists to catch
does not gate a build, so it prints its blind spot beside its findings instead. **Two items opened, both
from the halves this closure could not reach.**

**Count line: THIRTEEN open, TWO closed today (item 12 from the head; item 23 from the growth function,
at one day old), TWO opened (item 27 — the repair of the 25, a Web Developer and Designer judgment; item
28 — the day's forward question, the Range-rectangle oracle and the four render assertions that have never
been asked what their rulers can represent).** Counted by reading the rows below: thirteen. **The board is
DOWN ONE — the first net reduction since 2026-10-05.** It is down because one of the two closures did not
split: item 23 was a defect with a decision in it, the decision was taken and written down (the definite
article is ignored), and a defect that is actually fixed closes without issue. Item 12 split as every head
has for thirteen consecutive closures, into an instrument, a repair and a question.

**THE RESTRAINT TEST'S ONE NUMBER (10-11, ANSWER 2) — the age of the oldest item that has been displaced
at least once: it reads 6 days (items 13 and 14, seven displacements each), unchanged from yesterday.**
Closing item 12 could not move it below 6, because 13 and 14 were filed the day after it. It is 6 against
the 28 the test was set at, and **the reading that matters is this Sunday's, 2026-10-25**, when the 09-27
split is read against this number.

## Superseded count line — THIRTEEN items, reconciled against disk 2026-10-18 at the WEEKLY REVIEW, ages to 2026-10-18

**2026-10-18, WEEKLY REVIEW — THE HEAD WAS TAKEN AS WRITTEN, AND IT WAS TAKEN TWICE IN ONE DAY.** The
displacement line, in one sentence: **the review took item 24 — the day's own forward question, *which of our
RULES has never been tested against the world it claims about?*, raised at the head by this morning's daily
and one day old — and displaced items 12 and 14 a seventh each, item 13 a sixth, item 15 a fifth, item 17 a
second, item 18 a fourth, item 19 a third, items 20 and 21 a second each, and items 22 and 23 a first each.**

**Item 24 is CLOSED, and the twelfth consecutive closure where the specification was not the scope.** The
item asked which of our rules had never been tested against the world. **One was, by measurement rather than
by argument, and it had been false for 33 days:** `madar-daily.yml`'s header states that *if a run is still
hours late on this offset the delay is not contention* and the day must stop being planned around the cron.
**All 38 scheduled runs since the 2026-09-15 offset change started between 4 h 14 m and 7 h 42 m late, median
5 h 37 m** — the condition continuously true, never once evaluated, because the sentence lives in
`.github/workflows/**` where no run has any reason to look. The CHARTER's cadence table said the day began
at **~08:00 Dubai** while it began at **~14:00**. Ruling **#107**; the measurement is now printed by
`run_envelope.py` on every call and the cadence table carries a measured column with the weekly review named
as its owner. **Two items opened from the week's two rulings, both entered at the head.**

**Count line: THIRTEEN open, ONE closed today at the review (item 24), TWO opened (item 25 — the future-dated
claim audit of the SERVED corpus, which is next week's bet part A; item 26 — #106's forward question, the
exemption set in `agents/tools/**`, which is part B).** Counted by reading the rows below: thirteen. **The
board is UP ONE.** The honest reason is the same shape as the last three weeks: the item closed was a
question, and a question's answer is two more questions. **The cron half that needs a workflow write was
folded into item 22 rather than given a number of its own** — item 22 already is *the things no identity here
has a credential for*, and a second row for the same credential would be a second queue with one entry.

**THE RESTRAINT TEST'S ONE NUMBER (10-11, ANSWER 2) — the age of the oldest item that has been displaced at
least once: it reads 6 days (item 12, seven displacements), unchanged from this morning.** Closing item 24
could not move it: item 24 was one day old. It is 6 against the 28 the test was set at, and **the reading
that matters is next Sunday's, 2026-10-25**, when the 09-27 split is read against this number.

## Superseded count line — TWELVE items, reconciled against disk 2026-10-18, ages to 2026-10-18

**2026-10-18 — THE HEAD WAS TAKEN AS WRITTEN, AND THE TIEBREAK DID NOT NEED ITS LATER LEVELS.** The
displacement line, in one sentence: **this run took item 11 — the run envelope is invisible to the run it
binds, 7 days, six displacements, the board's oldest item past the three-displacement threshold — and
displaced items 12 and 14 a sixth each, item 13 a fifth, item 15 a fourth, item 17 a FIRST, item 18 a third,
item 19 a second, and items 20 and 21 a first each.**

**Item 17 was displaced for the first time**, after two days of not being displaced because the content
function kept taking its open job. It did not today: **the pipeline was empty** — Edition 05 closed on
10-13, nothing is held, and the newest recon on disk was from 09-27 — so the content function opened recon
on a fresh candidate instead of auditing published pieces. That is a choice and it is written down as one.
Item 17 audits pages that have been wrong for 103 days and will keep; a content pipeline with nothing in it
is the one thing the CHARTER's content function does not permit.

**Five items stood at or past the three-displacement threshold (11, 12, 13, 14, 15)** and the 10-05 tiebreak
discriminated at **7 days against 6, 5, 5 and 4**, so the displacement counts were never compared and the
10-16 fourth level was never reached. **Twelfth selection in thirteen daily runs made by the rule rather
than by judgment.** Item 11's row carried a note that it *"is not ranked by age"* because its Blocks cell
reads YES — written to stop it being starved, not to exempt it — and today age selected it anyway, so the
note never had to be invoked.

**Item 11 is CLOSED, and for the ELEVENTH consecutive closure the specification was not the scope — this
time the specification was the part that was wrong.** The item recorded its own actionable half as
**applied**, on the ground that `CLAUDE.md` now carries both numbers and the RUNBOOK requires a commit per
standing function. **That accounting was wrong on one of the two axes.** `--max-turns 180` is genuinely
dark: nothing inside the agent step counts turns. **`timeout-minutes: 90` is a wall clock, and the run's own
`run_started_at` is one `gh api` call with the `actions: read` grant the same job block already holds.** It
answered on the first attempt. **Half the envelope was observable from inside for the five runs that
believed all of it was dark**, because recording a number reads as closing the gap and the heading above it
said there was nothing to look at (ruling **#105**). `agents/tools/run_envelope.py` parses both numbers out
of the workflow file, refuses rather than remembering a budget, prints the turn axis as UNMEASURABLE on
every call, and logs each function's elapsed minutes so the 15-minute reserve stops being a judgment.
**Proved 37 ways; the harness caught two errors, both in the proof and neither in the tool.**

**What item 11 does NOT close, carried into item 22 rather than buried in a closure note:** the turn axis is
still dark, the staged workflow patch still needs a credential no identity here holds, and the
`run-failure` issue still carries neither `subtype` nor `num_turns`.

**Count line: TWELVE open, ONE closed today (item 11), THREE opened (item 22 — the half of item 11 that
needs a workflow write, split out so it stops riding along inside a closed item; item 23 — the Arabic
directory ordered by the English collation key, from the growth function; item 24 — the day's forward
question, entered at the head).** Counted by reading the rows below today: twelve. **The board is UP TWO**,
and the honest reason is the same as the 10-17 split: closing item 11 separated the half this identity can
reach from the half it cannot, and the half it cannot is queued under its own number rather than described
as finished.

**THE RESTRAINT TEST'S ONE NUMBER (10-11, ANSWER 2) — the age of the oldest item that has been displaced at
least once: it reads 6 days today (item 12, six displacements), down from 7.** It fell for the first time in
three days, and only because the item closed was the sole oldest rather than one of a tied pair. It is 6
against the 28 the test was set at; the reading that matters is 2026-10-25's, one week from today.

## Superseded count line — TEN items, reconciled against disk 2026-10-17, ages to 2026-10-17

**2026-10-17 — THE HEAD WAS TAKEN AS WRITTEN, AND THE TIEBREAK DID NOT NEED ITS FOURTH LEVEL.** The
displacement line, in one sentence: **this run took item 10 — four webfont families and 502 KB on an article
page, 7 days, five displacements, the board's oldest item past the three-displacement threshold — and
displaced item 11 a sixth time, items 12 and 14 a fifth each, item 13 a fourth, item 15 a third, item 18 a
second and item 19 a first.** **Item 17 was not displaced for the second day running: its open job was taken
by the content function again**, which is the 10-13 distinction.

**Six items stood at or past the three-displacement threshold (10, 11, 12, 13, 14, 15)** — the most the board
has ever offered — and the 10-05 tiebreak (*among items past threshold the oldest goes first*) discriminated
at **7 days against 6, 5, 4, 4 and 3**, so the displacement counts were never compared and yesterday's
newly-invented fourth level was never reached. **Yesterday's note called this in advance, in those words:
"it goes first tomorrow unless the tiebreak is overturned."** Eleventh selection in twelve daily runs made by
the rule rather than by judgment.

**Item 10 is CLOSED, and for the TENTH consecutive closure the specification was not the scope — this time
the specification was the part that was wrong.** The item named two reductions, *subset to our glyph
inventory* or *drop a family*, and both are real and neither was taken, because **the largest reduction
available was not in the fonts.** It was a stylesheet rule that had been in the file since the first publish
and in the cascade never: `[dir="rtl"] { font-family: var(--font-arabic) }` on `<html>` lost to
`body { font-family: var(--font-body) }`, because a declaration that matches an element always beats a value
that element inherits. Every Arabic page computed `<body>` as **Newsreader** — a face with no Arabic glyph —
for **145 days**, drew its Arabic from the system serif, and fetched **278,872 bytes per page to render
nothing** (ruling #103). Three further Arabic rules never matched at all, through Astro's scoping of a bare
attribute selector on `<html>`.

**And the item's own baseline was wrong in three ways, all one class.** `2,792,392 bytes` was a sum over the
stylesheet's **73 declarations** against a cell reading `34 files` — the bundle on disk is **1,333,968** —
so the mirror's worth is **832,104 bytes, not 2.29 MB**; and `EN article · 501,864` was **one page reported
as a property of 118**, against a measured population of 487,672 / 521,408 / 703,556. **The sampled page was
also the lighter edition: the Arabic article was the heaviest page in the publication the whole time, at
825,868 bytes, and nothing had ever measured it.** Corrected in place in the 10-10 note (#41).

**Count line: TEN open, ONE closed today (item 10), TWO opened (item 20 — the English half of item 10, which
is a Designer call and was never this lane's; item 21 — the day's forward question, entered at the head).**
Counted by reading the rows below today: ten. **The board is UP ONE**, and the honest reason is that closing
item 10 split it: the half that was a defect is fixed and the half that is a judgment is still a judgment,
so it is queued under its own number rather than buried in a closure note.

**THE RESTRAINT TEST'S ONE NUMBER (10-11, ANSWER 2) — the age of the oldest item that has been displaced at
least once: it reads 6 days today (item 11, six displacements), unchanged from yesterday's 6.** For the
second day running it did **not** fall, and for the same structural reason: the item closed was the oldest,
and the next in line inherited the position on the same day. Two days of a flat number is the number working.
It is 6 against the 28 the test was set at; the reading that matters is 2026-10-25's.

## Superseded count line — NINE items, reconciled against disk 2026-10-16, ages to 2026-10-16

**2026-10-16 — THE HEAD WAS TAKEN AS WRITTEN, AND THE TIEBREAK RAN OUT OF LEVELS.** The displacement
line, in one sentence: **this run took item 9 — the mandated reading list has no budget, 6 days, four
displacements — and displaced items 10 and 11 a fifth each, items 12 and 14 a fourth each, item 13 a
third, item 15 a second, and item 18 a first.** **Item 17 was not displaced: its open job was taken by
the content function**, which is the 10-13 distinction — *an item is displaced when something else is
chosen over it, not when it runs second inside a day that completed both.*

**Five items stood at or past the three-displacement threshold (9, 10, 11, 12, 14), and for the first
time neither the 10-05 tiebreak nor the 10-11 ANSWER 1 narrowing discriminated.** Items 9 and 10 are
tied at **6 days** *and* at **four displacements**, so *oldest past threshold goes first* did not
separate them and the finer clock was reached — and the finer clock is **the same commit**: both were
raised by the 10-10 daily, `e9a9338`, one from state verification and one from the growth function.
**The tiebreak's fourth level, adopted here and recorded rather than improvised:** *when two items share
a raising commit, the earlier-raised goes first, and the board already records which that is — item
numbers are assigned in raise order.* Item 9 was raised inside STEP 1, item 10 inside the growth function
of the same run. **This is the last level the artefacts can support**; below it there is no record, and a
fifth level would have to be invented rather than read. **Tenth selection in eleven daily runs made by
the rule rather than by judgment.**

**Item 9 is CLOSED**, and for the **ninth consecutive closure the specification was not the scope** —
this time by a small, precise margin. The item named two treatments and both were done: the guidebook's
`Series integrity` paragraph lost **27,679 bytes of extension trail on one line**, and the Edition 05
ledger went **198,580 → 4,502 bytes**. The mandated six went **412,908 → 219,435, −47%**, measured by
`stat` before and after. **What the specification did not contain is that the Edition 05 ledger was not
a long file needing pruning — it was a CLOSED edition's working ledger that `CLAUDE.md` was still naming
as the live state**, three days after the wave flipped. The reduction is a state error corrected, not a
compression achieved, and the standing rule that goes with it is in the reading list: *a wave's status
memo is reduced to its record in the flip commit's week, and that line names whichever edition is open.*

**Count line: NINE open, ONE closed today (item 9), ONE opened (item 19 — the day's forward question,
entered at the head).** Counted by reading the rows below today: nine. **The board is FLAT**, the first
time in three days it has not moved up, and the honest reason is that today's content work went into an
item that was already on the board rather than into finding a new one.

**THE RESTRAINT TEST'S ONE NUMBER (10-11, ANSWER 2) — the age of the oldest item that has been displaced
at least once: it reads 6 days today (item 10, five displacements), unchanged from yesterday's 5+1.** It
did **not** fall, because the item closed was the equal-oldest rather than the sole oldest; its twin
inherited the position. That is the number behaving correctly and saying something unwelcome, which is
what it was replaced in order to do.

## Superseded count line — NINE items, reconciled against disk 2026-10-15, ages to 2026-10-15

**2026-10-15 — THE HEAD WAS TAKEN AS WRITTEN, AND FOR THE FIRST TIME THE THRESHOLD CLAUSE HAD FOUR
CANDIDATES.** The displacement line, in one sentence: **this run took item 8 — the git-derived date compared
against a working-tree build, 7 days, four displacements — and displaced items 9, 10 and 11 a fourth each,
item 12 a third, item 14 a third, item 13 a second, and items 15 and 16 a first each.** Item 15 is
yesterday's forward question and entered at the head under clause (1); it was displaced by clause (2) on its
first morning, which is the rule working rather than failing, and the same thing that happened to item 14 on
10-14. **Four items stood at or past the three-displacement threshold (8, 9, 10, 11)** — the first time the
board has offered the tiebreak more than two — and the 10-05 tiebreak (*among items past threshold the
oldest goes first*) discriminated at **7 days against 5, 5 and 4**, so the displacement counts were never
compared. **Ninth selection in ten daily runs made by the rule rather than by judgment.**

**THE HEAD RAN FIRST**, and the ages are recomputed from each item's own raise date rather than incremented
from yesterday's cells (#57): the table below arrived carrying ages one day stale in every row — *item 8
read 5 days under a header claiming ages to 10-14* — which is the same arithmetic-agrees-with-itself defect
the ruling-range rule was written for, in the file that ranks the work.

**Item 8 is CLOSED**, and for the **eighth consecutive closure the specification was not the scope** — this
time the gap is in the item's own diagnosis of *where* the defect lives. The item said: *`qa_served_manifest
--check` has no honest home before the commit · the fix is a home or a guard.* Both halves needed correcting.
**The defect is a property of neither tool. It is a property of comparing a git-derived date against a
working-tree build**, which is why the 10-14 run hit it again in a second instrument and in the opposite
direction — so the remedy is one shared precondition, `agents/tools/lastmod_tree_guard.py`, not a fix in a
tool. And **a blanket refusal would have been wrong**: `qa_live_drift` has three axes and only one of them
reads provenance, so refusing the whole tool would have thrown away a URL-set and a sampled-head comparison
that need no git at all — *a check too blunt to run on a working day is a check that stops being run*, which
is the 09-13 lesson pointed at a guard instead of at a gate. The refusal is therefore **per axis**:
`--check` declines entirely (all four of its buckets key on `date_moved`), `qa_live_drift` declines the date
axis, keeps the other two, and may no longer print its `CLEAN` line from a state that cannot support it.
**Exit 4 = REFUSED**, distinct from drift (1) and from an unreachable origin (2), because the whole defect
was an unsupportable number being read as one of those two.

**The guard reads the resolver's own `CHROME_GLOBS` and `CONTENT_DIRS` on every run and copies neither.** A
copy would have made this file the list's second home and this guard the next member of the drift family the
09-27 amendment is about — *grep for it, do not remember it*. A parse that yields nothing is refused, not
empty. **Proved 11 ways, bites first, on clones under /tmp** — the subject of this guard is the working tree,
so a harness that dirtied the real one would be injecting into the thing it measures. **And the harness
caught itself twice:** the first run of bite 8 deleted a clone's `.git`, failed on read-only objects, left a
*partial* `.git` and refused for a reason the case did not claim (rebuilt by `git archive`, so the condition
is definitional); and every control would have passed for the wrong reason had `fresh()` not copied the
uncommitted instruments into each clone — *a guard that is not there cannot refuse.*

**Count line: NINE open, TWO closed today (items 8 and 16), TWO opened (item 17 — the expansion census; item
18 — the day's forward question, entered at the head).** Counted by reading the rows below today: nine. **Two closures in one day is a first for this board**, and they were not the same
kind of work: item 8 was the head, taken by rule; item 16 was the content function, taken because a dead
citation on a live page is the only open item a reader could see. The board is **UP ONE** rather than down two,
and the honest reason is the ninth consecutive closure whose specification was not its scope — item 16 said
*a sixth dead link* and the re-read found **a named institution wrong for 103 days** (item 17) and an
instrument that cannot tell a served article from a served listing (item 18). **Two closures and two
openings in one day, and both openings came out of work that was done rather than work that was imagined.**

**THE RESTRAINT TEST'S ONE NUMBER (10-11, ANSWER 2) — the age of the oldest item that has been displaced at
least once: it reads 5 days today (items 9 and 10, four displacements each), down from 6.** It fell
**because the oldest was closed**, which is twice in two days that the replaced definition moved for the
right reason.

## Superseded count line — NINE items, reconciled against disk 2026-10-14, ages to 2026-10-14

**2026-10-14 — THE HEAD WAS TAKEN AS WRITTEN, AND THE 10-13 NOTE'S WRITTEN PREDICTION HELD EXACTLY.** The
displacement line, in one sentence: **this run took item 5 — the five dead citations on four published
pieces, 9 days, three displacements, the board's oldest item past the three-displacement threshold — and
displaced item 8 a fourth time, items 9, 10 and 11 a third each, item 12 a second, item 13 a first, and
item 14, yesterday's forward question, a second.** Items 5 and 8 were both past threshold; the 10-05
tiebreak (*among items past threshold the oldest goes first*) discriminated at **9 days against 6**, so the
displacement counts were never reached and the 10-11 ANSWER 1 narrowing was never needed. **Eighth
selection in nine daily runs made by the rule rather than by judgment**, and the first one a previous day's
log called in advance in those words: *"tomorrow the tiebreak has nothing to weigh and item 5 goes first."*

**AND THE HEAD RAN FIRST TODAY**, which is worth recording because the last two dailies did not run it
first and both said why. Nothing outranked it: there was no flag to flip, no edition to lose, and ruling
#96's exception is for *content flag changes*, of which today had none. The repair was itself content work,
so the two lanes were the same lane.

**Item 5 is CLOSED**, and for the **seventh consecutive closure the specification was not the scope** — but
for the first time the gap is not a number that aged quietly. **It is a category error in the item itself.**
The item was filed as link hygiene: *five hard 404s, eight live pages, fix the links.* Re-probed twice each,
all five are still dead and **all four hosts answer 200 at their roots**, which is #54's *go look* signature.
Looking is what produced the actual finding: **three of the five dead citations were load-bearing for an
annotation the register does not support** — a $350–600 monthly take-home credited to an Education
International study that carries **no monthly figure in any of three readable copies** (the 2026 re-posting,
a 2026-02-03 Wayback capture of the dead 2025 posting, and the study's own summary PDF); an eleven-province
fee waiver credited to the wrong ÖSYM announcement, two weeks out, when the right one names *Adana …
Sivas-Gürün* verbatim; and a release dated *(early 2026)* that is dated **6 November 2025**, the flagged
horizon taken for the masthead. **Ruling #100**: a citation's death is the only event that ever makes anyone
re-open the register, so a 404 sweep is this operation's only standing audit of published annotations — and
**the other 338 outbound promises resolve, and have therefore never been re-read once.** Four dispositions
of *confirmed dead* are named and all four were used today; only one of them removes a link.

**Count line: NINE open, one closed today (item 5), TWO opened (item 15 — the day’s forward question;
item 16 — a sixth dead citation the closed item never named, surfaced by the full-population sweep AFTER the
closure).** Counted by reading the rows below today: nine. **The board is UP ONE**, and the honest reason is
that the day’s own instrument out-ran the day’s own specification: item 5 said five, five were repaired, and
`qa_sources_alive --sample 0` then returned 342 of 342 with **one 404 nobody had listed** — the seventh
closure’s lesson arriving a second time inside the same run. *A list inside a queue item is a measurement
with a date on it, exactly as a percentage is.*

**THE RESTRAINT TEST'S ONE NUMBER (10-11, ANSWER 2) — the age of the oldest item that has been displaced at
least once: it reads 6 days today (item 8, four displacements), down from 8.** It fell **because an item was
closed**, not because the clock turned — which is the second time the replaced definition has moved for the
right reason, and the thing the original definition could never do.

## Superseded count line — EIGHT items, reconciled against disk 2026-10-13, ages to 2026-10-13

**2026-10-13 — THE HEAD WAS TAKEN AS WRITTEN, ON A DAY WHOSE FIRST WORK WAS THE EDITION, AND THE RULE
STILL CHOSE THE QUEUE'S JOB.** The displacement line, in one sentence: **this run took item 7 — the
published oracle's auditor, 7 days, four displacements, the board's only item past the
three-displacement threshold — and displaced item 5 a third time, item 8 a third, items 9, 10 and 11 a
second each, and item 12, yesterday's forward question, a first.** The tiebreak had nothing to weigh:
one candidate past threshold, exactly as the 10-12 note predicted in writing. **Seventh selection in
eight daily runs made by the rule rather than by judgment.**

**AND THE ORDER WITHIN THE DAY IS RECORDED RATHER THAN SMOOTHED.** The queue head did **not** run first
today. Edition 05's flip ran first — twelve flags, the publish gate in writing, 71 days held — and was
committed and pushed before this item was opened. The reason is ruling #96 and it is about delivery,
not about priority: *any content flag change is committed in the turn it is finished*, and a run that
loses its envelope before the flip lands loses the edition for the third time. The head was taken
immediately after, with the whole day still ahead of it. **An item is displaced when something else is
chosen over it, not when it runs second inside a day that completed both.**

**Item 7 is CLOSED**, and for the sixth consecutive closure **the specification was not the scope.** The
item asked for an auditor covering *"the manifest's 216 claimed entries, of which 95 asset hashes and
one 404 entry are claimed and unverified — 44% of the file."* The file the origin actually serves today
claims **256** entries, because the 34 fonts landed after the item was written: **136 of them, 53%, had
never been checked by anything**, and the share the item quoted had grown while the item sat. *A
percentage inside a queue item is a measurement with a date on it, and this board does not print dates
on them.* First live run: **256 of 256 audited CLEAN** — the first time this operation has checked the
whole of its published oracle against the thing it describes.

**And the first live run found something the harness could not.** One page read as unserved on the first
pass and then returned 200 to `curl` three times in a row: a single dropped socket in 256 sequential
reads. Reported as written, that is *the origin does not serve what its manifest claims* — a finding
about the network wearing a finding's costume, and the fastest way to get an auditor switched off.
**Failures are now re-probed once and the recovery count is printed rather than smoothed** (#91, and the
publication's own rule that a single probe is not a measurement). **Proved eleven ways, bite first**, on
loopback copies of `dist` — six bites including the two sections nothing had ever reached, four
failure-to-check guards, and the control **last**. The control failed on its first run and **the harness
was the defect**: it rewrote the site prefix inside `sitemap-0.xml`, which is a file the manifest claims,
so the oracle disagreed with bytes the harness itself had changed. *An auditor is the easiest instrument
in the world to accuse of its harness's crime.*

**Count line: EIGHT open, one closed today (item 7), two opened (items 13 and 14).** Counted by reading
the rows below today: eight. The board is **up one**, and the honest reason is that both new items came
out of work that was done rather than work that was imagined — item 13 from a defect fixed in this
morning's flip commit, item 14 from the day's forward question.

**THE RESTRAINT TEST'S ONE NUMBER (10-11, ANSWER 2) — the age of the oldest item that has been displaced
at least once: it reads 8 days today (item 5, three displacements), up from 7.** It rose because item 5
was passed over again and the clock turned, and the test is working as designed by saying so: the number
it replaced would have read the same on a day nothing moved.

## Superseded count line — SEVEN items, reconciled against disk 2026-10-12, ages to 2026-10-12

**2026-10-12 — THE HEAD WAS TAKEN AS WRITTEN, AND IT IS THE SAME HEAD THE 10-11 DAILY TOOK AND LOST.**
The displacement line, in one sentence: **this run took item 6 — `history.jsonl`, 8 days, five
displacements, the oldest item past the three-displacement threshold — and displaced item 7 a fourth
time, item 5 a second, item 8 a second, items 9, 10 and 11 a first each, and the 10-10 forward question
once.** Nothing was argued. Items 6 and 7 were both past the three-displacement clause; the 10-05
tiebreak says *among items past threshold the oldest goes first*, item 6 is 8 days against item 7's 6,
and the displacement counts did not tie, so the 10-11 review's **ANSWER 1** narrowing (go to commit
timestamps only when the displacement counts also tie) was never reached. **Sixth selection in seven
daily runs made by the rule rather than by judgment, and the first one the rule has had to make twice.**

**Item 6 is CLOSED**, and like the four closures before it, **the specification was not the scope.** The
item reads *ten dates carry two snapshots*, which is a data problem and invites a de-duplication pass. The
measurement says otherwise in one line: **nine of the ten duplicated dates carry byte-identical payloads.**
So the file is not recording a second observation, it is recording a second *run* — a fact about the
operation, never about the publication — and every consumer that asks *what was true on date D* has been
getting the right answer on all 95 dates while the file was wrong. Only a **positional** reader can see it,
and the positional reader is `rows[-7]`, which is the CHARTER's own stated purpose for the file (*"so
week-over-week deltas accumulate"*), **and it does not exist yet.** That is **ruling #97**: a defect
visible only to a consumer you do not yet have is not latent, it is *scheduled*, and it arrives on the day
that consumer's first answer is trusted.

**Fixed at the write, not in the data.** `--log` now replaces the row carrying today's date; `--dedupe`
applies the same resolution backward to the existing series **as an instrument rather than by hand**,
because a point-of-filing rule leaves a step discontinuity exactly where it is written (10-04 second
amendment, limb two) — **108 → 95 rows, all 95 dates surviving, nothing invented, 13 deletions and no
other change.** Last-write-wins is measured rather than convenient: 2026-09-14 is the only date whose rows
differ, and its fourth row is the one that counts the Arabic twin that landed during the day. Both modes
**refuse to write and exit 2** on a line they cannot parse, because both rewrite the file. The date key
also moved from the runner's UTC to the operation's Asia/Dubai calendar — `date.today()` meant the
operation's calendar while the runs were on a Dubai desktop and silently became UTC at the 2026-09-14
cloud cutover. **Proved eleven ways, bite first**, on a copy in `/tmp`, including the HTML panel the brief
pastes coming out **byte-identical before and after**.

**Count line: SEVEN open, one closed today (item 6), one opened (item 12).** Counted by reading the rows
below today: seven. The board is flat, not down — which is the honest shape, because **the new item is the
day's forward question and the day's forward question is the thing the queue head displaced.**

**THE RESTRAINT TEST'S ONE NUMBER, on its replaced definition (10-11, ANSWER 2) — the age of the oldest
item that has been displaced at least once: it reads 7 days today (item 5, two displacements), down from
8.** Item 6, which held the number at 7 yesterday, has left the board. The replacement is already doing
what the original could not: it moved because an item was *closed*, not because the clock turned.

## Superseded count line — SEVEN items, reconciled against disk 2026-10-11 at the weekly review

**2026-10-11 — THE WEEKLY REVIEW ANSWERS THE THREE QUESTIONS THIS BOARD WAS OWED, AND IT TOOK NO HEAD,
because it is not a daily run and the day's daily run is gone.** The 10-11 daily took a head and did the
work — item 6's subject among others — and **delivered none of it** (181 turns against a cap of 180,
ruling #96). So the board records **no displacement today**: nothing was chosen over anything, ages moved
on the wall clock, and that is the second time in three days that *a run which produced nothing aged every
item and displaced none* — which the 10-10 note already called "not a mechanism anyone should rely on."

**ANSWER 1 — the tiebreak's third amendment: ADOPTED as written on 10-10, and narrowed.** Age at
finer granularity is still age, so going to the raising commits' own timestamps when dates tie is the
existing rule read at the resolution the artefacts actually record. **Narrowed in one way:** it applies
only when the displacement counts also tie, because displacement is a record of *choices* and age is a
record of the *clock* — a rule that reaches for a finer clock before exhausting the choice record would
let two quiet days outrank four deliberate displacements.

**ANSWER 2 — the restraint test's one number: REPLACED, and the complaint is upheld.** *The age of the
oldest open item* is not discriminating and the 10-08 and 10-10 notes were right about why: it is
dominated by how recently the last item was **raised**, it moves when a run fails and nothing is chosen,
and it rose two days this week for that reason alone. **It also cannot fall below the age of a board that
is being actively worked, which is the opposite of what it was built to reward.** Replacement, set today
and readable on 2026-10-25 exactly as the original was: **the number is the age of the oldest item that
has been DISPLACED at least once** — an item nobody has yet had to pass over is not evidence about the
queue, while an item passed over repeatedly is the only thing the one-queue rule promised to fix. It
reads **7 days today** (item 6, five displacements). *Still one number, still owned outright by the role,
still excluding assertion count in both directions.*

**ANSWER 3 — "if item 2 is displaced a thirteenth time the one-queue rule has failed": MOOT, and
honestly so.** Item 2 — the output-bounded served-bytes manifest, 29 days and twelve namings — **closed
2026-10-06** as `qa_served_manifest`, two days after the 10-05 note predicted its thirteenth displacement.
The rule was not vindicated by argument; the item landed. **Five for five on the one-queue rule across
10-05 → 10-10, and 0 for 1 since**, because 10-11's head was taken, worked, and lost — which is a failure
of delivery and not of selection, and the board should not credit the rule for it either way.

**Count line: SEVEN open, counted by reading the rows today.** Seven rather than six because **item 11 is
opened below** — the run envelope — and nothing closed, since the work that would have closed item 6
exists only in a discarded workspace. **Item 6's subject was addressed and its artefact is gone**;
re-verified against disk today and still true: `agents/stats/history.jsonl` holds **107 rows for 94
dates**, ten dates carrying duplicates and 2026-09-14 carrying four. One finding worth more than the
re-count, and it narrows the fix: **four of the ten duplicate dates are Sundays** — the weekly-review day,
when a daily and a weekly both snapshot — and the other six are weekdays. *So "two runs in one day" is a
cause and not the cause, and a de-duplication pass would not prevent the next one.* The fix is a
**per-date idempotent write — replace the row for today's date, never append** — which is correct
regardless of why two snapshots were taken.


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

### DEFECT — **TWO items.** The head comes from here while any row stands.

*The boundary is the artefact's, not a judgment: each row names **N > 0** artefacts, currently served or
currently founder-facing, that are **wrong, broken or unevidenced**. A question carries no such count,
because the count is what it would measure. Ordered by age; ages are `today − Raised` and are not written
down (#116).*

| # | Item | Owner | Raised | Verified how | Blocks |
|---|---|---|---|---|---|
| 33 | **Three published citations misquote their own registers, and a fourth is soft-dead** — found by standing assertion 36 on its first sweep and handed over, because a fix that changes served bytes is the Web Developer's even when an assertion found it (the 09-27 split). **(a)** `2026-05-28-iraq-mosul-library`, both editions: the annotation quotes `'Restoring the Mosul University Library'` and UNESCO's own project title is **`Restoring and modernizing the Mosul University Library`** — #101's removal performed by a truncation inside quotation marks, which is worse than an acronym because quotation marks are the one punctuation that promises no editing. **(b)** `2026-07-07-us-naep-honesty-gap`, both editions: ours reads `'Oklahoma board raises testing rigor to restore truth and transparency to student testing'`, theirs reads **`Oklahoma board raises rigor to restore 'truth and transparency' to student testing`** — a word inserted *and the register's own inner quotation marks dropped*, which converts a phrase the board was quoted as using into the newspaper's own description (#43 destroyed by punctuation). **(c)** `2026-06-17-korea-aidt-reversal`, both editions: the quotation is correct and the URL is `blogs.worldbank.org/en/education`, **the blog index**, not the article. **(d)** `2026-06-25-brazil-crianca-alfabetizada`, both editions: `agenciabrasil` answers **200** and serves `EBC - Página temporariamente indisponível` — their failure, ours to dispose of under #100's four dispositions. Every correction is written in the register's own words (#101 clause 4). | **[WD]** + Editor | **2026-10-22** (from item 18's close) | Each of the four registers opened by hand in served text today, after the instrument flagged them; `agents/stats/citation-identity.json` carries the dated row | nothing red — it is the only open item where a published page says a register printed words it did not print |
| 35 | **Four published acronym expansions have no evidence in the annotations of the piece that prints them** — found by standing assertion 37 on its first sweep and handed over, because a fix that changes served bytes is the Web Developer's even when an assertion found it (the 09-27 split). **(a)** `2026-07-04-kenya-cbe-grade10-pathways`: the body expands `KJSEA` as *Kenya Junior School Education Assessment* and the eleven annotations carrying the acronym never carry the name — **on the piece that earned #101, eight days after that correction shipped.** **(b)** `2026-07-07-singapore-psle-sbb`: *Primary School Leaving Examination* in the body, seven acronym-only annotations. **(c)** `2026-06-08-sierra-leone-tsc-teacher-matching`: *Teacher Management Information System* in the body, and neither the name nor the acronym in `sources[]`; the two EdTech Hub registers were read in served text 2026-10-23 and neither prints the expansion. **(d)** `2026-06-10-rak-iqra-arabic-diglossia`: annotations carry only `J-PAL MENA` — **and the anchor is SHORT by two words**, because J-PAL drops *Abdul Latif*, so the repair must use the owner's own *The Abdul Latif Jameel Poverty Action Lab* rather than copying the instrument's span. **Not repaired by the run that found them, for a second reason beyond the split:** `kjsea.knec.ac.ke` refuses the connection from this runner and `moe.gov.sg` answers 202 to every client here, so the expansion cannot be written *as the register prints it*, which is what #101 clause 1 actually requires — and a repair that guesses the wording is #101 again in the repair. All four are carried in the tool's `KNOWN_OPEN`, which is asserted to be a **subset** of the findings, so a repair that does not delete its own entry turns the build red. | **[WD]** + Editor | **2026-10-23** (from item 17's close) | Each flagged by the instrument and each read against its own frontmatter by hand today; the J-PAL name read in the owner's served chrome | nothing red — the gate is green with these four carried, by design, and goes red the moment a fifth appears |

### OPEN — **SIXTEEN items.** Ordered by age. The forward question enters at this block's head.

*Questions, coverage gaps and face judgments. The bytes are right and the rows say so. Reached only when
the DEFECT block is empty.*

| # | Item | Owner | Raised | Verified how | Blocks |
|---|---|---|---|---|---|
| 47 | **The only overflow gate this operation owns reads the artefacts, never the publication — and it reads them at exactly one width** — the day's forward question, entered at the head per the one-queue rule, and it inverts the rule that created its subject. `qa_artefact_render` is the **only** tool of the thirty-nine that measures overflow at all: `scrollWidth`/`clientWidth` appear in no other file in `agents/tools/`. Its scope is `agents/briefs` and `agents/reviews`. **So the 134 pages a reader is served — two scripts, one of them RTL, with the longest unbreakable tokens in the corpus sitting in `<code>` inside article bodies — have never been checked for overflow at any viewport width.** The 2026-08-23 perimeter rule was written to ADD the founder-facing artefacts to a perimeter that already covered `dist`; for this property the relation is the other way round, and nobody noticed because the rule's sentence reads as an extension. Second limb, cheaper and sharper: `VIEWPORT = 1280`, one number, and **an assertion with a parameter is an assertion about that parameter's value** — a layout correct at 1280 and broken at 390 is invisible to the gate promoted today, and the founder opens the brief on whatever is in his hand. Measure both before building anything: how many of the 134 served pages overflow at 1280, and how many of the 136 artefacts overflow at 390. | **[AE]** | **2026-10-27** | Enumerated by grepping `scrollWidth`/`clientWidth` across all thirty-nine tools (one hit, one file) and reading `VIEWPORT` in that file | nothing red today, and that is the point: no instrument can turn it red |
| 46 | **Nothing gates `copyrightYear`, the field that replaced the build clock on all 134 pages today** — raised by the growth function in the run that created its subject, exactly as item 44 was yesterday, and **the two should be closed by one instrument rather than two.** Today's growth action replaced `new Date().getFullYear()` in `SiteFooter.astro` with a year derived from `createLastmodResolver()`, so the served byte is now a fact about the tree instead of about the machine's clock. 134 of 134 pages carry it and 0 disagree with the sitemap's own date for `/` — **a measurement, not an assertion.** The general form, which is what makes it one item with item 44 and not two: **every date a template emits is derived from the tree, and none from the clock.** A build-clock date is the one claim no comparison this operation owns can ever catch, because it agrees with itself across any two builds run in the same period. | **[AE]** | **2026-10-27** | `copyrightYear()` evaluated against `createLastmodResolver()('/')` in node; footer markup diffed byte-for-byte across the before and after builds | nothing red — it is a gap in coverage, not a defect in bytes |
| 44 | **Nothing gates `dateModified`, the field that was missing from all 88 article pages until today** — raised by the growth function in the run that added it, because *a check nobody wires is a habit* (09-13) and **88 of 88 is a measurement, not an assertion.** Today's growth action wired `articleJsonLd` to `createLastmodResolver()`, the sitemap's own git-derived resolver, so the two channels now agree on all 88 URLs and disagree on none; a future template edit can drop the field silently and no build goes red. The cheap assertion belongs in **`qa_date_identity`**, which already owns the date-identity question and already gates: *every article page in `dist` carries a `dateModified`, it is ≥ that page's `datePublished`, and it equals the sitemap `<lastmod>` for the same URL.* Note the precondition — `lastmod_tree_guard.py` exists precisely because a git-derived date must not be compared against a working-tree build, so the third limb needs the guard the two existing lastmod instruments already share (exit 4 = REFUSED), and it is the reason this is a queue row rather than a line added this afternoon. | [AE] | **2026-10-26** | Measured in `dist` after the change: 88 of 88 carrying the field, 0 disagreeing with the sitemap, and the EN/AR `rak-iqra` split (10-26 against 10-25) proving the field discriminates | nothing red — the field is present on every page today and no gate would notice it leaving |
| 42 | **Four registers whose dates have now passed, re-read for what actually happened** — the measured half of item 25, split out because *an announcement correctly labelled as an announcement is not a measurement* (#117). This run's repair made four pieces' claims true by attributing them to their dated registers; it did **not** tell the reader what the register said next. The four: **(a)** `2026-06-10-rak-iqra-arabic-diglossia` — did Iqra in fact run in RAK private schools from September 2026, KG1–Grade 1? **(b)** `2026-07-07-turkiye-earthquake-school-recovery` — the September 2026 completion date has passed; MoNE's own ledger is the register and the piece's whole argument is that a published ledger invites exactly this check. **(c)** `2026-07-16-australia-naplan-reset` — ACARA's national NAPLAN 2026 results were due August 2026 and the piece says in terms that everything above it reads 2023–2025. **(d)** `2026-07-28-england-report-cards-first-term` — Ofsted's new statistical model took effect from September 2026. Each is a dated follow-up when it comes, never a rewrite (#41), and each must be read in served text, never from a result list. | Editor + **[WD]** | **2026-10-26** (from item 25's close) | The four claims are correctly attributed as of this run; what no run has read is the outcome | nothing red — the bytes are now true, and this is the difference between *announced* and *measured* |
| 21 | **RE-SPECIFIED 2026-10-27 UNDER RULING #118 — the first output is a PARTITION, not a byte count.** An unmatched selector is one of two things, and only one of them is dead weight: *superseded* (the design moved on and the rule is residue) or **orphaned** (the design stands and the markup walked away from it). An orphaned rule is **an unfiled defect report about the markup**, and item 27's repair was written out of two of them — `.push-block` sitting complete in seven briefs whose markup had stopped matching it, and `.container` sitting complete in two briefs whose `<main>` had been deleted. **Deleting an orphaned rule destroys the only surviving statement of what the document was supposed to look like.** So: partition first, answer the markup question each orphan raises, and only then count bytes. Original wording follows. **How many of the selectors this build ships match nothing on any page we serve?** — the day's forward question, entered at the head per the one-queue rule. Today found a stylesheet rule that had been in the file since 2026-05-25 and in the cascade never, and three more that Astro compiled into selectors no document this build can produce. **Every instrument we own reads an OUTPUT, and a rule that never matched leaves nothing in the output to read** (#103). The question is computable and cheap, which is the whole point: for each selector in the built CSS, does it match at least one element on at least one served page? `document.querySelectorAll` in the browser already driven by four assertions; the answer is a number, and the interesting half is not the dead selectors but the ones written for **one edition** that never reach it. Today's four were all Arabic-side, and that is unlikely to be a coincidence: the edition with fewer readers in the room is the edition whose rules nobody notices failing. | **[AE]** | **2026-10-17** (the daily's forward question) | Named from four defects found, measured and fixed today rather than from a hypothesis | nothing red |
| 26 | **Which other check's stated reason for NOT asserting something has quietly become false?** — #106's forward question, entered at the head per the one-queue rule. `qa_register_shape` declined the fifth home's numerator *because no membership list existed to check it against*; #95 wrote one on 10-11 and nothing re-read the comment, so two family counts went stale behind a check that passed. **The population is enumerable and nobody has ever read it as a set:** every *not derivable · cannot · out of scope · deliberately not asserted* comment in `agents/tools/**`, across thirty-two instruments, each one a dated claim about a subject that has moved since. **Next week's bet, part B.** **2026-10-25, weekly review — the three-item version of this question was taken and ONE OF THE THREE BIT.** The register's three non-gating assertions were re-read against the state they describe. `qa_sources_alive` still true; `qa_feed_validators` still true and still behind issue #7. **`qa_live_drift`'s reason is false in its load-bearing word:** it is excluded because *"the verify job below byte-compares the published artifact against it, which is strictly stronger"*, and verify byte-compares exactly six files — `sitemap-0.xml`, both home pages, both feeds, `sitemap-index.xml` — while `qa_live_drift`'s third axis samples **four page heads, two of them ARTICLE pages that no step in `astro-pages.yml` has ever compared against the origin.** Stronger on the sitemap axes and the front doors, weaker on half the excluded check's sample, and the only article-page origin comparison this operation owns is the one kept out. #93 from the other side; remedy already staged at `agents/patches/2026-10-10-verify-bridge-via-served-manifest.md`. **One bite in a sample of three says the population of thirty-nine is worth the day — the item stays open for the other thirty-six.** | **[AE]** | **2026-10-18** (weekly review) | not yet — the set has never been enumerated | no |
| 28 | **Which of our four render assertions rest on an oracle nobody has interrogated?** — the day's forward question, entered at the head per the one-queue rule, and it has a known first answer. Ruling #108: `el.scrollWidth` is silent on inline text overflowing an `overflow: visible` block, proved by injection — `scrollWidth == clientWidth == 1028` for text far wider — so assertion 33's overflow half **cannot be shown to bite** and does not gate. The correct oracle is a **Range rectangle** (`doc.createRange()` over an element's contents, `getBoundingClientRect().right` against the padding-box edge), which is a geometric question the layout engine must answer honestly. **And the same question is owed by four gating assertions that have never been asked it:** `qa_render` reads a raster, `qa_arabic_shaping` and `qa_arabic_joining` read a dumped DOM, `qa_feed_direction` reads a rendered feed. Six rulings say *a green check is scoped to what it enumerates*; all six ask what the check looked at, and none asks what its ruler can represent. | **[AE]** | **2026-10-19** (the daily's forward question) | Named from a blind spot measured by injection today, not from a hypothesis | nothing red |
| 29 | **Three of the four composition surfaces measured clean today have no gate behind them, and the run that filed a ruling saying the build CAN ask them gated only the cheapest** — the day's forward question, entered at the head per the one-queue rule. Ruling #109 states that the JSON-LD cross-page graph, the two feeds as one subscription, hreflang reciprocity and canonical uniqueness are **all statically computable from served bytes**. Assertion 34 gates **one** of them. The other three are three `/tmp` probes that will not survive this runner — worse than the 2026-09-13 defect, because a hand-run assertion is at least a file. **The demonstration arrived inside the same run:** the graph was measured clean at 09:50 and the growth function added **120 nodes** to it at 10:05, and the only reason it was re-measured is that I happened to remember. 266 → 386 distinct `@id`, a 45% enlargement, verified by hand. The taking: promote the three into `qa_composition` as further limbs or a sibling, **cross-page node agreement first**, each proved both ways per #35 and each with the *intended assembly* stated in code rather than inferred — which is #109's own second half turned on its author. | **[AE]** | **2026-10-20** (the daily's forward question) | Named from four measurements taken today, one of which was invalidated and re-taken within the same run | nothing red — it is the item that asks why today's own ruling was only one-quarter implemented |
| 31 | **Which of this operation's claims are checked only by the NEXT run's goodwill?** — the day's forward question, entered at the head per the one-queue rule. Every instrument runs inside the agent step and the deploy runs after that step ends, so **no run has ever observed its own publication.** Ruling #71 handles this in prose: every brief carries the previous run's deploy ID, conclusion and a `qa_live_drift` result. **Nothing fails when it is not met** — the 10-20 run finished green, pushed five commits, wrote a brief, and its deploy failed seven minutes later; the only reason anybody knows is that this run looked. First answer is cheap and named: an assertion that reads the previous deploy's conclusion through the `actions: read` grant the job already holds (`run_envelope.py` already calls that API) and goes RED when it failed. The wider half is the inventory — every *the next run should…* and *every brief carries…* in `CLAUDE.md`, the RUNBOOK and the guidebook, which is #107's shape (a condition true for 33 days and evaluated by nobody) read as a population. | **[AE]** | **2026-10-21** (the daily's forward question) | Named from a two-day publication gap measured today, not from a hypothesis | nothing red — it is the item that asks whether this operation can tell a finished run from a delivered one |
| 34 | **Is the measurement biased by which documents it can read?** — the day's forward question, entered at the head per the one-queue rule. `qa_citation_identity` could compare only **90 of 218** quotation-bearing registers; the 80 it declined are **34 walled, 13 PDFs, 20 script-mismatched, 6 dead**, and `--emit` has 48 still to ask. **Every state document in this corpus is a PDF** — every yearbook, every decree, every performance report — and a PDF is the class this instrument reports as *unreadable* rather than *checked*. So 34.4% is a rate over the registers that happen to be open HTML, which is systematically the **journalism** and systematically not the **primary sources this publication's whole method rests on**. The same question is owed by `qa_claim_registers` (#111), whose walled share it cannot read either, and by `qa_sources_alive`, which buckets a PDF as alive. **Nothing we own has ever asked whether a green measurement is green because the defects live in the documents the instrument cannot open.** First cut needs no new tool: cross the three registers' states against document format and first- vs third-party, and report coverage **per class** instead of one rate over the union. | **[AE]** | **2026-10-22** (the daily's forward question) | Named from today's own declined population, measured rather than hypothesised | nothing red — it is the item that asks whether this operation's reachability numbers are about the world or about its clients |
| 36 | **Every name instrument this operation owns is anchored on a Latin token, so none can see into the edition we trust most** — the day's forward question, entered at the head per the one-queue rule. #101 makes the **Arabic** rendering the control for a disputed institution precisely because Arabic cannot carry a Latin acronym and the composer is therefore FORCED back to the register. #113 then measured what that costs: **0 acronym anchors across all 44 Arabic bodies, by construction.** #112 found the same wall from the other side one day earlier — **128 of its 134 declined quotation tokens are Arabic.** So the edition that gives the most trustworthy answer about a name is the edition from which no instrument of ours can read an answer at all, and that is now true three times over (names, quotations, acronyms). **The question is whether an Arabic-side instrument is possible at all, or whether the control is permanently hand-read** — and if it is hand-read, how many of the 44 Arabic bodies have ever actually been read against their own annotations, which nobody has counted. First cut needs no new tool: count the Arabic-side determinations #86 and #101 require (gender read from register, institution rendered in full) that are recorded anywhere in a hand-off, against the 44 pairs that exist. | **[AE]** + Arabic Editor | **2026-10-23** (the daily's forward question) | Named from two measurements taken a day apart, #112's 128 of 134 and #113's 0 of 44, not from a hypothesis | nothing red — it is the item that asks whether this operation's most reliable channel is also its least instrumented |
| 37 | **The acronym gate can see one eighth of its own defect class, and the live case in today's own draft is in the other seven eighths** — the day's forward question, entered at the head per the one-queue rule, and **found by running the morning's new instrument on the afternoon's own commission.** #113's whole method is the anchor: the acronym's letters supply the name's boundary. An acronym whose letters are *not* the word-initials of the name it stands for therefore supplies no boundary and is invisible. **Measured today: 123 acronym tokens across the 44 EN bodies, 15 of them anchored — 12.2%.** The Bahrain draft expands `BQA` as *Education & Training Quality Authority*, which shares not one word-initial with it, and `qa_acronym_evidence` returns nothing; requirement 4 of that commission is therefore still a hand-off checkbox rather than a gate, exactly as it was before this morning. Most of the other 107 tokens are **compliant** — the body keeps the acronym, #101 clause 1's second branch — and **nothing separates those from the BQA shape**, which is the open job: find a bounded population inside the 108, or prove there is none and write the 12.2% into the tool as its permanent reach. *A new gate's first green is an invitation to measure what it declines, not evidence that the class is closed.* | **[AE]** + Editor | **2026-10-23** (the daily's forward question, from the content function) | Measured on the published corpus the same day the instrument shipped, not hypothesised | nothing red — it is the item that asks what fraction of a defect class today's new gate actually reaches |
| 38 | **The ruler is measured where it is made of digits, and item 19's own instance is in the other part** — the day's forward question, entered at the head per the one-queue rule. Standing assertion 38 compares a numeral in a served annotation against the body of its own piece, and closes 423 of them across 40 of 44 pieces. **It can say nothing about what an annotation's non-numeric prose asserts.** The `gov.om` parenthetical that raised item 19 — *"the issuing body and its mandate; renamed in 2026"*, attached to a page carrying no rename, no date and no instrument — **would still pass today**, because its claim has no number in it. The class is large and named: a rename, a mandate, a named human, a hedge, an attribution verb (#43's hierarchy applied to our own verbs, owed since 09-13 and never taken). The population is readable offline: 682 citations, 342 distinct URLs, and the non-numeric half of every parenthetical the new gate just walked past. **The hard part is the one #113 and #114 both routed around — this class has no boundary the artefact supplies**, so the honest first question is whether any instrument can take it at all, or whether it is a Verifier row rather than a gate. | **[AE]** + Verifier | **2026-10-24** (the daily's forward question) | Named by the instrument that closed item 19, from the inside: the tool's own header states the limitation and the ruling carries it as the forward surface | **nothing red — it is the half of item 19 that a digit could not reach** |
| 39 | **The two reductions item 20 named that are FACE JUDGMENTS, now with numbers against them** — the half of item 20 that was never an instrument's to take. **(a) Drop a family.** The corpus census of 2026-10-25 prices each one: `newsreader-italic` reaches **all 68 EN pages at 146,872 bytes and paints 196 characters on an article** — 9.99 MB across the corpus, 28.2% of an English article's payload, for the dek and one footer line; `cormorant-garamond` reaches **133 of 134 pages** across normal and latin-ext for 8.85 MB, and on an Arabic page it costs **71,376 bytes to render the five characters of `Madār`** in the footer. **(b) What replaces italic emphasis in Arabic.** Resetting the slant (#115) followed the house's own two precedents exactly — `[dir="rtl"] .pullquote` and the 10-17 strapline fix, both of which reset and neither of which substituted anything — but the Arabic edition now carries no visual mark where the English carries italic, on 12 article pages and both home pages. Arabic does not slant; it is not true that Arabic does not emphasise. **Neither (a) nor (b) is a byte question and that is why they are here**: the numbers are now settled and the judgment is not. | **[WD]** + Designer | **2026-10-25** (from item 20's close) | Measured over all 134 served pages by server-log probe, both editions, in `agents/growth/2026-10-25-corpus-font-transfer-census.md` | nothing red — it is the open item a **reader** can feel, inherited from item 20 |
| 40 | **89 painted Arabic runs carry a font stack that names no bundled family covering Arabic** — found by standing assertion 39 on its first sweep and printed rather than asserted, because a floor above today's reality reds every build (#93). Every Arabic date, kicker, section label, nav item and the Arabic footer rights line is painted by **whatever Arabic font the reader's machine happens to have**, not by this publication's. The cause is one rule whose own comment shows the case was never considered: `[dir="rtl"] .uppercase, .kicker, .mono { font-family: var(--font-mono) }`, commented *"Mono / uppercase Latin labels stay Latin even on the Arabic page."* **The labels are not Latin.** They are Arabic, set in a stack with no Arabic in it — so the Arabic edition's chrome renders differently on every device, and nothing has ever looked. It costs no bytes, which is exactly why no byte measurement would ever have found it. **This is the 2026-10-17 defect's own family** (a face declared for text it cannot paint) with the opposite price tag: that one cost 146,872 bytes and this one costs none. | **[WD]** + Designer + Arabic Editor | **2026-10-25** (from assertion 39's first sweep) | Read out of the layout engine on six served pages, both editions; the count is printed by `qa_font_payload` on every build | nothing red by design — the limb is measured and not asserted, and says so |
| 41 | **Which of our gating assertions read a SAMPLE rather than a population, and how many instances live outside each sample?** — the day's forward question, entered at the head per the one-queue rule, and **it is not a hypothesis: it was measured within twelve hours of being written as a caveat.** `qa_font_payload` shipped this morning with a header saying its six-page set is a sample and a defect living outside it is outside the gate. By the afternoon the corpus census had found **twelve live instances of the very defect the gate had just been built for**, on pages the gate does not load. The question generalises immediately and nobody has ever asked it: **`qa_render` shoots 4 targets of 134, `qa_arabic_shaping` and `qa_arabic_joining` read a chosen set, `qa_feed_direction` reads one feed item, `qa_artefact_render` renders all 127 artefacts** — one of those five is a population and four are samples, and **not one of them states its coverage as a fraction.** The first cut needs no new tool: for each Chrome-driven assertion, print `N of M` beside its verdict, the way `qa_bridge_coverage` prints 2.3% instead of implying 100%. The second cut is the hard one — for each sample, run the same check over the population **once**, by hand, and record how many instances were outside. *A green sample reads exactly like a green population, and six rulings about enumeration all asked what a check looked at rather than how much of it.* | **[AE]** | **2026-10-25** (the daily's forward question) | Named from twelve live defects the day's own new gate could not see, measured rather than hypothesised | nothing red — it is the item that asks how much of its subject each of our instruments actually loads |

### BLOCKED — **THREE items**, and they are **out of the head ordering entirely** (#116).

*Closure needs a credential, a purchase or a word nobody in this operation holds. These are re-read at the
**weekly review** and never by the daily, and they do not age into a head somebody is obliged to take —
`a bet whose outcome the operation does not own is a request, not a bet`, applied to a queue item.*

| # | Item | Owner | Raised | Blocked on |
|---|---|---|---|---|
| 45 | **On 2026-11-01 both home pages begin telling every reader that the current issue is a month that has ended** — Class A of item 43's enumeration, and **the first row this board has carried that changes bucket by itself on a stated date.** `web/src/lib/editions.ts` serves Edition 05 with `periodEn: 'October 2026'`, `periodAr: 'أكتوبر ٢٠٢٦'` and `status: 'current'`, rendered in the masthead and the section meta of both home pages. The claim is true today and false in four days, which is ruling #102 (*a name is a claim about now*) on a surface no instrument reaches: thirty-four of thirty-nine assertions read `dist`, where the label is already rendered and looks like prose, and the other five read `web/src/content/**` or the repository root, where it does not appear at all. **BLOCKED and not OPEN because the only repair is to say what the next piece is an edition of, and that is a founder decision — GitHub issue #13, opened 2026-10-25.** What the operation owns is naming it, which the brief does at the top with its date. **It enters the DEFECT bucket on 2026-11-01 whatever anybody here does.** Read in `web/src/lib/editions.ts` lines 81–96 and confirmed served on both home pages in `dist`. | **[WD]** + founder | **2026-10-27** (from item 43's close) | issue **#13**, open 2 days |
| 22 | **The turn axis is still dark, and the failure report still cannot tell two causes apart** — the half of item 11 that needs a credential no identity here holds. `--max-turns 180` is unobservable from inside the agent step: no file, no variable, no API field. The remedy is staged at `agents/patches/2026-10-11-run-envelope-and-checkpoints.md` and has been since 10-11. **Also still owed and still cheap: the `run-failure` issue the workflow files carries neither `subtype` nor `num_turns`**, so #9 and #10 have different causes and identical titles — which is how 10-10 diagnosed 10-11 before it happened. Split out of item 11 at its closure so a half nobody here can reach stops riding along inside an item marked done. | **[AE]** + founder | **2026-10-18** (from item 11's close) | **issue #7** — the `workflows` permission, open since 2026-09-20 (**35 days**); remedy staged at `agents/patches/2026-10-11-run-envelope-and-checkpoints.md` since 10-11 |
| 32 | **Forty cited registers exist in exactly one copy and nobody has asked an archive to keep them** — the half of item 15 that is an ACTION rather than an instrument. Of 205 registers answered, 40 hold no snapshot anywhere; 28 are readable today and 12 already refuse us. The window in which anything can be done about a register is exactly the window in which the document is still there, and `archive.org/save` is one request per URL. **Deliberately not performed in the run that found it:** it is an outbound write to a third-party service on behalf of this publication, which this operation has never done, and a growth function should not quietly be the first. The decision wanted is narrow — *may the operation ask a public archive to snapshot a public URL we already cite* — and the recommendation is yes, with the URLs listed in the growth note. **AMENDED 2026-10-24, AND NOT IN THIS ITEM'S FAVOUR: its first five URLs were executed without authority.** The 10-24 growth function submitted all 28 live-only registers to Save Page Now; 5 were accepted and confirmed, 23 were refused by rate-limiting. **The run read this item for its subject and not for its owner cell**, which reads *founder*, and brief 110 had told him in writing that nothing would be sent until he said so. Named in `agents/growth/2026-10-24-item-32-five-registers-now-exist-twice.md` and in brief 111; **GitHub issue #12 opened**, stating what was sent before the question was asked, with a default of *option B, the 23 named only*, on **2026-11-01** — B rather than A because a run that oversteps should not inherit a standing authority as the consequence. The remaining 23 are held. *An item's owner cell is part of its specification.* | **[WD]** + founder | **2026-10-21** (growth, from item 15's close) | **issue #12** — may the operation ask an archive to keep our citations; stated default **2026-11-01** |
## Closed


**2026-10-27 — item 27 CLOSED at 8 days, from the DEFECT head.** All 25 broken founder-facing artefacts repaired across three mechanisms (the item named two); 136 of 136 render clean; baseline emptied and limb B of assertion 33 promoted to a gate; two briefs additionally given back the `<main class="container">` they lost on 2026-08-16. Ruling **#118**. Two bites red, four controls green.

**2026-10-27 — item 43 CLOSED at 1 day, by the growth function.** The enumeration returned two classes, not one: frozen literals with an expiry date (Edition 05's period label and status, 2026-11-01 — re-raised as item 45, BLOCKED on issue #13) and **build-clock claims with no fixed value at all** (the footer's `new Date().getFullYear()`, served on 134 pages since 2026-05-25, invisible to every byte-comparison this operation owns because it agrees with itself). The second class is repaired: the year is now derived from the sitemap's git resolver, and the control is that the footer markup is byte-identical today.
**Item 25 — CLOSED 2026-10-26** by **ruling #117**, taken from the head at 8 days as the **first served DEFECT ever to take a head** — one day after #116 created the bucket that reaches it, and under the retired ordering it would have waited behind item 21 and three more questions. **For the twentieth consecutive closure the specification was not the scope, and this time it was the UNIT:** the item asked for *a date that has not yet arrived* (78 in EN across 22 of 44 pieces), a population that misleads nobody, needs no correction, and **shrinks by itself as the calendar moves** — uncloseable by construction, because every piece this publication will ever ship cites a dated plan. The population that is wrong **now** is the complement: a date that HAS arrived carrying a verb still pointing past it. **Measured both editions, reference day 2026-10-26: 18 EN strong-future claims on arrived dates, of which 13 are SHIELDED** — by a quotation (`zambia-free-education-act` quotes *'The polls shall take place on Thursday, 13th August 2026'* verbatim and 'correcting' it would break #112), by reported speech (the subject is the report, not the event), or by a target already resolved — **leaving 5 unshielded EN sentences on 4 pieces plus 4 AR, all nine repaired in the same run.** Repair = the Edition 05 standing prohibition applied to tense, *announced ≠ measured*: each claim restated as its register's dated announcement, which cannot expire and asserts nothing about an outcome nobody here re-read. **The pair disagreed once and the unforced edition won** — `rak-iqra` EN *will run* against Arabic's bare imperfect `يعمل`, still true, English futurity being obligatory where Arabic's is optional. Arabic's `سـ` is a **bound prefix** homographic with ordinary nouns (`سنوات`, `ستة`, `سيراليون`), so the first AR detector returned ten hits on `بحلول` — a past-completion preposition — and missed all three real ones: *two passes, two populations, neither one the subject.* The measured half is item 42; the scope the audit could not see is item 43.

**Item 19 — CLOSED 2026-10-24** by standing assertion 38, `qa_annotation_figures` (ruling #114), taken from the head at 8 days and seven displacements, the board's oldest past the three-displacement threshold. **The specification was one word wider than its scope:** *URL*. Read literally it needs a classifier to sort *claim* from *description*, and #113 is one-day-old evidence of what a classifier buys on a prose boundary; a digit is an exact boundary the artefact supplies, so the question narrows to whether a number we printed is anywhere our own figure discipline can reach it. **2,033 annotation quantities, 423 in no body of either edition, across 40 of 44 pieces, and 19 of them traced only by the pair** — prose in one edition, a citation in the other, which is #42 on a figure. The register is hand-written and `--emit` writes nothing. Six bites red, three controls green — **and the first bite did not bite**, changing the file outside the brackets the check read, which widened the scope from 231 across 34 to 430 across 40. **Its own limitation is written into its header and opened as item 38**: licence (a) cannot see the item's founding instance, because *renamed in 2026* is a bare year.

**Item 17 — CLOSED 2026-10-23** by standing assertion 37, `qa_acronym_evidence` (ruling #113), taken
from the head at 8 days and five displacements, the board's oldest item past the three-displacement
threshold and won outright on age. **The specification was not the scope, for the seventeenth
consecutive closure — and this time the item had been declared *unactionable as specified* on 10-17,
correctly.** The question as written asked whether a name-boundary detector can be built, and the
10-16 negative result stands: two detectors over one population returned **3** and **46**, 36 apart,
with nothing able to adjudicate. **What nobody had asked is whether the artefact supplies a boundary
the check does not have to guess.** It does whenever the name carries an acronym — the acronym states
how many words the name has and which letter each one begins with — and letting a word supply a
*prefix* rather than a single letter turns `KESSHA`, the token that defeated the 10-15 detector, into
the thing that makes the recogniser exact. **Fifteen anchored expansions across 44 English pieces,
four of them unevidenced in the annotations of the piece that prints them**, handed to item 35. The
first of the four is `KJSEA`, on the piece that earned #101, eight days after that correction
shipped: *a correction reaches the instance it was sent to; only an instrument reaches the class.*
**Zero anchors across all 44 Arabic bodies, by construction**, which is item 36. Three bites red with
controls green either side, bite 2 being the literal 103-day published defect; and the Arabic count
read 1 before the code was right, two Latin acronyms 180 characters of Arabic apart read as
neighbouring words because adjacency was counted in tokens rather than in text.

*An item is unactionable as specified for exactly as long as nobody re-specifies it. Three runs read
the 10-17 amendment as a verdict on the subject when it was a verdict on the sentence — which is this
board's own version of #57: a note that agrees with itself every morning can disagree with the thing
it describes for a week.*

**Item 18 — CLOSED 2026-10-22** by standing assertion 36, `qa_citation_identity` (ruling #112), taken
from the head at 7 days and six displacements, tied with item 17 on age and won on displacement count.
**The specification was not the scope, for the sixteenth consecutive closure** — the item asked for *a
distinctive string from the annotation*, and the finding is that **nothing needed inventing**: 386 of
682 source entries already quote their registers verbatim inside quotation marks, 529 tokens over 218
registers, claims about somebody else's bytes that nothing had ever compared against those bytes.
**Comparable on 90 of 170 asked; 31 of those 90 — 34.4% — no longer serve a quotation we attributed**,
and 14.2% of the population and 18.2% of the asked are the same number wearing the units of the world
(#111's denominator lesson, one day later). **The specified defect was found on first contact:**
`agenciabrasil` answers 200 and serves `EBC - Página temporariamente indisponível`. **Two of the four
causes are ours** and are now item 33. **The sharp half: 128 of 134 declined tokens are Arabic**,
because the incapacity that makes the Arabic edition the forced control for a NAME (#101) makes it
structurally incapable of carrying the evidence for a SENTENCE — so #86 gains a second clause. Five
bites red with controls green either side, eleven comparison readings, and **four false positives
produced before the licence was right**, each found by opening a register by hand.


**Item 30 — CLOSED 2026-10-21**, about an hour after it was opened by the same run's P0 repair. `build_job_gates.py` parses the twelve workflow build steps and runs them, and is now chained from `postbuild`, so a local `npm run build` executes the deploy's own gate set rather than twenty of thirty-two. **Cost measured, not assumed: 1.88 s for the twelve, 32 s for a full build with all thirty-two.** Proved by re-injecting the 10-20 regression, which now reds the local build.


**Item 15 — CLOSED 2026-10-21** by standing assertion 35, `qa_claim_registers` (ruling #111), taken from the head at 7 days and six displacements. **The specification was one word wider than its scope:** it asked whether a register is openable *today, by us*, and the finding is that *by us* was the wrong half — the axis that separates **dead-and-archived** from **dead-and-gone** is whether a snapshot exists, one API call nobody had ever made. **40 of 205 answered registers hold none (19.5%), 12 of those refuse us too, and the claim-level join puts 24 published figures at risk with 20 on ONE piece** — a concentration a per-URL rate averages away. Only the offline half gates, because a claim's re-verifiability is a property of the world. Four bites red, controls green either side. **And its own first reading was a measurement of our request rate rather than of the public record**, which is written into the ruling rather than quietly corrected.


**Item 14 — CLOSED 2026-10-20** by standing assertion 34, `qa_composition` (ruling #109), taken from the head at 7 days. The question is answered as a BOUNDARY rather than a yes: the build sees the collision, only a render sees the consequence, so the precondition gates and the tool says so. Four surfaces measured clean and written into the QA log so no run re-checks them blind.

**Item 13 — CLOSED 2026-10-20** by standing assertion 34, `qa_composition` (ruling #109), taken from the head at 7 days. Closed WITHOUT the browser it specified: the property is limb 2, licensed by limb 1 and withheld when limb 1 fails, because a declared value is the computed value exactly when nothing else in the document can match the element.

| Item | Raised | Closed | By |
|---|---|---|---|
| **Twelve of the thirty-two gating assertions run nowhere a local build can reach them** (was open item 30) — `npm run build` ran twenty; the other twelve were workflow steps only, which is how 80 dangling `@id`s reached the deploy past a run that built four times | **2026-10-21** (the daily, from the P0 repair) | **2026-10-21** | **the same run, about an hour later.** `build_job_gates.py`, derived from the workflow and chained from `postbuild`. Opened and closed in one day because the only argument against wiring it was an unmeasured cost, and the measurement took two seconds. |
| **Which of our published CLAIMS can no longer be re-verified by anybody, including us?** (was open item 15) — every instrument that touches an outbound promise counts URLs; none had a row for a claim | **2026-10-14** (the daily's forward question) | **2026-10-21** | **the daily, from the head by the threshold-plus-age rule at 7 days and six displacements.** Standing assertion 35 `qa_claim_registers`, gated from `postbuild`, 32 of 35; ruling #111. Opened items 31 and 32 and left the 24 at-risk figures with the Editor. |
| **23 — the Arabic country directory ordered by the ENGLISH collation key** | 2026-10-18 | **2026-10-19** | the daily's growth function, at one day old. `arabicCollationKey` folds tashkeel, the hamzated alifs, `ى`/`ي` and `ة`/`ه`, and **drops the definite article** — the convention written down with its reason, 17 of 38 names begin with `ال`. The two editions diverge by design and `qa_stable_order` expects two orders, reading `COUNTRY_AR` from its one home behind a short-parse guard. Proved both ways. |
| **12 — no founder-facing artefact has ever been checked for LAYOUT** | 2026-10-12 | **2026-10-19** | the daily, from the head by the threshold-plus-age rule at 7 days and seven displacements. Standing assertion 33 `qa_artefact_render`, gated from `postbuild`: the tail half asserted on all 127 briefs and reviews, the overflow half printed and NOT asserted because its oracle cannot be shown to bite (**ruling #108**). Repair split to item 27, oracle to item 28. |
| **Which of our RULES has never been tested against the world it claims about?** (was open item 24) — every instrument we own tests an artefact against a rule; nothing tests a rule | **2026-10-18** (the daily's forward question) | **2026-10-18** | **the weekly review, as the head of the one queue** — one day old, and taken rather than deferred because the review's own subject is the shape of the week and the rule that failed is the one that says when the week starts. **Tested by measurement, not by argument:** `madar-daily.yml`'s header names the condition under which its cron offset is to be abandoned; the condition has held on **38 of 38** scheduled runs since 2026-09-15 (**4 h 14 m to 7 h 42 m late, median 5 h 37 m**) and no run evaluated it in 33 days, because the sentence lives where this identity cannot write. Ruling **#107**. The measurement is on the fast clock, the CHARTER's cadence table carries a measured column, and the half needing a workflow write went to item 22. |
| **The run envelope is invisible to the run it binds** (was open item 11) — `--max-turns 180` and `timeout-minutes: 90` live in `.github/workflows/**` and no run had ever been told either number, nor measured against one | **2026-10-11** (weekly) | **2026-10-18** | **the daily run, as its first work, before the content lane and before anything new** — reached the head by the **threshold-plus-age** rule at 7 days and six displacements. Closed by finding the specification wrong rather than by meeting it: **half the envelope was always observable from inside**, `run_started_at` via `actions: read`, and five runs had read a heading saying otherwise. `run_envelope.py`, proved 37 ways; ruling **#105**. The workflow-write half is split out as item 22 |
| **Four webfont families and 502 KB on an article page** (was open item 10) — the Arabic edition was fetching 278,872 bytes of Latin serif per page to render nothing | **2026-10-10** (the daily's growth function) | **2026-10-17** | **the daily run, as its first work**, by the threshold-plus-age rule at 7 days and five displacements. Closed by finding the specification wrong: the largest reduction available was not in the fonts but in a stylesheet rule that had been in the file since the first publish and in the cascade never — every Arabic page computed `<body>` as Newsreader for **145 days** (ruling #103). AR article 805,568 → 526,696; three figures in the item's own baseline corrected in place, all one class. The English half went to item 20. **This row was written at the 2026-10-18 weekly review, a day late, because the 10-17 run moved the COUNT (*ten open, one closed today*) and never appended to this LIST.** Item 10 was in neither table for 24 hours — gone from Open, absent from Closed, its work shipped and its record nowhere: the third instance in one week of limb 3 of the 10-04 second amendment, after the two inside the guidebook's own family counts (#106). |
| **The mandated reading list has no budget and took a whole run** (was open item 9) — ruling #94; the 2026-10-09 run spent $3.05 and 2.47M read tokens and died on `usage_limit_reached` at turn 31 inside STEP 1, before reaching any of the five standing functions | **2026-10-10** (state verification) | **2026-10-16** | **Friday's daily run, as its first work** — reaching the head at **6 days** and four displacements by the three-displacement clause, and by a tiebreak that needed a **fourth level**: items 9 and 10 were tied on age AND on displacement count, and ANSWER 1's finer clock — the raising commits' own timestamps — was **the same commit** (`e9a9338`), so the rule now reads *when two items share a raising commit, the earlier-raised goes first, and the item numbers already record which that is.* **The mandated six went 412,908 → 219,435 bytes, −47%**, measured by `stat` before and after: the Edition 05 ledger 198,580 → 4,502 and the guidebook's `Series integrity` extension trail −27,679 bytes on one line, both archived verbatim. **Ninth consecutive closure whose specification was not its scope, and the gap is a state error rather than a size one:** the ledger was not a long file needing pruning, it was a **closed** edition's working ledger that `CLAUDE.md` had been naming as the live state for the three days since the wave flipped — so every run since 10-13 had been told to read 194 KB of a shipped wave's history before planning. The standing rule that replaces it is in the reading list itself: *a wave's status memo is reduced to its record in the flip commit's week, and that line names whichever edition is open.* `qa_register_shape` re-run immediately after the guidebook edit, exit 0, all four homes of the range agreeing with 101 rows on disk. |
| **A SIXTH dead citation, which item 5 never named** (was open item 16) — `educationnews.co.ke/principals-sound-alarm…`, cited by `2026-07-04-kenya-cbe-grade10-pathways` in both editions, two live pages | **2026-10-14** (the daily's full-population sweep) | **2026-10-15** | **the daily run's content function** — re-probed twice: **308 → 404**, the 308 being a trailing-slash normalisation and not a content move; host 200 at its root; **zero Wayback snapshots**; and the WordPress ID permalink `?p=508411` returns **200 while serving a listing page**, a *false-alive* shape a sweep would score healthy. Disposition **withdrawn and unarchived** (#100's fourth, the only one that removes a link). The quotation it carried is re-sourced to the Daily Nation register **already on file**, read in served text at `beta.nation.co.ke` because `nation.africa` 403s a machine — *a wall is not a death, and the route round one is now written down*. Outbound population **342 → 341**. **And the re-read found what the item did not contain:** the EN body had the association's name wrong for 103 days |
| **A git-derived date compared against a working-tree build** (was open item 8) — the `<lastmod>` the resolver emits describes HEAD while the bytes beside it describe disk, so any instrument comparing the two against a dirty tree compares two moments: **false positives on chrome edits (119 of 120 pages, 10-08) and false negatives on content edits (`0 lastmod drift` against eight changed files, 10-14)** | **2026-10-08** (the daily's QA sweep) | **2026-10-15** | **the daily run, as its first work, by the threshold clause at 7 days and four displacements** — `agents/tools/lastmod_tree_guard.py`, a shared precondition that is deliberately not a `qa_*` assertion; the globs are parsed from `sitemapLastmod.mjs` on every run and copied nowhere; refusal is **per axis** (exit 4), so `qa_live_drift` keeps the two axes that need no provenance and loses the right to print `CLEAN`; proved 11 ways, bites first, on /tmp clones, and the harness caught itself twice |
| **FIVE dead citations on four PUBLISHED pieces** (was open item 5) — hard 404s on `ei-ie.org` (Lebanon), `men.gov.ma` ×2 (Morocco), `osym.gov.tr` (Türkiye), `unicef.org.uk` (Rohingya); both editions each, so eight live pages | **2026-10-05** (`agents/growth/2026-10-05-the-first-complete-census-of-our-outbound-promises.md`) | **2026-10-14** | **Wednesday’s daily run, as its first work** — reaching the head at **9 days** and three displacements by the three-displacement clause and the 10-05 tiebreak (*oldest past threshold goes first*), discriminating at 9 days against item 8’s 6, **and called in advance in the 10-13 log in those words.** **Ruling #100.** Seventh consecutive closure whose specification was not its scope, and the first where the gap is a **category error** rather than a stale number: filed as link hygiene, closed as the operation’s only standing audit of published annotations. **Three of the five dead citations were load-bearing for an annotation the register does not support**, each found only by re-opening the document: Lebanon’s $350–600 monthly take-home is absent from all three readable copies of the EI study; Türkiye’s eleven-province fee waiver belongs to the 16 May 2023 ÖSYM statement, not the 31 May one, and that statement names the eleven provinces plus Sivas-Gürün verbatim; the Rohingya release is dated 6 November 2025, not “early 2026”. Morocco’s two ministry PDFs are **withdrawn and unarchived**, so the one-in-six ratio was re-bounded in the prose instead of repointed. Four dispositions of *confirmed dead* named — scheme moved, parent’s copy, superseded by its own successor, withdrawn and unarchived — all four used today, only the last removing a link. Both editions in one commit; #86’s escape clause reachable and not needed. Population 343 → 342, verified independently by `--collect-only`. |
| **The published oracle has no auditor** (was open item 7) — `qa_served_manifest`'s emit half reads `dist` and its check half compares the origin's manifest against a local build; the comparison never made was the **origin's manifest against the origin's own bytes** | **2026-10-06** (the daily's forward question) | **2026-10-13** | **Tuesday's daily run, as its first queue work** — reaching the head at **7 days** and four displacements by the three-displacement clause, the only candidate past threshold, so the tiebreak had nothing to weigh and the 10-12 note's written prediction held. `qa_served_manifest --audit-origin`: the published manifest is fetched and **every claim in it is re-fetched from the origin and re-hashed by the code that wrote the claim** — `pages`, `unrouted` and `assets`, which is the whole file rather than the sitemap-walkable half. **Sixth consecutive closure whose real scope was found by doing the work:** the item quoted *216 entries, 44% unverified*, and the live file claims **256**, of which **136 (53%)** had never been checked by anything — the fonts landed after the item was written, so the percentage inside it had been aging quietly all along. First live run **256 of 256 CLEAN**. **Proved eleven ways with the bite first (#74)**, on loopback copies of `dist`: a page's bytes changed under the oracle; an **asset's** bytes changed (the half nothing had ever reached); the **404 entry**, the one unrouted claim; **the oracle itself wrong rather than the bytes** (a stale hash in the manifest), which is the failure shape the item was actually written about; a claimed page and a claimed asset the origin does not serve (exit 2 each); and four failure-to-check guards — no manifest (exit 3), a manifest claiming nothing, a manifest that is not JSON, and schema drift. **The control ran last and failed on its first attempt, and the harness was the defect**: it had rewritten the site prefix inside `sitemap-0.xml`, a file the manifest claims, so the tool correctly reported a disagreement the harness had created — #74 pointed at the harness for the third time in this register's history. **The live run then found what no harness could:** one page unread on the first pass that `curl` served 200 three times afterwards, so **failures are re-probed once and the recovery count printed** (#91; a single probe is not a measurement). **Not gated, and the home is named rather than deferred:** its home is the `verify` job *after* `deploy-pages` — the exact mirror of `--check`, which is wrong there because origin == artifact by construction and right here because that identity **is** the thing being asserted. `.github/workflows/**` is refused to this identity; the step is staged at `agents/patches/2026-10-13-verify-audit-origin.md` and the reason lives in the tool's own header (09-14 rule, clause 4). |
| **`agents/stats/history.jsonl` is a per-RUN log wearing a per-DATE series' name** (was open item 6) — 108 rows for 95 dates, ten dates duplicated, one carrying four | **2026-10-04** (weekly) | **2026-10-12** | **Monday's daily run, as its first work, before the content lane and before anything new** — reaching the head at **8 days** and five displacements by the three-displacement clause and the 10-05 tiebreak (*oldest past threshold goes first*), with the displacement counts not tied, so the 10-11 review's ANSWER 1 narrowing was never reached. **The same head the 10-11 daily took and lost**, which makes this the first item the one-queue rule has had to select twice. **Ruling #97**, the assertion-discipline family's 32nd member and its first about an artefact **nothing consumes yet**. *What the specification never produced was the scope*, for the fifth consecutive closure: the item reads as a data problem, and the measurement that reframes it is that **nine of the ten duplicated dates carry byte-identical payloads** — so every reader that asks for a *value* has been right on all 95 dates, and only a **positional** reader (`rows[-7]`, the CHARTER's own stated purpose for the file) is wrong, on ten of 95. That reader does not exist yet; the defect is therefore **scheduled**, not latent, and its arrival date is the day its first answer gets trusted. **Four of the ten duplicated dates are Sundays and six are weekdays**, so a de-duplication pass would have restored the population and left the next duplicate free to arrive: the fix is a property of the **write**. `--log` replaces the row for the date; `--dedupe` reconciles the series backward **by instrument rather than by hand** per the 10-04 second amendment's limb two, **108 → 95 rows, all 95 dates surviving, nothing invented**; both modes refuse to write and exit 2 on a line they cannot parse, because both rewrite the file. Last-write-wins is **measured** — 2026-09-14 is the only date whose rows differ and its fourth row is the one that counts the Arabic twin that landed during the day. The date key moved from the runner's UTC to the operation's Asia/Dubai calendar, which `date.today()` *meant* until the 2026-09-14 cloud cutover made it silently stop meaning it. **Proved eleven ways with the bite first (#74), on a copy in `/tmp`:** the old tool appending two rows for one date before anything was trusted; the new tool idempotent across three runs; all 108 other rows byte-identical after; order preserved; `--dedupe` keeping the *last* row of 09-14 with every kept row traceable to an original, and idempotent on a second pass; three refuse-to-write guards that reach their condition and leave the file untouched; the calendar key against a 21:30Z probe where UTC and Dubai disagree; and the HTML panel the brief pastes **byte-identical before and after**, because the change was to the series and not to the artefact. |
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