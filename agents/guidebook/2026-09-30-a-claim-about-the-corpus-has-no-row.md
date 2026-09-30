# Ruling #77 — a claim about the corpus has no row in a per-source check

**Filed:** 2026-09-30, by the Verifier's verdict on Edition 05 row 6 (Rwanda).
**Origin artefact:** `content-drafts/verdicts/2026-09-30-rwanda-teacher-certification-verification.md`, item 2.
**Family:** the enumeration family (*a green check is scoped to what it enumerates*), pointed for the
first time at a **hand-off table** rather than at an assertion or an instruction.
**Cousins:** #57 (a section claiming no count cannot be caught claiming a wrong one), #70's amendment
of the 09-20 rule (a bucket set is an enumeration too), the 2026-08-17 orphan sweep (a link sweep
cannot find a page nothing points to), and the 2026-09-13 `annotation == sentence` rule, which this
ruling is about the *shape* of rather than a failure of.

---

## The ruling

**A sentence whose subject is the set of sources cannot be checked by any instrument whose unit is a
source.** The `annotation == sentence` table has one row per register; a claim about the *absence of a
property across all registers* has no row, so it passes every gate by not being addressable by any of
them. Such a sentence is verified by **enumerating the set and looking for the counterexample**, and
until that is done it is an assertion, not a finding — however much it reads like the most
carefully-earned sentence in the piece.

**And the corollary, which is the part that cost a real defect:** *a commission may not assert a
property of the corpus.* An instruction that says *say so in the piece* converts a claim into prose
without ever sending it through a gate. The drafter executes faithfully — that is what a good drafter
does with a written instruction — and the claim arrives in the body having been checked by nobody,
because at every desk downstream it looks like a decision that was already taken.

---

## What happened

Edition 05 row 6's §*What cannot be read* opened on the sentence the piece itself frames as the
load-bearing one:

> One absence is structural and belongs in print rather than in a footnote. **Every voice in the
> record for this story reaches us through the funder's channel or the ministry's own.**

It is false, and it is falsified **twice over**:

1. **By the piece itself, eight paragraphs earlier.** ¶99 reads: *"What connects those tiers to the
   2026 reform reaches us through **one newspaper**. The New Times of Kigali reported on 24 August
   2026 … State Minister for Education Claudette Irere … announced a five-year window."* A voice
   reaching the reader through a Kigali newspaper is neither the funder's channel nor the ministry's
   own — and the piece says so in its own words, twice, and builds a guardrail on it.
2. **By the newspaper's own page**, already in `sources[]`. Under the heading *"Teachers' reactions"*
   it carries two named teachers: **Antoine Butera**, of Kigali Parents School, in education since
   1990, and **Joseph Mushyikirano**, headteacher of Groupe Scolaire de Mayange A. Butera's quotation
   contains the piece's own unstated objection: *"The challenge, however, is that not all teachers may
   receive government support."*

The claim originates in the **commission** of 2026-09-25, at Test 4, in these words: *"the voice gap
is stated: every voice in the corpus reaches us through the funder's or the ministry's channel. Say
so in the piece."* The 09-25 recon had opened that newspaper page the same day, for the tier
question, and read past the reactions section.

---

## Why four gates could not see it

| Gate | Unit | Why it is blind to this sentence |
|---|---|---|
| The drafter's `annotation == sentence` table (09-13 rule) | one row **per source** | The sentence's subject is the *set*. There is no row to put it in, so it is not omitted — it is unaddressable. |
| The Editor's five tests | the **frame** | The frame is correct. The piece *is* about a record reached through two channels; the sentence overstates by one register. |
| The Arabic gate (#42) | **parity** | The Arabic says exactly what the English says. Parity is perfect and both are wrong — the 09-18 shape where `annotation == sentence` cannot help because both sides agree. |
| The numeral multiset | **digits** | The sentence contains no number. Fifth consecutive non-numeric verdict on this edition. |

The common property: **every instrument we own takes a source, a sentence, a digit or a page as its
unit, and this claim's unit is the corpus.** A universal negative over a set is the one shape a
per-member check cannot express — which is the orphan sweep of 2026-08-17 moved from the page graph
to the source list: *a check that walks the members cannot see a property of the membership.*

---

## What to do about it — three things, all cheap

1. **The hand-off gains one row that is not per-source: `claims about the corpus`.** The drafter lists
   every sentence whose subject is *the sources*, *the record*, *the corpus*, *every voice*, *no
   register*, *nothing read* — and states, per sentence, the enumeration that supports it. A sentence
   in that row without an enumeration behind it is an open item, exactly like an untraced figure.
2. **A commission may state a gap as a question, never as a fact.** *"Is there a voice outside the two
   channels? If not, state the absence in print"* survives being wrong; *"every voice reaches us
   through the funder's or the ministry's channel — say so"* does not. The Editor owns the frame; the
   corpus is the Researcher's and the Verifier's, and a commission that asserts one has crossed a
   desk.
3. **Bound the claim to what was actually enumerated.** The closing edit was two words shorter than
   the sentence it replaced: *"Every voice in **the programme's record** reaches us through the
   funder's channel or the ministry's own"* — verified against nine named voices, all nine inside the
   two channels. **A narrowed claim that is true is worth more than a wide one that is nearly true**,
   and it usually costs fewer words, because the scope was doing the work the adjective was pretending
   to do.

---

## The general form, which is the part worth carrying

*Absence is the one claim a publication cannot make by reading a document — it can only be made by
enumerating a set and saying which set was enumerated.* This operation already knows that about
**registers** (#69: *enumerated*, *found*, never *does not exist*; the four-channel enumeration in
this very piece is the rule executed well) and it did not know it about **its own source list**. The
piece stated a state's absence with an enumeration behind it, in the same file where it stated its own
corpus's absence with nothing behind it — **two absence claims, four paragraphs apart, one of them
proved and one of them assumed.**

And there is a reason the unproved one felt safer: the enumeration was ours. A claim about someone
else's channels is obviously a claim; a claim about our own reading feels like a report. **The corpus
is a register too, and it is the one register we never re-open.**
