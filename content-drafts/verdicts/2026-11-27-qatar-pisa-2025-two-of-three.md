# Editor's five-test verdict: `2026-11-26-qatar-pisa-2025-two-of-three`

**Draft** `content-drafts/drafts/2026-11-26-qatar-pisa-2025-two-of-three.md` · **Brief**
`content-drafts/briefs/2026-11-26-qatar-pisa-2025-two-of-three-brief.md` · **Edition** 06, piece 4 ·
**Read** 2026-11-27 (daily run) · **Editor** acting on the daily run

## VERDICT: **PASS, with eight repairs required and all eight closed in-run.** Title taken: *Qatar's decade and its three years*.

Two judgments the ledger asked this desk for in writing, both answered below: **the title change from the
commissioned one is taken**, and **the length is no longer short** — the repairs took the body from 1,157
words to **1,584**, inside the brief's 1,300 to 1,800, because five of the eight repairs add register the
draft had read and not printed rather than padding.

## Test 1, sourcing reality. PASS, after five repairs

Every URL in the frontmatter was opened in this run before this verdict was written. Both closed doors were
re-tested first, per #159's family, and both are unchanged: **`www.oecd.org` answers this runner 403** and
**`edu.gov.qa` returns no status code at all**. The refusal was not routed around; the OECD registers were
read from the Internet Archive's captures of the OECD URLs.

| register | capture | bytes | sha256 (first 16) | reproduced |
|---|---|---|---|---|
| R8 Chapter 2, *Student performance in PISA 2025* | 20261104162528 | **2,426,000** | `e5a429b011ff90e5` | **to the byte** |
| R1 press release, 8 Sep 2026 | 20261115… | **1,468,371** | `096bb651ddbda014` | **to the byte** |
| R3 launch speech, 8 Sep 2026 | 20261115… | **1,464,823** | `33b350b2803a4906` | **to the byte** |
| R2 Volume I full-report page | **20261114165129** | **1,614,913** | **`1c3018b4d17e205b`** | **NO — see repair 1** |

**All fifteen quoted spans in the body were checked one at a time against the served text**, not against the
draft, and every one is verbatim — including *"Each should therefore be examined in its own context"* with
the capital the register prints, and the doubled comma the draft already flags as the register's own.

**Every figure was read off the register's own rows rather than confirmed against the draft.** Table I.2.6
was read in full: Georgia 38/10/26, Cambodia 35/18/29, Jordan 32/20/26, Montenegro 32/13/5, UAE 26/15/21,
Saudi Arabia 23/5/1, Thailand 23/13/13, Türkiye 18/16/8, Philippines 17/20/16, **Qatar 2/−1/2**, OECD
average-35 −3/−14/−9. Table I.2.8: Qatar −0.8 and −0.1. Table I.2.9: Qatar 19/18/12, OECD average-35
−7/−27/−24. Table I.2.1: Qatar 434 and its seven-system comparison group. Table I.2.3: Qatar 434, OECD
average 482. The four-system table's order is the register's own, which ranks descending by the change in
science, and the 30-point spread is arithmetic on two rows of it.

### Repair 1 — R2's provenance triple does not reproduce, and the same triple was already SERVED

The draft inherited R2's row from the 11-26 bank: *snapshot of 16 November 2026, 1,614,913 bytes, sha256
`01b2bd4aa78bf802…`*. Measured today, twice: **the byte count is right and belongs to the capture of 14
November 2026 16:51:29 UTC**, whose hash is `1c3018b4d17e205b…`; the hash recorded reproduces from **no
capture of this page**; and `…/web/20261116id_/` today resolves to a *different* capture (20261116235912,
1,634,885 bytes) than it resolved to when the read was banked.

Two causes, both method rather than carelessness, both now written into the recon:

- **A Wayback request without a full fourteen-digit timestamp is resolved to the nearest capture, and which
  capture that is changes as the archive indexes more of them.** The date recorded was the date *asked for*.
- **One capture has three byte counts because it has three objects** — playback page, raw gzip, raw
  decompressed. For Chapter 2 they are 2,544,478, 279,017 and **2,426,000**. The third is the document the
  OECD served and the one the house cites; it is what reproduced R1, R3 and R8 to the byte this morning.

**This is a served defect, not only a draft one.** The same triple shipped two hours before this run opened,
in both editions of `2026-11-27-thailand-pisa-2025-fourth-list`. Both editions were repaired in this run and
the correction is stated in the annotation itself rather than made silently, because a published figure that
does not reproduce is a published wrong figure (#114 — a figure printed only in an annotation is still
published). Filed as **ruling #161**.

*What makes this worth the space: nothing was fabricated and nothing was stale. The URL resolved, the
document was the right document, and all six of that piece's quoted spans were verbatim. The only wrong
thing in the row was the evidence that the row could be checked again — and it read exactly like a row that
could.*

### Repair 2 — a row distance is a fact about a page, not about a table

The draft said the OECD average sat *"nine rows below Qatar's"*. **Table I.2.6 is printed as three panels
side by side**, so the served text runs across them: within Qatar's own panel the OECD average-35 row is the
twentieth against Qatar's fourth, and in the flattened text it is forty-eight entries later. Nine is not any
of those readings. The claim is deleted rather than corrected to a different number, and the piece now says
in one line why it gives no row distances. (#24, the position axis, on a layout instead of on a column.)

### Repair 3 — the share figures had no unit

*"The proportion of low performers in science changed by −0.8"* omits the ruler. The register's columns are
**"Change in percentage of low performers"** and **"Change in percentage of top performers"**: the figures
are **percentage points**, and the body now says so and names the columns.

### Repair 4 — a composite of rulers

The draft called −0.8 and −0.1 *"the smallest movements of any figure in this piece"*, ranking percentage
points against score points on one scale. Deleted, and replaced by a sentence saying in as many words that
the two kinds of figure are not comparable and that this piece does not rank them. (Standing prohibition:
no composite of rulers, #29/#30.)

### Repair 5 — 482 was attributed to a table that prints no such number

*"Table I.2.1 gives Qatar's science mean for 2025 as 434, against an OECD average of 482."* Table I.2.1
gives the 434. **It carries no numeric OECD average at all** — it sorts systems into three bands,
*significantly above*, *not statistically different from* and *significantly below* the OECD average. The
number 482 is in the chapter's **Table I.2.3**, whose first column is the same overall science mean (Qatar
434, OECD average 482), and in the report front page's own note 1: *"OECD average science scores fell from
489 to 482 points between 2015 and 2025."* Both are now cited for what each prints.

**And the repair paid for itself.** Note 1 and Table I.2.9's OECD average-35 row are the same fall on the
same decennial ruler, which gave the piece the one comparison it was missing: **Qatar 19/18/12 against the
OECD average-35's −7/−27/−24**, one measure, one span, no mixing. The draft had Qatar's decade and not the
average's.

Also repaired here: the comparison group is printed with the register's own marker, **Albania\***. The
chapter does not define the asterisk; it points to *Annex A2, "Population coverage, and school and student
participation rate standards"*, which was not read for this piece, so the mark is reproduced and explicitly
left uninterpreted rather than quietly dropped. A silently dropped marker is a dropped qualifier (#22).

## Test 2, specificity. PASS after repair 6

Place, span and instrument are named throughout: Qatar, 2015 to 2025 and 2022 to 2025, each table by number
and caption.

**Repair 6, the named human, and it is the same shape as yesterday's.** The draft named **no human at all**.
The Editor did not wave the test through on the ground that the registers are institutional; it went looking
for where a human was already load-bearing, and found one in the piece's own logic. **The press release's
both-ends list carries no period of its own.** The whole argument that Qatar's two list memberships are
ten-year ones therefore rests on one register and one speaker — **Mathias Cormann**, the OECD's
Secretary-General, in the remarks under the register's own title *"International launch of PISA 2025"* on 8
September 2026, marked **"Check against delivery"** and cited as the text as prepared. That dependency was
implicit in the draft and is now a paragraph.

**Gender:** no register read here carries a pronoun or a gendered title for Cormann, so the body carries
none, and the Arabic composer is instructed to avoid gendered verbs and gendered relative pronouns in the
same sentence (#86 clause 1 as amended by #134). The same applies to the OECD, which takes no person.

**And the Editor's own error, caught at this desk and recorded as the Editor's.** The first draft of that
paragraph placed the launch **in Geneva**. The word appears nowhere in the register — the page names no
venue at all — and it was composed because a global launch *sounds* like it has a city. It was removed before
the paragraph was read a second time. *A detail composed from plausibility reads exactly like a detail read
from a register, which is why the repair for repair 6 had to be checked the same way the draft was.*

## Test 3, why now. PASS after repair 7

PISA 2025 is eleven weeks old, the edition opened yesterday, and this piece exists because piece 1 printed a
hole and named what would fill it.

**Repair 7.** Paragraph two opened *"That piece said…"* with **no antecedent** — paragraph one never named
piece 1. A reader arriving at the sentence that carries the commission could not tell which piece was
speaking. *Three lists of risers* is now named in paragraph one, with its publication date, and again where
the decade list is explained.

Carried in the same repair: the both-ends list is now marked as a **ten-year** measurement at first mention
rather than four sections later. The piece's whole thesis is that a list is only as good as its clock, and
the draft stated two of the three clocks late.

## Test 4, dignity. PASS after repair 8

A senior Qatari educator would recognise the registers and the arithmetic. Three things were read
specifically for condescension and the posture holds: the piece offers **no cause** for any figure and says
so twice; it refuses to call the three years a success or a stall, because significance is carried in Table
I.2.6 by cell colour and a colour does not survive into served text; and it carries the chapter's
immigrant-composition instruction as the chapter's own instruction rather than as an explanation of Qatar's
results.

**Repair 8, and it is the sharpest thing the register had to offer.** The draft printed Qatar's two share
figures and never connected them to the membership they are about. Over 2022 to 2025 Qatar's share of low
performers in science is down **0.8 percentage points** and its share of top performers is down **0.1**. The
decade claim the OECD puts Qatar on is that it reduced low performers **and** increased top performers. Over
these three years the first half still holds and **the second does not.** The piece now says that, in the
register's own units, with the explicit statement that neither register contradicts the other — one is a
trend fitted across a decade, the other is the difference between two rounds, and the OECD prints both.

Leaving that out was the more comfortable draft and the less honest one. Printing it is also the opposite of
condescension: it credits the reader with the distinction the whole piece is built on.

## Test 5, the long arc. PASS

Edition 06's fourth piece and the second to be written off Chapter 2 — a register this operation read the
front door of three times across two days without opening a room. It extends the edition's method from
*which clock is this list on* to *which table is this number in*, and it is the first Qatar piece since
`2026-05-31-qatar-humanity-spark-strategy`, which it now rails back to.

## Measured at compose

- Title **34**/100 code points. Dek **196**/200.
- Body **1,584** words after repairs (1,157 before), inside the brief's 1,300 to 1,800.
- Fifteen quoted spans, every one verbatim against served text in this run.
- Four tables read in full; 41 figures in the body, every one traceable to a named table and column.

## Hand-off lines, checked

| Line | State |
|---|---|
| `dek: 196/200 · title: 34/100` | present |
| `annotation == sentence` per leaned-on source | **re-run by this desk** on all five; repairs 3, 5 and the Albania marker are three places it had drifted |
| `named humans — gender read from register: 0 of 1` | Cormann, no pronoun or gendered title in any register read, so no gendered construction in either edition |
| `acronyms expanded in the body: 0` | the body expands none; *OECD* and *PISA* appear as the registers print them |
| `cross-language pairs: 0` | none |
| `editorial futures: 1` | *"When Qatar's own authority publishes its reading of PISA 2025, it will be a different piece"* — a statement about this publication's own future conduct, carrying no register's claim and no date; allowed, and it is the only one |

## Prohibitions in the brief, checked one by one

| Brief's prohibition | Held? |
|---|---|
| No statement about Qatar's score between 2022 and 2025 without a register that prints it | **Superseded by the register arriving.** Chapter 2 prints it; every such statement in the body is Table I.2.6's or I.2.8's, by name. |
| No inference from the absence | **Held.** The body says Qatar *"is not among the systems the OECD counts as having raised their science average since 2022"* and nowhere says it fell or was excluded. |
| No comparison of Qatar with Jordan, Saudi Arabia or the UAE **across different lists** | **Held, and this is the piece's own device.** The four-system table is **one** table, one question, one three-year span — which is exactly what the prohibition was protecting. |
| Every figure carries scale, years and whose average | **Held after repairs 3 and 5**, re-read sentence by sentence. |
| No claim of statistical significance on this register's authority | **Held**, stated in the body and in the annotation. |

## Owed next

Cell 4, the Arabic composition, with the gender instruction above and with the three-panel note handled as
prose rather than as a layout claim; cell 5, the Arabic Editor's gate, which also owes the Arabic rendering
of the chapter's table captions; cell 6, the Verifier, **whose first job is to re-read Table I.2.6 and Table
I.2.8 independently of this verdict** — repairs 2 and 5 are both position errors, and position is what a
second reader catches; cell 7, hero still and share card; cell 8, the flip with forward rails into
`2026-11-26-pisa-2025-three-lists-of-risers` and `2026-05-31-qatar-humanity-spark-strategy`.
