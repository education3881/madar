# Draft — Bahrain, five cycles of the BQA's own grades

**Drafter:** Content Creator (CC1) · **2026-10-23** · EN draft, first pass.
**Commission:** `content-drafts/briefs/2026-10-21-bahrain-bqa-five-cycles-brief.md`
**Recon of record:** `content-drafts/recon/2026-10-18-bahrain-bqa-five-cycles-register.md`,
**as corrected twice** by `content-drafts/recon/2026-10-22-bahrain-bqa-test1-recount.md`.
**Working slug:** `2026-10-23-bahrain-bqa-five-cycles`
**Status:** awaiting Editor five-test verdict. **No slot claimed. `approved: false` when it lands.**

---

## HAND-OFF LINES — the Editor returns this unread if any is missing

**1 · Caps (2026-07-27).** `dek: 197/200 · title: 47/100` (code points, tashkeel +1 each; counted at
compose, not at the gate). **And the ruler earned its place this morning: the first dek composed came
out at 225 and was cut before anything left the drafter's hand.** Three times (Korea 06-17, Oman
06-20, Netherlands 07-22) this cap was first measured at the build and each time it cost a cycle; the
07-27 addendum moved the ruler to compose, and this is the fourth strike caught at the ruler instead
of at the backstop. A cap measured where the prose is written costs a sentence; measured at the gate
it costs a day.

**2 · `annotation == sentence` (2026-09-13), per leaned-on register.** Every figure below was
re-counted from the CSV's own bytes today, not carried from the recon's table and not carried from
the 10-22 recount either.

| Register | Hedge / noun / date / setting in the body | Matches `sources[]` |
|---|---|---|
| `data.gov.bh` CSV | *reviews*, never *schools*; *rows* where rows; every cycle named; C5 labelled **open** at every use | ☑ |
| BQA Annual Report 2025 | *"for outstanding performance"* quoted verbatim; **calendar 2025**; 22 government **and** 7 private, so the reader is not left to infer the total | ☑ |
| BQA Performance Report 2024–25 | **academic year 2024-25**, **batch of 76 government schools**, percentages never set beside cycle percentages without both clocks | ☑ |
| `bqa.gov.bh/open-data/` | *one of seven datasets the Authority publishes* — described, not quoted | ☑ |
| `2026-05-26-bahrain-bqa-public-grades` (ours, as served) | the closing question quoted verbatim with its date | ☑ |

**3 · Named humans — gender read from register: 0 of 0.** The draft names no individual. The
predecessor names Dr. Maryam Hasan Mustafa and that piece carries the determination; this one does
not re-report her (commission, binding consequence 2), so no determination is made here.

**4 · Acronyms expanded in the body: 1, each expanded in `sources[]`: ☑.** `BQA` is expanded once, as
**Education & Training Quality Authority**, and the expansion is carried in annotation 2 in the
Authority's own form. **This is now gated, not promised** — standing assertion 37
(`qa_acronym_evidence`, ruling #113, filed this morning) anchors on the acronym and fails the build if
a body expands what the annotation does not carry. Checked against the draft before hand-off.

**5 · Registers with no archival snapshot: UNKNOWN of 5 — OPEN, and it blocks the flag, not the
verdict (#111).** The Bahrain URLs are not yet in `agents/stats/claim-registers.json` because the
piece is not yet in the corpus. **Two of the five are PDFs on a state host and one is a CSV export
behind an API query string** — the classes #112's forward question (item 34) names as the ones our
instruments systematically cannot read. The Verifier runs `qa_claim_registers --emit` over these five
before the flag moves, and any figure resting on an unarchived single register is double-sourced or
dropped.

---

## TEST 1 — all five registers re-opened today, dates recorded (#76)

| # | Register | 2026-10-23 | Against 2026-10-22 |
|---|---|---|---|
| 1 | `data.gov.bh` CSV export | **200 · 183,242 bytes** · sha256 `d6b62bda651083dc…` | **byte-identical**, third consecutive reading |
| 2 | `bqa.gov.bh/publications/` | 200 · 92,292 bytes | reachable; index moves, nothing cited from it |
| 3 | BQA **Annual Report 2025** PDF | **200 · 13,440,188 bytes** | **byte-identical** |
| 4 | BQA **Performance Report 2024–25** PDF | **200 · 4,243,331 bytes** | **byte-identical** |
| 5 | `2026-05-26-bahrain-bqa-public-grades` as served | 200, live | the quoted question is on a page a reader can open |

**One finding from the re-probe, and it changes two `url:` values.** The Authority's publications
index links both PDFs on a **CDN hostname** — `784ec626.delivery.rocketcdn.me` — and not on its own
domain. The same paths under `www.bqa.gov.bh` serve **byte-identical** documents (13,440,188 verified
both ways). **So the citation is first-party and the index's own link is not**, and this draft cites
`www.bqa.gov.bh`. A CDN hostname in a citation is an opaque third-party string that will outlive
nobody's memory of what it was; the Authority's own host is the register.

---

## FOUR POPULATIONS — recounted from the bytes today, third independent count

No sentence in either edition may use one of these as another.

* **245** schools appear in the register · **242** have ever been *graded* · **76** appear in all five
  cycles counting monitoring visits · **52** have been *reviewed* in all five.
* Cycle coverage over the 242: **52** in five, **124** in four, **22** in three, **15** in two,
  **29** in one. *The modal school has been reviewed in four cycles, not five.* **The five cycles are
  not a panel** and the draft never writes them as one.
* **1,022 rows = 882 `Review` + 140 monitoring visits**, the latter in **three** row types
  (`Monitoring Visit` 45, `Monitoring Visit 1` 61, `Monitoring Visit 2` 34).
* **The four numbered grades appear on `Review` rows only**, confirmed again today: the 140 monitoring
  rows carry the three-band `(A)/(B)/(C)` scale exclusively — `(B) In Progress` 97, `(C) Insufficient
  Progress` 23, `(A) Sufficient Progress` 20. **Two instruments, two scales**; the piece says so once
  and never folds 1,022 into a statement about grading.

## THE PER-CYCLE DISTRIBUTION — computed today, and nothing had computed it before

Over the 882 `Review` rows, by cycle. **Counts are the register's; the percentages are ours and are
arithmetic over its rows.**

| Cycle | Reviews | `(1) Outstanding` | `(2) Good` | `(3) Satisfactory` | `(4) Inadequate` | Published |
|---|---|---|---|---|---|---|
| C1 | 202 | 7 (3.5%) | 60 (29.7%) | 94 (46.5%) | 41 (20.3%) | 2009-06 → 2011-05 |
| C2 | 206 | 14 (6.8%) | 48 (23.3%) | 89 (43.2%) | 55 (26.7%) | 2012-02 → 2015-03 |
| C3 | 207 | 31 (15.0%) | 39 (18.8%) | 70 (33.8%) | 67 (32.4%) | 2015-09 → 2019-04 |
| C4 | 128 | 10 (7.8%) | 25 (19.5%) | 41 (32.0%) | **52 (40.6%)** | 2019-06 → 2023-12 |
| **C5 — OPEN** | 139 | 23 (16.5%) | 30 (21.6%) | 56 (40.3%) | 30 (21.6%) | 2024-07 → 2026-04 |

**This is the piece.** It is not a trend line and the draft must not round it into one: the
distribution **widens for three cycles, inverts in the fourth, and narrows in the fifth.** C4 is the
only cycle in seventeen years in which `(4) Inadequate` is the **modal** verdict.

**Four hedges carried at every use of this table, in both editions:**

1. **C5 is OPEN.** 139 reviews to date, the cycle running to April 2026. A cycle in progress is not a
   result, and the 16.5% is the figure *so far*.
2. **C4 is the smallest cycle (128) and the longest (4.5 years)** — it spans the pandemic closures.
   The draft states the span and does not explain the dip, because the register does not say why.
3. **Not a panel** — 52 of 242. A movement between cycles is a movement in *who was reviewed* as well
   as in *how they did*.
4. **The ruler may not be constant.** The Authority names a *Schools Reviews Framework 2024* for the
   current batch; the four grade labels are unchanged across all five cycles, and whether the bar
   behind them is unchanged is **not something this register says**. So the table is a record of
   *verdicts issued*, not a measurement of schools over time — **no composite of rulers**, and the
   draft says this in the body rather than in a note.

---

## THE DRAFT

```yaml
title: "Seventeen years of one regulator's own verdicts"
dek: "Bahrain's quality authority has graded its government schools by name since 2009. Over all 882 reviews its most common verdict is Satisfactory — and the distribution moves more than the schools do."
date: 2026-10-23
edition: 6
country: Bahrain
region: MENA
level: K-12
themes: [government-led programs, access]
type: curated
related:
  - 2026-05-26-bahrain-bqa-public-grades
  - 2026-06-20-oman-school-performance-ratings
  - 2026-07-28-england-report-cards-first-term
contains_composites: false
approved: false
```

In May this publication read a single Bahraini document — the Education & Training Quality
Authority's performance report for 2024–2025 — and ended on a question it could not answer from one
year's figures. The closing lines are still on the page: *"The second harder question is whether the
four-grade scale flatters or punishes the median school, and whether the BQA's distribution across
the four grades reflects the school system or reflects the inspectorate's calibration. The 2024–2025
announcement does not give the cross-tabulation; the question is the kind that earns a follow-up
piece, not a parenthetical here."*

The cross-tabulation exists. It has existed the whole time, on the Kingdom's own open-data portal, as
one of seven datasets the Authority publishes there: every grade the BQA has issued to a named
government school since 2009, in English and Arabic, in a single file. This is that follow-up, read
from that register, 150 days later.

The file holds 1,022 rows. Eight hundred and eighty-two of them are reviews; the remaining 140 are
monitoring visits, which are a different instrument on a different scale and are set aside here after
this sentence. The reviews run across five cycles, the first published between June 2009 and May
2011, the fifth still open and running to April 2026. Two hundred and forty-five schools appear in
the register; 242 of them have ever been graded. Counted over all 882 reviews, the Authority's own
verdict on its own government schools divides like this: `(3) Satisfactory` 350, `(4) Inadequate`
245, `(2) Good` 202, `(1) Outstanding` 85.

Read that order again, because the second place is the surprising one. Across seventeen years, a
Bahraini government school was more likely to be told it was *Inadequate* than to be told it was
*Good*. That is not a scandal and this piece will not write it as one. It is what a four-point scale
looks like when a regulator actually uses all four points of it, in public, with the school's name
attached — which is a thing most education systems do not do at all, and the ones that do mostly
publish a scale whose bottom band is almost empty. The BQA's bottom band holds 28% of every verdict it
has ever issued.

The predecessor's question was whether the scale flatters or punishes the median school. The answer
from the whole register is neither, and it is more interesting than either: the median verdict has
been `(3) Satisfactory` in four of the five cycles, and the distribution around it has moved
enormously. By cycle, the share graded `(1) Outstanding` runs 3.5%, 6.8%, 15.0%, 7.8% and — in the
open fifth cycle, so far — 16.5%. The share graded `(4) Inadequate` runs 20.3%, 26.7%, 32.4%, 40.6%
and 21.6%. The distribution widens for three cycles, inverts in the fourth, and narrows in the fifth.
In cycle four, published between June 2019 and December 2023, `(4) Inadequate` was not the tail of the
distribution; it was the **most common verdict the Authority issued**, 52 of 128 reviews — the only
cycle in seventeen years of which that is true.

Four things have to be said about that paragraph before anyone does anything with it, and they are
the reason this piece is a reading of a register rather than a chart.

The fifth cycle is **open**. Its 139 reviews are the ones published so far, against a cycle that runs
to April 2026, and a cycle in progress is not a result. The fourth cycle is the smallest in the
register — 128 reviews — and by some distance the longest, four and a half years, spanning the period
in which Bahrain's schools, like everyone's, closed and reopened. The register records what the
Authority found; it does not say why, and neither will we.

The third thing is a population boundary, and it is the one most likely to be got wrong by anybody
who downloads this file. **The five cycles are not a panel.** Of the 242 schools ever reviewed, 52
have been reviewed in all five; 124 in four, 22 in three, 15 in two, and 29 exactly once. The modal
school in this register appears in four cycles, not five. So a movement between two cycles is partly a
movement in which schools were looked at, and a sentence beginning *"the same schools, five times"*
would be false for 190 of the 242.

The fourth is about the ruler. The four grade labels are identical in all five cycles — the file
prints them in both languages in the same row, `(1) Outstanding` / `(1) ممتاز`, `(2) Good` / `(2)
جيد`, `(3) Satisfactory` / `(3) مرضٍ`, `(4) Inadequate` / `(4) غير ملائم` — and the Authority names a
*Schools Reviews Framework 2024* for its current batch of reviews. Whether the bar behind an identical
label was identical in 2009 and in 2026 is not something this register answers. What the table above
records is therefore **verdicts issued**, not schools measured over time. That distinction is the
whole difference between reading a regulator's archive and scoring a school system, and the
distinction belongs in the body of the piece rather than in a footnote, because collapsing it is the
single easiest mistake available here.

There is one more figure in the Authority's own documents, and setting it beside the distribution is
where a careless reading would go wrong. In its Annual Report 2025 the BQA records that *"22
government schools and 7 private schools received Gold Seals for outstanding performance."* In the
performance report for the academic year 2024–2025, a batch of 76 government schools was reviewed
under the 2024 framework, and 26% of that batch was rated at the top grade. Those two numbers come
from two different clocks — a calendar year of recognitions, an academic year's cohort of reviews —
and the 26% is a share of 76 schools, not of the 139 reviews in cycle five, which run 16.5% at the top
grade over a cycle that is not finished. Three first-party figures about roughly the same period that
do not reduce to one another: 22 seals, 26% of a batch, 16.5% of an open cycle. The Authority
publishes all three and treats none of them as the others. Neither does this piece.

What the register will not tell you is the part worth ending on. It records a verdict and a date for
each school and nothing else — no intake, no size, no governorate, no teacher count, no expenditure,
and no reason. It cannot say whether cycle four's 40.6% was a worse set of schools or a harder
framework or a harder four years, and it cannot say whether cycle five's reversal is a recovery or a
recalibration or the first, easier half of a cycle that is not over. A regulator that publishes its
own verdicts by name for seventeen years has done the rare and difficult thing. It has not thereby
answered the question its own numbers raise, and reading the file honestly means arriving at a
sharper version of the predecessor's question rather than at its answer: not *does the scale flatter
or punish the median school*, but **how much of the movement in a published distribution belongs to
the schools, and how much to the instrument** — which no amount of the Authority's admirable openness
can settle, because the register that would settle it is one nobody publishes anywhere.

---

## SOURCES — composed with every register open, never from memory of an annotation (#113, #101, 09-13)

1. **`data.gov.bh` — *Results of Government Schools Reviews*, CSV export** (read in served bytes
   2026-10-23, HTTP 200, 183,242 bytes, sha256 `d6b62bda651083dc…`, byte-identical to the 10-18 and
   10-22 readings; 1,022 rows — 882 `Review` and 140 monitoring visits across three row types; 245
   schools in the register and 242 ever graded; the four numbered grades on `Review` rows only; cycle
   coverage over the 242 reviewed: 52 in five cycles, 124 in four, 22 in three, 15 in two, 29 in one;
   grade totals over the 882 reviews: `(3) Satisfactory` 350, `(4) Inadequate` 245, `(2) Good` 202,
   `(1) Outstanding` 85; per-cycle counts as tabulated above; publication dates 2009-06 → 2026-04)
   — `https://www.data.gov.bh/explore/dataset/01-results-of-government-schools-reviews-1/`
   **LICENCE: the portal prints `Licence unknown` and carries no licence statement. Counts are
   reported; the table is not reproduced, excerpted as a table, charted or embedded.**
2. **Education & Training Quality Authority — open-data page** (the dataset is the Authority's own,
   one of seven it publishes there; read 2026-10-23) — `https://www.bqa.gov.bh/open-data/`
3. **Education & Training Quality Authority — Annual Report 2025** (read in served bytes 2026-10-23,
   HTTP 200, 13,440,188 bytes, byte-identical to the 10-20 and 10-22 readings: *"22 government schools
   and 7 private schools received Gold Seals for outstanding performance"* — calendar year 2025, the
   Authority's own instrument and its own words)
   — `https://www.bqa.gov.bh/wp-content/uploads/2026/06/Annual-report-2025-.pdf`
4. **Education & Training Quality Authority — Performance Report 2024–2025** (read in served bytes
   2026-10-23, HTTP 200, 4,243,331 bytes, byte-identical: the batch cohort of 76 government schools
   reviewed under the Schools Reviews Framework 2024, 26% at the top grade — **academic year 2024-25,
   a batch, not a cycle**)
   — `https://www.bqa.gov.bh/wp-content/uploads/2025/09/Performance-Report-24-25-EN.pdf`
5. **Madār — *Bahrain grades its schools, by name, in public*, 2026-05-26** (the predecessor, whose
   closing question this piece answers; quoted verbatim from the served page, read 2026-10-23)
   — `https://education3881.github.io/madar/articles/2026-05-26-bahrain-bqa-public-grades/`

---

## FOR THE ARABIC CONTENT CREATOR — composition, not translation

Compose from the **Arabic column of the same CSV**, never from this draft. Every grade name and every
review-type name is a **forced rendering** (#101) and is printed by the Authority in the same row:
`(1) ممتاز` · `(2) جيد` · `(3) مرضٍ` · `(4) غير ملائم` · `(A) تقدم كافٍ` · `(B) قيد التقدم` ·
`(C) تقدم غير كافٍ` · review type `مراجعة الأداء` · monitoring types `زيارة المتابعة`,
`زيارة المتابعة 1`, `زيارة المتابعة 2`. A disagreement between the editions on any of these is a
defect settled by re-opening the register, never by preferring the English.

**The four populations must survive the composition.** If 245 / 242 / 76 / 52 cannot be held apart in
Arabic without a construction the Arabic Editor will not pass, that is a stated **park condition** and
it fires — it is not a thing to write around.

---

## WHAT THIS DRAFT DOES NOT CLAIM, named for the Editor and the Verifier

* **No school is named by its grade.** The register names them; the piece does not (Test 4).
* **No causal claim** about cycle four, the pandemic, or the 2024 framework.
* **No improvement claim.** `(1) Outstanding` rising from 3.5% to 16.5% is **not** written as
  improvement anywhere, because the floor is unstated and the panel is 52 of 242 — *improvement never
  without its floor*.
* **Nothing the predecessor reported is re-reported** — the 76/23/22/19 counts, the 24-improved and
  45-held movement, Dr. Maryam Hasan Mustafa's quotation and the publish-by-name posture are all
  established there and are referred to, not re-run.

— Content Creator · 2026-10-23 · *the recount was right to be required a second time: a third count
from the bytes today agreed with the second in every cell, and the per-cycle table nobody had computed
is what the piece turned out to be about*
