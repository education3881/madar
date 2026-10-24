# Ruling #114 — nothing measured the ruler

**Filed** 2026-10-24 (daily run, QA lane) · **Closes** standing-queue **item 19**, raised 2026-10-16 as
the daily's forward question, displaced from the head **seven** times, **8 days** open · **Family:**
assertion discipline, **thirty-ninth member** · **Instrument:** standing assertion **38**,
`agents/tools/qa_annotation_figures.py`, gated from `postbuild` · **Register:**
`agents/stats/annotation-figures.json`

---

## The ruling, in one line

**A check's operand is a claim too.** Four of this operation's instruments compare something against the
`sources[]` annotation, and the annotation itself had never been compared against anything — so a figure
printed only in an annotation was published outside every numeric check we own, and the silence read as
agreement.

## What item 19 asked, and the one word in it that had to go

The item asked *which of our annotations assert something their own URL does not support?* — after a
`gov.om` citation was found whose parenthetical read **"the issuing body and its mandate; renamed in
2026"** against a page that carries no rename, no date and no instrument. The claim was right by accident
and unsupported by the document it hung on, and it survived 118 days and four gates.

The word that had to go is **URL**. Taken literally the item is a network instrument that needs a
judgment first: classify each parenthetical as *claim* or *description*, then read the high-risk class
against the register. The classifier is the problem. #113, one day earlier, is the record of what
classification-by-detector buys on a prose boundary: two detectors over one population returned **3** and
**46**, thirty-six apart, with nothing able to adjudicate.

**The boundary the artefact supplies here is a digit.** A quantity is exactly extractable and a body is
exactly searchable, so the instrument never decides whether a parenthetical makes a claim. It asks a
narrower question that needs no judgment at all:

> **Is this number anywhere our own figure discipline can reach it?**

Every numeric instrument this operation owns reads a **body**: the numeral-multiset comparison, the
one-sided-figure grep, the prohibited-figure grep, the Verifier's eight trace axes, #27's two channels.
The annotation block is **served** — it renders on every article page, both editions. A quantity that
lives only there is a published figure standing outside all of them.

## What the sweep found

Over 44 approved pieces, 88 files, both editions:

| | |
|---|---|
| annotation quantities, after the four licences | **2,033** |
| printed in the body of their own piece | 1,603 |
| **annotation-only** | **430, across 40 of 44 pieces** |
| of those, printed in the body of the *other* edition | **19** |
| distinct (slug, token) pairs seeded into the register | 251 |

Shape rather than rate: the annotation-only figures are **91% of the pieces**, not a tail. They are not
small claims either — `~1 million resources`, `45.5% → 32.4% → 13.9%`, `~1.38m students`, `69.5%` learning
poverty, `1,000+ seats, 100,000+ books`, `adopted 440/441`. Each is a sentence about the world, printed
by this publication, in a block the publication's own figure doctrine does not read.

**The 19 that the pair rescues are the sharpest sub-population**, and they are #42 on a figure: the same
number is prose in one edition and a citation in the other, so it sits inside the trace axes in one
language and outside them in the other. They are registered as traced *via the pair* rather than as
untraced, because they are — and the register says which edition did the tracing.

## The four licences, each a coordinate rather than a claim

(a) **dates** — `6 September 2025`, `May 2025`, `14 Oct 2024`, ISO, bare years, year spans; (b)
**identifiers** — a numeral touching a letter: `534IRQ1002`, `PP39`, `QH15`; (c) **pointers** — `p. 12`,
`Article 23`, `Table 3`; (d) **named instruments** — `RA 10533`, `Resolution 218/2025/QH15`, where the
number *is* the document's name.

**Limitation (i), stated here rather than discovered later: licence (a) cannot see the instance that
earned the item.** *Renamed in 2026* is a bare year, and a bare year in an annotation is a publication
date far more often than an assertion. The licence is still the right call and its cost is one clause in
the tool's header. Item 19's own instance was found by a human reading a register, and the instrument
that would find the next one is a different instrument.

## Clause 2 — the register is hand-written, and that is the whole design

`--emit` prints the rows it cannot satisfy and **writes nothing**. A tool that seeded its own register
would be a check reading its answer off the field it supplements — the 2026-09-14 trap in a new costume:
run emit, go green, learn nothing. So a new annotation quantity **reds the build** until somebody either
prints it in the body or records in the register which register and which clause it was read from. A
placeholder provenance is REFUSED (exit 4).

**The seeded backlog is a known error with a known size**, per 2026-10-04's limb two: 232 entries marked
`UNTRACED 2026-10-24`, and the tool prints that count on every run, so the backlog cannot shrink out of
sight or grow in silence. Working it down is the Verifier's, not this instrument's.

## Proof — six bites red, three controls green, every injection asserted to have changed the file first

1. quantity inside a parenthetical, in no body → **1**
2. quantity **outside** any parenthetical → **1**
3. the same figure also printed in the body → **0**
4. a licensed date + instrument + page pointer, in no body → **0**
5. a register entry removed → **1**
6. placeholder provenance → **4 REFUSED**
7. register deleted → **1**
8. a corpus with no annotations at all → **2**, refusing to pass vacuously

## And the first bite did not bite — which is the part worth carrying

Bite 1, written against the item's own wording, injected a quantity into an annotation **outside its
brackets**. The injection changed the file; the harness asserted that it had; and the check exited **0**,
reading exactly like a passing control. The check was fine. The **scope** was the item's: *parenthetical*,
because that is where item 19's own instance happened to be.

Widening to the whole annotation title moved the population from **231 across 34 pieces** to **430 across
40** — the narrow scope was hiding **43%** of its own subject, and nothing inside it could have said so.

> **A bite aimed at the specification tests the specification.** 2026-09-14 already requires asserting
> that an injection changed the *file*; this adds the other half — assert that it changed the *surface the
> check reads*, because when those two differ the experiment fails silently and in the green direction.

Seventeen closures running, the specification has not been the scope. This is the first time the gap was
found **by the proof harness** rather than by doing the work: the bite was the instrument that measured
the item's own wording.

## Binding

1. **A quantity printed in a served annotation is either printed in a body, where the trace axes reach
   it, or recorded with the register and clause it was read from.** Gated by standing assertion 38.
2. **The hand-off to the Editor carries `annotation quantities not in the body: N, each registered: ☐`** —
   same teeth as the dek/title cap (07-27), `annotation == sentence` (09-13), the named-humans gender line
   (10-04) and acronym evidence (#101).
3. **When an instrument's scope is inherited from the wording of the item that commissioned it, a bite is
   aimed at the scope boundary itself**, and the harness asserts the injection changed the measured
   surface and not merely the file.
4. **A register that licenses an instrument's silence is hand-written**; an instrument that writes its own
   licence has no teeth.

## Where it sits

Assertion discipline's thirty-ninth member, and the first whose subject is **the operand every other
citation check takes as given**. #45–#47 compare a body against an annotation. `qa_sources_alive` asks
whether the URL answers. #111 asks whether anybody can ever re-open it. #112 asks whether the bytes are
still the document. All four measure *with* the annotation. This one measures the annotation — which is
#57 (*count against the population, never against yesterday's number*) moved off a count and onto a
citation, and #101's *the annotation's silence read as agreement* moved off a name and onto a figure.

**Forward surface, named so it is not forgotten:** this check compares a token to a body and can say
nothing about **what the annotation's non-numeric prose asserts** — the rename, the mandate, the named
human, the hedge. That is item 19's own founding instance and it remains unmeasured; 430 numbers are the
part of the ruler that happened to be made of digits.
