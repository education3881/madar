# Ruling #132 — THERE IS NO CONTROL EDITION, ONLY A CONTROL PER PROPERTY, AND THE TWO EDITIONS ANCHOR EACH OTHER IN OPPOSITE DIRECTIONS

**Filed 2026-11-07** · from the standing queue's own head, **item 36 at 15 days**, the oldest row in
OPEN · **non-numeric family, sixteenth member** · tool of record
`agents/tools/arabic_side_reach.py` (a measurement, not an assertion).

---

## The rule

**A property's control edition is a property of the property, not of the edition.** Where two editions
of one piece check each other, the edition that can be *parsed* for a question is frequently not the
edition that is *forced to answer* it — and which one is which **reverses from question to question**.
So:

1. **Name the property before naming the control.** #101 clause 3 says *where two editions render one
   institution, the FORCED rendering is the control*, and it is right about institutions. It is not a
   general rule about editions, and reading it as one makes Arabic the control for questions Arabic
   cannot locate at all.
2. **For a NAME, English is the anchor and Arabic is the evidence.** English capitalises and takes
   honorifics, so a name's span is parseable; English role nouns are grammatically neutral, so English
   commits nothing about the person.
3. **For a GENDER, Arabic is the anchor and English is at best a second opinion.** Arabic cannot write
   a role noun or a finite verb about a person without choosing, so the Arabic edition states a
   determination on every mention; English states one only when it happens to reach for a pronoun.
4. **An instrument built on one edition must say which property it is the control for**, and a check
   that needs both — *is this determination evidenced?* — needs the two editions in different roles at
   the same time.

## What earned it

Standing-queue item 36, raised 2026-10-23 as the daily's forward question, asked whether an
Arabic-side instrument is possible at all or whether the control #101 designates is permanently
hand-read. Three measurements made the question sharp and all three point the same way: #113 found **0
acronym anchors across all 44 Arabic bodies, by construction**; #112 found **128 of its 134 declined
quotation tokens are Arabic**; #101 made Arabic the control for a disputed institution precisely
because it cannot carry the Latin token.

**The row's own first cut, executed verbatim, came back ZERO.** Of the 44 published pairs, **none**
carries #86's mandated `named humans — gender read from register: N of M` hand-off line, and **none**
carries #101's acronym line. Six documents in `content-drafts/**` carry one, and all six are about the
single piece drafted since those rules existed. #86 was codified 2026-10-04, #101 on 2026-10-15, and
the last flip was 2026-10-13 — so **every published hand-off predates the rule that requires its
line**, and *a hand-off missing it is returned unread* has never once bitten anything that shipped.
That is the 2026-10-04 second amendment's **limb two** — *a point-of-filing rule fixes a count's future
and leaves a step discontinuity where it was written; it never reconciles backward* — in its fifth
instance and its first on an **obligation** rather than on a count.

**And the hard half has an answer, five tokens wide.** #113's method generalises exactly once more: an
acronym is a boundary because it states how many words a name has and which letter each begins with.
An **honorific** is a boundary for the same reason in the other direction — it cannot take a non-human
subject, and it commits a gender. Measured over all 44 pairs:

| | |
|---|---|
| AR pieces carrying ≥1 honorific gender commitment | **14 of 44** |
| Honorific gender commitments across the 44 AR bodies | **32** (20 masc, 12 fem) |
| EN pieces carrying ≥1 gendered pronoun or gendered title | **38 of 44** |
| EN pieces where an honorific anchors a name | **27 of 44**, **48 distinct names** |
| **Both channels present** | **10** |
| **One channel only** — AR commits, EN carries nothing that could disagree | **4** |

The four are `2026-06-20-oman-school-performance-ratings`, `2026-05-28-iraq-mosul-library`,
`2026-07-07-singapore-psle-sbb` and `2026-05-27-uae-madrasa-tiktok`. **#86 measured 19 single-channel
determinations by hand over six held pairs; this is the served corpus, and the shape survived the
change of population.**

## The expensive half — the first answer was a FABRICATED measurement

The first pass put honorifics and attribution verbs in one list and reported **318 gender commitments
across 44 of 44 Arabic bodies.** Every number in that sentence is meaningless. **Arabic agreement is
grammatical:** `أعلنت الوزارة` is feminine because `وزارة` is a feminine noun, and nothing about a
human has been determined. The probe counted ministries, authorities and commissions as women, and the
output read exactly like a large finding.

Corrected into two buckets before it was believed, with bucket B **printed rather than deleted** —
**293 agreement-only tokens across 43 of 44 bodies**, the number that looks like evidence and is a
fact about Arabic morphology. *A probe wider than the thing it targets manufactures the defect it was
aimed at, and a manufactured defect reads exactly like a found one* (#123, third instance; the first in
which the over-reach was a property of the **language** rather than of a regex).

**A second mis-attribution, caught the same way.** Section 1's first run reported *1 of 44* and named
the predecessor piece, because the detector matched a slug anywhere in a document and the Bahrain
draft *mentions* the predecessor in its `related:` rail. **A mention is not a subject.** Keyed to the
document's own filename, the answer is 0 of 44.

## Why this is a ruling and not a note

It changes a disposal. Before today, a disagreement between the two editions about a named human's
gender would have been settled under #101 clause 3 by preferring the forced rendering, which is
Arabic — and Arabic is forced to answer, so it would have won every time, including the two cases #86
found where **Arabic was wrong because the composer read the gender off how the name sounds.** The
correct disposal is: Arabic states the determination, English cannot contradict it in general, and
**neither edition is evidence** — the register is, and the determination is a **read** and not a parse
(#131). What the two editions buy is the *list of determinations to go and read*, which is what item 85
now carries.

## Its place among the edition rulings

* **#86** — which questions only ONE edition can answer.
* **#101** — which questions one edition is FORCED to answer, and a forced answer is a read.
* **#117** — which questions one edition is forced to answer WRONGLY.
* **#132** — which edition supplies the ANCHOR for a question the other must answer, and that the
  anchor **reverses by property**, so there is no control edition.

**Family:** non-numeric (sixteenth member — the family's fourth consecutive member in which the Arabic
edition holds a determination no instrument of ours could read, after #101, #117 and #120).
**Falsifier, stated so it can expire:** if an Arabic-side name boundary is ever found that does not
depend on an honorific or on a Latin token, clause 2 narrows, because English would no longer be the
only anchor for a name.

— Assertions Engineer · 2026-11-07
