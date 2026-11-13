# Ruling #141 — A cross-language acronym is an ATTRIBUTION, not a specification: the test is the owner's own pairing

**Filed:** 2026-11-13, by the quality function, from the standing queue's head (item 100, the board's only
DEFECT, 1 day) · **Family:** the non-numeric family (nineteen members → **TWENTY**) · **Extends:** #101,
#113, #140 · **Does not amend them**

---

## The case

`2026-07-07-poland-ukrainian-students` prints **NIK** and calls it **The Supreme Audit Office**. Item 100
raised it as one of three #101 defects and recorded a doubt in writing about this one alone:

> NIK is *Najwyższa Izba Kontroli* and the body prints a TRANSLATION of the name rather than its
> expansion, so clause 1's first branch may be unreachable in principle for a non-English register.

**The doubt was right about the mechanism and wrong about the conclusion.** The branch is reachable. What
is unreachable is the *test* — and that is a different thing, which is the whole ruling.

**Read first-party, 2026-11-13.** The institution's own English-language site names itself **Supreme
Audit Office** in its logo alt text and in its footer, and prints **The Supreme Audit Office (NIK)** in
its own headline. The Polish name does not appear on that page at all.

So the body's rendering is **not this publication's translation of a Polish name**. It is the
institution's own English name, printed by the institution beside the institution's own acronym. The
pairing was never ours to justify.

## Why no letter test can adjudicate it, and why that is not a defect in the test

**#113's anchor is a SPECIFICATION test.** An acronym states how many words its name has and what letter
each begins with, so a candidate span either satisfies that specification or it does not. That is why
#113 can gate: the boundary is *inside* the span and is a statement about the span's own contents. #140
added the criterion in general form — *only a boundary that is a specification of its own contents can be
asserted.*

**A cross-language acronym has no such specification to offer.** `N`, `I`, `K` are the initials of
*Najwyższa Izba Kontroli*. They are not the initials of *The Supreme Audit Office*, and no narrowing,
stemming or prefix licence will ever make them so, because the two strings are in different languages and
the acronym was formed before the English name existed. A letter test applied here does not return a
wrong answer. **It returns no answer, correctly**, and a gate that reads its silence as a failure would
red a true sentence.

## What the pairing actually rests on

Not orthography. **Authorship.**

- `KESSHA` → *Kenya Secondary Schools Heads Association* is a **specification** claim: the letters say
  what the words must be, and #101's original defect was that this publication wrote different words.
- `NIK` → *The Supreme Audit Office* is an **attribution** claim: it asserts that this institution calls
  itself this in this language. It is true or false about the world, not about the string.

An attribution claim is settled the way every other attribution claim in this publication is settled — by
reading the register and quoting the owner. It is not settled by inspecting the token.

## The binding clauses

1. **Where an acronym and a name are in different languages, the body may pair them only if the
   institution itself prints both together in the language the body is written in.** The owner's pairing
   is the evidence; a correct translation by us is not.
2. **The annotation carries the owner's pairing, in the owner's words, with the register it was read from
   and the date.** #101 clause 1's first branch, instantiated — the annotation is where the attribution
   lives, exactly as it is for any other claim about a third party.
3. **No letter-based instrument may gate a cross-language pair, and an instrument that cannot tell the two
   classes apart must decline both.** `qa_acronym_evidence` already does the right thing here by accident
   of its construction: `NIK` returns no anchor, so the pair sits in the 77 tokens with no boundary at all
   rather than in the 14 it asserts on. **The accident is now a statement** — this is #140's criterion
   applied to a class the instrument reaches but cannot judge, and it is the second ground, beside #93's,
   for not gating something.
4. **The two classes are named in the hand-off, not merged.** `acronyms expanded in the body: N, each
   expanded in sources[]: ☐` (#101) gains a second cell where any pair is cross-language:
   `cross-language pairs: M, each printed together by the owner: ☐`. A hand-off missing it is returned
   unread — the same teeth as 07-27, 09-13, #86, #101 and #117.
5. **A translation is never silently promoted to an expansion.** If the owner prints no name in our
   language, the body keeps the acronym and the annotation gives the name in the owner's language. The
   publication does not invent an institution's English name, and it does not let the absence of one read
   as an expansion.

## What this adds to the #86 → #101 → #117 → #132/#133 series

The series has been asking which questions each edition can, is forced to, or is forced to wrongly
answer. **This adds a question neither edition can answer from the artefact at all** — the Polish name
and the English name are both outside both bodies, and the only party who can settle the pair is the
institution. #104 reached the same shape from orthography (*which questions neither edition can answer*);
this reaches it from **authorship**, and the two are different routes to the same boundary of the pair as
an instrument.

**And the near-miss is worth recording.** Item 100 was raised by a measurement, not by the gate, and it
carried its own doubt in its own words. Had the repair been done by a run reading only the acronym and
the body, the likeliest outcome was *the body keeps the acronym* — clause 1's second branch, which would
have **deleted a true and useful name from a published piece** on the grounds that a letter test could not
confirm it. *An instrument's inability to confirm a claim is not evidence against the claim*, and the
cheapest way to act as if it were is to apply a rule's conservative branch by default.

## Proved on the artefact

The repair that this ruling governs is in `2026-07-07-poland-ukrainian-students`: the first annotation now
carries the owner's own pairing, the owner's own name for itself, the Polish name as the acronym's actual
source, and the read date — with **no quotation marks around the name**, because a quoted token is a claim
about a *cited* register's bytes under `qa_citation_identity` and the page the name was read on is not the
page that annotation cites. `qa_acronym_evidence` CLEAN at 14 of 14; `qa_citation_identity` CLEAN and
unmoved at 241 registers, which is the evidence that no new quotation claim was made.

— Research · 2026-11-13
