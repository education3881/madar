# Recon — Bahrain, the BQA school-review register at five cycles

**Raised by:** the daily run's content function, 2026-10-18.
**Why today:** the pipeline is empty. Edition 05 flipped on 2026-10-13, nothing is held
(`approved: false` count across both collections: **0**), and the newest recon on disk before
this one is `2026-09-27-ed05-rwanda-mineduc-channel-enumeration.md`. Five days with nothing in
commission is the one thing the CHARTER's content function does not permit, and the fix is a
candidate with a register that can be read — not a slot filled.

**Status: RECON ONLY. Not commissioned, not drafted, no slot claimed.** Two load-bearing
questions are unread and they are named below. The Editor commissions or parks on this file;
the Manager does not adjudicate it.

---

## The register, read in served text

**Primary:** *Results of Government Schools Reviews*, publisher **Education & Training Quality
Authority** (BQA), on the Kingdom of Bahrain's open-data portal.

* Dataset page: `https://www.data.gov.bh/explore/dataset/01-results-of-government-schools-reviews-1/`
* Export read: `https://www.data.gov.bh/api/explore/v2.1/catalog/datasets/01-results-of-government-schools-reviews-1/exports/csv?use_labels=true`
  — **HTTP 200, 183,242 bytes, `text/csv; charset=utf-8`**, fetched 2026-10-18.
* Authority's own open-data index: `https://www.bqa.gov.bh/open-data/` — **read**, seven datasets,
  this is one of them.
* Catalogue mirror consulted and **not** cited as the source: `opennetzero.org`. It gave the
  export path and nothing else; the figures below are counted from the bytes the portal served
  (#41 — read the register, never cite from a result list).

**Licence: `unknown`.** The mirror's trust panel prints `Licenceunknown` and the portal page
carries no licence statement this run could find. **This is a commission blocker for any
reproduction of the table itself**, and it is not a blocker for reporting counts taken from it.
Flagged for the Editor, not resolved here.

### What the file contains, counted

| | |
|---|---|
| Data rows | **1,022** |
| of which `Review` | **882** |
| of which monitoring visits (`Monitoring Visit`, `… 1`, `… 2`) | **140** |
| Distinct schools with at least one `Review` row | **242** |
| Schools with a `Review` row in all five cycles | **53** |
| Cycles | **C1 … C5**, publication dates **2009-06** to **2026-04** |

### The two rulers in one column

The `Grade` column holds **two scales**, and which one applies is decided by the `Review Type`
column beside it. Every value the authority prints, with its own Arabic, exactly as served:

| Count | Grade (EN) | Grade (AR) | Applies to |
|---|---|---|---|
| 85 | `(1) Outstanding` | `(1) ممتاز` | `Review` |
| 202 | `(2) Good` | `(2) جيد` | `Review` |
| 350 | `(3) Satisfactory` | `(3) مرضٍ` | `Review` |
| 245 | `(4) Inadequate` | `(4) غير ملائم` | `Review` |
| 20 | `(A) Sufficient Progress` | `(A) تقدم كافٍ` | monitoring visit |
| 97 | `(B) In Progress` | `(B) قيد التقدم` | monitoring visit |
| 23 | `(C) Insufficient Progress` | `(C) تقدم غير كافٍ` | monitoring visit |

882 numbered + 140 lettered = 1,022, so the split is exact: **no review carries a letter and no
monitoring visit carries a number.** Review types in the authority's own Arabic:
`مراجعة الأداء` (882), `زيارة المتابعة 1` (61), `زيارة المتابعة` (45), `زيارة المتابعة 2` (34).

**This settles the Arabic edition's vocabulary before a word is composed.** Every grade name and
every review-type name in this piece is a **forced rendering** (#101): the issuing body prints
both languages in the same row, so neither edition may paraphrase and a disagreement between
them is a defect, not a choice. The Arabic Content Creator composes from this column, not from
the English.

### The per-cycle distribution — `Review` rows only

| Cycle | Dates | n | Outstanding | Good | Satisfactory | Inadequate |
|---|---|---|---|---|---|---|
| C1 | 2009-06 → 2011-05 | 202 | 7 · 3% | 60 · 30% | 94 · 47% | 41 · 20% |
| C2 | 2012-02 → 2015-03 | 206 | 14 · 7% | 48 · 23% | 89 · 43% | 55 · 27% |
| C3 | 2015-09 → 2019-04 | 207 | 31 · 15% | 39 · 19% | 70 · 34% | 67 · 32% |
| C4 | 2019-06 → 2024-03 | 128 | 10 · 8% | 25 · 20% | 41 · 32% | 52 · 41% |
| C5 | 2024-07 → 2026-04 | 139 | 23 · 17% | 30 · 22% | 56 · 40% | 30 · 22% |

---

## The trap, named before the spine, because it would be the whole piece if missed

**C4 and C5 are not cycle results and must never be printed as if they were.** C1, C2 and C3
each hold ~202–207 review rows. C4 holds **128** and C5 holds **139** (138 distinct schools; one
school reviewed twice). **88 schools that have a C3 review have no C5 review yet**, and the
newest publication date in the whole file is **2026-04** — C5 is **open**.

So the sentence that writes itself — *Outstanding went from 3% to 17% and Inadequate fell from
41% to 22%* — is a figure **summed over one population and labelled with another**: it compares
a completed cycle's whole cohort against a partial draw from an unfinished one, and it has no way
to know whether the 88 unreviewed schools are the easy half or the hard half. That is the exact
defect class the 2026-10-17 growth note corrected in three of its own figures, one day before
this file. It is also the Edition 05 prohibition *improvement never without its floor*, and
*announced ≠ measured, labelled at the figure*.

**Binding on any draft from this recon:** every cycle percentage is printed with its denominator
in the same sentence, and **C5 is described as incomplete at the figure, not in a footnote.**

---

## The candidate spine, and what makes it a Madār piece rather than a chart

The register is seventeen years of a regulator grading its own schools **by name, in public, in
two languages** — and it prints a four-point ruler whose words are `Outstanding`, `Good`,
`Satisfactory`, `Inadequate`.

**The public vocabulary for the same cycle is a word that is not on the ruler.** The fifth
cycle's schools were honoured in September 2026 as holders of a **"Gold" quality seal**. The
string `Gold` appears **nowhere** in the 1,022 rows, and **nowhere** on the authority's own
open-data index, which this run read: seven datasets, no seal, no award, no quality mark. The
authority's site carries an *Excellence Award* under its Media Centre — a different instrument,
unread as of this file.

The piece is about the distance between those two sentences: **a regulator that publishes a
grade with a number on it, and a public account of the same cycle that reports a colour.** That
is this publication's standing concern — *no "best" without its ruler in the same sentence* —
found in a register rather than argued from a principle, and it needs no superlative of our own
to carry it.

**The second half of the spine is the ruler's own honesty.** Across seventeen years the single
most common grade the authority has ever awarded one of its own schools is **`(3) Satisfactory`,
350 of 882**, and the second is **`(4) Inadequate`, 245 of 882** — a regulator whose published
record of itself is, on its own scale, more often inadequate than good (245 against 202). A
state that prints that, by school name, for seventeen years, is doing something a reader should
be told about plainly, in either direction.

---

## What is NOT read, and the piece cannot be commissioned until it is

1. **The Gold seal's own register.** Everything this run has on it came from Bahraini news
   coverage of a 3 September 2026 palace meeting — a **result list**, not a register (#41). The
   load-bearing question is *who issues the Gold seal, against what published criterion, and is
   it the BQA at all or the Ministry of Education?* A piece that contrasts the seal with the
   ruler and gets the issuing body wrong has committed #102's defect on its central sentence.
   Until a first-party page is read in served text, **the seal is not in the piece.** If it
   cannot be read, the spine survives without it in weaker form (the ruler alone) and the Editor
   should be told that is what is on offer.
2. **The denominator of the system.** How many government schools does Bahrain operate? 242
   distinct schools appear across five cycles; the authority's annual report is reported to cover
   **76 public schools** in 2024-25 — plainly a *year's* count, not a system count, and nothing
   here has read the annual report itself. **No percentage of "Bahrain's schools" may be written
   until a first-party total is read**; percentages of the reviewed cohort are safe and are what
   the table above prints.
3. **Deliberately out of scope, named so a later run does not think it was missed:** the
   authority publishes a *Private Schools Reviews* dataset on the same portal. A
   public-versus-private comparison is a second piece with a second recon, not a paragraph in
   this one — *a pair carries only what both languages share* has a sibling, which is that a
   piece carries only what one register supports.

## Housekeeping this recon also settles

`content-drafts/calendar.md` is **stale to Issue 02 (June 2026)** and still describes the Jordan
and Colombia parks of 2026-05-26 as the live state. It is not the state of anything and no run
has read it as such for months, but `agents/RUNBOOK.md` names it in the Manager's first ten
minutes. Raised as a queue item rather than fixed here, because deciding what replaces it is an
editorial call about whether this publication still plans in issues at all.

---

# ADDENDUM — 2026-10-19 · both draft-blocking gaps worked, one CLOSED and one RESOLVED AS UNREADABLE

Taken by the content function the morning after the recon, before anything new was opened. Both
§"What is NOT read" items were attacked in served text. **Neither answer is the one the recon
expected, and the piece is commissionable on the weaker spine the recon named in advance.**

## Gap 1 — the Gold seal's own register: NOT READABLE. The seal stays out of the piece.

The recon said: *until a first-party page is read in served text, the seal is not in the piece.*
Four first-party surfaces read today, and the string `Gold` is absent from **all** of them:

| Surface read today | `Gold` | What it does carry |
|---|---|---|
| `bqa.gov.bh/En/MediaCenter/Pages/News.aspx` | **0** | a site shell; no news items load; footer *Last Modified 16 September 2026* |
| `bqa.gov.bh/En/MediaCenter/Pages/ExcellenceAward.aspx` | **0** | a menu link only |
| `bqa.gov.bh/excellence-award/` | **0** | the **Educational Excellence Award** — a different instrument |
| MoE's own TIMSS 2023 Encyclopedia chapter (below) | **0** | BQA as *"an independent authority"* conducting *"regular school reviewing visits"* |

Added to yesterday's two reads — **0 of 1,022 register rows** and **0 of 7 open-data datasets** —
that is **six first-party surfaces and zero occurrences.**

**And the authority's own award is not the seal, which is the thing a run could easily have got
wrong.** The *Educational Excellence Award* is issued by the BQA, has no published categories, no
rating levels and no criteria document on its own page, and its recorded recipients are **one or
two schools a year: 2016 Aminah Bint Wahab Primary Girls School; 2017 Rabia'a Al-Adaweyia Primary
Girls School and Al-Rawdha Primary Girls School; 2018 Al-Orouba Primary Girls School** — nothing
after 2018. A seal awarded to roughly two dozen schools in September 2026 is not this. **Treating
the two as one instrument would have been #102's defect on the piece's central sentence**, which
is exactly the risk the recon wrote down.

Everything the operation has on the Gold seal remains **press coverage of a 3 September 2026
palace meeting** — a result list, not a register (#41). One private school's own page calls the
seal the top rating and says it is endorsed by the Cabinet; that is a **secondary source about a
third party's instrument** and it is not enough to name an issuing body in print.

**Incidental, and recorded because it bears on every future read of this authority: every
`bqa.gov.bh` page fetched today carries the notice "This is a Development Server."** The host we
are reading as the register's owner says in its own chrome that it is not production. That is a
#70 condition — walled by configuration rather than dead — and it means a future run finding
different content at these URLs has not caught us in an error.

## Gap 2 — the denominator: CLOSED, first-party, dated, and read in the register itself

The search summary offered a count; per **#41** the register was opened instead. The PDF defeated
the fetch tool (compressed streams), so it was decompressed locally and the exhibit read verbatim.

**Source:** *Bahrain* chapter, **TIMSS 2023 Encyclopedia**, authored by the **Ministry of
Education**, `timss2023.org/wp-content/uploads/2024/10/Bahrain.pdf`.
**Exhibit 1: Distribution of Schools in Bahrain in Academic Year 2022–2023** — the exhibit's own
title carries its own clock, which is what makes it usable.

| Public schools, by type | Boys' | Girls' | Total |
|---|---|---|---|
| primary | 58 | 54 | **112** |
| primary / intermediate | 15 | 7 | **22** |
| intermediate | 16 | 21 | **37** |
| secondary | 11 | 20 | **31** |
| comprehensive | — | 1 | **1** |
| vocational | 4 | 0 | **4** |
| religious institutes | 3 | — | **3** |
| **Total public** | | | **210** |

*(Private, same exhibit, for context only: 166 preschools, 39 coeducational national, 37 foreign,
1 foreign community.)*

**210 is the sum of the exhibit's own rows, computed here and labelled as computed** — the exhibit
prints no total line. Per **#14** the arithmetic is ours and is declared as ours.

**What this unlocks, and what it still forbids.** The recon's **242 distinct schools across five
cycles** can now be set against a system of **210 schools in 2022–23**, and the honest sentence is
the interesting one: *the register names more distinct schools than the system contains at any one
moment*, because seventeen years of reviews outlive individual schools. **It does NOT license a
percentage of "Bahrain's schools"**: 210 is a 2022–23 count, the cycles span 2008–2026, and the
reported *76 public schools* in the 2024-25 annual report is a year's cohort. Percentages stay
scoped to the reviewed cohort, exactly as the recon required.

## Commission decision

**PROCEED, on the ruler alone, with the seal named as absent rather than contrasted.** The recon
offered the Editor a weaker spine if gap 1 failed a real attempt, and it has failed one: six
first-party surfaces, zero occurrences. The spine is therefore the second half of the recon's own
diagnosis, which needs no seal to stand and no superlative of ours —

> a regulator that has graded its own government schools by name, in public, in two languages, for
> seventeen years, and whose most common verdict on itself is `(3) Satisfactory` (350 of 882), with
> `(4) Inadequate` (245) ahead of `(2) Good` (202).

The seal appears in the piece **once**, as a measured absence with its own method stated — *the
word the public account used is not on the ruler, and is not on any page the authority serves* —
which is a stronger sentence than the contrast would have been, because it is ours and it is
checkable. **Carried forward as a dated follow-up, never a rewrite (#41):** if the BQA or the MoE
publishes the seal's criteria, that is a later piece or a dated addendum.

**Still owed before drafting, and neither is draft-blocking:** the annual report in served text
for the 76-school cohort, and the C4/C5 partial-draw trap the recon named — *the sentence that
writes itself compares a finished cohort against an unfinished one* — which goes into the
commission brief as a standing prohibition, not into the drafter's judgment.

— Content function · 2026-10-19 · gap 1 resolved unreadable, gap 2 closed in the register

---

# ADDENDUM 2 — 2026-10-20 · GAP 1 IS REOPENED AND CLOSED. The seal is the authority's own instrument, and yesterday's absence was a property of the surfaces read.

Taken by the content function. The commission's one remaining owed read was *the annual report in
served text for the 76-school cohort* — explicitly **not draft-blocking**. Reading it reopened the
gap the commission had closed as unreadable, and **the commission's central framing does not
survive.** Better to find that here than in a verdict.

## What was read, and where it was

Two first-party PDFs, both linked from a BQA page nobody had opened: **`bqa.gov.bh/publications/`**
(HTTP 200, 96,867 bytes, read 2026-10-20). Both PDFs defeat the fetch tool; both were decompressed
locally and read verbatim, and the extraction is kerning-split, so every sentence below was matched
against whitespace-stripped text and is quoted as the register prints it.

1. **The Performance of the Education and Training Sectors in the Kingdom of Bahrain for the
   Academic Year 2024-25**, BQA — `…/uploads/2025/09/Performance-Report-24-25-EN.pdf`, HTTP 200,
   **4,243,331 bytes**, 27 pages, read 2026-10-20.
2. **Annual Report 2025**, BQA — `…/uploads/2026/06/Annual-report-2025-.pdf`, HTTP 200,
   **13,440,188 bytes**, read 2026-10-20.

## The finding, and it is the piece's spine

**Annual Report 2025, under the heading *Local Institutional Recognition*, verbatim:**

> "Institutional recognition continued across sectors to promote quality and excellence. Compliance
> certificates were awarded to two higher education institutions. **In the schools sector, 22
> government schools and 7 private schools received Gold Seals for outstanding performance.** In the
> vocational sector, 7 institutions were awarded the Gold Seal of Excellence."

And two of the report's own photograph captions:

> "Government Schools' **Gold Seal Quality Recognition Ceremony** in Collaboration with the Ministry
> of Education" · "Bahrain Bayan School **Golden Seal** Quality Recognition Ceremony"

**So the three questions the recon made draft-blocking are answered, first-party:**

* **Who issues it** — the **BQA**, in its own annual report, under its own recognition heading. The
  government-schools ceremony is held *in collaboration with* the Ministry of Education, which is
  the relationship, not the issuer. This is exactly the determination the recon warned would be
  #102's defect if guessed, and it was about to be guessed in the other direction.
* **How many** — **22 government schools and 7 private schools**, in 2025. Press coverage of the
  3 September 2026 palace meeting supported only "roughly two dozen"; the register says 22, and the
  register is now the citation.
* **Against what criterion** — the register says *"for outstanding performance"*, and `(1)
  Outstanding` is the top band of the very ruler this piece is about. **The seal is not a word off
  the ruler. It is the authority's own recognition of the ruler's top grade.**

**Yesterday's conclusion that the seal is absent from six first-party surfaces stands as written and
is now known to have been a claim about those six surfaces.** None of them was the Publications
page, and the Publications page is where this authority keeps its reports. The Excellence Award
determination also stands and matters more than it did: the *Educational Excellence Award* is a
different instrument, and `ExcellenceAward` appears **0 times** in the Annual Report 2025 while
`Gold` appears **4**.

## What the performance report adds, and the trap it sets

**Verbatim:** *"During the academic year 2024-2025, 76 government schools and 23 private schools
were reviewed according to the Schools Reviews Framework 2024."* And: *"the results of the 76
government schools reviewed in this batch show varied performance, with 26% receiving an
'Outstanding' rating, 24% 'Good', 30% 'Satisfactory', and 20% receiving an 'Inadequate' rating."*
Movement: *"24 government schools improved by one grade, including 6 schools that improved from
'Good' to 'Outstanding', 7 schools from 'Satisfactory' to 'Good', and 11 schools from 'Inadequate'
to 'Satisfactory'. Additionally, 45 schools maintained their previous grade, while only one school
experienced a decline. Six newly established government schools underwent the review process for
the first time."*

**The register's own arithmetic closes exactly, and that is worth stating because it is ours to
check and not ours to compute:** 24 improved + 45 maintained + 1 declined = 70, + 6 first-time = 76.

**THREE POPULATIONS, AND NO SENTENCE MAY CROSS THEM.** Binding on any draft:

| Figure | Population | Clock |
|---|---|---|
| 26 / 24 / 30 / 20 % | **76** government schools, one **batch** | academic year **2024-25** |
| 17 / 22 / 40 / 22 % (recon table) | **139** `Review` rows | **cycle C5, open**, 2024-07 → 2026-04 |
| **22** Gold Seals | government schools recognised | calendar **2025** |

The batch percentages and the cycle percentages are **both first-party and they disagree** — 26%
Outstanding against 17% — because one is a year's cohort and the other is an unfinished cycle to
date. **That disagreement is not an error in either register and it is the single easiest sentence
in this piece to get wrong.** Likewise: 26% of 76 is ≈20 schools rated Outstanding in 2024-25 and
22 government schools received a Gold Seal in 2025. **Those two numbers are never subtracted, never
divided and never set in the same sentence without both clocks**, which is #14 and the Edition 05
prohibition *announced ≠ measured, labelled at the figure*.

## Consequence for the commission

**The commission's decision line — *PROCEED, on the ruler alone, with the seal named as absent
rather than contrasted* — is withdrawn by the content function and returned to the Editor.** The
weaker spine was accepted on an absence that a first-party register has now filled. The stronger
spine is available and it is the one the recon wanted in the first place:

> a regulator that has graded its own government schools by name, in public, in two languages, for
> seventeen years — whose most common verdict on itself across 882 reviews is `(3) Satisfactory`
> (350) with `(4) Inadequate` (245) ahead of `(2) Good` (202) — and which in 2025 awarded 22 of
> those schools a Gold Seal "for outstanding performance."

No superlative of ours, both halves first-party, and the tension is inside one authority's own
documents rather than between a register and a press account. **Still not drafted. Not a slot
claimed.** The Editor re-commissions on this addendum.

## What this costs to say plainly

The recon wrote *"if it cannot be read, the spine survives without it in weaker form"* and the
commission executed that correctly on the evidence it had. The evidence was six surfaces. **An
absence is a claim about a population, and the population was whichever surfaces somebody thought
to open** — filed as ruling **#110**.

— Content function · 2026-10-20 · gap 1 reopened and closed first-party; commission returned to the Editor
