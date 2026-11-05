# The Arabic register read — Bahrain, five cycles of the BQA's own grades

**Arabic Content Creator · 2026-11-05 · the first step of the composition, and it stopped the composition.**

Commission: `content-drafts/briefs/2026-10-21-bahrain-bqa-five-cycles-brief.md`
EN draft: `content-drafts/drafts/2026-10-23-bahrain-bqa-five-cycles.md` (Editor-approved 2026-11-02,
Verifier verdict 2026-11-03, archival coverage read 2026-11-04)

The draft's hand-off to this desk is one instruction: **"Compose from the Arabic column of the same
CSV, never from this draft."** That instruction was followed before any Arabic prose was written, and
**the read disagrees with the English draft about three of its four populations.** Nothing is composed
today. What follows is the read.

## 1 · What was read, and how

The Authority publishes the dataset through the portal's own export API, which serves it **per
language**. Both exports were taken today, within one minute of each other, and neither was taken
from the other:

| | URL | HTTP | Bytes | sha256 |
|---|---|---|---|---|
| **AR** | `https://www.data.gov.bh/api/explore/v2.1/catalog/datasets/01-results-of-government-schools-reviews-1/exports/csv?lang=ar&timezone=Asia%2FBahrain&use_labels=true&delimiter=%3B` | 200 | 122,633 | `1285778e3864f422…` |
| **EN** | same path, `lang=en` | 200 | 72,925 | `f10d992a40c6b7bf…` |

Header, Arabic: `دورة المراجعة ؛ تاريخ النشر ؛ نوع المراجعة ؛ اسم المدرسة ؛ الدرجة`.
**Row order is identical across the two exports** on cycle and publication date, row for row, all
1,022 — so the two files are two renderings of one table and the comparison below is a comparison of
columns, not of datasets. *(The byte lengths are not the draft's 183,191: the draft reads the portal's
own download link and this desk read the v2.1 export endpoint with `;` delimiters and labelled
headers. Two routes to one table, and the counts below are the test of whether they agree — not the
byte lengths, which cannot agree by construction.)*

## 2 · What the Arabic column CONFIRMS, cell for cell

Counted from the Arabic bytes by this desk, with no reference to the draft's table:

* **1,022 rows.** Row types: `مراجعة الأداء` **882**, `زيارة المتابعة 1` **61**, `زيارة المتابعة 2`
  **34**, `زيارة المتابعة` **45** — 140 monitoring rows in three types, as the draft states.
* **The four numbered grades appear on review rows only.** Monitoring rows carry the three-band scale
  exclusively: `(B) قيد التقدم` 97, `(C) تقدم غير كافٍ` 23, `(A) تقدم كافٍ` 20.
* **Grade totals over the 882 reviews:** `(3) مرضٍ` **350**, `(4) غير ملائم` **245**, `(2) جيد`
  **202**, `(1) ممتاز` **85**.
* **The per-cycle distribution — every cell, and the publication windows:**

| Cycle | Reviews | `(1) ممتاز` | `(2) جيد` | `(3) مرضٍ` | `(4) غير ملائم` | Published |
|---|---|---|---|---|---|---|
| C1 | 202 | 7 | 60 | 94 | 41 | 2009-06 → 2011-05 |
| C2 | 206 | 14 | 48 | 89 | 55 | 2012-02 → 2015-03 |
| C3 | 207 | 31 | 39 | 70 | 67 | 2015-09 → 2019-04 |
| C4 | 128 | 10 | 25 | 41 | **52** | 2019-06 → 2023-12 |
| C5 | 139 | 23 | 30 | 56 | 30 | 2024-07 → 2026-04 |

**This is the piece's spine and it is confirmed by an independent count in the other language.** Every
grade label is a **forced rendering** (#101) printed by the Authority in the same row, and every one
matches what the draft carries for the Arabic edition. C4's 52 of 128 — the only cycle in which
`(4) غير ملائم` is modal — is in the Arabic column exactly as it is in the English.

## 3 · What the Arabic column CONTRADICTS — three of the four populations

The draft's four populations are **245 schools in the register · 242 ever graded · 76 in all five
cycles counting monitoring visits · 52 reviewed in all five.** Counted the same way over the Arabic
column of the same 1,022 rows:

| Population | EN column | AR column |
|---|---|---|
| Distinct school names in the register | **245** | **248** |
| Distinct names ever *reviewed* | **242** | **245** |
| Names appearing in all five cycles (all row types) | **76** | **75** |
| Names *reviewed* in all five cycles | **52** | **52** |
| Cycle coverage over the reviewed set | 52 / 124 / 22 / 15 / 29 | 52 / 125 / 20 / 14 / 34 |

**The cause is that the register has no identifier column.** Cycle, date, review type, school **name**,
grade — five fields, and the only thing that can join a school to itself across seventeen years is the
name string. The two language columns do not partition the same way:

* **Eleven English names map to two Arabic names each** — the Arabic column writes the same school
  with and without the `مدرسة` prefix (`أم أيمن الابتدائية للبنات` / `مدرسة أم أيمن…`,
  `الضياء`, `المستقبل`, `البسيتين`), with `إ` and `ا` alternating in `الإعدادية` / `الاعدادية`
  (عراد, صفية بنت عبدالمطلب, الرفاع الغربي), with `عبدالرحمن` and `عبد الرحمن` as one word and two, and
  once with a **double space** inside `مدرسة  ابن طفيل`.
* **Six Arabic names map to two or three English names each** — transliteration variants on the
  English side: *Aminah / Aamna / Amina* Bint Wahab, *West Rifaa / West Riffa*, *Al-Khawarizmi /
  Al-Khawarezmi*, *Abu Bakher Al Seddiq / Abu Bakr Al-Siddeeq*, and — not a spelling variant at all —
  **`National Charter Intermediate Boys School` and `Bahrain Charter Intermediate Boys School` on one
  Arabic name.**

**So a count of distinct schools in this register is a count of NAME STRINGS, and the two editions of
one register disagree about how many strings there are.** A name-keyed join splits one school into two
wherever a spelling moved, which **overstates the school count and understates multi-cycle coverage** —
the draft's *52 of 242 reviewed in all five* is therefore a **floor**, not a count, and *"a sentence
beginning 'the same schools, five times' would be false for 190 of the 242"* is arithmetic over a
denominator the register does not supply.

### 3a · And normalising does not rescue it — the agreement it produces is a coincidence

Normalising the Arabic (strip the `مدرسة` prefix, unify `أ إ آ → ا`, `ى → ي`, `ة → ه`, collapse runs
of spaces) brings the reviewed-name total to **242 — the English figure exactly.** The partition still
disagrees:

| Cycle coverage over the reviewed set | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|
| EN column, as read | 52 | 124 | 22 | 15 | 29 |
| AR column, normalised to the same total | 52 | **126** | 22 | **10** | **32** |

**Two columns that agree on the total and disagree on the partition cannot be reconciled by spelling.**
The disagreement is in which rows belong to which school, and no amount of normalising a string can
settle that. *(And the normalisation is ours — our arithmetic over somebody else's orthography, which
is the thing a figure cited as read may never be.)*

## 4 · One row where the two columns disagree about the SCHOOL, not the spelling

Eight rows carry an `الروضة` / `Al-Rawdha` name. Seven agree on the school's sex in both columns.
One does not:

| Cycle | Published | EN column | AR column |
|---|---|---|---|
| C1 | 2010-06 | Al-Rawdha Primary **Girls** School | …الابتدائية **للبنات** |
| C1 | 2010-11 | Al-Rowdha Primary **Boys** School | …الابتدائية **للبنين** |
| C2 | 2013-10 | Al-Rawdha Primary **Girls** School | …الابتدائية **للبنات** |
| C2 | 2015-01 | Al-Rawdha Primary **Boys** School | …الابتدائية **للبنين** |
| C3 | 2017-10 | Al-Rawdha Primary **Girls** School | …الابتدائية **للبنات** |
| C3 | 2018-06 | Al-Rawdha Primary **Boys** School | …الابتدائية **للبنين** |
| **C5** | **2024-12** | Al-Rawdha Primary **Girls** School | **…الابتدائية للبنين** |
| C5 | 2025-03 | Al-Rawdha Primary **Girls** School | …الابتدائية **للبنات** |

**The December 2024 verdict is attached to the girls' school in English and to the boys' school in
Arabic.** This is not a transliteration question and neither column can be preferred — it is the
Authority's own table disagreeing with itself about which school received a grade, on a row inside the
open cycle. It is recorded here, it is **not** reported in either edition (the piece names no school
by its grade — Test 4 — so the contradiction is not load-bearing for anything the piece says), and it
is the sharpest available evidence that the name is not an identifier.

## 5 · The park condition, and what actually fired

The draft states a park condition in writing: *"If 245 / 242 / 76 / 52 cannot be held apart in Arabic
without a construction the Arabic Editor will not pass, that is a stated park condition and it fires."*

**On its own terms it did not fire.** The four populations can be held apart in Arabic perfectly well;
`عدد المدارس المدرَجة في السجل` and `عدد المدارس التي رُوجعت في الدورات الخمس` are different noun
phrases and the Arabic Editor would pass either. **What fired is a condition on the same four numbers
that nobody wrote down: three of them are different numbers in Arabic.** The specification was not the
scope, for the thirtieth time in this operation's record — and the thing that found it is the
instruction to compose from the register rather than from the draft, which is #101's mechanism
(*a forced read, not an optional one*) doing exactly what it was written to do, one step earlier in the
pipeline than it has ever done it before.

## 6 · What this desk recommends, and to whom

**To the Editor, because it changes what the piece says and not how it is worded.** Two of the four
populations are load-bearing in the English body as drafted (hedge 3, *not a panel*; and the paragraph
beginning *"The third thing is a population boundary"*). The recommendation is **(a)**:

* **(a) Strike the name-keyed counts from both editions and restate hedge 3 without a denominator.**
  What the register supports is *a school that appears in one cycle need not appear in the next, and the
  register supplies no identifier by which to say how often that happens.* The piece loses two figures
  and gains the reason they cannot be given — which is the same move the piece already makes about the
  ruler in hedge 4, and it is strictly more honest than either number.
* **(b)** Report both columns' figures side by side with their keys named. Rejected by this desk: it
  prints four numbers to say that none of them is a school count, and a reader cannot use any of them.
* **(c)** Normalise, merge, and report the reconciled partition. Rejected on the house rule — the
  merged figure is **our** arithmetic over the Authority's orthography, and §3a shows it does not even
  reconcile.

**Nothing is composed in Arabic until the disposition lands**, because the two sentences that would
carry these numbers are the two the Arabic Editor would have to gate, and composing them against a
denominator under review is the 2026-09-13 defect written on purpose.

---

**Signed** · Arabic Content Creator · 2026-11-05 · *the spine was confirmed in the other language,
cell for cell, and the populations were not; both of those are results of the same read.*
