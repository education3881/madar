# Ruling #128 — An assertion whose only repair path runs through the artefact it blocks cannot be gated

**Filed** 2026-11-05 · **Lane:** QA / assertion discipline · **Earned by** standing-queue item 31,
taken from the OPEN head at **15 days**, the oldest row on a board with no DEFECT open.
**Family:** assertion discipline — the **forty-ninth** member.
**Instrument:** standing assertion 42, `agents/tools/qa_prior_publication.py`.

---

## The rule

**A gate must not red on a condition whose only repair is an action that a red gate forbids.** Where
that shape occurs, the condition is **printed with its number and its owner**, and the gate asserts the
*upkeep of the record* instead — the thing that is in the operation's own hands on the day the gate
runs.

**The test, in one question:** *if this limb goes red, what is the next action, and can it be taken
while the limb is red?* If the answer is no, the limb is not an assertion; it is a lock.

## How it was earned, and the row asked for the lock by name

Standing-queue item 31 asked *which of this operation's claims are checked only by the next run's
goodwill?* and named the first answer in writing:

> an assertion that reads the previous deploy's conclusion through the `actions: read` grant the job
> already holds, and goes RED when it failed.

That assertion cannot be built. The chain is three steps and every step is an operating fact of this
publication:

1. A failed deploy is repaired by **pushing a commit** — the publish step dispatches `astro-pages.yml`
   when the origin moves, and nothing else here can make the origin move.
2. A push is made by a run **whose build is green**, because `npm run build` runs the gate set and a
   red build stops the run before its commit.
3. So a gate that reds on a red prior deploy **forbids the one action that clears it.**

Applied to the day it would have mattered: on **2026-10-20** the growth function shipped 80 dangling
JSON-LD `@id`s, `qa_jsonld` failed the deploy's build job, and the origin served the 10-19 build for
two days. Had this gate existed with the strand asserted, the **2026-10-21** run would have been unable
to build, unable to push, and therefore unable to repair the regression — **a two-day publication gap
converted into a permanent one, by an instrument built to shorten it.**

## Why this is NOT #93, and the distinction is the ruling

#93 declines a limb because **a floor above today's reality would red every build**: the subject is
wrong *now*, the gate would be correct, and the operation cannot afford to be stopped until the subject
is repaired. The decline is about **cost**, and it expires by arithmetic the moment the count reaches
zero (#71's watch, queue item 71).

This decline is about **reachability**, and it never expires. The gate would be correct, the subject
*can* be repaired, and the gate makes the repair unreachable. A #93 decline is a floor waiting for a
better corpus; **this is a floor waiting for a different universe.** The two look identical in a tool's
output — both print a number and assert nothing — and they must not be written the same way, because a
#93 decline is a **promise to come back** and this one is a **finding about the topology.**

Nor is it #125, a decline that delegates to a sibling: there is no sibling here. The condition has **no
owner among the instruments at all**, and the owner it does have is a human reading the brief (#71).

## What the instrument does instead, and what that buys

The subject splits in two, and only one half is in the operation's hands while the gate runs:

* **The publication's state** — did the last deploy succeed, and how many commits on `main` has no
  successful deploy carried? *Printed. Never asserted.* The strand is the number queue item 77 named as
  invisible in `git log` by construction, and it now exists in a file instead of in whichever run
  remembers to look.
* **The record's upkeep** — is there a register of observations, is it well-formed, is every row
  **re-derivable from this repository's own git history**, does it walk forward, and **did the daily run
  observe before it built?** *Asserted, all five limbs, from `postbuild`.*

**The second half is the whole of what a gate can honestly own here**, and it is not a consolation
prize: limbs 1–4 all stay green for a run that observes nothing at all, because the rows a previous run
wrote stay well-formed forever — which is item 31's own defect one level out. **Limb 5 closes it** by
requiring a row written by this `GITHUB_RUN_ID` when `GITHUB_WORKFLOW` is the daily run, and by printing
SKIPPED everywhere else. *A duty is not a gate (queue item 60); a duty scoped to the identity that owes
it is.*

## The corollary, which is where the generalisation lives

**Scope is what makes the difference between an assertion and a lock, and the scope must be proved by a
control rather than claimed in a comment.** Limb 5 would be a lock if it ran in the deploy job: the
deploy owes no observation, so every deploy would red on the daily run's silence — and the deploy is the
publication. The proof that it does not is **control 4**: bite 5's own failing tree, re-read with
`GITHUB_WORKFLOW` set to the deploy job's name, which must exit 0. Nine proofs were run; that is the
one that distinguishes this gate from the lock it nearly was.

## The general form

> **Before gating a condition, trace its repair path. An assertion is a demand for an action; if the
> assertion's own red light blocks that action, it is not a demand but a deadlock — and a deadlock in a
> build gate is indistinguishable from a correct refusal, for exactly as long as the condition it
> watches stays true.**

The family's three declines now read as a ladder: **#93** — *I cannot afford to assert this yet*;
**#125** — *somebody else asserts this, and I must check that they do*; **#128** — *nobody can assert
this, because the assertion would prevent its own remedy.*

---

*Proved per #35: five bites red (dropped field · falsified `strand_len` · newest row naming a foreign
SHA · a register walked backwards · a newest row written by somebody else's run), four controls green
(the register as written · two rows walking forwards · an old foreign-SHA row with a sound newest row,
which must stay green and print one unverifiable · bite 5's tree read from the deploy job). Every
injection asserted to have changed the file first (09-14). **Bite 1 was caught by two limbs**, so
provenance now declines a row the schema has already failed — a defect two limbs catch proves neither
of them necessary.*
