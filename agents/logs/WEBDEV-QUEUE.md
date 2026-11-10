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

## Weekly reconciliation — **2026-11-08 (weekly review).** Board **FORTY-EIGHT**, and last week's figure was wrong by three.

**Counted by reading the rows, which is the only method this file accepts (#57):** **ONE DEFECT, FORTY-FOUR
OPEN, THREE BLOCKED = 48.** The daily read 47 this morning and was right; this review raised **item 90** at
OPEN's head, so the board closes the week at 48.

### The board arithmetic reconciles to the row — once last week's number is corrected

| | |
|---|---|
| Board on 2026-11-01, **reconstructed from today's rows** | **35** — 26 OPEN still live + 3 BLOCKED still live + 6 closed since, all raised before 11-01 |
| Board the 2026-11-01 review **printed** | **32** — *"zero DEFECT, twenty-nine OPEN, three BLOCKED, counted by reading the rows"* |
| Under by | **three**, in the OPEN bucket: 29 printed against **32** |
| Forward from the true figure | 35 + **18** raised − **6** closed = **47**, which is exactly the daily's count this morning; +1 for item 90 = **48** |

**The reconciliation closes to the row, and it only closes on 35.** That is the strongest available evidence
that the error is last week's and not this week's: three independent numbers — today's row count, this
week's raises and this week's closures — agree with 35 and none of them agrees with 32. **And it propagated.**
The 11-01 rate table (*Raised 27, Closed 13, Net +14*) was computed from 18 → 32, so its net movement is
understated by three; the figure travelled a full week before anything compared it to a row.

**This is the third board mis-count in eight days and the second in two runs.** 2026-10-25 found fifteen of
eighteen rows understating their own age; today's daily wrote 46 against a true 47 **in the same file that
quotes #57 two paragraphs above it**, and caught itself; last week's review wrote 32 against a true 35 and
**did not**, because nothing re-reads a board after the review that wrote it. *An arithmetic that is
internally consistent is invisible, and the only thing that catches it is the population.*

### Rates, and the breach date is PINNED BY A RAISE DATE rather than by the closure rate

| Rate | This week (11-02 → 11-08) | Last week (10-26 → 11-01) |
|---|---|---|
| Raised | **19** (2.71/day) — 18 by the dailies, 1 by this review | 27 (3.86/day) |
| Closed | **6** (0.86/day) | 13 (1.86/day) |
| Net board movement | **+13** (35 → 48) | +14 (true 21 → 35) |
| Date the oldest item reaches 28 days | **2026-11-29** | printed as 2026-11-11 — **and that date was impossible** |

**Closures halved and the raise rate fell by a third.** Six closures against thirteen is the worst closure
week since 10-18, and one of the seven days closed nothing at all. The cause is visible in the heads: five
of this week's seven heads were **OPEN rows at exactly 15 days** and the other two were the DEFECT, so the
board spent the week paying down 15-day-old questions one at a time while nineteen new rows landed on top.

**The breach date, computed by the stated method and not carried.** Oldest-first, one closure per day from
2026-11-09, no re-ordering: the first row still open on the day it turns 28 is **item 65**, closing
2026-11-29 at exactly 28 days. *(Today's daily named item 67 and the same date; 67 is the third of the
cohort and breaches at 30.)*

**And the number is unmoved for the fifth consecutive restatement for a reason nobody has stated: it is
pinned by a RAISE DATE, not by the closure rate.** Items **64 through 70 were all raised on 2026-11-01** —
seven rows in one day — and 2026-11-01 + 28 = **2026-11-29**. No closure rate this operation can reach moves
that date; the rate decides only **how many of the seven breach and by how much**. At one closure per day
exactly one does (item 65, at 28); at this week's observed 0.86/day, **four of the seven breach**, the last
at 36 days. *Restating that the breach date is "unmoved" reads as evidence the closure rate is adequate, and
it is evidence of nothing at all.* **#116 requires this review to print the date as a claim about rates —
so the honest claim is about the cohort: a seven-row single-day raise sets a cliff twenty-eight days out,
and the only lever on the cliff is not raising seven rows in one day.**

**Last week's 2026-11-11 was arithmetically impossible** and is withdrawn here rather than quietly dropped.
It was computed as *board ÷ closure rate*, which yields a **steady-state age** (32 ÷ 1.86 ≈ 17 days), not the
date a particular row crosses 28. For any row to be at 28 days on 2026-11-11 it would have to be 25 days old
today, and **the oldest row on the whole board is item 22 at 21 days — and it is BLOCKED, so out of the
ordering entirely.** Two methods have been circulating under one name; the oldest-first simulation is the
one #116's wording supports, and it is the method of record from today.

### BLOCKED — three rows, re-read here as this review is required to do, and never by the daily

| # | What it needs | Age | Movement this week |
|---|---|---|---|
| **22** | A credential no identity here holds — **issue #7**, open **49 days** | **21 days** | **Still the most expensive row on the board, and this week it cost a brief again.** The 11-03 run died at the turn cap; the remedy for the envelope has been staged at `agents/patches/` since 10-11 and cannot be applied from here. **What changed is on our side, not his:** ruling #136 lit the turn axis from outside the run this morning, so the *measurement* no longer waits on the credential even though the *cap* still does. Nine staged patches now sit behind this issue. |
| **45** | What the next piece is an edition of — **issue #13** | **12 days** | **CLOSABLE NEXT WEEK, and for the first time by us.** Its blocker's stated default fell due today and was applied: `_STANDING_LEDGER.md` is open, pieces ship as singles, and the row's question now has an operative answer even though the founder's half is untouched. **It stays BLOCKED this week** because the half that is genuinely his — the frame — is still open, and a row must not leave this bucket because a default papered over it. Re-read it at the 11-15 review against whether anything is still waiting on him. |
| **32** | Permission to write to a third party on this publication's behalf — **issue #12** | **7 days** | Default applied 2026-11-04, three days late. Unchanged since. The window is still the moving part: 40 cited registers exist in exactly one copy and 12 already refuse us. |

**All three are correctly out of the head ordering.** *An item whose closure the operation does not own is a
request, and a request must not occupy a head somebody is obliged to take.* Item 22 at 21 days would have
taken a head three times over under the retired rule, and each time the run would have spent a day on work
it cannot finish.

### Tomorrow's head

**Item 85** — the board's only DEFECT, 2 days old, 22 of its 32 tokens still unread. It outranks all 44
OPEN rows whatever their age (#116), exactly as today's and yesterday's boards both forecast. **If it closes,
the head falls to item 37 at 17 days**, the oldest row in OPEN.

## Open — **FIFTY-FOUR items in THREE BUCKETS, reconciled against disk 2026-11-10**

**2026-11-10 — THE DEFECT HEAD WAS TAKEN AS WRITTEN AND IT CLOSED, AFTER ITS UNIT HAD TO BE CORRECTED
TWICE BEFORE IT COULD BE TAKEN AT ALL.** The displacement line, in one sentence: **this run took item
85** — *32 gender determinations about named humans are served in 14 of the 44 Arabic pieces and not one
has evidence on file* — raised 2026-11-07, **3 days**, the board's only DEFECT, so it outranked every
OPEN row whatever its age — **and displaced items 93, 92, 91, 90, 89, 88, 87, 86, 84, 83, 82, 81, 80,
79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 60, 57, 56, 55, 53, 52, 50, 48,
47, 46, 44, 41, 40, 39, 38 and 37.** The three BLOCKED rows (45, 22, 32) were not displaced, being out of
the ordering entirely. **Thirty-fourth selection in thirty-six daily runs made by the rule, fifteenth
under #116**, and the third consecutive head the DEFECT bucket routed away from age. Yesterday's board
forecast this head by name and by bucket and was right about both — for the third day running.

**ITEM 85 CLOSES AT 3 DAYS, AND IT CLOSED ON ITS POPULATION WHILE ITS COUNT MOVED THE OTHER WAY.**
`arabic_side_reach` read **32** tokens when the row was raised, **39** at the start of this run and
**54** at its close. The rise is the repair: the provenance #86 clause 2 *requires* is itself an Arabic
honorific gender commitment, written into the annotation the detector reads, so **the cure is a member of
the population and the numerator grows the denominator.** What closed is the thing the row was actually
raised about — *determinations with no provenance on file* — now **0 of 19**: four evidenced by their own
cited register (Shawki, Baba-Moussa, Ashiamah, Reddy), eight declared as this edition's own with the
settling fetch named, **zero wrong** across all nineteen, where #86's own sample of ten had found two.
Filed as **ruling #138**. Full read in `agents/logs/qa-2026-11-10.md`.

**Count line: FIFTY-FOUR open — ONE DEFECT, FIFTY OPEN, THREE BLOCKED. ONE closed today (85),
THREE opened** — **94**, the day's forward question, at OPEN's head; **95**, `arabic_side_reach`'s two
unit defects, raised from 85's closure rather than carried as a note; and **96**, from the growth
function, **the board's only DEFECT and therefore tomorrow's head.** 94 is a coverage gap and a face
judgment and 95 names an instrument's wrong output rather than a wrong served byte, so neither is a
DEFECT; **96 names 47 served sitemap entries that are wrong now, on every deploy**, and that is #116's
boundary read straight. **Board UP THREE, 51 → 54, and the count is against the rows: 1 + 50 + 3 = 54.** *(A fourth row, **97**, was raised by the BRIEF function after this line was first written at 53: a founder-facing artefact can be structurally malformed and pass every check we own. It is OPEN, not a DEFECT, because brief 125 was repaired in the run that found it — but it stood malformed for a day and nothing could have told us.)*

**TWO COUNT ERRORS WERE ON THE BOARD ON ARRIVAL, AND BOTH WERE IN THE TABLES RATHER THAN IN THE PROSE.**
**(i)** Rows 91, 92 and 93 were physically appended by the 11-09 run **to the DEFECT table**, carrying the
word `OPEN` in their `Blocks` cell in place of a bucket — so the board's prose said *one DEFECT* while its
DEFECT table held four rows. It changed no head either way, the oldest DEFECT being item 85 on both
readings, but **#116 orders the buckets and the buckets are the tables**; a board that is right only in
its prose is one careless read from handing out the wrong head. Moved. **(ii)** The OPEN block's own
heading read **FORTY-THREE** against 44 rows, and has since 11-08. Both were found the same way and it is
the only way that works: **counted against the rows (#57), not against yesterday's number** — which is
the fifth consecutive week this register has earned that ruling, and the second time in three days that
the defect was a count sitting beside the rows it describes.

**The 28-day breach date is unmoved at 2026-11-29 and is still PINNED BY A RAISE DATE**, not by the
closure rate: items 64–70 were all raised 2026-11-01 and 11-01 + 28 is 11-29. Today's single closure does
not move it and could not. **Seventh consecutive restatement, same meaning every time: the rate decides
how many of those seven breach, never when.**

**Rates, carried and moved by today:** raised 3 + 3 + 4 + 4 + 4 + 4 + 5 + 2 + 1 + 4 + 3 + 2 + 2 + 3 + 3 +
**4** · closed 1 + 2 + 1 + 2 + 2 + 3 + 2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 0 + **1** · board 51 → **54**.

### Tomorrow's head

**Item 96** — the board's only DEFECT, raised today, **0 days**, naming 47 served sitemap entries that
are wrong on every deploy. It outranks all 50 OPEN rows whatever their age (#116). **If it closes, the
head falls to item 37 at 18 days**, the oldest row in OPEN.

**Note what the DEFECT bucket did today, because it is the third falsification of its own emptiness in
sixteen days.** It held item 85 at the open, emptied at 85's closure, and was re-occupied within the hour
by item 96 — **not by a new regression but by a 65-day-old question that finally carried a number.** The
bucket measures what the board can currently COUNT, never what the corpus currently IS (#116 ii), and
every one of the three falsifications arrived by a measurement rather than by a render.

### The daily record for 2026-11-09 follows, unaltered.

## Open — **FIFTY-ONE items in THREE BUCKETS, reconciled against disk 2026-11-09**

**2026-11-09 — NO HEAD WAS TAKEN, AND THAT IS A DEPARTURE STATED AS ONE.** The board's head is **item 85**, the only DEFECT, raised 2026-11-07 and therefore **2 days** old, with 22 of its 32 gender-evidence tokens unread; under #116 it outranks every OPEN row whatever the age. **This run spent its content and quality functions on the standing ledger's named next action instead** — the Arabic Editor's gate on `bahrain-bqa-five-cycles`, then the still, the og card, the publish gate and the flag — and **shipped the first piece in 43 days**, the first single under the ledger opened yesterday. So item 85 was displaced by a publication rather than by another row, and it displaced nothing itself.

**Why this is not the rule being broken, and why it is written down anyway.** #116 orders *this board*. It does not order the publication against this board, and the pipeline had an eight-cell gate one cell from closing. *A run that reads a queue rule as ordering the publication will never ship.* But a departure nobody records is indistinguishable from a rule quietly lapsing — which is the whole reason clause 3 of the one-queue rule exists — so: **item 85 stays the head, was not taken, and takes tomorrow's slot.** It is now the second consecutive day the DEFECT head has gone untaken, the first being a day on which it was taken and narrowed rather than closed.

**Count line: FIFTY-ONE open — ONE DEFECT, FORTY-SEVEN OPEN, THREE BLOCKED. ZERO closed today, THREE opened** — **91** (the 2026-11-08 weekly review has no artefact, from state verification), **92** (the editions standing block now holds two populations under one heading, from growth) and **93**, the day's forward question, at OPEN's head. **None is a DEFECT** by #116's boundary: 91 names an artefact that does not exist rather than N served artefacts that are wrong, 92 is a legibility question at a population of two, and 93 is a coverage gap — *the bytes being right* in all three. **Board UP THREE, 48 → 51, and the count is against the rows: 1 + 47 + 3 = 51.**

**The 28-day breach date is unmoved at 2026-11-29 and is still PINNED BY A RAISE DATE**, not by the closure rate: items 64–70 were all raised 2026-11-01 and 11-01 + 28 is 11-29. Today's zero closures do not move it and could not — no closure rate reachable from here does. **Sixth consecutive restatement, and it means the same thing every time: the rate decides how many of those seven breach, never when.**

**2026-11-08 — THE DEFECT HEAD WAS TAKEN AS WRITTEN, IT CAME BACK ZERO WRONG, AND THE EVIDENCE TURNED OUT
NOT TO BE WHERE EVERY INSTRUMENT HAS BEEN LOOKING.** The displacement line, in one sentence: **this run
took item 85 — *32 gender determinations about named humans are served in 14 of the 44 Arabic pieces and
not one has evidence on file* — raised 2026-11-07 from item 36's closure, **1 day**, and the board's only
DEFECT, so it outranked every OPEN row whatever its age — and displaced items 86, 84, 83, 82, 81, 80, 79,
78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 60, 57, 56, 55, 53, 52, 50, 48, 47,
46, 44, 41, 40, 39, 38 and 37.** The three BLOCKED rows (45, 22, 32) were not displaced. **Thirty-third
selection in thirty-four daily runs made by the rule, fourteenth under #116**, and the second consecutive
head the DEFECT bucket routed away from age. **Yesterday's board forecast this head by name and by bucket
and was right about both.**

**Item 85 is NARROWED and NOT CLOSED, at 10 of its 32 tokens.** The row sends the four pieces with no
second channel first and those are what this run took: **10 honorific tokens, 6 named humans, 4 served
pairs**, each read against the register its own annotation names. **8 EVIDENCED · 2 UNDETERMINED by their
registers · 0 WRONG** — and #86's own sample of ten found two wrong, so a zero is a result. *The finding
is the distribution, not the verdict:* of the eight evidenced, **ONE** rests on a pronoun and **FOUR** on
a **morpheme inside the name as the register prints it** (`Sayyid`, `bin`, and `bint` in `gov.om`'s own
Latin management listing), so **half the evidence this class has was forbidden by #86 clause 1's words
*never off the name*** — filed as **ruling #134**, this register's first amendment to the scope of a
prohibition it already carried. *Two of the four pieces are not one-channel:* Oman's **English**
annotation already printed `HH Sayyid Theyazin bin Haitham`, invisible to a closed class holding neither
token (#113 from the other side); and Singapore inverts **#101** — the register prints `Mrs Grace Chua`
and `Mr Mohamed Ashiq`, **Arabic kept both and ENGLISH reduced them to `Principal` and `Year Head`**, the
free edition deleting the evidence the forced edition needed. Both restored. For Janke and Al Ali the
cited registers print `Dr.` and no pronoun, so **#86 clause 2** was applied: declared in both editions as
this edition's own, dated, with the settling fetch named. **The row stays a DEFECT and stays the head
tomorrow**, because 22 tokens over 10 both-channel pieces are still served with no provenance.

**Count line: FORTY-SEVEN open — ONE DEFECT, FORTY-THREE OPEN, THREE BLOCKED. ZERO closed today** — the first
day since 10-28 on which the head was taken and nothing closed, and it is the correct outcome: the row's
population is 32 and this run read **10 of them properly rather than 32 of them quickly**. **THREE
opened** — **87** (704 served JSON-LD citation nodes whose `name` is our annotation and not the
document's; from growth), **88** (#96 and the publish-gate rule pull opposite ways whenever content
changes a served byte, second consecutive day, from the QA log), and **89**, the day's forward question.
**Neither 87 nor 88 is a DEFECT by #116's boundary**: 87 names 653 served nodes that are wrong now and
**would** be a DEFECT, except that the run that found it also specified and *refused* the fix, so it is
entered as the measurement it is — **this is a judgment call and it is written down as one**, the
alternative reading being that 653 wrong served bytes is a DEFECT whatever the fix costs. **Board UP THREE, 44 → 47, fourth consecutive rising day — and this line was written FORTY-SIX first.** The
run computed 44 + 3 − 1 in its head against a true 44 + 3 − 0 and wrote a board count that disagreed with
its own rows by one, then caught it by running the count. **#57, committed by the run that quotes #57 two
paragraphs up:** *count against the population, never against yesterday's number* — and the arithmetic
felt perfectly safe because every term in it was true except the one that was carried.

**The 28-day breach date, recomputed by the stated method rather than carried.** Oldest-first, one closure
per day, no re-ordering: the first row still open on the day it turns 28 is **item 67 (or any of 67, 68,
69, 70, all raised 2026-11-01), taken on 2026-11-29 at exactly 28 days** — **unmoved for the fourth
consecutive restatement.** Today's zero closures do not move it, because 67 is not reached under the best
case until well after 11-29 either way; what a zero-closure day does move is every row *behind* the
DEFECT, and the DEFECT will take tomorrow's slot too.

**Rates, carried and moved by today:** raised 3 + 3 + 4 + 4 + 4 + 4 + 5 + 2 + 1 + 4 + 3 + 2 + 2 + 3 + 3 ·
closed 1 + 2 + 1 + 2 + 2 + 3 + 2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + **0** · board 44 → **47**.

### The daily record for 2026-11-07 follows, unaltered.

## Open — **FORTY-FOUR items in THREE BUCKETS, reconciled against disk 2026-11-07**

**2026-11-07 — THE HEAD WAS TAKEN AS WRITTEN, THE ROW'S HARD HALF HAS AN ANSWER FIVE TOKENS WIDE, AND
THE BOARD GAINS ITS FIRST DEFECT SINCE 10-31 OUT OF THE SAME MEASUREMENT.** The displacement line, in
one sentence: **this run took item 36 — *every name instrument this operation owns is anchored on a
Latin token* — raised 2026-10-23 as the daily's forward question, **15 days**, the oldest row in OPEN —
and displaced items 37, 38, 39, 40, 41, 44, 46, 47, 48, 50, 52, 53, 55, 56, 57, 60, 62, 63, 64, 65, 66,
67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82 and 83.** The three BLOCKED rows (45, 22,
32) were not displaced. **Thirty-second selection in thirty-three daily runs made by the rule,
thirteenth under #116.** Item 37 tied at 15 days on the same `Raised` cell and the second and last rung
— raise order — decided it. **Yesterday's board forecast this head by name and got its age wrong**,
writing *"item 36 goes tomorrow at 14"* against a true 15: a number derivable from a cell three columns
to its left, computed by hand anyway, which is this file's own reason for deleting the Age column.

**Item 36 is CLOSED at 15 days as `agents/tools/arabic_side_reach.py` (ruling #132), a MEASUREMENT and
deliberately not an assertion** — no `qa_` prefix, outside the counting glob, so **no count in
`CLAUDE.md` moved.** *The first cut the row asked for came back **ZERO**:* of 44 published pairs, **0
carry #86's `gender read from register` hand-off line and 0 carry #101's acronym line**, and all six
documents that do carry one are about the single piece drafted since those rules existed. #86 was
codified 10-04 and #101 on 10-15; the last flip was 10-13; every published hand-off predates its rule.
That is the 10-04 second amendment's limb two — *a point-of-filing rule never reconciles backward* —
fifth instance and the first on an **obligation** rather than a count. *The hard half has an answer:*
an **honorific** is a boundary the Arabic artefact supplies, exactly as an acronym is in #113, because
it cannot take a non-human subject and it commits a gender — **32 commitments across 14 of 44 AR
bodies, 10 pieces with both channels and 4 with only one.** And the direction is the finding:
**English supplies the NAME boundary and commits no gender; Arabic commits the GENDER and supplies no
name boundary**, so there is no control edition, only a control per property (#132). *The expensive
half:* the first pass reported **318 commitments across 44 of 44** by putting attribution verbs in the
same list, and every number was meaningless — `أعلنت الوزارة` is feminine because `وزارة` is, so the
probe counted ministries as women. Bucket B is printed and not deleted: **293 agreement-only tokens
across 43 of 44 bodies.**

**Count line: FORTY-FOUR open — ONE DEFECT, FORTY OPEN, THREE BLOCKED. ONE closed today** (item 36
from the OPEN head at 15 days), **THREE opened** — **85**, the board's **first DEFECT since
2026-10-31**, 32 unevidenced gender determinations on 14 **served** Arabic pieces by the #35 precedent;
**84**, our own forecast overtaken by an event, raised from a served sentence repaired this morning; and
**86**, the day's forward question. **The board is UP TWO**, for the third consecutive rising day.
Counted by reading the rows below, not by arithmetic, per #57.

**Tomorrow's head is item 85 and it is not the oldest row on the board** — a DEFECT outranks every OPEN
row whatever its age (#116), and this is the first time since the bucket was emptied on 10-31 that the
rule routes the head away from age. **In nineteen rule-made selections before 10-25 not one head was a
served defect**; this is the second since, and both came out of a measurement taken the same morning.

**The 28-day breach date, recomputed by the stated method rather than carried.** Oldest-first, one
closure per day, no re-ordering: the first row still open on the day it turns 28 is **item 67 (or any of
67, 68, 69, 70, all raised 2026-11-01), taken on 2026-11-29 at exactly 28 days** — **unmoved for the
third consecutive restatement**, which is what a real method does; today's DEFECT takes tomorrow's
closure slot and the OPEN queue therefore slips one day behind its own best case, which is the first
time the two orderings have cost each other anything.

**Rates, carried and moved by today:** raised 3 + 3 + 4 + 4 + 4 + 4 + 5 + 2 + 1 + 4 + 3 + 2 + 2 + 3 ·
closed 1 + 2 + 1 + 2 + 2 + 3 + 2 + 1 + 1 + 1 + 1 + 1 + 1 · board 42 → 44.

### The daily record for 2026-11-06 follows, unaltered.

## Open — **FORTY-TWO items in THREE BUCKETS, reconciled against disk 2026-11-06**

**2026-11-06 — THE HEAD WAS TAKEN AS WRITTEN, THE ROW'S OWN HYPOTHESIS WAS FALSIFIED IN BOTH
DIRECTIONS, AND THE SIBLING INSTRUMENT TURNED OUT TO BE THE EVIDENCE.** The displacement line, in one
sentence: **this run took item 34 — *is the measurement biased by which documents it can read?* —
raised 2026-10-22 as the daily's forward question, **15 days**, the oldest row in OPEN — and displaced
items 36, 37, 38, 39, 40, 41, 44, 46, 47, 48, 50, 52, 53, 55, 56, 57, 60, 62, 63, 64, 65, 66, 67, 68,
69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80 and 81** in OPEN, including items 80 and 81 on their
second morning. The three BLOCKED rows (45, 22, 32) were not displaced. **Thirty-first selection in
thirty-two daily runs made by the rule, twelfth under #116.** Sixth consecutive day the backlog was
reached, and **yesterday's note predicted this head by name and by age** — *"item 34 goes tomorrow at
15"* — which is the first time this board has forecast its own next head and been right.

**Item 34 is CLOSED at 15 days as `agents/tools/register_coverage.py` (ruling #130), a MEASUREMENT and
deliberately not an assertion.** The row asked for one — *report coverage per class instead of one
rate over the union* — and there is no floor here that could gate (#93), so the tool carries no `qa_`
prefix and the register stayed at **42 / 39 / 27**: the first time in six days that a new tool landed
and **not one of `CLAUDE.md`'s nine prose counts had to move.** What it found falsifies the row:
**PDFs are the BEST-archived class in the corpus (18 of 19, 94.7%) and official hosts are archived
better than the rest (85.8% against 80.9%)**, both the opposite of the row's prediction; and while the
identity instrument's **reach** is worse than the row thought — **0 of 19 PDFs comparable, HTML the
only format it reaches** — its **rate** is flat, **29.1% failing on official hosts against 31.4% on
everything else**, with 39% of the comparable population official rather than a journalism remainder.
*A reach gap is not evidence of a hidden defect population, and the instrument that CAN see a class is
the evidence about that class* — `qa_claim_registers` asks an archive about the very PDFs
`qa_citation_identity` cannot read, and answers for 18 of 19 (ruling #131).

**Count line: FORTY-TWO open — ZERO DEFECT, THIRTY-NINE OPEN, THREE BLOCKED. ONE closed today** (item
34 from the OPEN head at 15 days), **TWO opened** — **82** (the `PDF` class holds text, worse-text and
not-text, so the partition's next unit is whether a text layer is present) and **83**, the day's
forward question. **Neither is a DEFECT** by #116's boundary: both are questions and carry no count of
defective artefacts. **The board is UP ONE**, for the second consecutive day. Counted by reading the
rows below, not by arithmetic, per #57.

**The 28-day breach date, recomputed by yesterday's stated method rather than carried.** Oldest-first,
one closure per day, no re-ordering — the board's own ordering and its best case — the rows are taken
in raise order and the first row still open on the day it turns 28 is **item 67 (or any of 67, 68, 69,
70, all raised 2026-11-01), taken on 2026-11-29 at exactly 28 days.** Unmoved from yesterday's
restatement, which is what a method that is actually a method does: it did not need a new sentence of
arithmetic. Item 36 goes tomorrow at 14, and every row ahead of position 24 is still taken younger
than 28.

**Rates, carried and moved by today:** raised 3 + 3 + 4 + 4 + 4 + 4 + 5 + 2 + 1 + 4 + 3 + 2 + 2 ·
closed 1 + 2 + 1 + 2 + 2 + 3 + 2 + 1 + 1 + 1 + 1 + 1 · board 41 → 42.

### The daily record for 2026-11-05 follows, unaltered.

## Open — **FORTY-ONE items in THREE BUCKETS, reconciled against disk 2026-11-05**

**2026-11-05 — THE HEAD WAS TAKEN AS WRITTEN, ITS FIRST HALF IS A GATE, ITS SECOND HALF IS MEASURED, AND
THE BOARD'S OWN BREACH DATE TURNED OUT NOT TO BE DERIVABLE FROM THE ROWS.** The displacement line, in one
sentence: **this run took item 31 — *which of this operation's claims are checked only by the NEXT run's
goodwill?* — raised 2026-10-21 as the daily's forward question, **15 days**, the oldest row in OPEN — and
displaced items 34, 36, 37, 38, 39, 40, 41, 44, 46, 47, 48, 50, 52, 53, 55, 56, 57, 60, 62, 63, 64, 65,
66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78 and 79 in OPEN**, including items 77, 78 and 79 on
their second morning. The three BLOCKED rows (45, 22, 32) were not displaced. **Thirtieth selection in
thirty-one daily runs made by the rule, eleventh under #116.** Fifth consecutive day the backlog was
reached.

**Item 31 is CLOSED at 15 days as standing assertion 42, `qa_prior_publication` (ruling #128), and for
the thirtieth consecutive closure the specification was not the scope.** The row named a cheap first
answer — *an assertion that reads the previous deploy's conclusion and goes RED when it failed* — and
**that assertion cannot be built as named**: an assertion whose only repair path runs through the
artefact it blocks cannot be gated, because a red prior deploy is cleared by a push and a push needs a
green build, so gating it would have converted 10-20's two-day gap into a permanent one. What was built
instead gates the **register** of observations (schema, provenance re-derived from `git rev-list`,
monotonicity, the newest row verifiable) and **limb 5, the duty**: inside the daily run the register must
carry a row written by this `GITHUB_RUN_ID`, scoped by `GITHUB_WORKFLOW` so the deploy job prints SKIPPED
and can never red for the daily run's silence. The strand — commits on `main` no successful deploy has
carried, item 77's invisible number — is **printed and not asserted.** Nine proofs: five bites red, four
controls green, the fourth being bite 5's own failing tree read from the deploy job; **bite 1 was caught
by two limbs**, so provenance now declines a row the schema has already failed. **The row's wider half
was measured rather than deferred: 54 obligation sentences across 28 of 168 documents, by seven
patterns, of which exactly one became a gate today** — raised as item **80**.

**Count line: FORTY-ONE open — ZERO DEFECT, THIRTY-EIGHT OPEN, THREE BLOCKED. ONE closed today** (item
31 from the OPEN head at 15 days), **TWO opened** — **80** (the partition of the remaining 53
obligations) and **81**, the day's forward question. **Neither is a DEFECT** by #116's boundary: both are
questions and carry no count of defective artefacts. **The board is UP ONE.** Counted by reading the rows
below, not by arithmetic, per #57 for the eleventh consecutive week. **Gate count moved: 42 tools, 39
gating, 27 `postbuild` entries**, all three derived by running `qa_patch_queue` and then moved in nine
homes in `CLAUDE.md` by hand, because that file's counts are prose and prose is maintained by whoever
notices.

**And the 28-day breach date is restated rather than carried, because the carried one cannot be
re-derived.** This board has printed a breach date since #116 required one; yesterday's was **2026-11-09**
and the day before's **2026-11-10**, each moved by a sentence of arithmetic about raise and closure rates.
**Computed from the rows instead** — oldest-first, one closure per day, no re-ordering, which is the
board's own ordering and its best case — the rows are taken in raise order and the first row still open on
the day it turns 28 is **item 67 (or any of 67, 68, 69, 70, all raised 2026-11-01), taken on 2026-11-29 at
exactly 28 days.** Nothing reaches 28 before then: item 34 goes tomorrow at 15, and every row ahead of
position 24 is taken younger than 28. The carried 11-09 is not reachable by that method, nor by *the
oldest row's own age plus the days to 28* (which gives 11-19 for item 34), and no run that printed it
recorded a third method. **It is #75 again — a derivable number copied forward — one desk over from the
Age and Displaced columns that were deleted for exactly this.** The method is now written beside the
number so the next run can falsify it instead of inheriting it.

**Rates, carried and moved by today:** raised 3 + 3 + 4 + 4 + 4 + 4 + 5 + 2 + 1 + 4 + 3 + 2 · closed 1 +
2 + 1 + 2 + 2 + 3 + 2 + 1 + 1 + 1 + 1 · board 40 → 41.

### The daily record for 2026-11-04 follows, unaltered.

## Open — **FORTY items in THREE BUCKETS, reconciled against disk 2026-11-04**

**2026-11-04 — THE HEAD WAS TAKEN AS WRITTEN, THREE OF FOUR SURFACES WERE PROMOTED, AND THE FOURTH WAS
WITHDRAWN BECAUSE THE RULING'S OWN ENUMERATION WAS WRONG BY ONE.** The displacement line, in one
sentence: **this run took item 29 — *three of the four composition surfaces measured clean have no gate
behind them* — raised 2026-10-20 as the daily's forward question, **15 days**, the oldest row in OPEN —
and displaced items 31, 34, 36, 37, 38, 39, 40, 41, 44, 46, 47, 48, 50, 52, 53, 55, 56, 57, 60, 62, 63,
64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75 and 76 in OPEN, including items 73, 74 and 75 on their
second morning and item 76 on its first.** The three BLOCKED rows (45, 22, 32) were not displaced.
**Twenty-ninth selection in thirty daily runs made by the rule, tenth under #116.** Fourth consecutive
day the backlog was reached.

**Item 29 is CLOSED at 15 days, and for the twenty-ninth consecutive closure the specification was not
the scope.** The row said *promote the three*; **three were promoted and the fourth was withdrawn.**
Limb 3 — every JSON-LD `@id` **described** on more than one page agrees on every property the pages
share, the intended assembly stated in code because a consumer merges **by `@id`**, so a bare `@id` is
a reference that claims nothing: **1,206 nodes, 386 distinct, 2 described twice, 0 disagreements**, and
the 386 is item 29's own hand-verified figure now derived by a gate. Limb 4 — the two feeds are **one
subscription**: 44 + 44, 0 shared `guid`, 0 shared `link`, because a reader taking both holds one list
and a shared identity means one item silently swallows the other. Limb 5 — the **canonical namespace**:
one per served page, no two the same, and the single exemption is **positional** (#113) — `404.html`
must declare none, a property already written in `qa_reachability`'s **prose** and asserted nowhere
(#125 again). **WITHDRAWN: hreflang reciprocity is not ungated** — `qa_hreflang_clusters` clauses 1-2
have asserted it as a **build step since 2026-09-01**, so #109 named three ungated surfaces and there
were two, and a blind promotion would have put one number in a second place to drift. Proved **14 ways**,
bite first, every injection asserted to have changed the file; **bite 5 was caught twice** so a sixth
isolates the clause, because *a defect two limbs catch proves neither of them necessary*. The withdrawal
is proved both ways: silent here, **red next door**. **Ruling #127** was filed by the research function
on a different subject — a **classifier's** kernel, found twice in one day by the content and growth
functions *using* `qa_claim_registers` rather than auditing it.

**Count line: FORTY open — ZERO DEFECT, THIRTY-SEVEN OPEN, THREE BLOCKED. ONE closed today** (item 29
from the OPEN head at 15 days), **THREE opened** — **77** (the publish step's `if: success()`, so a
run that overruns banks its work and publishes none of it; patch staged), **78** (the brief template's
`code { display: block }`, repaired in one artefact on 11-02 and still in 122 independent copies), and
**79**, the day's forward question. **None is a DEFECT** by #116's boundary: 77's strand closes on this
run's push, 78's instance was repaired in the run that found it, and 79 is a question. **The board is
UP TWO.** Counted by reading the rows below, not by arithmetic, per #57 for the tenth consecutive week.
**The gate count did not move: 41 tools, 38 gating** — three limbs and two classifier states were
added and **no tool was**, so `qa_patch_queue` derives yesterday's three numbers (verified by running
it). *A run that adds a limb and reports a tool is how a count drifts.*

**So tomorrow's head is item 31 at 14 days** — *which of this operation's claims are checked only by
the NEXT run's goodwill?* — raised 2026-10-21. Founder issue **#13** is open 10 days, stated default
**2026-11-08**, **not** applied today because the date has not arrived. **Founder issue #12's default
WAS due — 2026-11-01 — was recorded by that review as "8 days, unchanged" rather than applied, and was
applied today, three days late, and named as applied**; re-asked with a new stated default of
**2026-11-11**.

**Rates, carried and moved by today:** raised 3 + 3 + 4 + 4 + 4 + 4 + 5 + 2 + 1 + 4 + 3 · closed 1 + 2
+ 1 + 2 + 2 + 3 + 2 + 1 + 1 + 1 · board 38 → 40 · the 28-day breach date **moves in to 2026-11-09**,
one day earlier than yesterday's 11-10, because a day that raises three and closes one lengthens the
queue ahead of the oldest row.

### The daily record for 2026-11-03 follows, unaltered.

## Open — **THIRTY-EIGHT items in THREE BUCKETS, reconciled against disk 2026-11-03**

**2026-11-03 — THE HEAD WAS TAKEN AS WRITTEN, AND THE ROW'S ANSWER WAS A KERNEL PER INSTRUMENT RATHER
THAN AN AUDIT OF ORACLES.** The displacement line, in one sentence: **this run took item 28 — *which of
our four render assertions rest on an oracle nobody has interrogated?* — raised 2026-10-19 as the
daily's forward question, **15 days**, the oldest row in OPEN — and displaced items 29, 31, 34, 36, 37,
38, 39, 40, 41, 44, 46, 47, 48, 50, 52, 53, 55, 56, 57, 60, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71 and
72 in OPEN, including items 71 and 72, yesterday's forward question and yesterday's growth row, on
their first morning.** The three BLOCKED rows (45, 22, 32) were not displaced. **Twenty-eighth
selection in twenty-nine daily runs made by the rule, ninth under #116.** Third consecutive day the
backlog was reached.

**Item 28 is CLOSED at 15 days, and for the twenty-eighth consecutive closure the specification was not
the scope.** The row expected an audit of four oracles; the answer is that **every ruler is a projection
and every projection has a kernel** — a set of distinct states it maps to one output — and the kernel is
a property of the *arithmetic*, so it cannot be closed by enumerating more targets. Four instruments,
four kernels: `qa_render` collapses **extent** (every raster it had ever read was 1200×900 against
documents 2,559–5,648 px tall, so the ruler held **15.9%–35.2%** of each page) and **position** (the EN
home's whole-page dark passes a 0.003 floor at 0.0053 while its own last band reads **0.0006**);
`qa_arabic_shaping` collapses **the layer below**, already interrogated, and assertion 18 is the
successor; `qa_arabic_joining` collapses **locality** — 1 of up to 49 eligible runs read, one broken
join invisible to three decimals, **128 of 511 joins broken reads 0.742 against a 0.90 threshold**;
`qa_feed_direction` collapses **dimension** (`b.top` discarded) and **its kernel is EMPTY by
construction**, the probe pinning `white-space: pre; width: 60000px` with the reason in the comment.
`qa_render` widened today, proved three ways with the control green either side, bite A red on the new
ruler and **green on the old** — which is the measurement of what the widening bought. **Ruling #126.**
*Six rulings ask what entered the measurement; none asks what the measurement cannot distinguish once
it is in.*

**Count line: THIRTY-EIGHT open — ZERO DEFECT, THIRTY-FIVE OPEN, THREE BLOCKED. ONE closed today**
(item 28 from the OPEN head at 15 days), **FOUR opened** — items **73**, **74** and **75** from the head's
own closure, and item **76** from the growth function; none is a DEFECT, and the one defect the day found
— 22 Arabic pages serving an English description in three fields each — was **fixed in the run that found
it** rather than raised, so it never became a row. **The board is UP THREE.** Counted by reading the rows
below, not by arithmetic, per #57 for the ninth consecutive week. **The gate count did not move: 41
tools, 38 gating** — an existing gate's ruler was widened and a limb added, and no tool was added, so
`qa_patch_queue` derives yesterday's three numbers (verified by running it). *A run that widens a ruler
and reports a tool is how a count drifts.*

**So tomorrow's head is item 29 at 15 days** — *three of the four composition surfaces measured clean
have no gate behind them* — raised 2026-10-20. Founder issue **#13** is open 9 days, stated default
**2026-11-08**, **not** applied today because the date has not arrived.

**Rates, carried and moved by today:** raised 3 + 3 + 4 + 4 + 4 + 4 + 5 + 2 + 1 + 4 · closed 1 + 2 + 1
+ 2 + 2 + 3 + 2 + 1 + 1 · board 35 → 38 · the 28-day breach date **moves in to 2026-11-10**, one day earlier than yesterday's
11-11, because a day that raises four and closes one lengthens the queue ahead of the oldest row.

### The daily record for 2026-11-02 follows, unaltered.

## Open — **THIRTY-FIVE items in THREE BUCKETS, reconciled against disk 2026-11-02**

**2026-11-02 — THE HEAD WAS TAKEN AS WRITTEN, AND THE ROW'S ANSWER WAS A POPULATION OF FIVE REASON-KINDS
RATHER THAN A LIST OF CHECKS.** The displacement line, in one sentence: **this run took item 26 — *which
other check's stated reason for NOT asserting something has quietly become false?* — raised 2026-10-18 at
the weekly review, **15 days**, the oldest row in OPEN — and displaced items 28, 29, 31, 34, 36, 37, 38,
39, 40, 41, 44, 46, 47, 48, 50, 52, 53, 55, 56, 57, 60, 62, 63, 64, 65, 66, 67, 68, 69 and 70 in OPEN,
including items 67 and 70, the daily's and the weekly review's own forward questions, on their first and
second mornings.** The three BLOCKED rows (45, 22, 32) were not displaced. **Twenty-seventh selection in
twenty-eight daily runs made by the rule, eighth under #116.** Second consecutive day the backlog was
reached, which is what an empty DEFECT bucket is for.

**Item 26 is CLOSED at 15 days, and for the twenty-seventh consecutive closure the specification was not
the scope.** The row asked *which check's reason has become false* and expected a list of checks; the
answer is a **partition by reason-kind**, because the kind is what tells you what would falsify it:
**A delegated to a sibling (1) · B blocked on a permission (3) · C a #93 floor above today's reality (7) ·
D an oracle limit (6) · E a missing artefact (3)**, out of 76 declining statements across 21 of the 41
instruments, 20 of which are genuine declines. **Two of the five kinds have now produced a falsified
reason, and this row found both** — kind E on 10-18 (#106) and **kind A today**:
`qa_third_party_origins` declined **1,203 declarations** on the stated ground that their *"format and
origin are `qa_consumer_surface`'s subject"*, and `qa_consumer_surface` **has no origin comparison in it at
all** — three literal-origin hits in the file, all three in prose, zero in code. The format half was true
and the origin half was false on the day it was written, 25 days ago. **Limb 2 now asserts it**, measured
at 0 of 1,203 foreign before anything was asserted so the floor sits at today's reality (#93), with
`author`/`license`/`me` exempt **by rel** and printed. **Ruling #125.** *A decline that says nothing checks
this invites somebody to check it; a decline that says the instrument next door checks this closes the
question for every reader who does not go and look.*

**Count line: THIRTY-FIVE open — ZERO DEFECT, THIRTY-TWO OPEN, THREE BLOCKED. ONE closed today** (item 26
from the OPEN head at 15 days), **TWO opened** — item **71**, the day's forward question, and item **72**, raised by
the growth function over the `related:` rail's direction. **The board is UP ONE.** Counted by reading the rows below, not by arithmetic, per #57
for the eighth consecutive week. **The gate count did not move: 41 tools, 38 gating** — an existing gate
grew a limb and no tool was added, so `qa_patch_queue` derives yesterday's three numbers, which is the
correct outcome and is stated because *a run that adds a limb and reports a tool is how a count drifts.*

**So tomorrow's head is item 28 at 14 days** — *which of our four render assertions rest on an oracle
nobody has interrogated?* — raised 2026-10-19 as the daily's forward question. Founder issue **#13** is
open 8 days, stated default **2026-11-08**, **not** applied today because the date has not arrived.

**Rates, carried and moved by today:** raised 3 + 3 + 4 + 4 + 4 + 4 + 5 + 2 + 1 · closed 1 + 2 + 1 + 2 + 2
+ 3 + 2 + 1 · board 34 → 34 · the 28-day breach date stands at **2026-11-11**, and a one-for-one day does
not move it.

### The daily record for 2026-11-01 (weekly review) follows, unaltered.

## Open — **THIRTY-FOUR items in THREE BUCKETS, reconciled against disk 2026-11-01 (weekly review)**

**2026-11-01, WEEKLY REVIEW — the board grew by FOURTEEN on the best closure week this operation has
posted, and the 28-day breach moved two weeks CLOSER.** Counted by reading the rows, per #57 for the
seventh consecutive week: **zero DEFECT, THIRTY-ONE OPEN, three BLOCKED, thirty-four total.** Two rows
raised by this review and neither is a DEFECT: **item 69** (the review's own tables ran off the page at
390px and nothing this operation owns can see it — repaired in the instance, unasserted in the class, 140
artefacts unmeasured) and **item 70** (the review's forward question, entering at OPEN's head, and the
thing ruling **#124** generates rather than closes).

**The rates, printed as #116 requires — and the guarantee is a claim about a rate, so here it is stated as
one.** Over 2026-10-26 → 2026-11-01 the board took **27 raises against 13 closures, 18 → 32** before this
review's two. Thirteen closures beats last week's ten and is the best figure on record. **And the board
still grew by fourteen, because the instruments that close rows are the instruments that raise them.**
Under oldest-first the oldest age converges on board ÷ closure rate; the board grows at 2.0/day and closes
at 1.86/day, so **the oldest item reaches 28 days on 2026-11-11** — against the **2026-11-25** this review
printed last week. *It moved two weeks closer on a week in which closures improved by 30%.* That is the
raise rate doing its job and it is not fixed by closing faster. **The candidate amendment for 2026-11-08,
recorded here rather than applied today because one ordering change per week is the lesson of #116: a
bucket for rows nobody intends to close soon** — the DEFECT/OPEN/BLOCKED partition has no way to say *this
is a measurement we chose to keep open*, so every such row ages toward a head somebody is obliged to take.

**BLOCKED re-read, which is this review's job and never the daily's.** Item **45** — its stated defect was
**dissolved rather than deferred**, and today is the date it named: *October 2026* is the issue's name and
a name does not expire, the defect was the `status: 'current'` flag, it was **ours**, it had been served
eighteen days, and it was repaired 10-31. Verified in the origin this morning: the live EN home serves
*Latest edition* and *Current edition* appears in zero files of `dist`. **The row did not enter DEFECT, and
nothing false is being served.** It stays here for the half that is genuinely his — issue #13, open 7 days,
stated default **2026-11-08**, which falls on next Sunday's review. Item **22** at 21 days — **it cost a
publication day this week**: the 10-30 run died on `error_max_turns` with 45 of 90 wall-clock minutes
unused, and the remedy has been staged since 10-11 behind a permission nobody here holds (issue #7, open 42
days). Item **32** at 8 days — unchanged, and the window is what moves: 40 registers in one copy, 28
readable today, 12 already refusing us.

**The week's bet is READ and it PASSED**, the first this operation has passed: *the DEFECT bucket is empty
by Sunday 1 November.* It is empty. Items 25, 27, 33 and 35 closed on four consecutive days, and items 51
and 58 entered and closed inside two days each. **It passed because #116 put DEFECT ahead of age**, not
because anybody tried harder — in the nineteen rule-made selections before 10-25 not one head was ever a
served defect; in the seven after, five were.

### The daily record for 2026-11-01 follows, unaltered.

## Open — **THIRTY-TWO items in THREE BUCKETS, reconciled against disk 2026-11-01**

**2026-11-01 — THE HEAD WAS TAKEN AS WRITTEN, AND WITH THE DEFECT BUCKET EMPTY THE BOARD WENT BACK TO ITS
BACKLOG FOR THE FIRST TIME IN SIX DAYS.** The displacement line, in one sentence: **this run took item 21 —
*how many of the selectors this build ships match nothing on any page we serve* — raised 2026-10-17 as the
daily's forward question, **15 days**, the oldest row in OPEN and the oldest head this board has handed out
since 2026-10-25 — and displaced items 26, 28, 29, 31, 34, 36, 37, 38, 39, 40, 41, 44, 46, 47, 48, 50, 52,
53, 55, 56, 57, 60, 61, 62 and 63 in OPEN, including item 63, yesterday's forward question, on its first
morning.** The three BLOCKED rows (45, 22, 32) are out of the ordering entirely and were not displaced.
**Twenty-sixth selection in twenty-seven daily runs made by the rule rather than by judgment, and the
seventh under #116.** Item 63 was displaced on the morning after it was raised — **the sixteenth
consecutive day a fresh forward question lost its slot.** After five days in which a young served defect
took every head (6, 2, 1, 1 days), this is what an empty DEFECT bucket is for: the backlog is reached.

**Item 21 is CLOSED at 15 days, and for the twenty-sixth consecutive closure the specification was not the
scope — this time by inverting its own answer.** The row asked for a count of dead weight and #118 had
already replaced the count with a partition. The count came back **1 of 399**: of 44 unmatched selectors,
**43 are not dead at all.** 27 are an untaken template branch — six of them the CHARTER's mandated CSS-only
wordmark fallback, which is *required* to match nothing while the SVG is present, so the honest two-bucket
answer would have called a non-negotiable residue and invited its deletion. 10 are latent element-type
rules whose removal is how item 57's class returns. 5 are superseded, all five by one cause: **markdown
cannot attach a class.** 1 is genuinely orphaned. **Standing assertion 41, `qa_selector_coverage`**, is what
the closure earned, and **ruling #123** is what the mistakes earned: two of those five were filed as
ORPHANED defects first and both were fabricated by their own proofs.

**Item 61 is CLOSED at 1 day by the content function**, and the answer is that **the ten percent stands**.
The suspected restatement from ten to fifteen percent was a unit error: 129,120 and 137,505 are regional
aggregates and the ten percent is a per-province floor, so an aggregate of 15.4% contradicts nothing. The
register that settles it was **already cited by the piece** — we had taken its investment-programme lines
and left the finish line it prints unread for 117 days.

**Count line: THIRTY-TWO open — ZERO DEFECT, TWENTY-NINE OPEN, THREE BLOCKED. TWO closed today** (item 21
from the OPEN head at 15 days, item 61 by the content function at 1 day), **FIVE opened** — item 64 (the
one genuinely orphaned selector, and an orphaned rule is an unfiled defect report about the markup), item
65 (the global layer states the thematic break three times and the pullquote twice, and only the
per-component statements reach a reader), item 66 (valence's cascade is the one no instrument of ours can
audit, and the 42-selector gap between its static and live figures *is* the runtime markup), and item 67
(**the day's forward question**), and item 68 (**`qa_font_payload` limb 2 reds intermittently on an unchanged tree**, raised by the brief function after seeing it red once and clean twice with nothing touched in between). **The board is UP THREE.** Counted by reading the rows below, not by
arithmetic, per #57 for the seventh consecutive week: zero DEFECT rows, twenty-nine OPEN rows, three
BLOCKED rows.

**Nothing raised today is a DEFECT, and that is a statement about the rows rather than about the
publication (#116 ii).** All five name coverage gaps, questions or instrument defects; every byte they
touch is currently correct, and items 64, 65 and 68 say so explicitly. **So tomorrow's head is item 26 at 15 days** —
*which other check's stated reason for NOT asserting something has quietly become false?* — raised at the
2026-10-18 weekly review, and it will be the second head running to come from the backlog. Founder issue
#13 is open 7 days, stated default **2026-11-08**, **not** applied today because the date has not arrived.

**Rates, carried and moved by today:** raised 15 + 3 + 3 + 4 + 4 + 4 + 4 + 5 · closed 10 + 1 + 2 + 1 + 2 +
2 + 3 + 2 · board 29 → 32 · the 28-day breach date stands at **2026-11-25**, and today's two-for-five does
not move it.

## Superseded count line — **TWENTY-NINE items in THREE BUCKETS, reconciled against disk 2026-10-31**

**2026-10-31 — THE HEAD WAS TAKEN AS WRITTEN, AND THE DEFECT BUCKET IS NOW EMPTY FOR THE FIRST TIME SINCE
IT WAS CREATED.** The displacement line, in one sentence: **this run took item 58 — *the one served
document still skipping a heading level*, raised 2026-10-30 by the growth function, 1 day, the only row in
the DEFECT bucket — and displaced items 59, 57, 56, 55, 53, 52, 50, 48, 47, 46, 44, 42, 21, 26, 28, 29,
31, 34, 36, 37, 38, 39, 40 and 41 in OPEN, including item 59, yesterday's forward question, on its first
morning.** The three BLOCKED rows (45, 22, 32) are out of the ordering entirely and were not displaced.
**Twenty-fifth selection in twenty-six daily runs made by the rule rather than by judgment, and the sixth
under #116.** Item 59 was displaced on the morning after it was raised — **the fifteenth consecutive day a
fresh forward question lost its slot** — and, as on 10-30, it was displaced and then answered anyway, by
hand, in the content function.

**Item 58 is CLOSED at 1 day, and the specification was not the scope for the twenty-fifth consecutive
closure — this time by a factor of more than four.** The row named **three** static `<h4>` sub-claims under
one `<h2>`. Rendered in a browser after valence's own JS has run, the document carries **thirteen**
defective heading elements in **two** sections: 3 static in `#aiPrinciples`, 1 in `#aiDetail` and **9 in
`#timingCap`** — the last ten written at runtime by template literals and therefore absent from the served
bytes a static parse reads. **Three of thirteen is 23%.** And the row's stated blocker was not on the
critical path: it is a Designer judgment only if the **tag** selects the voice, and in this file no tag
ever does — every heading rule is scoped to an id or a class and the document declares no bare heading rule
at all. Tag and selector moved together; all thirteen elements identical on every one of thirteen computed
properties, tagName alone excepted.

**Item 42 is CLOSED at 5 days**, its fourth and last sub-item taken by the content function: the Türkiye
national ledger. The document that could falsify our sentence had been published for 267 days and we had
never cited it.

**Item 59 is CLOSED at 1 day**, answered by contact rather than by argument in the same run that displaced
it — see the content function. The answer is the sharper half: the document was not new, **our search
was**, and the hedge the piece already carried is the only reason the sentence is corrected rather than
contradicted.

**Count line: TWENTY-NINE open — ZERO DEFECT, TWENTY-SIX OPEN, THREE BLOCKED. THREE closed today** (item
58 from the DEFECT head at 1 day, item 42 by the content function at 5 days, item 59 by the same function
at 1 day), **FOUR opened** — item 60 (nothing gates the envelope log's own labels, #122 clause 1), item 61
(the Türkiye surplus target may have been restated from 10% to 15% and we have not read it), item 62
(nothing gates a closed edition being labelled current, raised by the growth function in the run that
repaired it), and item 63 (**the day's forward question**). **The board is UP ONE.** Counted by reading the
rows below, not by arithmetic, per #57 for the sixth consecutive week.

**THE DEFECT BUCKET IS EMPTY, AND THAT CHANGES TOMORROW'S HEAD BY A WEEK.** Five consecutive days handed
the head to a young served defect — 6, 2, 1 days — because a defect our instruments found yesterday is by
construction newer than every question they asked last week (#116 ii). With the bucket empty the board
returns to its backlog, so **tomorrow's head is item 21 at 15 days**, the oldest head this board has handed
out since 2026-10-25. **And item 45 does NOT enter DEFECT on 2026-11-01 as it stated it would**, because
the growth function found its unit was wrong: the period label is the issue's name and names do not
expire; the defect was the `status: 'current'` flag, it had been served for eighteen days, it was ours
rather than the founder's, and it is repaired. The row stays BLOCKED for the half that genuinely is his.
Founder issue #13 is open 6 days, stated default **2026-11-08**, **not** applied today.

**Rates, carried and moved by today:** raised 15 + 3 + 3 + 4 + 4 + 4 + 4 · closed 10 + 1 + 2 + 1 + 2 + 2 +
3 · board 28 → 29 · the 28-day breach date stands at **2026-11-25**, and today's three-for-four does not
move it.

## Superseded count line — **TWENTY-EIGHT items in THREE BUCKETS, reconciled against disk 2026-10-30**

**2026-10-30 — THE HEAD WAS TAKEN AS WRITTEN, AND IT IS THE FIFTH SERVED DEFECT EVER TO TAKE ONE — AND THE
YOUNGEST HEAD THIS BOARD HAS HANDED OUT.** The displacement line, in one sentence: **this run took item 51
— *three daily briefs whose `<meta description>` describes an earlier day's finding, and nothing anywhere
reads a founder-facing artefact's `<head>`*, raised 2026-10-28 by the brief function, 2 days, the only row
in the DEFECT bucket — and displaced items 55, 54, 53, 52, 50, 48, 47, 46, 44, 42, 21, 26, 28, 29, 31, 34,
36, 37, 38, 39, 40 and 41 in OPEN, including item 55, yesterday's forward question, on its first morning.**
The three BLOCKED rows (45, 22, 32) are out of the ordering entirely and were not displaced.
**Twenty-fourth selection in twenty-five daily runs made by the rule rather than by judgment, and the fifth
under #116.** Item 55 was displaced on the morning after it was raised — **the fourteenth consecutive day a
fresh forward question lost its slot**, and today it was displaced and then answered anyway, by hand, in the
content function.

**Item 51 is CLOSED at 2 days, and the specification was not the scope for the twenty-fourth consecutive
closure — this time by a factor of three.** The row named three stale brief summaries; standing assertion
40 found **nine**, in seven collisions, because the assertable unit is not a stale sentence but a
**collision**: a description summarises one day, so two dates sharing one summary means at most one of them
describes its own day. All nine rewritten from each brief's own Today section. Limbs 1 and 3 then found an
**eleventh** instance of the derivable class the 10-28 run repaired ten of **by hand** — `2026-06-08`,
whose `<title>` and description both read 06-07 against a masthead reading *Monday 08 June · No. 11*.
**Ruling #121** is what the closure earned, and its fifth home found the assertion-discipline family's own
count reading thirty-six against its own membership list's forty.

**Item 54 is CLOSED at 1 day by the growth function**, and it was a coverage gap that turned out to hold a
defect on 89 of 135 served documents: **88 of them one element.** Every article page in both editions
jumped from the `h1` title to an `h4`. Repaired to `h2` with its selector, proved visually inert in the
browser by reconstructing the pre-change served bytes in a copy of `dist` — identical bounding boxes to the
pixel and all thirteen measured properties identical. **135 served documents, 89 skipping a level → 1**,
and that one is raised as item 58.

**Count line: TWENTY-EIGHT open — ONE DEFECT, TWENTY-FOUR OPEN, THREE BLOCKED. TWO closed today** (item 51
from the DEFECT head at 2 days, item 54 by the growth function at 1 day), **FOUR opened** — item 56 (15 of
20 weekly reviews carry no `<meta description>` at all, printed by assertion 40 rather than written by it),
item 57 (**heading order has no gate**, and the class returns the day somebody adds a heading), item 58 (the
**one** served document still skipping a level), and item 59 (**the day's forward question**). **The board is
UP TWO.**

*This paragraph first read twenty-seven, one DEFECT and twenty-three OPEN, three opened — because the
forward question was written as an addendum to the raise count instead of as one of it. It was corrected
before the commit by **counting the rows below**, which is #57 for the fifth consecutive week: the
arithmetic 26 − 2 + 3 was self-consistent and disagreed with the population. Counted after removing items
51 and 54 in the same commit as their closure, per the 10-24 rule: **one DEFECT row, twenty-four OPEN rows,
three BLOCKED rows.***

**The DEFECT bucket is ONE again and it is a different one** — item 58, raised today by the growth function
that emptied the bucket's previous occupant, which makes **tomorrow's head item 58 at 1 day**, younger
still than today's. **And item 45 enters DEFECT on 2026-11-01**, two days from now, whatever anybody here
does. Founder issue #13 is open 5 days.

**Rates, carried and moved by today:** raised 15 + 3 + 3 + 4 + 4 + 4 · closed 10 + 1 + 2 + 1 + 2 + 2 ·
board 26 → 28 · the 28-day breach date stands at **2026-11-25** and today's two-for-four does not move it.

## Superseded count line — **TWENTY-SIX items in THREE BUCKETS, reconciled against disk 2026-10-29**

**2026-10-29 — THE HEAD WAS TAKEN AS WRITTEN, AND IT IS THE FOURTH SERVED DEFECT EVER TO TAKE ONE.** The
displacement line, in one sentence: **this run took item 35 — *four published acronym expansions with no
evidence in the annotations of the piece that prints them*, raised 2026-10-23 from item 17's close, 6 days,
the oldest row in the DEFECT bucket — and displaced items 51 and 49 inside that bucket, and items 50, 48,
47, 46, 44, 42, 21, 26, 28, 29, 31, 34, 36, 37, 38, 39, 40 and 41 in OPEN, including item 50, yesterday's
forward question, on its first morning.** The three BLOCKED rows (45, 22, 32) are out of the ordering
entirely and were not displaced. **Twenty-third selection in twenty-four daily runs made by the rule rather
than by judgment, and the fourth under #116.** Item 50 was displaced on the morning after it was raised —
**the thirteenth consecutive day a fresh forward question lost its slot.**

**Item 35 is CLOSED at 6 days, and the specification was not the scope for the twenty-third consecutive
closure — this time in the other direction: the row said the repair was impossible and three of its four
cases were repairable on the day it was raised.** Both of its stated walls were re-measured this morning
and both still stand (`kjsea.knec.ac.ke` does not resolve; `moe.gov.sg` answers 202 to every client here),
and in three of the four cases **the register that PRINTS the name was a different host from the one cited
for the story, and open** — `seab.gov.sg` for PSLE, `tsctmis.org` for TMIS, `povertyactionlab.org` for
J-PAL, all three read in served text today and all three now quoted in `sources[]` in both editions. The
fourth, KJSEA, took **#101 clause 1's second branch for the first time ever on a published piece: the body
keeps the acronym**, in both editions. **Ruling #120** is what the closure earned.

**Item 49 is CLOSED at 1 day by the growth function**, and its blocker turned out to be stated against one
of three candidates rather than against the item: promoting the visible strapline needs no visually-hidden
utility class. Both front doors now carry an `<h1>`, proved visually inert in the browser before and after
— both bounding boxes identical to the pixel. **134 served documents, 2 with no top-level heading → 0.**

**Count line: TWENTY-SIX open — ONE DEFECT, TWENTY-TWO OPEN, THREE BLOCKED. TWO closed today** (item 35
from the DEFECT head at 6 days, item 49 by the growth function at 1 day), **FOUR opened** — item 52 (the
KJSEA expansion goes back in, with its evidence, when its owner becomes readable), item 53 (**this
operation owns no visually-hidden utility class**, raised by the growth function rather than invented in
passing), item 54 (heading **order** is unaudited on the other 132 served pages), item 55 (**the day's
forward question**). Counted by reading the rows below after removing items 35 and 49 in the same commit as
their closure, per the 10-24 rule: twenty-six. **The board is UP TWO.**

**And the DEFECT bucket is down to ONE for the first time since it was created on 2026-10-25** — item 51,
raised yesterday by the brief function, which makes **tomorrow's head item 51 at 2 days**, the youngest head
this board has ever handed out. Three days from now that stops being true whatever anybody does: **item 45
enters DEFECT on 2026-11-01**, when both home pages begin telling every reader that the current issue is a
month that has ended. Founder issue #13 is open 4 days.

**Rates, carried and moved by today:** raised 15 + 3 + 3 + 4 + 4 · closed 10 + 1 + 2 + 1 + 2 · board 24 →
26 · the 28-day breach date stands at **2026-11-25** and today's two-for-four does not move it back.

## Superseded count line — **TWENTY-FOUR items in THREE BUCKETS, reconciled against disk 2026-10-28**

**2026-10-28 — THE HEAD WAS TAKEN AS WRITTEN, AND IT IS THE THIRD SERVED DEFECT EVER TO TAKE ONE.** The
displacement line, in one sentence: **this run took item 33 — *three published citations misquote their own
registers and a fourth is soft-dead*, raised 2026-10-22, 6 days, the oldest row in the DEFECT bucket — and
displaced item 35 inside that bucket, and items 47, 46, 44, 42, 21, 26, 28, 29, 31, 34, 36, 37, 38, 39, 40
and 41 in OPEN, including item 47, yesterday's forward question, on its first morning.** The three BLOCKED
rows (45, 22, 32) are out of the ordering entirely and were not displaced.

**Twenty-second selection in twenty-three daily runs made by the rule rather than by judgment, and the third
under #116.** Under the retired ordering the head this morning would have been **item 21** at 11 days, and
item 33 would have waited behind six questions while four published pages said a register printed words it
did not print. **Item 47 was displaced on the morning after it was raised — the twelfth consecutive day a
fresh forward question lost its slot.**

**Item 33 is CLOSED at 6 days, and for the twenty-second consecutive closure the specification was not the
scope: it named FOUR instances and there were SIX, the fourth was never dead, and one of the six was already
sitting in the instrument's own register as `absent` on 2026-10-22.** All six repaired in both editions;
five registers re-read in served text this morning and a sixth through its own archive snapshot. **Ruling
#119** is what the repair earned: a headline is not one string, so a quotation mark promises a **named form**
of the source — and every one of the six was a form the register serves *about* the document (the URL slug
twice, the `<title>` element once, a Title Case re-casing once, a dropped conjunct once, and once a form
served by nobody at all) rather than the `<h1>` it prints. Fixing the last one's URL found the figure
underneath: **₩1 trillion and $736 million attributed to the World Bank belong to the Korea Times**, and
the near-agreement with the World Bank's own $0.74 billion is what hid the merge — not *averaged* across
registers, **paired**.

**Count line: TWENTY-FOUR open — THREE DEFECT, EIGHTEEN OPEN, THREE BLOCKED. ONE closed today** (item 33
from the DEFECT head at 6 days), **THREE opened** — item 48 (the extractor's apostrophe blind spot, 33
spans it cannot see, found by the closure itself), item 49 (**both home pages serve no `<h1>` at all**,
raised by the growth function, DEFECT at two artefacts), item 50 (**the day's forward question**) and item 51
(**three brief descriptions carry an earlier day's summary sentence**, DEFECT at three artefacts, raised by
the brief function after it repaired the derivable half of the same drift in ten files).
Counted by reading the rows below after removing item 33 in the same commit as its closure, per the 10-24
rule: twenty-four. **The board is UP THREE.**

**Rates, carried and moved by today:** raised 15 + 3 + 3 + 4 · closed 10 + 1 + 2 + 1 · board 21 → 24 · the
28-day breach date stands at **2026-11-25** and today's one-for-four does not move it back.

**And a row changes bucket by itself in four days:** item 45 is BLOCKED today and **enters DEFECT on
2026-11-01**, when both home pages begin telling every reader that the current issue is a month that has
ended. Nothing anybody here does changes that; founder issue #13 is open 3 days.

## Superseded count line — **TWENTY-ONE items in THREE BUCKETS, reconciled against disk 2026-10-27**

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

### DEFECT — **ONE item.** The head comes from here while any row stands (#116).

*Emptied again 2026-11-10 by the closure of item 85, after three days occupied. **The row closed on its
population and not on its count, and the two moved in opposite directions:** `arabic_side_reach` read
**32** tokens when the row was raised, **39** this morning and **54** at the close, because the
provenance #86 clause 2 requires is itself an Arabic honorific gender commitment inside the annotation
the detector reads. What closed is *determinations with no provenance on file*, now **0 of 19** — four
evidenced by their own register, eight declared as this edition's own with the settling fetch named,
**zero wrong.** Ruling #138. The emptiness is a statement about the board, not about the corpus (#116
ii), and it is worth saying twice in two weeks.*

*RE-OCCUPIED THE SAME AFTERNOON, by item 96, and the two closures are the same lesson from opposite
ends. Item 85 closed because its count was the wrong unit and rose while the work was done; item 96
opens because a question this board has carried since 2026-09-06 **acquired a count** — 47 served
sitemap entries wrong now, on every deploy — and #116's boundary is the artefact's and not a judgment.
The bucket was empty for about one hour.*

| # | Item | Owner | Raised | Verified how | Blocks |
|---|---|---|---|---|---|
| 96 | **47 served sitemap entries carry a `<lastmod>` with nothing behind them, on every deploy, and the change signal is 28% precise** — measured today by `qa_served_manifest --check` against the bytes the origin is actually serving: of 138 pages compared, **18** changed their rendered content and moved their date (correct), **47** moved their date with byte-identical content, **0** changed silently. The JSON-LD half has no complement to hide in: **100% of the 90 article pages claim a `dateModified` later than their `datePublished`, and 78 of them claim 2026-11-09**, which is the day the site CHROME changed; `2026-05-25-bo-teacher-chalk` tells every machine that reads it it was modified that day and its own bytes have not moved since May. **Cause:** `web/src/lib/sitemapLastmod.mjs` resolves `max(chrome, newest file under web/src/content/)`, which is provenance-derived and honest about being so. **This is the 2026-09-06 forward question, 65 days old, and it is entered as a DEFECT rather than a question because it has finally acquired a count.** The 09-06 review ruled it *a design question for the Web Developer, not a defect* — correctly, because the honest instrument did not exist; `qa_served_manifest` was built 2026-10-06 and the origin has carried a baseline manifest ever since. **The ask: an output-bounded date** — per-URL content hash across deploys, which the served manifest already computes — so a page's date moves when its own served bytes move and not when a template it depends on does. **The cost of not doing it is paid on the REAL changes**: a crawler that finds a `lastmod` unreliable stops believing it, so today's 18 genuine amendments are indistinguishable from outside from the 47 that are not. Measurable after the fix by the same instrument without anybody's permission: precision from **18 of 65 toward 18 of 18**. Full read in `agents/growth/2026-11-10-lastmod-precision-the-one-signal-we-own.md`. **Do this BEFORE any reader-facing amended-on notice** (named in that note and deliberately not built): a visible notice on top of a 28%-precise signal publishes the noise to readers too. | **[WD]** | **2026-11-10** | `qa_served_manifest --check` against the live origin, served bytes to served bytes, after the guard repair that made the comparison supportable | **47 served entries wrong NOW, every deploy** — and the 18 true signals are hidden among them |

*Emptied 2026-10-31 by the closure of item 58 — the first time this bucket has stood at zero since #116
created it on 2026-10-25. It does not mean the corpus is clean. It means no row currently NAMES a count of
served or founder-facing artefacts that are wrong, which is a statement about the board rather than about
the publication (#116 ii, read in the other direction).*

*The boundary is the artefact's, not a judgment: each row names **N > 0** artefacts, currently served or
currently founder-facing, that are **wrong, broken or unevidenced**. A question carries no such count,
because the count is what it would measure. Ordered by age; ages are `today − Raised` and are not written
down (#116).*

### OPEN — **FIFTY items.** Ordered by age. The forward question enters at this block's head.

*Rows 91, 92 and 93 were physically appended to the DEFECT table by the 2026-11-09 run and carried the
word OPEN in their `Blocks` cell instead of a bucket. **Moved here 2026-11-10 by the run that noticed.**
It changed no head — the oldest DEFECT was still item 85 either way — but a board whose buckets are
correct in its prose and wrong in its tables is one careless read away from handing out the wrong head,
and the prose is not what #116 ordered.*

*Questions, coverage gaps and face judgments. The bytes are right and the rows say so. Reached only when
the DEFECT block is empty.*

| # | Item | Owner | Raised | Verified how | Blocks |
|---|---|---|---|---|---|
| 97 | **A founder-facing artefact can be structurally malformed and pass every check we own, because the one that opens it in a browser asserts that content RENDERS and never that the document is WELL-FORMED** — found today by the ordinary act of copying the brief template forward, not by any instrument. Brief 125 carried a **duplicated `</style></head><body><main class="container">` line**: two `<main>` elements with one never closed, a second `<body>`, and a `</style>` with no opener. The founder's page rendered inside **two nested `.container` wrappers**, so its column was narrower than every other brief, and the document was invalid. `qa_artefact_render` rendered it at 1280px and asserted both its limbs green — correctly, because **a doubled container is still a container and a narrower column is not a broken page** — and `qa_brief_head` read its `<title>` and description and found both right. **This is 2026-08-16 inverted**: that day the template LOST its wrapper and two briefs rendered edge to edge for two days; this time it GAINED one. **The ask: a well-formedness limb over the 128 briefs and 21 reviews** — tag balance, exactly one `<body>`, exactly one top-level `<main>`, no nested `.container`, `<style>` open/close parity. Offline, no browser, and the whole corpus is on disk. **Both operands exist and nothing compares them** (#89's movement). Brief 125 was repaired in the same run that found it, so no founder-facing artefact is wrong **now** and this is OPEN rather than a DEFECT — but it stood for one day and nothing could have told us. | **[AE]** | **2026-11-10** | Observed directly: `<main>` nesting depth 2 with 1 unclosed at EOF, 2 `<body>`, 1 `<style>` against 2 `</style>`; both existing instruments green on the same file | nothing red — and nothing CAN go red, which is the item |
| 94 | **Nothing this operation owns can tell a claim about the WORLD from a claim about this operation's own METHOD, and the second kind is now served to readers on nine pieces** — the day's forward question, entered at this block's head, and it is a measurement rather than a worry. The twenty-two provenance appends written today under #86 clause 2, plus eight on 11-08, were read by `arabic_side_reach` as **+22 new gender-committing tokens** (32 → 39 → 54) while the population they record fell to zero unevidenced. The tool was not wrong about the bytes: *«الدكتورة» هنا تحديدٌ تملكه هذه الطبعةُ وحدها* is, to any parse, an honorific beside a name. **The class is wider than one instrument** — the gender provenance, #137's byte-length and title observations, the `annotation == sentence` assurances and the archival dispositions all live inside `sources[]`, in the same field and the same grammar as the claims about somebody else's document that `sources[]` exists to carry. **The ask, in two parts, and the second is not a parse.** (1) Measure it: how many bytes of served annotation across the 90 files are about our own process rather than about a register, and is there a boundary the artefact itself supplies in #113's sense, or is this a class with no exact edge? (2) Then the face judgment no measurement can make: a reader opening the Ghana piece's Arabic annotation now reads a sentence about how this desk settled a gender. **Is that a feature of a publication that stands on named primary sources read in served text, or operational exhaust in reader-facing bytes?** Nobody has decided and today added twenty-two instances without deciding. | **[AE]** + Editor | **2026-11-10** (the daily's forward question) | Observed directly: the count moved 32 → 54 in the direction opposite to the work, measured three times in one run | nothing red — and nothing CAN go red, which is half the item |
| 95 | **`arabic_side_reach` has two unit defects, both found by taking the row it was built to serve, and both are #123's shape — a probe wider than its subject** — raised from item 85's closure rather than carried forward as a note. **(a) It reads body PLUS frontmatter**, so the provenance #86 clause 2 *mandates* is counted as a fresh determination needing provenance; the count therefore rises as the defect is repaired, 32 → 39 → 54 across two runs, and the row it serves could never have closed on it. **(b) Bucket A's stated boundary is *an honorific states that the next token names a person*, and an eponymous institution defeats it**: `2026-06-10-rak-iqra-arabic-diglossia`'s الشيخ sits inside **مؤسسة الشيخ سعود بن صقر القاسمي**, the Foundation's own proper name, and was counted as a gender claim about a living person. One of 20 candidates was a false positive, so the honest population was **19**. **The ask: give the file a unit it can defend** — count *determinations about persons*, not honorific tokens; exclude a honorific that falls inside a named institution; and either exclude annotation prose that carries its own provenance clause or report body and annotation as two populations rather than one sum. **Not a DEFECT by #116's boundary**: no served byte is wrong, the instrument's own output is, and the file is a measurement that gates nothing. | **[AE]** | **2026-11-10** (from item 85's closure) | Measured three times in one run against the same corpus, and against a per-person hand count of 19 | nothing red — the file carries no `qa_` prefix and fails no build |
| 93 | **No gate in this repository can tell a Madār URL from anybody else's** — the day's forward question, and ruling #137's own unasserted half. Four instruments touch a `sources[]` entry (`qa_sources_alive`, `qa_claim_registers`, `qa_citation_identity`, `qa_annotation_figures`) and **all four are built on the premise that the register belongs to someone else**: their host answers, their archive kept a copy, their bytes still carry our quotation. Turn the citation inward and all four premises are false at once and not one of them asks whether they are. #137 clauses 1 (no byte length in a self-citation) and 2 (a Madār title is read off the page) are therefore **prose nothing can fail** — which is what #71 was before `qa_prior_publication`. Enumerate every `sources[]` entry whose `url` is a Madār URL and ask of each whether any gate treats it differently in any respect. Population is **2 today and growing**, singles making follow-ups cheaper. **NARROWED 2026-11-10, and the premise was wrong in the useful direction: the answer is not *no instrument*, it is *exactly one*.** `qa_annotation_figures` does not contain the string `education3881`; `qa_sources_alive` and `qa_citation_identity` contain it once each, inside the User-Agent they send. But `qa_claim_registers` holds `OUR_ORIGIN` as a live branch of `classify()`, scoring our own origin `ours-git-archived` rather than `live-only` — **built 2026-11-04 under ruling #127, five days BEFORE the instance arrived**, with its own docstring saying that is the only version of the change which is not a correction, and today's build shows it firing (`ours-git-archived 2`). **So the remaining ask is propagation, not invention:** carry that notion into the other three, where #137 clauses 1 and 2 would then have something that can fail them. *A coverage question that assumes zero coverage mis-specifies the fix even when it correctly finds the hole.* | **[AE]** | **2026-11-09** | the two defects #137 was earned on were caught by luck of scope — the title only because a title happened to be a quoted identity token, the byte length by nothing at all | nothing red — and today's test found that one instrument ALREADY distinguishes it, which is the narrowing |
| 92 | **`/editions/`'s standing block now holds two populations under one heading with nothing distinguishing them** — a published single and a standalone interactive instrument, and the Arabic side already carries a per-row note explaining that VALENCE's text is English. A per-row exception is where a bucket set starts going wrong (#57 / #70). Reads fine at one of each; at five singles and one instrument it reads as a miscellany. **Deliberately not solved at a population of two**, named so the next run sees it coming. | **[WD]** | **2026-11-09** | growth function, from the ship that created the first single | nothing red — a legibility judgment at a population of two |
| 91 | **The 2026-11-08 weekly review has no artefact** — the run died at `error_max_turns` (181 turns, 35 min, 55 of 90 unspent, the first WEEKLY ever to hit the cap) after four of five function commits were on `origin`. Four functions' work is in the repository; the **fifth, the weekly review HTML the founder opens, was never written**, so `agents/reviews/` jumps 2026-11-01 → 2026-11-15. The week's findings are recoverable from the four commit messages and the files they carry. Decide at the 11-15 review whether to reconstruct the missing artefact from them or to record the absence and move on — **and note that recording an absence is what ruling #135 and item 90 are about**, one register over. | Manager | **2026-11-09** | `run_envelope --observe-turns` recovered the run's own `num_turns` and `subtype` from its Actions log | nothing red — the artefact does not exist, which is the item |
| 90 | **A consolidation section's own ABSENCE is the one thing in this register nothing can see, because it looks exactly like a week with no review** — and it has now happened twice, 2026-09-27 and 2026-11-01. Both reviews consolidated well; neither wrote its `## Consolidation — <date>` section, so the `Last consolidation:` line at the head of `agents/guidebook/INDEX.md` read a stale date for **fourteen days** the second time, and both times **the items the review recorded as owed forward had no successor section to be copied into**: in 2026-09-27's case §0's eight-axes debt was carried a third time in silence, and in 2026-11-01's the archive roll due on 11-08 was recorded **only in that review's own HTML** and was found by reading last week's review rather than this register. #135 closed the count-against-count gap in `qa_register_shape` this morning; **this is the other half and it is cheaper**, because both operands are on disk and derivable: the newest `agents/reviews/*-weekly-review.html` filename against the date in INDEX.md's `Last consolidation:` line, with a section heading present for that date. **The ask: assert that the register names its own most recent consolidation.** Two limbs, both offline — the dates agree, and a `## Consolidation — <that date>` heading exists. **Deliberately NOT built by the run that found it**, because the run writing this week's section is the run whose artefact the limb would judge, and #135's own lesson is that a check author who is also the subject cannot see the gap. | **[AE]** | **2026-11-08** (the weekly review) | Observed directly: the header read 2026-10-25 on arrival, fourteen days stale, with `qa_register_shape` green across every build in that window | nothing red — and nothing CAN go red, which is the item |
| 89 | **Every provenance claim this run wrote into an Arabic annotation is invisible to the one instrument that could check it, so the run had to BE the instrument** — the day's forward question, entered at this block's head per the one-queue rule, and it is not a hypothesis: it happened this morning. `qa_citation_identity` turned the build red over **two** English quotations and said nothing about the **four Arabic annotations carrying the same register strings in the same hour**, because the Arabic side writes them inside `‏…‏` directional marks rather than quotation marks and #112 already declines **128 of 134** Arabic tokens by construction. So the edition #86 and #101 make the FORCED channel on a name is the edition whose evidence **nothing gates**. **The ask: of the 348 shared annotations across 44 pairs, how many carry a verbatim register string on the Arabic side that no instrument has ever compared against the register's bytes — and is the gap a property of Arabic SCRIPT, of our QUOTATION CONVENTION, or of our own MARKUP?** The three have different fixes and only one is hard. First cut needs no oracle: count Latin-script runs of ≥12 characters inside Arabic annotation blocks and compare that population against the tokens `qa_citation_identity` actually asks about. Second limb is #93's — **if the answer is our quotation convention, the fix is one house rule and the instrument already works**, which would make this the cheapest member of the #112 family and the reason it has stood seventeen days. | **[AE]** + Arabic Editor | **2026-11-08** (the daily's forward question) | Observed directly: two EN tokens gated, four AR provenance clauses ungated, same registers, same hour | nothing red — the gap is that nothing CAN go red |
| 88 | **Ruling #96 and the publish-gate rule pull in opposite directions whenever the content function changes a served byte, and the conflict has now been resolved by force on two consecutive days** — #96 says *commit and push at the close of every standing function, never once at the end*, because in this cadence no disk survives the run and a staged block is a lost block; the publish-gate rule says *run the gate in writing before committing anything editorial.* On 11-07 and again on 11-08 the gate was written **after** the content commit, and #96 won because its failure mode costs the whole day while the gate's costs a re-run. **Nothing has been caught by the wrong order on either day** — which is the item: a conflict that is free on the day it is noticed is the one still unresolved on the day it is not. Candidate shapes, none chosen: a per-function gate fragment written and committed *with* its function; or the gate scoped to the flag change it was written for (#18) and explicitly NOT to an annotation repair, which is what both days actually were. The second is cheaper and may be the honest reading of the original rule. | Manager + Editor | **2026-11-08** (from the publish gate, second consecutive day) | Both days' gate files are timestamped after their content commits in `git log` | **zero NOW** — no defect has been shipped by the ordering; the exposure is a day on which one would be |
| 87 | **This publication serves a machine-readable citation graph of 704 nodes and not one of them names a document** — 88 article pages each emit a JSON-LD `Article` node carrying a `citation` array; all 704 `CreativeWork` nodes have `@type`, `name` and `url`, and **`name` is our whole annotation about the document rather than the document's name**: median **262** characters, mean 414, longest **3,237**, and **653 of 704 — 92.8% — over the 110 characters at which a consumer stops showing a title.** A machine is told a Singapore press release is titled with our commentary on why we opened it. This is the 2026-08-18 share-card defect one surface over and worse: a promise that resolves, renders and **says the wrong thing** cannot 404, so nothing can notice. **The one-line fix was measured and REFUSED** — cutting at the first ` (` improves 503 and **damages 163 (23.2%)**, because in *The Straits Times (Tang Yi Qing)* the first parenthesis is a byline; a heuristic right 71% of the time on a served field is 11-01's `hr.rule` fabricated defect repeated. **The work partitions on a boundary the artefact supplies: 452 of 704 (64.2%) carry a quoted document title**, so bucket 1 is mechanical and already checkable (`qa_citation_identity` fetches exactly those strings, 100 registers confirmed today) and bucket 2 (252) needs an editorial `sources[].name` field, not a parser. **Buckets separable — bucket 1 can land alone.** | **[WD]** + Growth | **2026-11-08** (growth) | Counted over `dist` this morning: 704 nodes, length distribution, 452 quoted, 163 damaged by the naive fix | nothing red — `qa_jsonld` is green because every promise parses and dereferences; it has never asked whether a value means what the key says |
| 86 | **Every claim this publication makes about what somebody ELSE will do next is unverifiable by every instrument we own, and today one of them had been false for four months** — the day's forward question, entered at this block's head per the one-queue rule, and **it is not a hypothesis: it was found this morning in a served pair.** `2026-05-26-bahrain-bqa-public-grades` closed, in both editions, with *"The 2025–2026 report will appear in roughly twelve months"* — published 2026-05-26, pointing at roughly May 2027 — and the Authority has served that report on its Arabic publications index since an upload path dated **July 2026** (HTTP 200, 2,635,898 bytes, `Last-Modified` 4 October 2026, not linked from the English index). **No byte changed on either side and the date the sentence names has NOT arrived**, so #117's *arrived date* trigger cannot fire: what arrived early is the **event**. Every instrument we own compares a document against a document that exists; a claim about a document that does not exist yet has nothing to compare and no calendar to wait for. **The ask: how many sentences in the served corpus make a claim about what a third party will publish or do, and for each, what single fetch would settle whether it is still true?** First cut needs no oracle — `will appear`, `is due`, `expected`, `by <year>`, `in roughly` over 44 bodies and 44 annotation blocks. **The Arabic half must report its own blindness** (#117 clause 4: `سـ` is a bound prefix homographic with the first letter of ordinary nouns, and today's Arabic instance was found by a human reading for a quotation). Second limb is #93's: the output is a **reading list ordered by how cheap the settling fetch is**, not an assertion, because a claim about the future cannot be gated by anything except going and looking. | **[AE]** + Editor | **2026-11-07** (the daily's forward question) | One instance found today in a served pair and repaired; the population is unmeasured | nothing red — no instrument can turn it red, which is the item |
| 84 | **Our own forecast about somebody else's publishing schedule was overtaken by the event, and the class has no trigger** — raised by the content function in the run that repaired the instance. Both served editions of `2026-05-26-bahrain-bqa-public-grades` forecast the 2025–2026 report *in roughly twelve months*; it has existed since July 2026. **Repaired in both editions today**, with the register's dated state (upload path July 2026, `Last-Modified` 4 October 2026, English index does not link it) in place of a new estimate, per #117's own precedent of repairing in the run that finds it. **This row is the population, not the instance** — it was found because a composer opened the predecessor's Arabic page to copy a quotation, which is not a method. **It is OPEN and not DEFECT because the instance is repaired and the population is unmeasured**: a row must name N > 0 artefacts that are wrong *now*, and after this morning the count of known-wrong forecasts is zero. The distinction from item 86 is deliberate and is the two-rows-one-finding shape this board has used before: 86 asks for the **enumeration**, this asks for the **re-reads** once the enumeration exists, because each one costs a fetch of somebody else's register and they are not interchangeable. | Editor + **[AE]** | **2026-11-07** (content, from a served sentence) | One instance confirmed by probe and repaired; the forecast's own date had not arrived, which is why no instrument could see it | **zero NOW** — repaired in the run that found it; the class is unasserted and unmeasured |
| 83 | **Every instrument this operation owns measures a document it can FETCH, and the artefacts a reader is actually handed are rendered by machines we do not own** — the day's forward question, entered at this block's head per the one-queue rule, and it is item 34's own class boundary turned outward. Today's measurement partitioned 354 registers by format and publisher and found the identity instrument reaches **only HTML** — and every boundary it used (`ctype`, a host suffix, a `/ToUnicode` table) is a property of **the response we received.** Three of this publication's own outbound promises are never fetched by us at all: **an og card rendered by a social consumer, a feed item rendered by a reader, and a title-and-description pair rendered by a search engine.** #117's rule asserts the og card's *format*; `qa_feed_direction` probes one item in a geometry we built (item 75); and yesterday's growth function wrote **133 distinct descriptions whose rendering nobody has ever seen.** The ask: of the artefacts handed to a machine we do not own, how many has anybody **ever** observed in the consumer's own rendering — by any means, including a human looking once — and what is the honest answer for the ones nobody here can? First cut needs no oracle and no credential: enumerate the handover points and record observed/never-observed per point. Second limb is #93's — for the unobservable ones the instrument is **a written statement of what is unverifiable**, because measuring our side of a handover and reporting it as the handover is the 2026-08-18 defect, 83 days of share cards that resolved perfectly and rendered nowhere. | **[AE]** + Growth | **2026-11-06** (the daily's forward question) | Named from today's own class boundaries, every one of which is a property of a response we received | nothing red — no instrument can turn it red, which is the item |
| 82 | **The `PDF` class holds text, worse-text and not-text, and the register records which nowhere** — raised by item 34's closure, measured on one publisher's own series within twelve hours of the partition being built. Item 34's answer partitions by format and `PDF` is one cell; this morning's content function read **three documents from one publisher, one series, one format**, and they are not one class: the BQA 24–25 **Arabic** report carries **17** `/ToUnicode` CMaps and **207** cmap glyphs and extracts to 63,344 characters; the 24–25 **English** report — *the edition this publication cites* — carries **80** cmap glyphs and drops whole words and figures, so the complete four-grade distribution had to be recovered from the Arabic edition; and the AY **2025–2026** report carries **zero** `/ToUnicode` CMaps, reducing 39 pages to 3,565 characters of unanchored numerals. **A PDF with no text layer is not a document our instruments decline; it is a document they cannot know they declined**, because `ctype` says `application/pdf` either way. The ask is one field — *text layer present* — on each PDF register, at one fetch per URL, which also makes item 34's `PDF 0 of 19 comparable` separable into *could not be read* and *was never readable by anyone*. Population: **19 PDF registers in `citation-identity`, 14 of them on a host the party rule calls official.** | **[AE]** | **2026-11-06** (from item 34's close) | Three documents measured by hand this morning, same publisher and series, `/ToUnicode` counts read out of the files | nothing red — it is a field the registers do not carry, not a byte that is wrong |
| 81 | **Every citation instrument this operation owns treats a URL as THE DOCUMENT, and a register that publishes in two languages is two documents that can disagree** — the day's forward question, entered at this block's head per the one-queue rule, and **it is not a hypothesis: the content function was bitten by it this morning.** `qa_sources_alive` asks whether a URL answers; `qa_claim_registers` whether anybody can re-open it; `qa_citation_identity` whether our quoted string is still in its bytes; `qa_annotation_figures` compares its numerals against our own body. **All four fetch one rendering of one URL.** `data.gov.bh` serves the Bahrain review table **per language from one dataset** — 1,022 identical rows either way, and the Arabic column yields **248 / 245 / 75** school names where the English yields **245 / 242 / 76**, with one December 2024 verdict attached to the girls' school in English and the boys' school in Arabic. **Every instrument above would have been green on both, because each was asked about a different URL and each answer was true.** The ask: which of the 353 cited registers publish the same document in more than one language, and on how many has this publication ever read only one side? First cut needs no new oracle — a language marker in a URL (`lang=`, `/ar/`, `-EN.pdf`) is a string, and both registers already store an `observed` date. Second limb is #86 pointed **outward**: our two editions are a second channel on our annotations, and a source's two editions are a second channel on the source — one we have never used once. **BOTH LIMBS ANSWERED 2026-11-06, the first by the growth function and the second by the content function, and the row is NARROWED rather than closed.** *Limb 1, the population:* the two editions cite **the same 345 of 353 URLs** — 4 EN-only, 4 AR-only — so the independence #86 and #101 buy on the prose has never once extended to the source; **47 URLs carry a language marker (41 `en`, 1 `EN`, 4 `ar`, 1 `fr`)**, 42 had an Arabic variant derived mechanically and probed, **10 answered 200/206 and only FOUR are a genuinely different Arabic rendering** (letter share 0.63–0.96 against 0.00), four being the marker changing the chrome not the document (two byte-identical PDFs under an `/ar/` path, two pages still English) and two needing a reader. **So the string cut's false-positive rate among URLs that ANSWER is 6 in 10** — a status code is not a document and a path segment is not a language, which is #112's soft-200 met for the third time in one run. *Limb 2, the second channel used for the first time:* the content function read both language editions of the BQA's 24–25 performance report and **they AGREE in every figure checked**, so one disagreement (`data.gov.bh`) plus one agreement is not a rate — **and the second channel paid anyway, by recovering text our own extraction of the English edition had dropped.** Measured in `agents/growth/2026-11-06-the-arabic-edition-cites-english-documents.md` and `content-drafts/recon/2026-11-06-bahrain-bqa-arabic-register-second-read.md`. **What is left of the row, and it is all that is left:** three of the four confirmed renderings have **not** been read for the claim their annotation attributes, so they may not be substituted (#131 — a different rendering is a different document until somebody reads it), and the fourth is `gov.om`'s authority page, which is the surface ruling **#102** was filed on. One read per run, Arabic Editor's gate, `gov.om` to the Editor with #102 attached. | **[AE]** + Editor + Arabic Editor | **2026-11-05** (the daily's forward question, from the content function) | Measured this morning on both exports of one dataset, row order verified identical on cycle and date | nothing red — every one of the four instruments is green on a register that disagrees with itself |
| 80 | **Fifty-three of the fifty-four obligations this operation writes down are still checked by nothing but the next run's goodwill, and the open job is the PARTITION rather than the gating** — raised by item 31's closure, which measured the population the row had only named. Seven patterns over all 168 documents in `CLAUDE.md`, `agents/RUNBOOK.md`, `agents/CHARTER.md` and `agents/guidebook/**`: *the next / following run* **21**, *the hand-off carries* **13**, *at the close of every standing function* **6**, *the run that fixes / writes / moves / notices* **5**, *every brief carries / names / reads* **4**, *every run owes / reads / logs / states* **3**, *re-read / reconciled at the weekly review* **2** — **54 across 28 of 168 documents, and exactly one of them became a gate on 2026-11-05.** The job is not *gate them all*: patterns 2 and 5 name a string in an artefact that exists and are cheap (the brief's deploy line is now a gate; the hand-off checkboxes are not), pattern 1 mostly names a judgment no instrument can evaluate, and pattern 7 names a **cadence**, which is #107's original defect — a condition true for 33 days and evaluated by nobody. **Partition the 53 into checkable / judgment / cadence before anybody writes a line of Python**, and report the fraction, because a count of obligations is not a count of gaps. | **[AE]** | **2026-11-05** (from item 31's close) | Counted today by seven regexes over 168 files; the patterns and the per-pattern counts are in `agents/logs/qa-2026-11-05.md` §2a | nothing red — it is the item that asks how much of this operation's own written discipline is enforced by anything |
| 79 | **Every brief holds its own private copy of the brief template, and nothing has ever compared the copies** — the day's forward question, entered at this block's head per the one-queue rule, and **item 78 is its first measured instance.** There is no template: there is a **122-long chain of copies**, each made from the one before by a run that read it and pasted it, so a repair enters the chain where it was made and reaches **forward only** — and a repair made in a brief the next run did not copy from reaches nothing. The ask: **how many distinct copies of the brief `<style>` block exist across 122 briefs and 21 reviews, and which repairs reached only one link?** Measurable today with no new oracle — hash each artefact's `<style>` block and diff the distinct ones. **Why no instrument can see it:** `qa_artefact_render` renders each artefact *independently* and asks whether that one is sound, `qa_brief_head` reads each `<head>` *independently*, and `qa_selector_coverage` reads the publication's stylesheet while the briefs are not in `dist`. Every founder-facing instrument we own is scoped to **one artefact** and this is a property of **the set** — which is assertion 34's own subject one corpus over. | **[AE]** | **2026-11-04** (the daily's forward question) | Named from item 78's cause, which is a repair that reached one link in a chain nobody has counted | nothing red — it asks how far every past repair to this artefact family actually travelled |
| 78 | **`.push-block code { display: block; white-space: pre }` is in all 122 briefs' independent copies of the style block, and it splits any sentence that carries an inline code span in a lede** — raised by the brief function in the run that reproduced it. On **2026-11-02** a commit hash in a `<code>` inside the lede rendered as a full-width dark block and broke a sentence mid-clause; that run removed **its** `<code>` and re-rendered, **and left the rule.** Today's lede wrote `<code>main</code>` into a sentence and would have split it the same way — found by reading the brief's own stylesheet for rules targeting `code`, not by any gate. *A correction reaches the instance it was sent to; only an instrument reaches the class* (#113), second instance two days later in the same artefact family. **The rule is residue**: it was written for the founder push block, which no longer carries a command. The taking is to delete it, or scope it to a `pre`, in whatever the answer to item 79 says *the template* is. Repaired in brief 120 by removing the span, which is the instance again and is said so. | **[WD]** | **2026-11-04** (brief function, from reproducing the 11-02 defect) | Read the brief's own `<style>` for rules whose selector matches `code`; one rule, `display: block` | nothing red — the served publication does not carry this rule, only the founder-facing artefacts do |
| 77 | **The publish step is conditional on the run's own conclusion, so a run that overruns banks its work and publishes NONE of it** — raised by the state verification that opened the day, and it is **#122's corollary measured a second time** rather than a new finding. `madar-daily.yml`'s last step carries `if: success()`. #96 banks the work at the close of every function and it does; the deploy is dispatched only by a run that *finishes*. **2026-10-30**: `error_max_turns` at 181, five of six commits landed, no deploy, strand closed next morning by the 10-31 run. **2026-11-03**: `error_max_turns` at 181, four of five commits landed and pushed, **no deploy, and the origin served the 11-02 build for two days** with four commits on `main`. **The self-healing is accidental** — the strand lasts until the next run happens to succeed, and is unbounded if runs fail consecutively; **and it is invisible in `git log`** by construction. The step's own body already compares `origin/main` before and after and dispatches only if the origin moved, so the `if:` adds exactly one behaviour and it is not a safety one: the deploy's safety is the deploy's own gates. **One-word patch staged** at `agents/patches/2026-11-04-publish-step-must-not-depend-on-the-run.md` with its three proof cases; it needs the `workflows` permission of **issue #7**, so it is OPEN rather than BLOCKED only because the patch is written and the recovery is documented. | **[WD]** + issue #7 | **2026-11-04** (state verification) | Read from the raw log per #96(d): `error_max_turns`, `num_turns` 181, 36.4 of 90 minutes; `publish what the run pushed` skipped; zero deploy runs between 11-02 13:00Z and today | nothing red NOW — this run's push carries both days, which is the recovery and not the design |
| 76 | **44 of 134 served pages describe themselves IDENTICALLY, and the wrong-language half of it was fixed today while the uniqueness half was not** — raised by the growth function from a measurement over the built corpus. Every `<title>` is distinct (134 of 134); **every `<meta name="description">` was not: 91 distinct values over 134 pages, with one value on 44 of them** — both homes, both browse indexes, all 16 region pages, all 16 topic pages, 8 Arabic country pages and both editions indexes, because none of those templates passes a `description` and `Base.astro` held a single default. **22 of the 44 were Arabic pages serving ENGLISH**, in three fields each — `description`, `og:description`, `twitter:description` — 66 declarations including the Arabic edition's own front door; that is the 2026-09-13 wrong-language class in a field **neither `qa_a11y_lang` nor `qa_ar_language` enumerates**, because both read text a reader can SEE and a `<meta>` content attribute is served without ever being painted (#121's shape on the publication instead of the brief). **Closed today with no new prose:** both feeds already carried this publication's self-description as a composed, Arabic-Editor-gated pair, so the pages were given the same pair — and the English default turned out to be the feed's sentence with its last clause, *A research instrument, not a magazine*, cut off. **NARROWED 2026-11-05 to FOUR PAGES by the growth function, and the Arabic half of the repair is the finding.** All 32 facet pages and both hubs now derive their own description from the collection at build time — **133 distinct over 135 served pages, against 91 over 134 before**, with 4 pages sharing in two pairs and both pairs being `home ≡ editions index`, which is all that is left of this row. Derived rather than hand-written (2026-06-07), so the forty-four pieces of copy the row feared are two template edits. **A derived count in Arabic is FOUR constructions, not one**: `مادة واحدة` · `مادتان` (the dual, which English lacks) · `٦ مواد` · `٤٤ مادة` — so the obvious translation of the English template would have been ungrammatical on most of the corpus, and silently, a `<meta>` content attribute never being painted (#121's shape meeting #86's). **Still owed: the Arabic Editor's gate on the FRAME's wording**, not on the arithmetic. Measured in `agents/growth/2026-11-05-per-facet-descriptions.md`. **Original row follows.** **What remains is the ask:** the 44 now serve two strings rather than one, so a region page and a topic page still describe themselves identically, and a description is the one piece of copy we control in a search result. Per-facet descriptions are **derived, not hand-written** (2026-06-07: anything that must equal the current article set is build-generated) — but the frame around the derivation is forty-four pieces of copy in two languages, and the Arabic half needs the Arabic Editor's gate. | Editor + Arabic Editor + **[WD]** | **2026-11-03** (growth) | Measured over all 134 built pages: 134 titles / 134 distinct, 91 distinct descriptions, the duplicate population enumerated by page kind and by `lang` attribute | nothing red — no gate asserts description uniqueness, which is part of the ask |
| 75 | **`qa_feed_direction`'s projection is sound only in a geometry WE arranged, and it is not the consumer's** — raised by item 28's closure. `signature()` pushes `b.left` and discards `b.top`, so a line wrap and a direction flip are the same symbol: in an LTR host the first character of a new line sits far to the left of its predecessor and scores `-`, exactly as an RTL run does. **The kernel is empty anyway**, because the probe pins `white-space: pre; width: 60000px` so no field can wrap, with the reason written in the comment at the point of construction — this is the only one of the four render rulers whose author interrogated it, and the method is the template: *where you cannot widen a ruler, construct the geometry in which its kernel is empty.* The residue: **a subscriber's reader wraps**, and the probe's own header says it carries no site CSS precisely because *a subscriber's reader does not have ours* — so the direction question is answered in a layout no reader is in (#16, turned on our own probe). The ask is a two-key `(line, x)` signature compared at a realistic reader width, and a decision about whether a wrapped field's base-direction behaviour is ours to assert at all. | **[AE]** | **2026-11-03** (from item 28's close) | `b.top` absent from the signature, read in the code; the pinning read in the probe's own stylesheet and comment | nothing red — the assertion is sound as scoped, which is why this is OPEN and not DEFECT |
| 74 | **`qa_arabic_joining`'s SERVED half reads ONE run per page and its scalar cannot represent WHICH join broke** — raised by item 28's closure, measured by injecting N evenly-spaced ZWNJ into the real longest run on each target, N broken joins and nothing else changed. **Eligible Arabic runs per page: 37 / 49 / 11 / 1. Runs read: 1.** One broken join is invisible to three decimals on three of four targets; on the AR article **128 broken joins of 511 reads 0.742 against the 0.90 threshold**, and on the AR home **79% of the run broken reads 0.863 and passes.** Only VALENCE's 14-character run can cross the threshold at all. **And the two limits cause each other:** a ratio over a short run has no dynamic range (`مدار`, 4 chars, measures 0.972 shaped and the tool's own header says no threshold can separate it), so `SERVED_MIN_LEN = 12` forces the *longest* run to be selected — and the longest run is the one in which a single broken join is most diluted. *The ruler's dynamic range and its locality trade against each other, and a single scalar admits no other resolution.* The ask is a per-word or per-join ruler, which changes what the gate expects of served bytes, so it is handed over rather than fixed by the instrument that found it. | **[WD]** + **[AE]** | **2026-11-03** (from item 28's close) | Nine injection levels measured per target on the real served runs today, every injection changing only the ZWNJ count | nothing red — every run on this build shapes, and the worst served ratio is 0.689 against 0.90 |
| 73 | **`qa_render`'s per-band DARK and ACCENT are measured and NOT asserted, and the decline expires by a change of ruler rather than by arithmetic** — raised by item 28's closure as that decline's own stated falsifier (#93 for the floor, #125 for how a decline must be written: it names **no sibling instrument**, because there is none). Measured today on the real build: the EN home's footer band reads dark **0.0006** and the EN article's **0.0008** — both legible, both small muted type, and `dark` counts only pixels within 90 of INK. **A per-band dark floor at the whole-raster 0.003 would red this build today; a floor low enough to pass the footer (0.0005) sits too close to what a genuinely white-on-white band produces (≈0) to separate them.** So the ruler cannot hold per-band legibility *because it is an absolute count*. The ask is the ruler change that empties the kernel: **dark relative to the band's own ink** rather than to the band's area, which separates small-muted-but-legible from white-on-white at any density. Unlike a kind-C floor this does not expire by the corpus improving (item 71) — it expires only when somebody changes the arithmetic, which is why it is written down as a row and not as a watch. | **[AE]** | **2026-11-03** (from item 28's close) | 21 bands across 5 targets measured and printed by the widened gate on every build | nothing red — P1 per band is asserted and green; this is the limb that is printed |
| 72 | **The `related:` rail only points BACKWARDS IN TIME, so the likelier landing page is the one with no route to our own later work on its question** — raised by the growth function in the run that turned three edges round, because the other 31 are editorial judgments and not a graph operation. Measured over all 44 approved pairs: **138 directed edges, 98 reciprocated, 40 one-way — and 34 of the 40 point from a newer piece to an older one.** Connectivity is clean (0 pieces with no inbound rail, 0 with no outbound, 0 dangling, EN and AR identical), so this is not an orphan finding; **it is a clock.** A rail is curated when a piece is written and at that moment only the older pieces exist, so every follow-up can point back and none can point forward, and nothing ever goes back. **Sixteen published pieces are pointed at by a newer piece and offer no forward path**, worst `oman-school-performance-ratings` with five followers and zero forward paths — and the older piece is the likelier landing page, having the longer accumulated exposure. `qa_body_links` asserts a rail slug RESOLVES and `qa_reachability` asserts a page is reachable from its own front door; **neither has ever asked which direction the rail points.** **NARROWED 2026-11-07 by the growth function, which took the Editor pass this row said was not a graph operation — and the useful half is what it DECLINED.** Re-measured first: 138 edges, 98 reciprocated, 40 one-way, **33 backward over 18 distinct older targets**, so the row's shape held. **One of its numbers did not survive re-measurement and is corrected:** the row says *sixteen pieces are pointed at by a newer piece and offer no forward path*; under the strict reading — no rail to anything newer at all — today's count is **three**, and 18 is the count with an *unreciprocated* follower. Two questions, one number carried for both. **Not one of the 33 is between two pieces on the same country**, every one being a cross-system comparative, so the only available test was whether the newer piece is on the same QUESTION. **Eleven edges added across five older pieces, both editions** — Oman's ratings piece to Chile, NAEP and NAPLAN; Korea's reversal to NCEA and PSLE; RAK Iqra to Egypt and the Philippines; NAEP to NAPLAN and England; Zambia to the two Edition 05 pieces that followed it — capped so no piece exceeds the proven maximum rail count of 6. **Twenty-two were left alone and that is the pass's output:** the commonest reason is that the newer piece cites the older as one of several comparators and the older piece's reader is not looking for it. After: **149 edges, 120 reciprocated, 29 one-way, 22 backward, EN and AR identical**, build exit 0 with `qa_body_links` and `qa_pair_frontmatter` green. Measured in `agents/growth/2026-11-07-the-rails-now-point-forward.md`. **What stays open is the half that stops it regenerating** — the commission-template step — plus the 22 declined edges, whose judgment expires when a later piece turns one of those comparisons into a real follow-up. **Original row follows.** **The ask is NOT a reciprocity sweep.** The defect regenerates with every unit of normal work — the Bahrain draft verdicted today declares three rails, all three backward — so the fix is a step in the commission template (*name the pieces this one follows up, and add the forward edge to each in the same commit*) plus one Editor pass over the remaining 31 to decide which reverse edges are warranted. | Editor + **[WD]** | **2026-11-02** (growth) | Graph computed from frontmatter over both editions, before and after; build exit 0 with `qa_body_links` PASS | nothing red — every rail resolves and no byte is wrong, which is why this is OPEN and not DEFECT |
| 71 | **A kind-C decline expires by ARITHMETIC, and nothing watches the arithmetic** — the day's forward question, entered at this block's head per the one-queue rule, and the thing item 26's closure generates rather than closes. Seven of the twenty declines this operation owns are #93 floors — *a floor above today's reality would red every build* — and **every one is true only while its own count is non-zero.** Today they read **408** unanchored body numerals, **42** registers no longer serving a quotation we attributed, **7** fetches justified by punctuation alone, **91** painted Arabic runs naming no bundled family, **129** unmatched valence selectors, **15 of 21** reviews with no meta description, and a **median 8%** vocabulary-provenance rate. **The day any one reads zero the decline is stale and the assertion is free** — which is exactly how the declarations class became free once somebody counted it — and no instrument prints *this decline is now assertable*. **The one that reaches zero is the one nobody will look at**, because a measurement that has stopped finding anything is the least interesting line in the output. First cut costs nothing: each of the seven already prints its count, so the tool that prints it can compare it against the floor its own header says it cannot afford, and say so. | **[AE]** | **2026-11-02** (the daily's forward question) | Seven counts read off today's own build output, not hypothesised | nothing red — it is the item that asks which of our written reasons has already expired without anybody noticing |
| 70 | **Every hand-written quantity this operation parses has a capture with a CEILING, and a ceiling reads as a clean pass** — the weekly review's forward question, entered at this block's head per the one-queue rule, and the thing ruling **#124** generates rather than closes. `qa_register_shape`'s ratio limb read `ninety` on 2026-10-07, `one hundred` on 10-14 and **nothing at all from 10-15**, for eighteen days through two weekly consolidations, because its capture counted tokens and three number-words would not fit a two-word group. `words_to_int` could parse the number the whole time; the wall was one function call upstream. And the first repair had the same defect one step out — widening two tokens to four still counts tokens, and a five-token phrase matched nothing. **The question is the population:** enumerate every regex across `agents/tools/**` that captures a number in order to compare it, partition into *counts tokens* against *delimits and lets the parser judge*, and for each one in the first bucket name the largest value it can read and how far its subject currently is from that value. A ceiling is a date, not a surprise. | **[AE]** | **2026-11-01** (the weekly review's forward question) | One instance found today by being bitten by it, and repaired | nothing red *(the ceiling is silent by construction — that is the finding)* |
| 69 | **The weekly review's own tables ran off the page at 390px, and no instrument can see it** — found by rendering this morning's review at mobile width and looking at it (08-23), after item 27's repair had already passed every artefact through `qa_artefact_render`. The three-column tables carry monospace cells that do not wrap, so the rightmost column was cut off the viewport; repaired in this file's own CSS with a narrow-width scroll rule and the reason written at the point of change. **The row is the population, not the instance:** `qa_artefact_render` renders 138 artefacts at ONE width and asserts the container, which is the 10-27 mechanism and not this one. Nothing this operation owns asks whether an artefact's own content fits the viewport it is rendered into — and the population is 141 — 120 briefs and 21 reviews — every one of them carrying tables. Needs a second width in the render harness and an assertion that no element's right edge exceeds the viewport at it. | **[WD]** | **2026-11-01** (weekly review, by looking) | 1 artefact confirmed and repaired; **140 unmeasured** | repaired here; the class is unasserted |
| 68 | **`qa_font_payload` limb 2 failed and then passed TWICE on an unchanged tree, and an intermittent red is worse than a hard one** — raised by the brief function after observing exactly that sequence: one build red with *1 fetched font file nothing on the page justifies*, then two builds clean, no file touched in between, the tool run standalone also clean. **The bytes are right; the instrument is not deterministic**, which is why this is OPEN and not DEFECT. The suspected mechanism is in the tool's own harness rather than in its logic: fetches are attributed per page by clearing one shared list before each page's load, so a request still in flight from the PREVIOUS page can land after the clear and be charged to the next page, where nothing justifies it. That would be a false RED only — it cannot hide a real dead fetch — but it is the more corrosive failure anyway, because **a gate that sometimes reds on correct work teaches the next run to re-run it rather than to read it**, and that is 2026-09-13's *a hand-run assertion is a habit, not a gate* arriving by a different road: an assertion nobody trusts is switched off by re-running, not by unwiring. The work is to make the attribution deterministic — a per-page server or a barrier before each load — and to prove it by running the gate N times on one tree and asserting N identical verdicts, which is a property none of the 41 assertions has ever been asked for. | **[AE]** | **2026-11-01** (brief function, from a flake observed today) | Observed red once and clean twice on a byte-identical tree, plus clean standalone | **nothing red, and that is the problem** — it reds CORRECT work at an unknown rate |
| 67 | **Every gating assertion this operation owns contains numbers that were TRUE THE DAY THEY WERE WRITTEN, and nothing distinguishes those from the ones derived** - the day's forward question, entered at this block's head per the one-queue rule. `qa_date_identity` refused today's build because its non-vacuity guard said *expected exactly 1* declared standing row. It was written 2026-09-22, it was correct for 40 days, and what falsified it was an ordinary content change rather than a defect. That is **#57 living inside the instrument built to catch #57**, and the fix was one line: derive the expectation from the tree (the set of pages carrying a standing row equals the set of editions indexes) instead of copying a count into the assertion. **The question is the population.** `qa_patch_queue` exists because a count in prose is maintained by nobody; a count in a non-vacuity guard is maintained by nobody *and reads as rigour*. Enumerate every literal integer across all 41 assertions, partition into derived-from-the-tree against written-by-hand, and for each hand-written one name what would falsify it and whether that thing is a defect or a Tuesday. | **[AE]** | **2026-11-01** (the daily's forward question) | One instance found today by being bitten by it, and fixed | nothing red |
| 66 | **The one served document whose cascade no instrument of ours can audit is the one that needs it most** - raised by assertion 41's first sweep. `valence/index.html` carries 266 inline selectors and **129** match nothing under a static parse. Under a LIVE load with JS running the figure is **87**, and the 42-selector gap between those two numbers *is* the runtime markup - which makes the gap a measurement of exactly what no static instrument can reach. So both limbs decline it with the reason printed (#93), and the result is that the 540 KB instrument shipped 2026-08-08, the largest single document this operation serves, is the one page whose dead rules, orphaned rules and markup regressions are all invisible. Item 58's closure proved the shape from the other side: 10 of its 13 defective headings were written at runtime and absent from the served bytes. The work is to decide whether a driven probe (scroll to the end, settle, then query) turns 129 into a number that means something, or whether the honest answer is that a document which builds itself is outside this class of audit and should say so once, loudly. | **[AE]** | **2026-11-01** (from assertion 41's first sweep) | Both figures measured today, 129 static and 87 live, by the same oracle | nothing red |
| 65 | **The global layer states the thematic break THREE times and the pullquote TWICE, and only the per-component statements reach a reader** - raised by assertion 41's partition, where all five SUPERSEDED entries turned out to share one cause. The design system was authored as hand-built HTML with classes (`div class=pullquote`, `hr class=rule` in three mockups); the publication's bodies are markdown and markdown cannot attach a class; so each rule was restated as an element selector scoped to `.body-main` (`:global(blockquote)`, `:global(hr)`) and the classed original became residue the cascade can never reach. **Nothing is broken and no byte is wrong** - all five served breaks and all six served blockquotes paint correctly - which is why this is OPEN and not DEFECT. It is 2026-10-25's slanted-Arabic shape inverted: there two per-component statements failed to reach a third instance, here the per-component statements are the only ones that reach anything. The work is a Designer/Web Developer call: consolidate to one statement per property, or keep the global rules as the design's record and say so at each one. **Deleting them is explicitly NOT the default** (#118). | **[WD]** + Designer | **2026-11-01** (from assertion 41's partition) | Five entries classified with what supersedes each, measured in the computed style | nothing red |
| 64 | **`.body-grid--resumed` is the one genuinely ORPHANED selector in the build, and an orphaned rule is an unfiled defect report about the markup (#118)** - raised by assertion 41. The rule has been in `global.css` since 2026-05-25 and in the cascade never. Its markup exists in all three `design-assets/article-mockups/*/index.html` as a `body-grid body-grid--resumed` div and in no Astro template, and unlike the five SUPERSEDED entries **nothing restates it** - no `:global` variant, no scoped variant, nothing. So the design stands (a body grid that resumes after a full-bleed interruption takes zero top margin) and the markup walked away, and the rule is the only surviving machine-readable statement of it. The question is the markup's, not the rule's: does the article template have a resumed body grid silently carrying a top margin the design says should be zero, or did the full-bleed interruption the modifier exists for never ship? | **[WD]** + Designer | **2026-11-01** (from assertion 41's partition) | Grepped: present in 3 mockups, 0 templates, 0 content files, 0 served pages | nothing red |
| 63 | **Every instrument this operation owns runs in a context that can end without warning, and not one of them knows that** — the day's forward question, entered at the head per the one-queue rule. Today's run opened by diagnosing a predecessor that died at 181 turns with 45 of 90 wall-clock minutes unused, and #122 put the envelope reading onto the commit discipline. That fixes the *measurement*. It does not touch the deeper shape: **every gate, every emit and every probe this operation runs assumes it will finish.** `qa_claim_registers --emit` tops a register up across runs and already carries a request budget, which is the one instrument that has faced this. The others have not been asked. Which of them, interrupted at an arbitrary point, leaves a file that a later run will read as complete rather than as truncated? `agents/stats/*.json` are whole-file rewrites; `run-envelope.jsonl` and `history.jsonl` are appends; the register emits are read back by their own `--check` halves as coverage. **A partially written register is indistinguishable from a register about a smaller corpus** — which is #57's defect produced by a clock rather than by a mistake, and the first cut is to ask which of these writes is atomic. | **[AE]** | **2026-10-31** (the daily's forward question) | not yet measured | **nothing known** — the question is whether a crash can make an instrument lie, and no run has looked |
| 62 | **Nothing gates a closed edition being labelled the current one** — raised by the growth function in the run that repaired it, exactly as items 44 and 46 were, because *a check nobody wires is a habit* and the repair that shipped today was found by reading rather than by any instrument. For eighteen days `web/src/lib/editions.ts` carried `status: 'current'` on Edition 05 while `content-drafts/_EDITION_05_STATUS.md` said **CLOSED 2026-10-13** in its first line, and both home pages printed *Current edition* and *الإصدار الحالي* over it in the served bytes. **Two files in this repository disagreed about one fact and nothing compared them.** The assertable shape looks cheap and should be measured before it is believed: at most one edition may be `status: 'current'`; an edition whose status memo records a closure date may not be `current`; and no served page may print a *current*-register label over an edition the registry does not mark current. The third limb is the one that actually bit, and it is a render question rather than a source one. | **[AE]** | **2026-10-31** (growth, from item 45's repair) | read in `editions.ts` lines 81–96 against the status memo's first line, and confirmed in `dist` on both home pages and the editions index | **zero** — repaired today; the row is for the gate, not the defect |
| 60 | **Nothing gates the envelope log's own labels, so the one question it was built to answer still cannot be asked of it** — #122 clause 1 made `run_envelope.py . --log --label` a duty at the close of every standing function, riding on #96's commit. A duty is not a gate. The measured starting state: **34 marks over 10 run ids, of which 25 carry no label at all (73.5%), and the runs of 10-29 and 10-30 logged nothing whatever** — the second of those being the run that died of its envelope. An assertion here is awkward in exactly the way #93 warns about: a floor on marks-per-run would red every build made from a tree whose last run crashed, which is the condition the log exists to record. The honest shape is probably not a floor but a **completeness check on the rows that do exist** — every mark carries a non-empty label, and labels within one `run_id` are distinct — plus printing marks-per-run without asserting it. | **[AE]** | **2026-10-31** (from ruling #122) | 34 rows of `agents/stats/run-envelope.jsonl` parsed; 9 labelled, 25 not; 10 run ids against 13 daily runs since 2026-10-18 | **zero served** — the subject is the operation's own instrument, like #122 itself |
| 57 | **SPECIFIED 2026-10-31 BY ITEM 58'S CLOSURE — the gate must RENDER, not parse, and that is not a preference.** Valence carries thirteen defective heading elements and **ten of them are written by a script**, so a gate that parses served bytes sees 3 of 13 and reports 23% of its own subject as the whole of it. Four of this operation's assertions already drive a headless Chrome, so the capability is owned; what is new is that for this class the render is the *only* correct instrument, and a cheap static version would be worse than none because it would pass. The 09-14 trap applies twice over: the probe must be written against the served shape, and it must wait for the page's own JS. **Original row follows.** **Heading order has no gate, and the class returns the day somebody adds a heading** — raised by the growth function in the run that closed item 54, because that closure was a **hand sweep**: 135 documents parsed by a script written this morning and thrown away, which is 2026-09-13's *a hand-run assertion is a habit, not a gate* in the lane that keeps earning it. The assertion is cheap and exact — every served document has exactly one `h1`, no document skips a level, and the `h1` comes first — and its exception list is already measured rather than guessed: **`404.html` carries two `h1`s on purpose** (one per language on a bilingual page that is in no sitemap), and **`valence/index.html` skips 2 → 4** until item 58 is judged. A floor written before those two are named reds every build (#93), which is why this is a row and not a commit. | **[AE]** | **2026-10-30** (growth, from item 54's close) | Today's sweep: 135 documents, 1 skip, 1 document with two `h1`s, 0 without one | nothing red — the bytes are right as of today, and nothing can say so tomorrow |
| 56 | **15 of the 20 weekly reviews carry no `<meta name="description">` at all** — printed by standing assertion 40 on its first sweep and **not** written by it, because an instrument that composes the prose it checks is reading its answer off its own field (#75). The founder reads the weekly review; a link to one previews with whatever the client invents, and five of the twenty already carry a description, so the convention exists and fifteen files are missing it. The repair is editorial — each review's own findings, in one sentence — and it is **one morning for fifteen files**, the same shape as item 51's editorial half, which took one function. Their `<title>` dates are already asserted by assertion 40 and are clean, 20 of 20. | Manager + **[AE]** | **2026-10-30** (printed by assertion 40) | `qa_brief_head` prints the count on every build; the five that carry one were read | nothing red — a link preview with no description is absent rather than wrong, which is why this is OPEN and not a DEFECT |
| 55 | **Every instrument this operation owns asks whether what we QUOTED is still there; none asks whether the register has said something NEW since we read it** — the day's forward question, entered at the head per the one-queue rule, and **today's content function is the hand-done version of it.** `qa_sources_alive` asks whether a URL answers. `qa_claim_registers` asks whether anybody can re-open it. `qa_citation_identity` asks whether our quoted string is still in the bytes. All three are satisfied by a document that has published a correction, a result or a retraction on the very question the piece turns on — because none of them compares the document against the document we read. Item 42 exists only because a human split #117's measured half into four named pieces by hand; **the population is every piece whose argument rests on a register that has published again, and nothing knows which those are.** The first cut needs no new data source: both registers already store an `observed` date per URL, so a `Last-Modified` header or a stored body hash gives a *moved since we read it* flag over all 348 registers for the cost of one sweep. It would have named today's RAK register without anybody thinking of it. Second limb, and it is the honest half: a moved byte is not a new claim — a cookie banner moves every fetch — so the output is a **reading list ordered by change**, not an assertion, and #93's reasoning applies before anyone tries to gate it. | **[AE]** + Editor | **2026-10-29** | Named from the content function's own morning: the evaluator's page had published effect sizes, two unit conversions and three null results since this publication last read it, and the only thing that routed anybody there was a queue row a human wrote | nothing red today, and that is the point: every reachability instrument we own is green on a register that has changed its mind **AMENDED 2026-10-30 by the content function, which answered this by hand and found the first cut insufficient: the newer thing a register publishes may sit at a URL we have never cited** — see item 59. The `observed`-date cut stands as the cheap half and is now known to be a strict subset. |
| 53 | **This operation owns no visually-hidden utility class, and the only off-screen rule it has reveals itself on focus** — raised by the growth function rather than invented in passing, which is the whole point of the row. Item 49's three candidate shapes included a visually-hidden `<h1>`; that candidate was unavailable and **still is.** `.skip-link` is the sole off-screen rule in the house and it is correctly designed to become visible when focused, which an `<h1>` must not. Any future page that needs a heading, a label or a landmark name it cannot display has the same gap. **It is a Designer decision and not a Web Developer one**, because the house has no off-screen convention and the three idiomatic implementations differ in what they do to a screen reader's pause, to text selection and to print: a `clip-path` inset, a 1px-square `clip`, and `position: absolute` off-canvas are not interchangeable. **Not urgent and not a defect** — item 49 was closed by a candidate that needs none of this. | **[WD]** + Designer | **2026-10-29** (growth, from item 49's close) | Enumerated by reading every off-screen rule in the built CSS: one, `.skip-link`, which reveals on focus | nothing red — it is a missing tool, not a broken byte |
| 52 | **The KJSEA expansion goes back in, with its evidence, when its owner becomes readable** — raised by the run that closed item 35 so that a repair with a known cost does not become a permanent silence. Both editions of `2026-07-04-kenya-cbe-grade10-pathways` now keep the bare acronym, under #101 clause 1's second branch, because `kjsea.knec.ac.ke` does not resolve from this runner, its only archive snapshot is a shell serving a `<title>`, `knec.ac.ke`'s own snapshot never prints the name, `nation.africa` answers 403 here, and the readable third-party registers **disagree between *Junior School* and *Junior Secondary***. The cost is the reader's: a reader who does not know the acronym is now told less than before. **And the Arabic edition holds a vote nobody can count** — it had rendered «التعليم الإعدادي», the PREPARATORY stage, i.e. the *Junior Secondary* reading, for 117 days (#120). The row closes when any first-party register is readable from a runner, or when a human reads one from outside this environment; **it does not close by preferring a wording.** Re-test is one `curl` and costs nothing, so it is cheap to carry. | Editor + **[WD]** | **2026-10-29** (from item 35's close) | Four routes to the owner's wording tried and recorded today: direct DNS, two archive snapshots, the third-party host of ten of the piece's twelve citations | nothing red — the gate is green at 14 anchors with 0 carried, because the body no longer makes the claim |
| 50 | **Four instruments ask whether a quoted string is IN a document; none asks whether it is the string the document leads with** — the day's forward question, entered at the head per the one-queue rule, and **it is not a hypothesis: one of this morning's six proves it live.** `restofworld.org` serves *both* `South Korea's AI textbooks fail after rushed rollout` (its `<title>`) and `AI-powered textbooks fail to make the grade in South Korea` (its `<h1>`), and **both are in the document**. So `qa_citation_identity`'s substring search over served text will confirm a `<title>`-derived quotation forever, and would have confirmed the wrong one of those two had the apostrophe not hidden it from the extractor altogether (item 48). #119 says a quotation mark promises a **named form**; no instrument of ours can tell the forms apart, because all four flatten the document to text before comparing. The first cut needs no network: parse each served register's own `<h1>`, `<title>`, `og:title` and JSON-LD `headline` out of the bytes `qa_citation_identity` already fetches, and for every `found` token report **which form it matched** — `h1` is evidence, `title` and `og:title` are a warning, `slug` is a counterfeit. Second limb, cheaper and owed by the census that raised this: **a feed item's `<title>` and an og card's rendered title are a seventh and eighth form of our own headline and the census read neither.** | **[AE]** | **2026-10-28** | Named from one of the six misquotations repaired this morning, measured rather than hypothesised | nothing red today, and that is the point: a check that searches the whole body cannot turn red on the wrong form |
| 48 | **`qa_citation_identity` silently extracts NO token from 33 of 290 straight-single quoted spans — 11.4%, all English — and the dropped spans are systematically the headlines** — found by the closure of item 33, which is where two of the 33 turned out to be confirmed misquotations. The pattern is `(?<![A-Za-z])'([^'‘’]{10,260})'(?![A-Za-z])`: the character class excludes `'`, so a match cannot cross an **English possessive apostrophe**, and the apostrophe fails both guards. *South Korea's*, *Egypt's*, *Nation's Report Card*, *Can't Wait to Learn* — the result is **not a declined token, it is no token**, and the row then reports fewer quoted entries for the piece without reporting that it could not read them. **0 Arabic spans affected**, guillemets having no such ambiguity and Arabic no possessive apostrophe, which makes this the first instrument defect that is English-only. Measured and proved this morning: the tool extracts **257**, a strict rule treating `'` as an apostrophe only when a letter stands on **both** sides extracts **290, with zero regressions against the 257**; a looser rule (any following letter) recovers 34 and **mis-splits two nested quotations**. **Not shipped by the run that measured it** — the 33 new tokens must each be asked before the register can report on them, and at least one (`the date is the index's, not the article's`) is an annotation's internal note rather than a claim about anybody's bytes, so the false-positive class needs naming before the rule ships (#93). | **[AE]** | **2026-10-28** (from item 33's close) | Measured over all 88 approved pieces by an independent script with the live pattern as its control; two of the 33 are misquotations confirmed by hand against their registers today | nothing red — the gate is green and the population it declines is invisible in its own output, which is the defect |
| 47 | **The only overflow gate this operation owns reads the artefacts, never the publication — and it reads them at exactly one width** — the day's forward question, entered at the head per the one-queue rule, and it inverts the rule that created its subject. `qa_artefact_render` is the **only** tool of the thirty-nine that measures overflow at all: `scrollWidth`/`clientWidth` appear in no other file in `agents/tools/`. Its scope is `agents/briefs` and `agents/reviews`. **So the 134 pages a reader is served — two scripts, one of them RTL, with the longest unbreakable tokens in the corpus sitting in `<code>` inside article bodies — have never been checked for overflow at any viewport width.** The 2026-08-23 perimeter rule was written to ADD the founder-facing artefacts to a perimeter that already covered `dist`; for this property the relation is the other way round, and nobody noticed because the rule's sentence reads as an extension. Second limb, cheaper and sharper: `VIEWPORT = 1280`, one number, and **an assertion with a parameter is an assertion about that parameter's value** — a layout correct at 1280 and broken at 390 is invisible to the gate promoted today, and the founder opens the brief on whatever is in his hand. Measure both before building anything: how many of the 134 served pages overflow at 1280, and how many of the 136 artefacts overflow at 390. | **[AE]** | **2026-10-27** | Enumerated by grepping `scrollWidth`/`clientWidth` across all thirty-nine tools (one hit, one file) and reading `VIEWPORT` in that file | nothing red today, and that is the point: no instrument can turn it red |
| 46 | **Nothing gates `copyrightYear`, the field that replaced the build clock on all 134 pages today** — raised by the growth function in the run that created its subject, exactly as item 44 was yesterday, and **the two should be closed by one instrument rather than two.** Today's growth action replaced `new Date().getFullYear()` in `SiteFooter.astro` with a year derived from `createLastmodResolver()`, so the served byte is now a fact about the tree instead of about the machine's clock. 134 of 134 pages carry it and 0 disagree with the sitemap's own date for `/` — **a measurement, not an assertion.** The general form, which is what makes it one item with item 44 and not two: **every date a template emits is derived from the tree, and none from the clock.** A build-clock date is the one claim no comparison this operation owns can ever catch, because it agrees with itself across any two builds run in the same period. | **[AE]** | **2026-10-27** | `copyrightYear()` evaluated against `createLastmodResolver()('/')` in node; footer markup diffed byte-for-byte across the before and after builds | nothing red — it is a gap in coverage, not a defect in bytes |
| 44 | **Nothing gates `dateModified`, the field that was missing from all 88 article pages until today** — raised by the growth function in the run that added it, because *a check nobody wires is a habit* (09-13) and **88 of 88 is a measurement, not an assertion.** Today's growth action wired `articleJsonLd` to `createLastmodResolver()`, the sitemap's own git-derived resolver, so the two channels now agree on all 88 URLs and disagree on none; a future template edit can drop the field silently and no build goes red. The cheap assertion belongs in **`qa_date_identity`**, which already owns the date-identity question and already gates: *every article page in `dist` carries a `dateModified`, it is ≥ that page's `datePublished`, and it equals the sitemap `<lastmod>` for the same URL.* Note the precondition — `lastmod_tree_guard.py` exists precisely because a git-derived date must not be compared against a working-tree build, so the third limb needs the guard the two existing lastmod instruments already share (exit 4 = REFUSED), and it is the reason this is a queue row rather than a line added this afternoon. | [AE] | **2026-10-26** | Measured in `dist` after the change: 88 of 88 carrying the field, 0 disagreeing with the sitemap, and the EN/AR `rak-iqra` split (10-26 against 10-25) proving the field discriminates | nothing red — the field is present on every page today and no gate would notice it leaving |
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
| 45 | **AMENDED 2026-10-31, AND ITS STATED DEFECT IS DISSOLVED RATHER THAN DEFERRED.** This row chose the **period label** as its unit and said the defect arrives on 2026-11-01. Re-asked one level up (#121's corollary), the row bundled two claims and only one is the founder's. The label is not the defect: *October 2026* is the issue's NAME, and a name does not expire — Edition 04 is labelled *August 2026* over pieces dated 07-07 to 07-28, the convention the registry's own comment states. **The defect was the `status: 'current'` flag, it was ours, and it had been SERVED FOR EIGHTEEN DAYS** — repaired by the growth function on 2026-10-31, with `hasOpenEdition` added so no consumer can print *current* over a fallback, and both home pages now reading *Latest edition* / *أحدث إصدار*. **So this row does NOT enter DEFECT on 2026-11-01.** What remains here is genuinely blocked and genuinely his: what the next piece is an edition of. The gate for the half that was ours is item 62. **Original row follows.** **On 2026-11-01 both home pages begin telling every reader that the current issue is a month that has ended** — Class A of item 43's enumeration, and **the first row this board has carried that changes bucket by itself on a stated date.** `web/src/lib/editions.ts` serves Edition 05 with `periodEn: 'October 2026'`, `periodAr: 'أكتوبر ٢٠٢٦'` and `status: 'current'`, rendered in the masthead and the section meta of both home pages. The claim is true today and false in four days, which is ruling #102 (*a name is a claim about now*) on a surface no instrument reaches: thirty-four of thirty-nine assertions read `dist`, where the label is already rendered and looks like prose, and the other five read `web/src/content/**` or the repository root, where it does not appear at all. **BLOCKED and not OPEN because the only repair is to say what the next piece is an edition of, and that is a founder decision — GitHub issue #13, opened 2026-10-25.** What the operation owns is naming it, which the brief does at the top with its date. **It enters the DEFECT bucket on 2026-11-01 whatever anybody here does.** Read in `web/src/lib/editions.ts` lines 81–96 and confirmed served on both home pages in `dist`. | **[WD]** + founder | **2026-10-27** (from item 43's close) | issue **#13**, open 2 days |
| 22 | **The turn axis is still dark, and the failure report still cannot tell two causes apart** — the half of item 11 that needs a credential no identity here holds. `--max-turns 180` is unobservable from inside the agent step: no file, no variable, no API field. The remedy is staged at `agents/patches/2026-10-11-run-envelope-and-checkpoints.md` and has been since 10-11. **Also still owed and still cheap: the `run-failure` issue the workflow files carries neither `subtype` nor `num_turns`**, so #9 and #10 have different causes and identical titles — which is how 10-10 diagnosed 10-11 before it happened. Split out of item 11 at its closure so a half nobody here can reach stops riding along inside an item marked done. | **[AE]** + founder | **2026-10-18** (from item 11's close) | **issue #7** — the `workflows` permission, open since 2026-09-20 (**35 days**); remedy staged at `agents/patches/2026-10-11-run-envelope-and-checkpoints.md` since 10-11 |
| 32 | **Forty cited registers exist in exactly one copy and nobody has asked an archive to keep them** — the half of item 15 that is an ACTION rather than an instrument. Of 205 registers answered, 40 hold no snapshot anywhere; 28 are readable today and 12 already refuse us. The window in which anything can be done about a register is exactly the window in which the document is still there, and `archive.org/save` is one request per URL. **Deliberately not performed in the run that found it:** it is an outbound write to a third-party service on behalf of this publication, which this operation has never done, and a growth function should not quietly be the first. The decision wanted is narrow — *may the operation ask a public archive to snapshot a public URL we already cite* — and the recommendation is yes, with the URLs listed in the growth note. **AMENDED 2026-10-24, AND NOT IN THIS ITEM'S FAVOUR: its first five URLs were executed without authority.** The 10-24 growth function submitted all 28 live-only registers to Save Page Now; 5 were accepted and confirmed, 23 were refused by rate-limiting. **The run read this item for its subject and not for its owner cell**, which reads *founder*, and brief 110 had told him in writing that nothing would be sent until he said so. Named in `agents/growth/2026-10-24-item-32-five-registers-now-exist-twice.md` and in brief 111; **GitHub issue #12 opened**, stating what was sent before the question was asked, with a default of *option B, the 23 named only*, on **2026-11-01** — B rather than A because a run that oversteps should not inherit a standing authority as the consequence. The remaining 23 are held. *An item's owner cell is part of its specification.* | **[WD]** + founder | **2026-10-21** (growth, from item 15's close) | **issue #12** — may the operation ask an archive to keep our citations; stated default **2026-11-01** |
## Closed

**2026-11-07 — item 36 CLOSED at 15 days, from the OPEN head, as `agents/tools/arabic_side_reach.py`
(ruling #132) — the row's first cut came back ZERO and its hard half came back FIVE TOKENS WIDE.** The
row asked whether the edition #101 designates as the control can be instrumented at all, or whether the
control is permanently hand-read. **The first cut, verbatim as the row specified it — count the
Arabic-side determinations #86 and #101 require that are recorded in a hand-off, against the 44 pairs
that exist — is 0 of 44 on both lines**, every published hand-off having been written before the rule
that requires it (#86 codified 10-04, #101 on 10-15, last flip 10-13). So the answer is sharper than
either branch the row offered: *the control has not been read even once in a way anybody can check.*
**The hard half: an honorific is a boundary the Arabic artefact supplies**, on #113's own model, because
it cannot take a non-human subject and it commits a gender — 32 commitments across 14 of 44 AR bodies,
10 pieces with both channels, **4 with only one.** And the direction is worth more than the counts:
**English supplies the name boundary and commits no gender, Arabic commits the gender and supplies no
name boundary**, so there is no control edition, only a control per property (#132). The first pass
reported 318 commitments across 44 of 44 and was a **fabricated measurement** — Arabic agreement is
grammatical, so the probe counted ministries as women — corrected into two buckets and bucket B printed
rather than deleted (293 agreement-only tokens across 43 of 44). **Generated item 85, the board's first
DEFECT since 10-31.**

**2026-11-06 — item 34 CLOSED at 15 days, from the OPEN head, as `agents/tools/register_coverage.py`
(rulings #130 and #131) — and the row's hypothesis is FALSIFIED in both directions.** The row asked
whether this operation's reachability numbers are about the world or about its clients, and predicted
that the primary sources — *every yearbook, every decree, every performance report*, all PDFs — were
the hidden population. Measured per class over both registers, offline and re-runnable: **PDFs are the
best-archived class in the corpus, 18 of 19 at 94.7%**, and **official hosts are archived better than
the rest, 85.8% against 80.9%.** The identity instrument's **reach** is worse than the row thought —
**0 of 19 PDFs comparable, HTML the only format it reaches at all** — and its **rate** is flat:
**29.1% failing on official hosts, 31.4% on everything else**, with 39% of the comparable population
official. So *a reach gap is not evidence of a hidden defect population* (#130), and *the instrument
that can see a class is the evidence about that class* (#131) — `qa_claim_registers` asks an archive
about the very documents `qa_citation_identity` cannot read. **It is a measurement and not an
assertion**, carries no `qa_` prefix for that reason, and the register stayed at 42 / 39 / 27 with
**none of `CLAUDE.md`'s nine prose counts moving** — the first such landing in six days. Two rows
opened: **82** (within `PDF`, text against not-text, measured on one publisher's series the same
morning) and **83**, the forward question.

**2026-11-05 — item 31 CLOSED at 15 days, from the OPEN head, as standing assertion 42
(`qa_prior_publication`, ruling #128) — and the assertion the row specified could not be built.** The
row asked *which of this operation's claims are checked only by the next run's goodwill*, named the
first answer as *an assertion that reads the previous deploy's conclusion and goes RED when it failed*,
and that assertion is a **deadlock**: a red prior deploy is cleared by a push, a push is made by a run
whose build is green, so gating it forbids the one action that clears it — on 2026-10-21 it would have
turned a two-day publication gap into a permanent one. The shipped gate asserts the **register** of
observations instead (schema · `strand_len` re-derived from `git rev-list --count` · the newest row
verifiable, which is item 67's derived non-vacuity guard · monotonic deployed SHA) and **limb 5, the
duty** — inside the daily run the register must carry a row written by this `GITHUB_RUN_ID`, scoped by
`GITHUB_WORKFLOW` so the deploy job prints SKIPPED and cannot red for the daily run's silence. The
network `--observe` half asks the Actions API, computes the **strand** (commits on `main` no successful
deploy has carried — item 77's number, invisible in `git log`), writes no row at all if the API does not
answer (#111), and gates nothing. **Nine proofs:** five bites red, four controls green, the fourth being
bite 5's own failing tree read from the deploy job, which is the only proof that limb 5's scope is real
rather than claimed in a comment. **Bite 1 was caught by two limbs** and provenance now declines a row
the schema has already failed. **Wider half measured, not deferred: 54 obligations across 28 of 168
documents, one of them now a gate** → item **80**. Gate register moved to **42 tools, 39 gating, 27
`postbuild`**, derived by `qa_patch_queue` and then moved by hand in nine homes in `CLAUDE.md`.

**2026-11-04 — item 29 CLOSED at 15 days, from the OPEN head, and three of four surfaces were promoted
while the FOURTH WAS WITHDRAWN.** #109 states that the JSON-LD cross-page graph, the two feeds as one
subscription, hreflang reciprocity and canonical uniqueness are all statically computable, and that
assertion 34 gated **one**. It gated **one of three**. **Limb 3:** every `@id` *described* on more than
one page agrees on every property the pages share — the intended assembly stated in `ld_nodes()` because
a consumer merges **by `@id`**, so `{"@id": X}` alone is a reference that claims nothing while
`{"@id": X, "name": …}` is a description that does, and two pages describing one node differently is a
contradiction **in neither page**. 1,206 nodes, **386 distinct**, 2 described twice, 0 disagreements —
and the 386 is this row's own hand-verified figure, now derived by a gate instead of remembered.
**Limb 4:** the two feeds are one subscription — 44 + 44, 0 shared `guid`, 0 shared `link`, 0 repeats,
0 absent, because a reader taking both holds one list keyed by `guid`. **Limb 5:** the canonical
namespace — 134 over 135 documents, no two the same, and the exemption is **positional rather than a
list that grows** (#113): `404.html` must declare **none**, a property already written in
`qa_reachability`'s *prose* and asserted nowhere. **WITHDRAWN — hreflang reciprocity:**
`qa_hreflang_clusters` clauses 1-2 have asserted membership, dereferencing and reciprocity **since
2026-09-01, as a build step**, so the duplicate would have put one number in a second place to drift
from; the count is printed (264 alternates across 132 pages, #109's 396 less the x-default per page) and
the decline names the sibling **having read it and proved it**, per #125. *A claim about what is NOT
checked is read off the wiring, never off the ruling that wrote it.* Proved **14 ways** on copies of the
real `dist`, bite first, every injection asserted to have changed the file; five bites red, three
controls green including the load-bearing one — a bare `@id` **reference** must stay silent and does —
**and bite 5 was caught twice**, by the error-page clause and the uniqueness clause, so bite 6 gives
`404.html` a canonical nothing else claims: *a defect two limbs catch proves neither of them necessary.*
The withdrawal is proved both directions: the two hreflang bites are silent here and **red in the
sibling**, control green either side. Gate count unchanged at **41 tools, 38 gating** — limbs are not
tools.

**2026-11-03 — item 28 CLOSED at 15 days, from the OPEN head, and the row's answer is a KERNEL per
instrument rather than an audit of oracles.** Every ruler is a projection and every projection has a
kernel: a set of distinct states it maps to one output. Six standing rulings say *a green check is
scoped to what it enumerates* and all six ask what entered the measurement; **none asks what the
measurement cannot distinguish once it is in** — and because the kernel lives in the arithmetic rather
than in the target list, it cannot be closed by enumerating more. Four instruments, four kernels.
**`qa_render`: extent and position, both closed today.** `--screenshot` under `--headless=new` captures
the **viewport**, not the document — old headless captured the full page and the flag name did not
change when the behaviour did — so every raster this tool had ever read was **1200×900 against documents
2,559 to 5,648 px tall**, the ruler holding **29.6% / 35.2% / 15.9% / 16.9%** of its four targets while
printing one line per *page*. Not a regression: the floors were calibrated 2026-09-15 from the same crop
and today's viewport numbers reproduce that range to the digit. And widening the raster **alone would
have reduced sensitivity**, because a pixel count has no coordinates and the lower page is less
ink-dense — the EN home's whole-page dark passes a 0.003 floor at **0.0053** while **its own last band
reads 0.0006**. So the shot is now taken at the document's own height, **verified rather than assumed**
(measured at 900 px, re-measured at the height about to be shot, the page refused if they disagree), and
**P1 NOT BLANK is asserted per 900 px band**: the property is now *no screenful of any page is blank*,
which is what the 2026-08-16 edge-to-edge defect actually was, rather than *the page as a whole drew
something*, which no page with a masthead can fail. Floors from measurement before assertion (#93): band
ink runs 0.0114–0.0612 across all 21 bands, so the floor sits at 0.006. Per-band dark and accent are
**printed and not asserted** with the falsifier stated — item 73. **`qa_arabic_shaping`: the layer
below**, already interrogated in its own header (*"computed style reports what was ASKED FOR, never what
the font DELIVERED"*), and assertion 18 is that interrogation's successor; one of four, and it took a
day. **`qa_arabic_joining`: locality** — 1 of up to 49 eligible runs read, one broken join invisible to
three decimals, 128 of 511 joins broken reading 0.742 against a 0.90 threshold, and the dynamic-range
requirement *forces* the longest-run selection that maximises the dilution; item 74. **`qa_feed_direction`:
dimension** — `b.top` discarded — **and its kernel is empty by construction**, the probe pinning
`white-space: pre; width: 60000px` with the reason in the comment, which is the template for the other
three and leaves only the residue that the geometry is ours and not the consumer's; item 75. Proved per
#35 with the control green either side, **bite A red on the new ruler and GREEN on the old**, which is
the measurement of what the widening bought, and bite B's height guard fixed from a traceback to a
sentence. **And the first harness was wrong before the code was:** both bites reported GREEN with the
injections verifiably applied, because `if cmd; then …; fi; rc=$?` captures the exit of the `if` — *a
harness that projects {0, nonzero} onto {0} has a kernel too*, committed against the proof of the day's
own thesis. Cost measured and stated: **8.0 s → 32.2 s**, and no sampling introduced to pay for it.
**Ruling #126.**

**The item 28 row, as it stood:**

| # | Item | Owner | Raised | Verified how | Blocks |
|---|---|---|---|---|---|
| 28 | **Which of our four render assertions rest on an oracle nobody has interrogated?** — the day's forward question, entered at the head per the one-queue rule, and it has a known first answer. Ruling #108: `el.scrollWidth` is silent on inline text overflowing an `overflow: visible` block, proved by injection — `scrollWidth == clientWidth == 1028` for text far wider — so assertion 33's overflow half **cannot be shown to bite** and does not gate. The correct oracle is a **Range rectangle** (`doc.createRange()` over an element's contents, `getBoundingClientRect().right` against the padding-box edge), which is a geometric question the layout engine must answer honestly. **And the same question is owed by four gating assertions that have never been asked it:** `qa_render` reads a raster, `qa_arabic_shaping` and `qa_arabic_joining` read a dumped DOM, `qa_feed_direction` reads a rendered feed. Six rulings say *a green check is scoped to what it enumerates*; all six ask what the check looked at, and none asks what its ruler can represent. | **[AE]** | **2026-10-19** (the daily's forward question) | Named from a blind spot measured by injection today, not from a hypothesis | nothing red |

**2026-10-31 — item 58 CLOSED at 1 day, from the DEFECT head, and the row named 3 of 13.** Valence's
heading order is repaired: `#aiPrinciples` (3 static), `#aiDetail` (1) and `#timingCap` (9) promoted from
`h4` to `h3` with their ID-scoped selectors moved alongside, so the painted result is preserved **by
construction** rather than by luck. Proved by probing both states in one headless Chrome with
`getComputedStyle` after the page's own JS had run — the only difference across all thirteen elements is
`tagName`, with family, size, style, weight, colour, line-height, both margins, letter-spacing,
text-transform, variation settings, display, width and height identical on every one. Screenshots were
**rejected as the instrument** rather than skipped: valence places its network dots randomly, so its
pixels are not deterministic and a pixel diff could not separate inert from noise. The rendered sequence is
now `H1,H2,H3…` with no skip in 35 headings. **The row's stated blocker — a Designer judgment about which
of valence's six heading voices the sub-claims should speak in — was not on the critical path**, because it
is a judgment only if the tag selects the voice, and this document declares no bare heading rule at all.
*A repair declared a design judgment may only be a coupling; ask whether the styling is scoped to the
selector before accepting that a judgment blocks a structural fix.* Specification handed to item 57.

**2026-10-31 — item 42 CLOSED at 5 days**, fourth and last sub-item taken. **42b, Türkiye:** MoNE's own
national ledger — *Asrın Gayreti: Maarifin İyileştirici Gücü*, 6 February 2026, 161 pages in thirteen
chapters — had been published for **267 days** and this piece had never cited it. Read in served text, it
outranks the podium (#43): completed **14,202** against the 14,304 a news agency carried from the
minister's remarks the *same day*, and the loss revised from *about 9,500* to **9,799** against a pre-quake
stock of 119,200 — a correction that runs against our own story by making the surplus harder. Both deks
moved to the published figures, counted at compose (EN 181/200, AR 158/200). The ledger's decomposition
reordered the story the headline tells: **about 85,000 classrooms repaired against 14,202 built new.** The
last line is still missing and is now a *finding* rather than a gap in our search — the report predates the
September 2026 deadline by seven months, and MoNE's own national 2026-27 opening release of 14 September
2026 does not carry the word *deprem* at all. (42a 10-29, 42c 10-28, 42d 10-30.)

**2026-10-31 — item 59 CLOSED at 1 day**, answered by contact in the run that displaced it. *Which of our
claims can be falsified only by a document we have never cited?* The Türkiye piece's 27 October sentence
reserved exactly this: *that is a record of our search rather than a finding about the ministry's
publishing.* **The document was not new; our search was.** The generalisation worth keeping: an absence
claim scoped to *what we looked for* survives contact with the document it missed, and the same claim
scoped to *what exists* would have been false for 267 days. **Hedge the scope you actually searched, and a
correction becomes an extension instead of a retraction.**


**2026-10-30 — item 51 CLOSED at 2 days, from the DEFECT head, the youngest head this board has handed
out.** It named **three** stale brief summaries and there were **nine**, in seven collisions, because the
assertable unit is a **collision** rather than a stale sentence: a description summarises one day, so two
dates sharing one summary means at most one of them describes its own day, and that is a fact about the
pair rather than a judgment about either. All nine rewritten from each brief's own Today section (09-09,
09-11, 10-12, 10-14, 10-18, 10-19, 10-21, 10-26, 10-27). Limbs 1 and 3 found an **eleventh** instance of
the derivable class the 10-28 run repaired ten of by hand — `2026-06-08`, title and description both
reading 06-07. **Standing assertion 40, `qa_brief_head`**, wired into `postbuild`, four limbs, proved seven
ways with bite 4 the real published defect restored exactly. **Ruling #121**, whose fifth home found the
assertion-discipline family's count reading thirty-six against its own list's forty. Vocabulary provenance
built, measured and **not** asserted (#93).

**2026-10-30 — item 54 CLOSED at 1 day, by the growth function.** Raised as a coverage gap and it held a
defect on **89 of 135** served documents, **88 of them one element**: every article page in both editions
jumped from the `h1` title to the marginalia rail's `h4`, since the first publish on 2026-05-25. Promoted
to `h2` with its selector; proved visually inert by reconstructing the pre-change served bytes in a copy of
`dist` and probing both states in one Chrome — identical bounding boxes to the pixel, thirteen measured
properties identical. **89 → 1**, the remaining one raised as item 58 because its repair is a Designer
judgment and not a tag swap.


**2026-10-28 — item 33 CLOSED at 6 days, from the DEFECT head.** It named **four** instances and there were
**six**, on two pieces, all repaired in both editions. **Ruling #119:** a headline is not one string, so a
quotation mark promises a *named form* of the source. The six provenances — UNESCO's title with *and
modernizing* dropped; Oklahoma Voice's and the Korea Times' **URL slugs de-hyphenated**, which is why the
register's own inner quotation marks vanished (a slug cannot carry punctuation); Rest of World's `<title>`
element, on a page whose `<h1>` is a different sentence; the World Bank's headline **re-capitalised** into
Title Case, with the URL pointing at the blog index rather than the article; and the Korea Herald's long
form, which **no snapshot of that page has ever served** — #41 performed inside quotation marks. Fixing the
World Bank URL found the figure underneath: **₩1tn / $736m attributed to the World Bank belongs to the Korea
Times**, ₩533.3bn to the Korea Herald with an *at least* the body had dropped, and $0.74bn is a third figure
in a third scope. The body now gives each its own register. **And item 33's fourth instance was never
dead** — `agenciabrasil` serves its whole page today and the quotation is `found`, so none of #100's four
dispositions applies: they are dispositions of a **document** and that was a disposition of a **moment**.
Five registers re-read in served text, one via its own archive snapshot; `--emit` re-asked the rows and five
return `confirmed` on 2026-10-28 against `absent`, `absent`, not-extracted, `absent` and
`script-mismatch`/`too-short` before. Two new rows raised by the closure itself: item 48 (the extractor's
blind spot that hid two of the six) and item 50 (no instrument can tell one served headline form from
another).


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
| **How many of the selectors this build ships match nothing on any page we serve?** (was open item 21) — re-specified under #118 as a partition before a byte count. The count is **1 of 399**; the partition is 27 CONDITIONAL, 10 LATENT, 5 SUPERSEDED, 1 ORPHANED, and two of the five superseded were filed as ORPHANED defects first and both were fabricated by their own proofs. Closed by **standing assertion 41, `qa_selector_coverage`**, wired from `postbuild`, five bites red and three controls green; **ruling #123**. | 2026-10-17 | 2026-11-01 | the daily run, from the queue head at 15 days |
| **The Türkiye surplus target may have been restated from ten percent to fifteen** (was open item 61) — **the ten percent stands.** MEB's own register of 25 January 2024, read in served text, sets the target total at 129,120 at an aggregate 8.3% — a third number, below the piece's ten, which is what exposed the error: the two totals are regional aggregates and the ten percent is a per-province floor. The piece already carried the third unit as a 16% average. No correction; both annotations and both bodies gained what that register actually prints. | 2026-10-31 | 2026-11-01 | the content function at 1 day |
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