# Ruling #113 — An acronym is a boundary the name itself does not have

**Filed** 2026-10-23, by the daily run, from the standing queue's own head — **item 17, 8 days
old, five displacements**, the board's oldest item past the three-displacement threshold.
**Family:** assertion discipline (thirty-eighth member). **Instrument:** standing assertion 37,
`agents/tools/qa_acronym_evidence.py`.

---

## The ruling, in one sentence

A name's boundary is not a textual property **in general**, and it is one **exactly when the name
carries an acronym** — because the acronym is a written specification of the span it expands: it
states how many words the name has and which letter each one begins with. **So where a detector
cannot be built, a detector anchored on the defect's own evidence can.**

## What it is about

Ruling **#101** (2026-10-15) was earned by a published error: `2026-07-04-kenya-cbe-grade10-pathways`
printed *Kenya **Senior** School Heads Association* where the register prints *Kenya **Secondary**
Schools Heads Association*, in English, for **103 days**, through four gates, with the Arabic edition
correct throughout. Nothing this operation owns could have caught it, because the English annotation
named the body only as `KESSHA` — **the annotation's silence read as agreement**, which is #57's
defect moved off a count and onto a name.

#101's clause 1 is binding and was written as a hand-off checkbox: *either the annotation carries the
full name as the register prints it, or the body keeps the acronym — the expansion and its evidence
ship together or not at all.* Standing-queue item 17 then asked the harder question: **is a
name-boundary assertion possible at all?** Two runs answered no, and both answers were correct.

| Date | Recogniser | Population returned | Verdict |
|---|---|---|---|
| 2026-10-15 | acronym must equal the name's word initials | **3** across 44 pieces | **would have missed the instance that earned #101**, because `KESSHA` is not `KSSHA` |
| 2026-10-16 | any 3+ word institution name absent from the piece's own frontmatter | **46** across 28 of 44 pieces | two detectors over one population disagreeing by 36, with nothing able to say which is right |

The 10-16 note filed the correct negative result — *a name's boundary is not a textual property*,
#85's shape on the input side — and the 10-17 run amended the item to **unactionable as specified**.
It had been displaced ever since.

## The turn

The 10-15 detector failed because it allowed each word to contribute **exactly one letter**. Allow a
word to contribute a **prefix of any length** and the same anchor that defeated it becomes the thing
that makes it exact:

```
KESSHA  ->  KE·nya  S·econdary  S·chools  H·eads  A·ssociation
KJSEA   ->  K·enya  J·unior  S·chool  E·ducation  A·ssessment
PSLE    ->  P·rimary  S·chool  L·eaving  E·xamination
```

There is no threshold in the recogniser, no head-noun list, and no judgment. The acronym supplies
the span; the span is compared against the piece's own `sources[]`. **Fifteen anchored expansions
across 44 English pieces**, and it finds `KESSHA` — the one the narrow detector was built for and
missed.

## What the first sweep found

**Four of fifteen anchored expansions — 26.7% — are not evidenced in the annotations of the piece
that prints them.** Every one is #101's defect class, served:

| Piece | Acronym | Body expands it as | In `sources[]` |
|---|---|---|---|
| `2026-07-04-kenya-cbe-grade10-pathways` | `KJSEA` | Kenya Junior School Education Assessment | no — the acronym appears eleven times, the name never |
| `2026-07-07-singapore-psle-sbb` | `PSLE` | Primary School Leaving Examination | no — seven annotations, all acronym-only |
| `2026-06-08-sierra-leone-tsc-teacher-matching` | `TMIS` | Teacher Management Information System | no — neither the name nor the acronym |
| `2026-06-10-rak-iqra-arabic-diglossia` | `J-PAL` | Jameel Poverty Action Lab | no — the annotations carry only `J-PAL MENA` |

**The first of these is on the piece that earned #101, and the run that corrected KESSHA eight days
ago walked past it.** That is the ruling's sharpest fact and it is not a reproach to that run: it
re-read the register a *dead link* had routed it to, which is exactly the route #100 describes, and
nothing routes anybody to the second acronym on the same page. *A correction reaches the instance it
was sent to. Only an instrument reaches the class.*

All four are handed to the Web Developer and the Editor as **standing-queue item 35**, not fixed
here, per the 09-27 split — and for a second reason that is #70's: two of the four registers cannot
be read from this runner today (`kjsea.knec.ac.ke` refuses the connection, `moe.gov.sg` answers 202
to every client available here), so the expansion cannot be written **as the register prints it**,
which is what clause 1 actually requires. A repair that guesses the wording would be #101 again in
the repair.

## The limitation that is not a false positive

`J-PAL` drops a leading element of its own name — the owner prints **The Abdul Latif Jameel Poverty
Action Lab** (read in their served chrome, 2026-10-23). The anchor therefore recovers *Jameel Poverty
Action Lab*: a true **suffix** of the name, not the name. **The flag is right and the quoted span is
short by two words.** Where an acronym is partial, the instrument locates the defect and under-states
the name — which is the safe direction, and is written into the tool beside the finding so the repair
does not copy the anchor.

## The false positive that mattered, and why it is the general lesson

The first build reported **one Arabic anchor**: `KYK`, spanning `KPSS … YKS` in the Türkiye piece,
across **180 characters of Arabic**. The word recogniser emits only Latin words, so in an Arabic body
two unrelated Latin acronyms are **consecutive tokens**, and the adjacency guard was counting token
indices rather than text. Adjacency was then measured in the source text and the count fell to zero.

**A recogniser's notion of "the next word" is a claim about the script it was written for.** This is
#109's lesson — *a composition check's error rate is set by whether it knows the intended assembly* —
arriving on the input side, and it is the fourth time in three weeks that this operation's harness
produced a false positive before its code was right. The header's claim *0 Arabic anchors, by
construction* is true only because it was measured and found false first.

## What this completes, and the asymmetry that is now true twice

#101 clause 3 makes the **Arabic** rendering the control for a disputed institution, because Arabic
cannot carry a Latin-script acronym and the composer is therefore **forced** back to the register. An
instrument anchored on the acronym consequently has **no purchase on the edition #101 trusts most** —
0 anchors across all 44 Arabic bodies, by construction.

Yesterday's #112 found the same asymmetry from the other side: **128 of its 134 declined quotation
tokens are Arabic**, because Arabic cannot hold a Latin quotation either. So:

> **The edition that is forced to answer the name question is the edition no instrument of ours can
> read the answer from.** #86 asked which questions only one edition can answer; #101 added which
> questions one edition is *forced* to answer; **#113 adds the cost — a forced answer is the most
> trustworthy one we have and the least machine-readable, and the two properties have the same
> cause.** Every instrument we build on the English side widens that gap.

## Proof

Three bites, controls green on either side of each, every injection asserted to have changed the file
before the check was run on it (#35, and the 09-14 trap).

| | Injection | Result |
|---|---|---|
| control | none, clean tree | **exit 0** |
| bite 1 | strip `Sierra Leone Education Innovation Challenge` from a clean piece's `sources[]`, body untouched | **exit 1**, names the piece and the acronym |
| bite 2 | restore the literal 103-day published defect — `Kenya Senior School Heads Association` in the body | **exit 1** — *the instrument catches the error that earned #101* |
| bite 3 | repair a carried finding so `KNOWN_OPEN` goes stale | **exit 1** — the exception list is asserted to be a subset of the findings, so it can only shrink |
| control | after all three, tree restored | **exit 0** |

## Binding

1. **Where a body expands an acronym, the piece's `sources[]` carries that expansion** — #101 clause 1,
   now gated rather than checked at a hand-off. Standing assertion 37, wired into `postbuild`.
2. **An exception list inside an assertion is asserted to be a subset of its own findings.** An
   exception nobody is forced to delete is a permanent exemption wearing a date.
3. **When a recogniser cannot bound its subject, look for a second token in the artefact that bounds
   it.** The general form, and the part worth carrying past acronyms: *two detectors disagreeing by 36
   over one population is not a tuning problem, it is the absence of a specification — so stop tuning
   and go looking for where the artefact already states the answer.* A footnote marker bounds a
   footnote; a quotation mark bounds a quotation (#112 found 529 of them the same way); an acronym
   bounds a name.
4. **Adjacency is measured in the source text, never in the token index**, in any recogniser this
   operation writes that will ever meet a second script.

## Counts moved at the point of filing

**Five homes** — §3's range, §3's heading, §1's count line, `CLAUDE.md`'s non-negotiables, and the
conditional fifth: the **assertion-discipline family's member count, which this ruling takes to
thirty-eight.** Register after this filing: **37 tools · 22 `postbuild` · 34 of 37 gating**, all three
derived by `qa_patch_queue` rather than counted by hand.
