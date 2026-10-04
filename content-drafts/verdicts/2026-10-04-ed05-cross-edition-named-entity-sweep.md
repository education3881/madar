# Edition 05 — cross-edition named-entity sweep, all six held pairs

**Date:** 2026-10-04 · **Run:** autonomous daily · **Lane:** Verifier + Arabic Editor, jointly
**Trigger:** the 2026-10-03 named forward question, executed before anything new was added, per the
2026-08-23 RUNBOOK rule.
**Scope:** every named entity each `sources[]` annotation attributes a claim to — institution,
publication, named human, role — in both editions of all six held pairs. **Not a tool. A measurement.**
**Outcome:** institutions and publications CLEAN. **Two defects confirmed against registers read in
served text today, both in the Arabic edition, both fixed in-run. One role title corrected. Five
determinations recorded as unsourced.** Ruling **#86** filed.
**Body prose:** untouched in both editions of all six pairs. No numeral moved in any body. Every edit is
inside `sources[]`.

---

## 1. What was asked, and why it was the hard version

The 10-03 run closed Sudan's confirmation read and found that the two editions disagreed about a named
institution — *the National Council for Literacy **and Adult Education*** — and that **the Arabic was
right**. The finding under it: Madār composes the Arabic rather than translating it, so the Arabic
Content Creator reads every register independently, which makes the second language a free second channel
on our own annotations, **and nothing we own compares them.**

The question written for today was deliberately not *build a comparator*. The obvious comparator had
already failed: 10-01 measured annotation numeral parity across languages at **117 false positives out of
338** and filed it as a negative result. So the question asked for a **count** instead: take the six held
pairs, compare by hand the one class of fact that crosses scripts without a parser, and find out whether
10-03 was a one-off or a rate. *If it is a rate, the instrument is worth specifying; if it is a one-off,
the Arabic edition gets named as a verification channel in the RUNBOOK rather than a cost.*

It is neither. It is a **structural asymmetry**, and both of its defects today ran the *opposite*
direction from yesterday's.

## 2. The denominator

| | EN | AR |
|---|---|---|
| Zambia | 9 | 9 |
| Sierra Leone | 8 | 8 |
| Sudan | 10 | 11 — declared asymmetry, unchanged |
| Slot 3 (ruler) | 10 | 10 |
| Egypt | 11 | 11 |
| Rwanda | 8 | 8 |
| **Total annotations** | **56** | **57** |

684 source promises across the corpus; **338 shared annotations** by `qa_pair_frontmatter`'s own count.
**43 individual humans named** across the six held pairs.

## 3. Institutions and publications — CLEAN

Every institution, statute, report, newspaper, programme and funder named in the held set resolves to
the same body in both editions. The cases most likely to drift were checked explicitly and hold:

- **Same owner, two names, each matching its own register.** OPM's lot map says *Rising Academy
  Network*; the EOF programme page says *Rising Academies*. Both editions follow the register in front of
  them rather than each other — which looks like an inconsistency and is the opposite of one.
- **Latin left as Latin where the owner offers no Arabic.** `ZICTA`, `NYAF`, `KOICA`, `FCDO`, `REB`,
  `NESA`, `EducAid`, `Street Child`, `IBO`, `SCUK`, `Bond`.
- **Yesterday's fix holds in both editions.** *National Council for Literacy and Adult Education* /
  «المجلس الوطني لمحو الأمية وتعليم الكبار».
- **Sudan's declared asymmetry is honest.** The two UNICEF stories cited in their official Arabic
  editions on the AR side carry their *own* publication dates (31 Aug 2020 against 27 Aug; 2 Nov 2022
  against 1 Nov) — different documents, not one URL localised — plus one AR-only UN News Arabic interview
  cited solely as the spelling register for «مكانّا». `qa_pair_frontmatter` prints all three as declared
  and unchanged.

**One loose rendering recorded and NOT changed.** HSRC is «مجلسُ البحوث العلمية للعلوم الإنسانية», which
parses the name differently than *Human Sciences Research Council* does. It names the same council, a
reader identifies it, and nothing in the piece rests on the parse. **A rendering is not an attribution**,
and changing it today would spend an edit on taste at the confirmation-read margin.

## 4. The defects — and they are in the grammar, not the entities

The Arabic edition attaches a grammatically gendered role or predicate to **24 of the 43** named humans.
The English edition carries the same determination for **5**. **Nineteen named humans are therefore
gendered in Arabic on the composer's judgment alone.** Ten were taken back to their registers today.

### DEFECT 1 — Sierra Leone, source 6, Arabic. A quoted woman was printed as a man.

The Arabic annotation read «ومديرُ التنمية في FCDO أليكس ماكلين» — **masculine**. The register, re-read
in served text today, quotes her twice and uses the pronoun: *"The discussions I joined were incredibly
informed and engaged," **she** said.*

Fixed to «ومديرةُ التنمية». The same read confirmed the annotation's other three determinations against
the register's own pronouns — Gauld *her*, Sackey *he* — and found that **Edward Kpakra carries no
pronoun on the page at all**, so his masculine agreement is recorded in the annotation as this edition's
own and not the register's, per #86's binding item 2. A clause now states all four, with the read date.

**The mechanism, stated because it will recur:** *Alex* is a name that sounds male in English and reads
male to a composer working from the name. The register was open when the figures were taken from it and
was not open when the role noun was closed. This is the 09-13 shape — *the annotation and the sentence
are written from the same open register* — with the register right there in the same annotation.

### DEFECT 2 — slot 3, source 8, Arabic. The register's own grammar was contradicted.

The Arabic annotation read «مديرُ ديوان **وزيرة** التعليم الأوَّلي والابتدائي في بنين» — **feminine**.
The register is in French, and French makes exactly this determination: *« le directeur de cabinet du
**ministre** béninois des enseignements maternel et primaire »*. **Masculine, on the page, in the
sentence our annotation is built from.**

This is the worse of the two, because the register did not merely fail to support the claim — it carried
the opposite one, in a language that cannot avoid the marking, one clause from the name we took.

Fixed to «مديرُ ديوان الوزير البينينيِّ للتعليم الأوَّلي والابتدائي», with the register's own clause
quoted and the correction dated.

**And the same read produced a free attribution sharpening, carried into both editions for parity.** Both
annotations said *"the results whose publication the report gives as announced for the last quarter of
2026"* — attributing the quarter to the newspaper. The register attributes it to a named human: *«
Dèwanou Avodagbe a souligné l'attente suscitée par les résultats, dont la publication est annoncée pour
le dernier trimestre 2026 »*. Both editions now carry the speaker. **This matters beyond tidiness: it is
the clause ledger Item B rests on** — the piece's closing sentence narrows that quarter to *December*,
and the register's authority for the quarter is now named rather than generic. Item B is unchanged and
still the Editor's call.

### DEFECT 3 — Sierra Leone, source 7, Arabic. One human, one English title, two Arabic titles.

Source 3 rendered *Senior Education Evidence and Learning Advisor* as «مستشارُ الأدلّة والتعلُّم
التربويِّ الأول» — a grade. Source 7 rendered the identical English title as «كبيرُ مستشاري الأدلّة
والتعلُّم التربوي» — **the head of a function**. The same edition also uses «كبيرُ مسؤولي التعليم» for
*Chief Education Officer* two annotations earlier, so the construction is doing two jobs in one piece and
one of them is a promotion.

The register settles it, read today: *"Senior Education Evidence and Learning Advisor **within** Save the
Children UK's Global Outcomes Department"* — a grade inside a department, not its head. Source 7
harmonised onto source 3's reading, with the register's full title quoted and the reason stated.

**Second finding on this one annotation in three days.** 10-02's #84 found it crediting the repository to
an organisation because the handle said `SCUK`; today it was overstating the same person's rank. Both
times the body was the careful side. Both times `qa_pair_frontmatter` passed, correctly.

### The five unsourced determinations — recorded, not guessed

| Named human | AR | Register | Disposition |
|---|---|---|---|
| Edward Kpakra, Chief Education Officer | masculine | no pronoun | **recorded as unsourced in the annotation today** |
| Saima Sohail Malik, Senior Education Specialist | feminine | byline only | carried to Rwanda's confirmation read |
| Leon Mugenzi, Head of Teacher Development | masculine | byline only | carried to Rwanda's confirmation read |
| Kate Radford, CWTL Programme Director | feminine | no pronoun | carried — Sudan's read is CLOSED, see below |
| Dr. Aiman Badri, Ahfad University for Women | masculine | no pronoun; two further routes read today name no such person at AUW | carried — Sudan's read is CLOSED, see below |

**And the awkward part, stated rather than smoothed: three of these pieces have confirmation reads
already closed.** Zambia (10-01), Sierra Leone (10-02) and Sudan (10-03) were each read and signed off
before this defect class was named. **A confirmation read closed before a class existed did not check for
it.** The reads are not re-opened wholesale — that would be a fortnight's work against a 10-11 gate — but
this one class is re-opened on them and tracked in the ledger. Sierra Leone's two defects were fixed
today, inside a read that closed two days ago, which is the evidence for the statement rather than a
counter-example to it.

## 5. Proof

- **`npm run build` exit 0** after the fixes. 121 pages (held state), 135 routes, **all thirteen
  `postbuild` gates CLEAN**, all twelve CI build-step assertions clean.
- **`qa_pair_frontmatter` CLEAN** — 44 pairs, 38 approved, 6 held, 432 identity fields, 684 source URLs,
  338 shared annotations, 3 of 3 declared asymmetries used and unchanged. **It passed on both defects,
  correctly.** It does not compare composed prose, because composed prose is supposed to differ.
- **`qa_ar_language` CLEAN on all 59 Arabic pages** with a French clause newly added to an Arabic
  annotation — which is the right result and was worth confirming rather than assuming, since that gate
  bit on 235 Arabic fields printing English when it was first wired.
- **`qa_census` CLEAN** — 22 numbers from 15 instruments.
- **No body prose touched.** No numeral moved in any body in either language. Word counts unchanged: EN
  1,592 / AR 1,343 (Sierra Leone), and slot 3's body untouched.
- **Every register claim above was read in served text today**, not carried from a search summary (#41).
  Where a name could not be found at all — Aiman Badri at AUW, on two routes — the absence is recorded as
  an absence and nothing is narrowed from it, per 10-02's rule that *absence from a page we cannot open is
  not evidence*.

## 6. What this changes in the ledger

- **Ruling #86** filed; five counts moved at the point of filing per the 09-27 amendment.
- **The RUNBOOK gains the Arabic edition as a named verification channel** — with its bound, which is the
  whole of today's finding and the opposite of what 10-03 expected to be writing.
- **Items A, B and C remain open and remain the Editor's.** Nothing here touches them. Item B's register
  authority is now named, which makes the Editor's call on it cheaper, not different.
- **Slot 3's and Egypt's confirmation reads are still owed** — 4th and 5th of five. Today's sweep is not
  one of them and does not substitute for one.

— the Verifier and the Arabic Editor · 2026-10-04
