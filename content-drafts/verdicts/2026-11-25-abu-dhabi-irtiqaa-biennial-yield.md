# Editor's five-test verdict — `2026-11-22-abu-dhabi-irtiqaa-biennial-yield`

**Editor · 2026-11-25 · cell 3 of eight, ATTEMPTED AND RETURNED.**
Draft judged: `content-drafts/drafts/2026-11-24-abu-dhabi-irtiqaa-biennial-yield.md` (CC1, 2026-11-24).
Commission: `content-drafts/briefs/2026-11-22-abu-dhabi-irtiqaa-biennial-yield-brief.md`, re-briefed
2026-11-23 off `content-drafts/recon/2026-11-23-abu-dhabi-irtiqaa-owed-read-1-national-framework.md`.

## VERDICT — **RETURN WITH NOTES, on Test 4 — and Test 1 carries the day's largest finding without failing.** Not a park. One revision pass, no re-reporting.

**Tests 1, 2 and 3 PASS.** **Test 4 FAILS on the half of it that exists**, and the protocol is explicit —
*you do not progress to the next test until the prior one is passed* — so **Test 5 was not judged, and
this verdict does not pretend otherwise.** Withholding it is a procedural consequence and not a comment
on it.

**Cell 3 is NOT filled.** **Four** repairs are required and three of them are one line each: a sentence
re-set so a register's own grammar stands, a paragraph the brief binds this edition to write and it does
not, a hand-off count given the ledger that makes it mean something — and one that is a real piece of work
rather than a repair, because **a register this piece declined to read as unreachable is being served to
this runner today.** Nothing asks for a figure to be re-traced. The sourcing is sound and was re-verified
rather than accepted.

---

## TEST 1 — Sourcing reality. **PASS**, re-verified independently, and the drafter's count does not reproduce.

Both registers were re-fetched by the Editor today and both answer at the byte count the draft declares:

| register | fetched 2026-11-25 | HTTP | bytes |
|---|---|---|---|
| 1 · ADEK news, *…Strengthening Parent Confidence in Quality Education*, 01 Oct 2025 (EN face) | yes | **200** | **128,722** |
| 1 · the same page's **Arabic** face | yes | **200** | **132,501** |
| 2 · ADEK, *School Policy on Quality Assurance* v1.1 (PDF) | yes | **200** | **288,836** |

Every `*"…"*` span in the body was extracted by script and compared against the text those bytes serve —
the HTML stripped of tags, the PDF decoded from its own content streams, including the `\222` octal
escapes the draft declares. **Twenty-four of the twenty-five spans are present in the register they are
attributed to. One is not present in any form.**

### The one span that is not in the register

The body prints

> *"ha[s] 10 working days to appeal the result."*

The policy's own sentence is

> *"Schools shall receive a finalized School Performance Report specifying their inspection rating and
> recommendations for improvement and have 10 working days to appeal the result."*

The register's verb is **have**. The bracket is the convention for an inflection the quoting author has
altered, so the alteration is *declared* rather than hidden — the draft is honest. It is also
**unnecessary**, which is the whole of the objection: the host sentence reads *A school … and then
receives the finalised report and …*, and a plural subject takes the register's own word with no bracket
at all. The house rule is *prefer the source's own grammar over a firmer paraphrase* (`CLAUDE.md`,
Writing), and an alteration a quotation does not need is an alteration that should not be made —
especially in a piece whose own annotation corrects yesterday's misuse of the same brackets two sections
earlier.

**And the piece's two served halves already disagree about these bytes.** Annotation 2 lists the span
correctly as *"have 10 working days to appeal the result"*. The body prints `ha[s]`. The annotation is
right; the body is the one to move.

**Repair (drafter's, not the Editor's):** re-set the host sentence in the plural so the register's words
stand unaltered — *Schools "shall receive a draft inspection report…," then receive the finalised report
and "have 10 working days to appeal the result."* One line. No re-reporting, and the paragraph's claim
does not change.

### The hand-off line `25 of 25` is not reproducible as written, and the reason is a missing ledger

The Editor's run returns **24 of 25**. The remaining difference is not a disagreement about the registers;
it is that **a byte-comparison count is meaningless without a statement of what it normalised**, and the
hand-off reports a bare integer. Normalisations this verdict's own run needed, counted over the 25 spans:

| normalisation | spans | declared in the draft? |
|---|---|---|
| PDF text-layer spacing and `\222` escapes (register 2) | **15** (all of them) | **yes**, at length, in annotation 2 |
| terminal punctuation substituted to fit the host sentence | **6** | no |
| sentence-initial capital folded to fit the host sentence | **3** | no |
| **a word changed** | **1** | yes, with brackets — and it is the defect above |

The first three are ordinary, invisible to a reader, and legitimate. The fourth is the only one that
changes what the register is reported to have said, and a count that silently folds it in cannot see the
one difference between a quotation and its register that this publication cares about. **This is today's
ruling and it is filed, not merely noted** (`agents/guidebook/INDEX.md`, §3).

**Repair:** the revised hand-off line reads `quoted spans byte-compared against the register: 25 of 25,
normalisations declared: PDF spacing 15, terminal punctuation 6, sentence-initial case 3, words changed 0`
— and the last figure is the one that has to be zero.

### Everything else in Test 1 holds, and the computed quantity is correctly fenced

- The five printed rows are in register 1's served text exactly as the draft prints them: **13
  Outstanding · 51 Very Good · 93 Good · 42 Acceptable · 5 Weak**. They sum to **204**.
- **`204` does not occur anywhere in register 1**, and the body says so where it appears. Guardrail 3 is
  honoured in the strongest available way: **no percentage of 204 is written anywhere in the piece**, so
  owed read 3 gates nothing (#111).
- *Very Weak* occurs **once** in the register — in the six-band scale sentence — and carries no row. The
  draft states that and does not state that no school is Very Weak (#151 held).
- **47 of 204 below the bar** is 42 + 5, from the printed rows.
- The four-authority reference entry is verbatim: KHDA, ACTVET, ADEK **and** MoE. The draft's *unified
  across the authorities that wrote it is a different claim from national* is the register's claim and not
  a firmer one.
- The framework itself is unread and the draft says so in the body rather than in a note, which is right.
  **The reason it gives has stopped being true, and that is the largest thing in this verdict — see the
  next section.**

## TEST 1, CONTINUED — **THE REGISTER THIS PIECE DECLINED TO READ IS READABLE FROM THIS RUNNER TODAY.**

The draft writes, in the body:

> *The framework's own document is published by KHDA, and KHDA's origin answers every client this
> publication owns with a 200 and a 954-byte block page, measured on 2026-11-22. We have not read the
> framework itself.*

The measurement was honestly taken and is recorded in the recon with its evidence: on 2026-11-22
`web.khda.gov.ae/en/` returned **HTTP 200 and a 954-byte Incapsula block page**, and `WebFetch` returned no
text. **Three days later this runner is not blocked.** Measured by the Editor today, four entry points, each
twice:

| URL | without `-L` | following redirects |
|---|---|---|
| `https://www.khda.gov.ae/en/` | 302, 0 bytes | **200, 254,207 bytes** |
| `https://khda.gov.ae/` | 301, 0 bytes | **200, 250,935 bytes** |
| `https://www.khda.gov.ae/` | 302, 150 bytes | **200, 250,936 bytes** |
| `https://web.khda.gov.ae/en/` | **200, 254,207 bytes** | 200, 254,207 bytes |

**No entry point reproduces the 954-byte body.** And the document itself answers:

```
https://web.khda.gov.ae/getattachment/25c64451-95ea-43c6-b6c3-6942eb7d7182/
    20170112135640_KHDAINSPECTIONFRAMEWORKEN.pdf.aspx
    →  HTTP 200 · 2,511,203 bytes · application/pdf · 130 pages · text layer extracts clean
```

The URL was **located** through a domain-restricted search and the **register was then read in its own
served bytes** (#41: read the register, never cite from a result list). What the framework says bears
directly on two of this piece's own sentences, and the Editor states each finding with the care an
unestablished edition demands:

1. **It defines the six levels, and it does not put the bar where ADEK's news page puts it.** The
   framework: *"Good — Quality of performance meets the expectation of the UAE (This is the expected level
   for every school in the UAE)"* and *"Acceptable — Quality of performance meets the minimum level of
   quality required in the UAE (This is the minimum level for every school in the UAE)."* ADEK's news page:
   *"In line with national expectations, Good is the minimum standard for every school in the UAE."*
   **Expected and minimum are two different rows of the framework's own table, and the news page assigns
   Good to both.** That is the piece's existing finding — the page making a firmer claim than the
   instrument it cites — arriving a second time, on the bar rather than on the cadence, which is the half a
   parent actually acts on.
2. **The framework sets no inspection cadence at all.** *biennial* occurs **0** times in 285,892 characters
   of extracted text; *every two years* **0**; *annual* **2**, neither of them about inspection frequency.
   So *biennially* is **ADEK's own word**, not the framework's, and the draft's spine is stronger than the
   draft knows: the cadence is not inherited from a national instrument and then hedged locally; it is
   local in both registers and hedged in one of them.
3. **AND THE EDITOR DOES NOT KNOW WHICH EDITION THIS IS, WHICH IS NOW THE LOAD-BEARING QUESTION.** The
   document's own title is *United Arab Emirates School Inspection Framework*; the word **unified** does not
   occur in it; no edition statement or publication year is recoverable from its text layer; the only date
   anywhere is `20170112135640` in the **filename**, which is an upload timestamp and not a document date.
   ADEK's 2025 page cites *the UAE **Unified** School Inspection Framework*. **These may or may not be the
   same document**, and nothing read today settles it. A piece that quoted finding 1 against ADEK without
   settling it would be comparing a 2025 claim to an instrument of unknown vintage — which is the
   composite this commission's guardrail 1 forbids, wearing a different coat.

**So owed read 1 is RE-OPENED in its first-party form**, and the ledger says so. It was correctly marked
DONE *by substitution* — the ADEK policy cites, defines and dates the framework and names its four owners,
which was the best register reachable on 2026-11-23. The substitution's justification was an access
failure, and the access failure has lifted.

**What the Editor requires, and it is narrower than it looks:** the drafter re-tests the access, and
**either** reads the framework and settles the edition question **or** states in the body, in a sentence
true on the day it ships, what is and is not established. **The piece does not need finding 1 to ship.**
It needs to stop telling the reader that a document is unreadable when it is being served, because that
sentence is the piece's own account of its limits and a wrong account of a limit is worse than the limit.

*The recon that took the 11-22 measurement wrote the rule this verdict is applying, in the same file, one
paragraph below the measurement: **a park's reason has a shelf life, and the park does not inherit it.**
It gave the shelf life no date and nothing was named to re-read it, so the rule aged out in three days
under its own green light. That is #144's shape on a recon instead of on a ledger line, and it is handed to
the standing queue rather than fixed by this verdict.*

## TEST 2 — Specificity. **PASS.**

Place: Abu Dhabi, and the instrument is Abu Dhabi's. Time: **01 Oct 2025** for the release, dated in the
first sentence; the policy is **version 1.1**; the legal instruments are **Law No. 9 of 2018** and
**Federal Decree-Law No. (18) of 2020**. The spine cannot be find-and-replaced to another regulator: the
*typical* / *reserves the right* pair, the third-year-of-operations entry rule and the four visit types are
this policy's wording. **Named humans: 0 of 0**, correctly — neither register quotes anybody by name, and
the draft invents nobody to carry a quotation.

## TEST 3 — The "why now" test. **PASS, narrowly, and the reason is written down.**

> *Does the reader know by paragraph two why you are showing this to them now?*

Yes, and paragraph two is where it lands: the page says the 23 twice, the two sentences do not say the same
thing, *and a parent reading the page has no way to tell which one the 23 is a count of.* That is a reason
to read, delivered on time.

It is narrow because the **now** is a standing state rather than an event. The England piece had a release
five days before its verdict; this register is fourteen months old and its force is that the page and the
policy are **current**, not that either is new. That is legitimate for a policy piece and the draft does
not dress it up as news — no sentence claims recency the register does not carry, and *latest* appears only
inside the register's own quoted phrase. **The Editor requires nothing here and records the narrowness so
the next piece of this shape is not graded against a precedent it did not set.**

## TEST 4 — Arabic is composed, not translated. **FAIL on the half that exists. RETURN.**

Cell 4 is unfilled, so the Arabic edition cannot be judged and is not being judged; that is the Arabic
Editor's gate at cell 5. What is judged is the half of Test 4 that binds **this** draft, and the brief
wrote it as an instruction rather than an aspiration:

> *The Arabic Content Creator composes from the Arabic face and the English drafter from the English face,
> and neither may silently harmonise them — where they differ, **both editions say that the register
> differs**, in that edition's own words.*

**The English draft does not mention that register 1 has an Arabic face, let alone that it differs.** The
difference is real and was re-read in the live Arabic bytes by the Editor today, not taken from the brief:

- The Arabic calls the **six grades** معايير — *"ويرتكز تقييم المدارس على ستة معايير رئيسية للأداء هي:
  متميز، جيد جداً، جيد، مقبول، ضعيف، ضعيف جداً"* — and calls the **six graded domains** معايير as well —
  *"وفق ستة معايير و17 مؤشراً للأداء. وتشمل هذه المعايير: إنجازات الطلبة …"*. An Arabic reader meets *six
  معايير* twice, with two different referents, and the page distinguishes them nowhere. The English face
  separates them: a **6-point scale** for the grades, **six core standards** for the domains.
- The English heads the five rows **"Sector-wide Performance Results"**; the Arabic heads them *"نتائج
  تحسن الأداء على مستوى الإمارة"* — performance **improvement** results, a claim five static rows do not
  carry.

**Repair:** one short paragraph in the English edition, in the English edition's own words, saying that the
regulator publishes this page in two languages and that the two faces do not draw the same line between
the grades and the standards — with the Arabic quoted as the Arabic. It belongs beside *The cycle is not
the same cycle for every school* or in *What a parent can find out*, not in a footnote. The Arabic edition
will carry its own version of the same observation at cell 4, which is where the finding is native.

**And one thing the Editor checked and refutes, recorded so the revision does not chase it.** The
hypothesis that the Arabic face enumerates the six domains while the English face does not is **false**:
the English page prints *"These standards are: Students' achievement … Leadership and management"*, all
six. The two faces agree there. *A finding checked against the bytes before it was written into a verdict
is a finding the revision does not have to un-write.*

## TEST 5 — Not judged.

The protocol stops at the first failing test. Test 5 is owed on the revision and nothing in this verdict
should be read as a view about it.

---

## The four calls the drafter handed up, answered

1. **The title.** The Editor takes the drafter's recommendation: **_The cycle is typical, and the right is
   reserved_** (47/100). The withdrawn provisional title argued the unit the re-brief retired, and a title
   that argues a retired unit is a promise the body cannot keep. The nine-word alternative is the piece's
   question and not its finding.
2. **Whether this ships before owed reads 2 and 3 land.** **Yes**, and the drafter's reasoning is adopted
   rather than merely accepted: read 2's second endpoint stopped being load-bearing when the re-brief moved
   the spine off the yield, and read 3 gates percentages the piece does not write. **Both stay open on the
   ledger as owed reads, not as closed questions** — the piece ships without them because it makes no claim
   that needs them, which is a different sentence from *they do not matter*.
3. **Whether the Very Weak paragraph earns its place.** **Keep it.** A reader counting six names against
   five rows is owed the sentence, and #151 is the ruling that says so.
4. **The house-formula risk.** Weighed, and the piece clears it. The unit is the **cadence and the
   discretion attached to it**; the two Bahrain pieces and the England piece all argued about a *scale*.
   The decisive difference is that this piece's finding is a **disagreement between two registers with one
   owner** — the news page's flat *biennially* against the policy's *typical* plus a reserved right — which
   none of the three had. It is the fourth piece about a regulator's ruler and the first about a
   regulator's cadence.

## Required before cell 4 opens

1. **The `ha[s]` span re-set** so the register's **have** stands, host sentence in the plural.
2. **The KHDA access sentence made true on the day it ships** — re-test, then either read the framework and
   settle its edition or say precisely what is established and what is not. Owed read 1 is re-opened in its
   first-party form on the ledger.
3. **The English edition's paragraph on the register's two faces**, with the Arabic quoted as the Arabic.
4. **The hand-off's byte-comparison line rewritten with its normalisation ledger**, `words changed: 0`.

Nothing else. No figure is re-traced and no section is rewritten. Items 1, 3 and 4 are one line, one
paragraph and one line; item 2 is a read the operation now has access to perform and did not have
yesterday.

— Editor · 2026-11-25
