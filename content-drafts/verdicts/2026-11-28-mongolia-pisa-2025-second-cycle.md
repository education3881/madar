# Editor's verdict, cell 3 — `2026-11-28-mongolia-pisa-2025-second-cycle`

**PASS with FIVE repairs, all closed in-run. Title TAKEN as drafted. Six registers, where the draft arrived with five.**

Read at the Editor's desk 2026-11-28 by the evening content run. Every register re-reached from a clean
directory with a different user agent; no figure and no span was taken from the draft, the recon or the
hand-off.

---

## Test 1 — Sourcing reality. **PASS, after one real repair and three disclosures**

### What was re-reached, and how

| Register | Re-read | Result |
|---|---|---|
| R1 `https://eec.mn/` | **direct, second independent fetch** | **200, 574,233 bytes** — the count reproduced |
| R2 the national report PDF | **direct, re-tested** | **404, 8,388 bytes** — reproduced |
| R3 the archived greeting | capture `20260417030826` | **200, 110,004 bytes** — reproduced to the byte |
| R4 Chapter 2 | capture `20261104162528` **and a SECOND independent capture, `20260910092914`** | 2,426,000 bytes / sha256 `e5a429b0…` reproduced (**fifth time**); the second capture 2,422,806 bytes, sha256 `a7b1df1938beee4d2422ecb058133b42e9fc5e7662466468e98cc3d06a120403` |
| R5 the full-report front door | declared capture, **re-fetched and re-hashed** | 1,614,913 bytes, sha256 `1c3018b4…` reproduced; its risers span and `bucking the trend` both verified |
| **R6 the launch press release** | **ADDED AT THIS CELL** — capture `20261115232402` | **1,468,371 bytes**, sha256 `096bb651…`; see repair 5 |
| `www.oecd.org` direct | **re-tested in this run** | **403.** Not routed around |

**Spans: 10 of 10 Mongolian verbatim** in the re-fetched register. **15 of 15 OECD spans verbatim in BOTH
captures**, and after repair 5 below, **15 of 15 bold-quoted spans in the body matched to a cited register** — including all three of I.2.9's note sentences, which this piece turns on.

**Figures: every one re-derived from the second capture, and every one agrees.** I.2.1 424 with its
eight-system not-different list in the table's own order; I.2.3 424 · 425 · 421 · 421 against 482; I.2.4
443; I.2.6 12 · −4 · −6 against −3 · −14 · −9; I.2.8 −6.6 · 0.1 against 1.2 · −0.3; I.2.10 19 · 8 · −11
against 5 · −8 · −13; I.2.11 −11.4 · −2.2 · 0.0 · 0.4; I.2.12 16 · 7 · −9 against −2 · −3 · −1; I.2.13
−8.7 · −4.3 · 0.2 · 0.0.

**All four derived counts reproduced on the second capture**, which is the only reading that matters since
the hand-off's figures cannot verify themselves: I.2.6 **75 entries / 74 systems**, science up in **30**,
all three up in **12**, science up with reading and mathematics both down in **13** with **Mongolia largest
at 12 and Uruguay next at 9**, **11 above and exactly 3 at 12**. I.2.10 **74 entries / 73 systems**,
narrowed in **49**, **34** with the advantaged falling, **15** with both rising. The sweep: **29
occurrences, nine tables, I.2.9 absent** — and the second run located each occurrence by byte offset
against the fourteen `<table>` spans rather than by reading rows, so the two runs do not share a method.
*A derived count is the one kind of claim in this corpus that no outside register can falsify for us, which
is exactly why it is re-derived rather than re-read.*

### REPAIR 1 — the real one. **The draft gave one cycle's legal basis to both cycles**

The draft opened: *"Mongolia sits the Programme for International Student Assessment because a law says it
must."* **The register does not say that.** It gives the two cycles **two different bases**, in two
consecutive sections, and the draft read the second one and generalised.

- **2025** — General Education Law article 35.6, quoted: every three years, by an authorised international
  body. This is what the draft has.
- **2022** — not a statute at all. The government's state education policy for **2014–2024**, section 7,
  which specified that Mongolia would take part **in 2021**; and then, in **September 2018**, a contract
  signed by the ministry with the OECD to take part in **PISA 2022**.

This is axis **#22** exactly — *does a shared qualifier govern both falls, or one?* — on a legal basis
instead of a figure, and it is the sort of error that survives every check that looks at numbers. **It
also cost the piece a better fact than the one it printed:** between Mongolia's two cycles the basis for
sitting PISA moved **from a policy target to a statutory interval**, and the policy target was for 2021
and was met in 2022. *A country whose first sitting was a year late against its own policy and whose
second was compelled by statute is a sharper opening than a country with a law*, and it makes the title do
work the draft left it standing next to.

**Repaired in-run.** The opening now carries both bases, in the register's order, with the statute attached
to the cycle the register attaches it to.

### REPAIR 2 — R1 declares no sha256, and must say why it cannot

`eec.mn/` was fetched twice. **Both responses are 574,233 bytes and their sha256 digests differ** —
`1a38b30baf557cfda1eca8536617cafd6cd964643efb89bc705c73b603094dc3` and
`e385df2e19e170ef9bcf5a96e8dbf523a8d4f23ef00779b2cfcc5054c110a3e9`. The PISA page's decoded text is
**byte-identical across the two, 15,722 characters**, and a diff of the raw documents returns **five short
hexadecimal substitutions and nothing else** — a per-response nonce, netting to zero length.

**So this register's content is reproducible and its bytes are not.** Every other register in this piece
carries a hash; a reader who notices that this one does not is owed the reason, and the reason is a
positive finding rather than an omission. *A hash that cannot be reproduced is worse than no hash, because
it invites exactly one re-run and then reads as a discrepancy in the document rather than in the server.*
**Repaired in-run:** R1 now declares the reproduced byte count, the absence of a hash, and the nonce.

### REPAIR 3 — "verbatim" is not what this corpus has been checking, and it is not this piece's fault

The chapter serves **`boys’ performance`** with U+2019. The draft writes **`boys' performance`** with
U+0027, in the body and in the annotation. The span is therefore not verbatim as the hand-off claims.

**Before treating that as a defect, the corpus was counted.** Across the three Edition 06 pieces checked —
Saudi Arabia, Uzbekistan and *Three lists of risers* — there are **zero occurrences of U+2019 and zero of
U+201C**, and between 58 and 149 ASCII apostrophes. Every one of them already quotes OECD spans containing
apostrophes (`economies' performance`, `students' performance`) in ASCII, from a register that serves
U+2019. **So folding Unicode punctuation to ASCII is an established, corpus-wide convention, this piece
follows it, and it is written nowhere in the repository** — not in `docs/40_voice_and_style.md`, not in the
Content Creator's persona, nowhere.

**The defect is in the sentence, not in the bytes.** Every `N of N verbatim` this publication has printed
means *verbatim after Unicode punctuation is folded to ASCII*, and nothing has ever said so. **Repaired in
this piece by disclosure:** R4 now states the folding and names the one span it applies to. **The general
case is named for the standing queue and not built here** — this is a content run, the convention is right,
and what is missing is one line of written house rule plus a decision about whether the span checks should
report the fold. *A check whose report is truer than its wording is the cheapest kind of wrong to live with
and the easiest to stop noticing.*

### REPAIR 4 — the 2022 cohort did questionnaires too

The draft has the 2022 students *"working through mathematics, science, reading and creative thinking on
computers."* The register says **`даалгавар болон асуулга судалгааг`** — tasks **and** questionnaires. Small,
and it matters only because the piece's own later point is about which questionnaires Mongolia added in
2025; a reader who is told 2022 was tasks only will read the 2025 addition as larger than it was. Repaired.

### REPAIR 5 — the expensive one, and no human found it. **The body quoted a register the draft did not cite**

After the four repairs above were applied, every bold-quoted string in the body was extracted
mechanically and tested against all five declared registers, in two independent captures where two exist.
**Thirteen of fourteen matched. One matched nothing** — the clause the whole equity section is built on:
*"largely because advantaged students performed less well rather than improvements among disadvantaged
students."*

It is not in Chapter 2. It is not on the full-report front door — searched, zero occurrences. **It is in
the 8 September launch press release, which this publication cited on *Three lists of risers* on 26
November and which this draft cited nowhere.** The body said *the release said it was*, and there was no
release in `sources[]`. **A quoted span with no cited register is the fabricated-apparatus class whatever
its provenance turns out to be**, and the provenance here was good: the sentence is real, it is ours to
quote, and the piece simply never named where it came from.

Fetched, hashed and added as **R6**: capture `20261115232402`, **1,468,371 bytes**, sha256
`096bb651ddbda01432c64263718fced2b978a5be3ac26bf8b92766bb671166a5`, re-verified rather than carried across
from our own published piece (#101). **Span audit re-run: 15 of 15 matched to a cited register.**

**And reading the register repaired the argument as well as the apparatus**, which is the part worth
keeping. The release's sentence is longer than the clause the draft quoted, and the half the draft dropped
is where the hedge lives: *"The gap narrowed between 2022 and 2025, but **largely** because…"*. The
sentence is also about the OECD average, not about each system. **So 34 of 49 is not a correction of the
release — it is what *largely* means, counted.** The draft's line *"accurate about the average and about
two systems in three"* was already the right posture, but the piece now prints the hedge and the
85-point scale sentence that fixes the claim's scope, and says in writing that the release names the
pattern while the table names the exceptions. *An apparatus repair that improves the argument is the sign
the apparatus was load-bearing.*

**Why this is the cell's most useful finding:** the Editor read this draft closely enough to catch a legal
basis given to the wrong cycle, and still read past a quotation with no source — because **a quotation
whose words you recognise does not read like an unsourced quotation.** Four of the five repairs on this
piece came from reading. This one came from a script that cannot recognise anything. Named for the
standing queue beside the ASCII-fold item: *the span audit is twenty lines and it is the only check here
that is immune to the reviewer already knowing the answer.*

### What did NOT need repair, recorded because it was expected to

- **No ordinal for Mongolia anywhere.** The three-way tie at +12 is respected throughout. The drafter
  wrote *"A position inside a tie is a statement about how a list was sorted, not about a country"* and put
  it in the body rather than only in the annotation, which is #19's guardrail-in-the-sentence rule obeyed
  without being asked.
- **The percentage-point boundary holds.** I.2.8's unit is flagged in the body at the figure — *"a different
  unit from everything above, and not comparable with a score point"* — which is the trap that cost the
  Uzbekistan piece a cell-4 return.
- **The significance limit is in the body, once, at the first change figure**, not buried in the annotation.
- **No causal sentence joins the major domain to the science rise.** Checked line by line. The section says
  in writing that neither register joins them and that the question is open.
- **No present-tense claim of office.** Checked. The closing paragraph says *"Whether he still holds the
  post is not something this publication can read anywhere."*

---

## Test 2 — Specificity. **PASS, and the named human stays, on the narrow ground the brief set**

Place: Mongolia, with its sample given as 191 schools. Time: two dated cycles, a dated statute, a dated
contract, a dated timeline step. Neither is in question.

The named human is, and the drafter was right to ask (open question 2). **The ruling: he stays, and the
reason is that the piece's last section is about *whose account a reader can obtain*, which makes the
identity of the body that owes it load-bearing rather than ornamental.** The rubric's word is *decorative*,
and a decorative name is one the piece would read identically without. Cut this one and the closing
paragraph loses its subject: *the body that owes Mongolia's account of its own results names nobody today,
and the last time it named anyone was seven months ago on a page its own rebuild deleted.* That is the
measurement the section exists to make.

**Two conditions on it, both already met in the draft and both now checked rather than trusted:** no
present-tense claim of office, and no view on the 2025 results attributed to him. **And one the Editor
adds:** the English words *director of the Education Evaluation Centre* must stay a description of the post
and never become the institution's English name, which §0 of the brief and R1's #141 sweep already forbid.

*The honest summary is that this is the weakest Test 2 in the edition and it is still a pass. Uruguay had a
coordinator on a live team page. Mongolia has a role noun in an archive. The difference is in the register,
not in the drafting, and a piece does not get held for the shape of the country's website — it gets held
for claiming more than that website supports, which this one does not.*

---

## Test 3 — Why now. **PASS**

Paragraph two gives the reader the two cycles and the number in each. The chapter is seven weeks old, the
edition is its subject, and the national report's September 2026 date is in the register. No encyclopedia
risk.

## Test 4 — The dignity check. **PASS, after reading the last two sections twice for tone**

This was the test the Editor expected to fail, because a piece that ends on a broken link can read as a
publication scoring a point off a national institution. **It does not, and the reasons are structural
rather than tonal.**

- The 404 section **states its cause** — a WordPress tree and a rebuilt site — rather than leaving a gap
  for a reader to fill with incompetence or concealment. A named mechanism is the opposite of an
  insinuation.
- It says in bold that **nothing here says the report does not exist**, and credits the register's own
  statement that it was presented.
- The section immediately before it is **Mongolia collecting more about itself than the comparison
  required** — 1,331 science teachers and the students' parents, with the centre's own reason given. The
  piece reaches the unreachable link having just established that this is a body doing more than it was
  asked, which is the order a senior Mongolian educator would recognise as fair.
- The equity section credits the country with the thing the OECD's own headline sentence does not: **both
  ends rose.**

**One line was checked and left alone:** *"A country can raise its disadvantaged students by nineteen points
and still have its boys further below the line than its girls."* It is two of the chapter's own findings in
one sentence with no verdict attached, and the restraint is the point.

## Test 5 — Long arc. **PASS**

It is the fourth distinct thing this edition has found out about how the chapter's tables gate their
populations — after Jordan's baseline, Qatar's two of three, Saudi Arabia's two rulers and Uzbekistan's
subject condition — and the **first** to find the gate on the *clock* rather than on the subject. It also
gives the edition its second first-party non-OECD register read directly, and its first counter-case to
the release's equity sentence counted from the table that sentence sits on. That is the arc.

---

## The title

**TAKEN AS DRAFTED: *Mongolia's second cycle*.** 23 of 100.

The drafter's rejected alternatives were both correctly rejected and the second one for the right reason.
*Mongolia has no decade* makes one of four findings the whole piece. *The largest rise among the systems
that fell twice* is true, derived here, and reads like a riddle — and the Editor notes it is also the one
title that would have needed its own derivation defended in a tab, which is where a title goes and the
derivation does not.

**What makes the drafted title correct after repair 1 and not before it:** *second cycle* now names the
thing the piece is actually about, because the two cycles differ in their basis as well as in their count —
a contract and a policy target, then a statute. A title that was a label over the old opening is an
argument over the new one.

**Dek taken as drafted**, 179 of 200, measured not asserted.

---

## The open questions, ruled

1. **The major-domain section stays, at its length. NOT overruled.** The drafter asked to be overruled
   rather than have the fence weakened, and offered to compress three paragraphs to two sentences. The
   Editor declines both. It is the only place in this edition where a register of ours supplies the domain
   structure of two cycles for one country, and the three paragraphs are three because each one does
   separate work: what the register says, what the two numbers are, and what cannot be concluded. **A
   withheld inference needs more room than an asserted one, not less** — compress it and the fence goes
   before the claim does.
2. **Ruled above.** The name stays.
3. **The overrun is accepted, and the accepted figure is 1,965 words and not the 1,790 the draft handed
   up.** The brief said 1,400 to 1,600; the Editor wrote that brief before the register had been read to the
   bottom, and three of the four findings arrived after it. *A word count in a brief is an estimate made in
   ignorance of the piece; the piece is the evidence about the estimate.* Nothing is cut. **And the 175-word
   difference is this verdict's own repairs 1 and 5**, measured after applying it rather than left at the number
   the draft reported — *a verdict that orders a repair and then quotes the pre-repair measurement is the
   hand-off defect with a different letterhead.* **Recorded so the next brief in this edition says 1,900
   where it means it.**
4. **Both rejections upheld**, see above.
5. **Upheld, and it is the right instinct.** No sentence about Mongolian school conditions, herder
   households or boarding schools. No register read for this piece carries any of it and the piece would be
   furnishing a country out of general knowledge, which is the house's oldest prohibition.
6. **The rail arithmetic is correct and the Editor adds the consequence in writing.** Two of the four slugs
   in `related:` are held today. **This piece cannot flip before both Uzbekistan and Uruguay do**, and the
   board's own order puts those at 2026-11-29 and 2026-11-30. So the earliest flip for this piece is
   2026-11-30 and more realistically 2026-12-01, which is inside Edition 06's window to 6 December with
   five days to spare. **On the rail cap:** `2026-11-26-pisa-2025-three-lists-of-risers` was at 6 as of the
   Uruguay draft, so cell 8 **displaces or declines and says which** — and the Editor's instruction is to
   **displace**, naming the displaced edge, because this piece is the first to count the table under that
   piece's own headline sentence and that is a stronger edge than any rail it currently holds.

---

## Cell 4's instructions to the Arabic composer

- **Compose from the registers re-opened at compose time (#101), not from the English.** R1 is Mongolian and
  R4 is English; both are third-language-to-Arabic in the sense #160 cares about, and **R1 collapses into
  the Qatar/Uruguay configuration: a register in a language that is neither of ours makes both editions
  equal, because neither can do anything but reproduce it.** Expect the Mongolian spans to be reproduced in
  Mongolian in both editions, exactly as the Spanish spans were.
- **`«…»` means *these are the register's bytes* and nothing else.** The Uruguay pair spent three
  corrections on this. A Madār title, a word-mention, our own Arabic rendering of a foreign role noun —
  none of them wears those marks.
- **#86 does not engage and must not be made to.** One named human, a role noun `захирал` and no gendered
  morpheme on the name. **This is the Uzbekistan and Saudi configuration, not Uruguay's** — there is no
  `Coordinadora` here, and an Arabic determination would be unlicensed. Two Ed06 pieces were corrected at
  cell 6 this morning for exactly that.
- **The unit words cannot be elided in Arabic**, which is how the Uzbekistan draft's dropped *percentage*
  surfaced at composition. I.2.8's −6.6 is `نقطة مئوية` and I.2.6's 12 is a score point. **If the Arabic
  forces a distinction the English elided anywhere, send it back to the English.**
- **The Mongolian script runs keep their own script's conventions** and are marked with their `lang`, per
  the 2026-11-15 settlement on Latin runs inside Arabic bodies, which applies to Cyrillic by the same
  reasoning.
- **Six sources, the same six URLs in the same order as the English**, written at this cell. **The English
  edition's `sources[]` exists and was read at this desk** — stated explicitly because the last two pieces
  of this edition both reached cell 7 with no English `sources[]` at all, and in both cases a verdict at
  this cell passed them without mentioning sources once. **It is written, it has five entries, and the five
  were re-read here.**
