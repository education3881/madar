# Ruling #140 — An outside boundary locates a population and cannot classify it

**Filed 2026-11-12 · from the quality function, taking the standing queue's own head (item 37, the oldest
OPEN row, 20 days) and closing it · family: assertion discipline, fifty-fourth member**

---

## The rule, in one line

**A boundary the artefact supplies from OUTSIDE a span can find the span and cannot say what it is — so
it is a measurement and never a gate. Only a boundary that is a SPECIFICATION of the thing it bounds can
be asserted.**

## What happened

Ruling **#113** (2026-10-23) found the first exact boundary this operation had ever been handed: an
acronym states how many words its name has and which letter each of them begins with, so a name that
carries an acronym has a textual boundary and `qa_acronym_evidence` can be a gate. The same day's forward
question became standing-queue item 37, and it asked the hard half: **the gate reaches 15 of 123 tokens —
12.2% — so what is the other 87.8%, and is any of it reachable?** The row offered two branches: find a
bounded population inside the 108, or prove there is none and write the reach into the tool as permanent.

**Neither branch was the answer.** There *is* a bounded population, its boundary is punctuation, and the
boundary is useless as a gate for a reason that is structural rather than a matter of effort.

Measured today over the 127 acronym tokens in the 45 approved EN bodies:

| cell | n | what bounds it |
|---|---|---|
| anchored | **14** (11.0%) | the acronym's own letters — #113, and the only exact boundary |
| parenthetical | **1** | brackets — exact, and this house barely uses the form |
| appositive, **name-shaped** | **15** | em-dash or comma, then title case |
| appositive, gloss-shaped | **20** | em-dash or comma, then lower case |
| no boundary at all | **77** | nothing in the artefact ties any name to this token |

The appositive is genuinely in the artefact. This publication's house style writes *The Transition and
Resilience Education Fund — TREF — launched…*, *ACARA — the Australian Curriculum, Assessment and
Reporting Authority*, *The Supreme Audit Office, NIK, whose report…* — nobody has to guess where to look.

**And then all 15 name-shaped candidates were read by hand, and 5 of them are not expansions at all:**

- `UNICEF, UNHCR and a set of national and international NGOs`
- `STEM, Social Sciences, or Arts and Sports Science`
- `coordinated with GPE, UNESCO and Sudan's Local Education Group`
- `the World Bank–UNHCR INSPIRE programme` (an en-dash inside a compound, not an apposition)
- `partnership between UNICEF, the Ministry of Education, Ahfad University`

**Precision 10 of 15 = 66.7%.** Two of the ten true ones are also truncated by their own punctuation:
`PARAKH — Performance Assessment` stops at the comma inside *Performance Assessment, Review and Analysis
of Knowledge for Holistic Development*.

## Why this is not a tuning problem

**The comma that introduces an apposition is the comma that separates list members, and the artefact does
not record which job it is doing.** English overloads the mark. So does the em-dash. No amount of
narrowing recovers the distinction, because the distinction is not in the bytes: it is in the syntax the
writer had in mind, and the reader reconstructs it from meaning.

Contrast what makes #113's boundary exact. The acronym is **a specification of the name**: it states a
word count and a letter per word, and a span either satisfies that specification or does not. That is why
the gate can hold. The appositive states only *something stands beside this token*. It is a **pointer**,
not a specification — it says where to look and nothing about what is there.

So the asymmetry is not about inside versus outside as geometry. It is this:

> **A boundary is assertable exactly when it is a specification of its own contents. A boundary that
> merely delimits is a place to look.**

Orthography is the one part of the classification the artefact really does supply, and it is why the
partition has a gloss cell rather than a binary: `ZUS, the social-insurance agency` is lower case and is a
description; `the National Assessment of Educational Progress` is title case and is a name. English
capitalises proper names, so case is a weak specification of **type** even where nothing specifies
**extent**. That cell is reliable and is doing real work — 20 tokens correctly set aside.

## What was done about it

**The tool gains a measurement, not a limb.** The five-cell partition prints on every run of
`qa_acronym_evidence`, inside the gate that already runs — not behind a flag somebody must remember,
which is 2026-09-13's *a hand-run assertion is a habit, not a gate* in its other direction. The gate's
assertions are untouched and were re-proved both ways after the edit, because a measurement added to a
gate must not move the gate: bite (`Fictional Quality Board — FQB` injected into
`2026-07-16-australia-naplan-reset`, the injection asserted to have changed the file first) → exit 1;
control (file restored) → exit 0.

**The reach is computed and no longer quoted.** It reads **11.0%** today where item 37 recorded 12.2% on
2026-10-23. Both figures are right about their own day — 14 of 127 over 45 pieces against 15 of 123 over
44 — which is exactly why a reach belongs in code and not in a sentence. *A literal is a measurement that
has stopped being taken.*

**And the measurement's real output is work, not a number.** Three served EN pieces expand an acronym
their own `sources[]` does not evidence, which is **#101's own defect class, 103 days after #101 earned
it, on pieces the shipped gate returns nothing for**:

| piece | body expands | annotations |
|---|---|---|
| `2026-07-07-india-parakh-hpc` | **PARAKH** → *Performance Assessment, Review and Analysis of Knowledge for Holistic Development* | carry none of `Performance`, `Review`, `Analysis`, `Knowledge`, `Development` |
| `2026-07-16-australia-naplan-reset` | **ACARA** → *the Australian Curriculum, Assessment and Reporting Authority* | carry none of `Curriculum`, `Assessment`, `Authority` |
| `2026-07-07-poland-ukrainian-students` | **NIK** → *The Supreme Audit Office* | carry neither `Supreme` nor `Office` |

Raised as standing-queue item **100** and handed over rather than repaired: a fix that changes served
bytes is the Web Developer's even when an assertion found it (the 09-27 split), and **#101 clause 4 wants
the register's own wording**, which needs three first-party reads this run did not take.

**The third one is a question #101 does not answer, and it is recorded rather than resolved.** NIK is
*Najwyższa Izba Kontroli*. The body prints *The Supreme Audit Office*, which is a **translation of the
name** and not an expansion of the acronym — the acronym's letters belong to the Polish and the body's
words belong to the English. #101 clause 1's first branch (*the annotation carries the full name as the
register prints it*) may be unreachable in principle here, because the form the register prints is in a
script and a language the body is not written in. Clause 1's second branch (*the body keeps the acronym*)
is reachable and may be the only exit, exactly as it was for `KJSEA` under #120. **Named, not settled.**

## Binding

1. **A boundary is asserted only when it is a specification of its own contents.** An acronym specifies
   its name; a bracket specifies an extent; a quotation mark specifies a span (#119). A comma, an
   em-dash, a sentence end and a paragraph break **delimit** and specify nothing — they may locate a
   population and must not gate one.
2. **A located-but-unclassified population is published as a measurement with its precision stated, in
   the instrument, computed on every run.** Not in a log, not behind a flag, and not as a literal.
3. **The precision is established by reading the WHOLE located population by hand, once, on the day the
   detector is built** — 15 of 15 here. A precision estimated from a sample of a population small enough
   to read entirely is a choice to not know.
4. **A measurement added to a gated assertion is proved not to move the gate**, bite and control, in the
   same commit (#35's discipline applied to an addition that asserts nothing).
5. **Where a body renders a foreign-language name in translation, the acronym's letters and the body's
   words belong to different languages**, and #101 clause 1's first branch may be unreachable. The
   second branch is the exit until a ruling says otherwise.

## Family, and what it joins

Fifty-fourth member of the **assertion-discipline** family, and it pairs with two members directly:

- **#113** supplied the exact boundary. This ruling supplies the boundary's *criterion*, which #113 had
  by luck of its subject rather than by statement.
- **#93** says an assertion whose only repair path runs through the artefact it blocks cannot be gated.
  This is the other reason a check stays a measurement: not *the repair is impossible* but *the
  classification is*. Two distinct grounds for the same decision, and the operation now has both written
  down — which matters, because #93's ground was being quoted for cases that are actually this one.
- **#130** (*a reach gap is not a defect population*) is the near-miss to avoid: 77 tokens have no
  boundary at all, and that is **not** evidence that 77 defects are hiding there. It is evidence that 77
  tokens are, in all likelihood, correctly bare under #101 clause 1's second branch.

## The counts this filing moved

Four always, plus the conditional fifth, plus the ratio on both sides (10-04 second amendment, limb one):

1. §3's series-integrity range — `#1–#139` → **`#1–#140`**
2. §3's heading — `#1–#139` → **`#1–#140`**
3. §1's count line — 135 rows → **136 rows** (this file is row 136)
4. `CLAUDE.md`'s non-negotiables — `#1–#139` → **`#1–#140`**
5. The assertion-discipline family's running member count — **FIFTY-THREE → FIFTY-FOUR**, with the
   membership list appended in the same commit (the 09-28 defect: a count incremented beside a list that
   was not appended to)
6. The families ratio, moving on both sides — **fifty-four of one hundred forty**

Counted, not inherited: 139 rows before this commit, 140 after.
