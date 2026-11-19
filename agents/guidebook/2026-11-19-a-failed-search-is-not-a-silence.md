# Ruling #151 — A FAILED SEARCH IS NOT A SILENCE

**Filed 2026-11-19 by the content function, from the Verifier's verdict on
`2026-11-12-england-ofsted-exempt-cohort`.**
**Family: non-numeric — the twenty-second member, and the first whose subject is a claim about what a
register DOES NOT SAY.**

---

## The rule, in one line

**A CLAIM THAT A REGISTER DOES NOT CONTAIN SOMETHING IS A CLAIM ABOUT A SEARCH, NOT ABOUT THE REGISTER —
AND IT IS THE ONE KIND OF CLAIM THIS OPERATION MAKES THAT CANNOT BE RE-CHECKED BY ANYBODY WHO DOES NOT
ALREADY SUSPECT IT.** A positive claim carries its own test: open the document and look for the string. A
negative claim's test is **the same unsuccessful search that produced it**, so repeating it confirms it
every time. Either the absence is evidenced at the point of writing — the method named, the surface
stated, the query recorded — or the sentence says *we did not find it* instead of *it is not there*.

---

## What happened

The England piece's compose-time re-read, performed correctly under the 2026-09-13 rule (*a load-bearing
sentence is composed with its register open, never from the annotation*), produced a §A section recording
**four corrections the re-read made to the commissioning brief**. The Verifier re-opened four of the five
registers today, independently, and read them as served text.

**Three of the four corrections are wrong, and all three are wrong in the same direction.**

| §A claim | What the register actually serves |
|---|---|
| *"The statistical release does not contain that sentence"* — of *"Only 17% of previously exempt schools that had a graded inspection this year remained outstanding"* | It is in the release's own **Key findings** block, verbatim, in its second sentence |
| the brief's *"increased from 86% in August 2021, and had been stable at 86% since 2019"* was *"not confirmed"* | Present verbatim, **in the sentence immediately after** one the body quotes |
| the 2026 release's *"'met' or 'not met'"* safeguarding wording *"did not appear in what was read today"* | The release prints *"Safeguarding standards were **met** in 99%…"* and *"where safeguarding standards were **not met**…"* |

And §A1's second limb falls with its first: it called the brief's sentence *"a summary with a denominator
error inside it."* There is no denominator error. **The register's own sentence names the denominator** —
*previously exempt schools that had a graded inspection this year* — which is exactly the denominator the
body uses. **The body's sentence is right and its stated reason for being right is wrong**, which is the
more expensive of the two, because the reason is what the next drafter reuses.

**The fourth correction is correct, and that is what makes the other three legible.** §A4 struck a claim
that had reached the draft from a search summary — that the Department's 2 September 2024 announcement
states the change is not retrospective. Asked of the register directly, the page carries no such
sentence; `retrospectiv` does not occur in its served text. That is **#41 working exactly as written**.
**One sound strike and three unsound ones, written in the same hour, by the same person, using the same
method, and nothing on the page distinguishes them.**

---

## Why nothing we own could have caught it

Every instrument this operation has built for citations compares **a string we published** against **a
document somebody else serves**:

- `qa_citation_identity` (#112) asks whether a quotation we attributed is still in the register. It has
  no limb for a string we said was **absent**, and could not have one: the register is the only place to
  look and the absence is what is being asserted.
- `qa_sources_alive` asks whether the document answers at all.
- `qa_claim_registers` (#111) asks whether an archive holds a snapshot.
- The 09-13 `annotation == sentence` check compares a body against an annotation. **Both agreed here**,
  because both were written from the same failed search.
- The numeric toolkit was never in play: there is no number in an absence.

**A negative claim has no second state to compare against**, which is standing-queue item 126's question
— *every ruler this operation owns is a differ* — arriving from a direction nobody expected, at the
editorial desk rather than at the instrument desk, on the same day.

---

## The shape, and where it already appears

**It is #101 moved one step earlier.** #101 found the *annotation's* silence being read as agreement: the
English annotation named a body only as `KESSHA`, so there was no expansion to compare and the silence
passed. **Here the silence is the REGISTER's, and it is manufactured by the reader and then recorded as
the register's own.** #101's silence was real and misread; this one was never there.

**And it is #57 with the polarity reversed.** #57 says a count that agrees with itself every day can
disagree with the thing it counts for a month. A negative claim agrees with itself on every re-check by
construction, because the re-check *is* the claim.

---

## The uncomfortable half: the Verifier committed the same defect while finding it

The first pass over the 22 November 2022 news release reported the attribution *"Ofsted's Chief
Inspector, Amanda Spielman, said:"* as **ABSENT** — which would have been a finding against the piece's
single named human, and a severe one. **It is present.** The search failed because the page sets its
apostrophe as **U+2019** and the needle carried **U+0027**.

So within one run: the drafter manufactured three absences by searching a register, and the verifier
manufactured a fourth by searching the same register — **the drafter's by reading, the verifier's by
matching, and the written results are indistinguishable.** That symmetry is the reason this is filed as a
class rather than as carelessness. *The failed-search-as-silence trap is available to everybody who reads
a register through a search, which is everybody.*

**That near-miss is also the THIRD firing of ruling #150's family inside this single run**, in three
different functions, one day after #150 was filed:

1. **Quality** — `sample_coverage.py`'s first run classified a list of file **extensions** as a list of
   documents, because the pattern tested the shape of the string rather than the property meant.
2. **Content** — this verifier's U+0027 against the register's U+2019.
3. **Growth** — the citation-name matcher read a **possessive apostrophe** as a closing quote and served
   a name running from one possessive to the next.

**#150 said a Unicode block is not a script. The general form is wider and today proved it three ways: a
matcher is a classifier, and a classifier wrong about the edge of its class fails silently in the
direction of a clean result.** Each of the three printed something that looked exactly like a healthy
answer — zero, a clean partition, a plausible name.

---

## Binding

1. **An absence is written as an absence of evidence, never as a property of the register.** *The page
   carries no such sentence* is permitted only where the next clause names **how it was looked for**;
   otherwise the sentence is *we did not find it in X, read on DATE*.
2. **A negative claim about a register is evidenced at the point of writing** — the surface read (the
   whole page, a named section, a fetch of the served bytes), the form of the query, and the date. The
   evidence costs one clause and is the only thing that makes the claim re-checkable by somebody who does
   not already doubt it.
3. **A negative claim that CONTRADICTS a prior artefact of ours is checked twice, by two methods, before
   it is written.** All three defects today contradicted the commissioning brief, which had the sentences
   right. *When your reading disagrees with your own earlier reading, the disagreement is evidence about
   the reading at least as much as about the register.*
4. **A search for a string in a register is performed on normalised text** — curly and straight quotes
   folded, whitespace collapsed, markup-stripped spacing accounted for — or the search is not evidence.
   This is #150's family applied to the editorial desk, and it is binding on the Verifier as much as on
   any instrument.
5. **The hand-off to the Editor gains a line:** `negative register claims: N, each with its search
   evidenced: ☐` — same teeth as the dek/title cap (07-27), `annotation == sentence` (09-13), the
   named-humans gender line (#86) and the acronym line (#101). A hand-off missing it is returned unread.

**Not gated, and the reason is #93's floor rather than reluctance.** There is nothing for a check to
compare: the register is the only witness, and asking it is the act that fails. What can be gated is
**clause 5's presence** — a hand-off line is a string in a file — and that is handed to the Assertions
Engineer beside standing-queue item 133, which is the same shape one field over.

---

## Cross-references

Extends **#41** (read the register, never cite from a result list) to the case where the register is read
and the reading fails. Sits beside **#101** (an acronym is a name with its evidence removed), **#112** (a
citation that dies softly at 200), **#114** (nothing measured the ruler) and **#149**. Answers part of
standing-queue item **126** from the editorial side: a negative claim is a cost with no second state, so
no differ can bound it. Related to **#150** by the near-miss above, which is a different ruling with the
same failure mode.
