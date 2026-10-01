# Ruling #82 — the guard that proves an injection landed must name which tree it is comparing against

**Filed:** 2026-10-01, by the QA lane, from inside its own proof procedure — the third time in five
days that proving an assertion has produced a ruling about proving assertions.
**Artefact:** the bite harness for standing assertion 28, rewritten after its guard fired falsely on
the most valuable bite of the set.
**Family:** assertion discipline (twenty of eighty-two).
**Cousins:** #74 (*a hash proves the injection landed, not where*), #79 (*assert the bitten instrument
still executes, or a syntax error will pass for a finding*), #35 (prove both ways), and the 2026-09-14
rule that an injection is written against the **served** shape.

---

## The ruling

#74 and #79 between them require three things of a bite: that it changed the artefact, that it changed
the region its label names, and that the bitten instrument still runs. Today adds the fourth, which
is smaller and sharper than any of them:

> **A guard that asks "did the file change?" must be told *change from what*.** Asking `git` is the
> obvious implementation and it is wrong for the single most valuable bite in any set — the
> **historical** bite, which re-introduces a defect the same run has just fixed in the working tree.
> That injection is, byte for byte, a **revert to `HEAD`**. `git diff --quiet` therefore reports *no
> change*, the guard reports *failed experiment*, and the best bite available is thrown away as
> broken.

The fix is one line: snapshot the file, inject, compare against the **snapshot**, restore from the
snapshot. Never against the index, never against `HEAD`.

---

## The case

Seven bites were written for `qa_pair_frontmatter`. Bite 1 was the real defect of the day: remove the
`arabicVersion:` line this run had just added to the Egypt pair, and confirm the check fails on it.
The harness's guard was `git diff --quiet -- <file>`, written from #74's instruction to assert that the
injection landed.

What happened, in order:

1. Bite 1 removed the line. The file became **identical to `HEAD`**, because the line was today's
   uncommitted fix.
2. `git diff --quiet` returned 0 — no change — so the guard printed *INJECTION DID NOT CHANGE THE
   FILE — failed experiment, not a passing control* and skipped the run.
3. The harness then "restored" the file with `git checkout --`, **which discarded the fix.**
4. Bites 2 through 5 each ran against a tree that silently carried the Egypt defect again. They all
   exited 1 — correctly, for their own reasons — but each reported **two** findings instead of one,
   and the exit code alone could not tell the difference.

Both halves of that are #79's lesson arriving from new directions. *The exit code alone reads exactly
like a successful bite* — here it read like **seven** successful bites, one of which had not run at
all and five of which were contaminated. Counting the **findings** rather than the exit code is what
separated them, exactly as counting the failing **fixtures** did yesterday.

Rewritten with `cp` snapshots, the same seven bites produced **exit 1 with exactly one finding each,
each the finding its label named.** Nothing about the assertion changed between the two runs.

### The second limb: a restore is part of the experiment

`git checkout --` is a plausible-looking restore that is only correct when the file was clean before
the injection. In a run that fixes a defect and then bites it, it is a **destructive** restore, and it
destroys precisely the work the bite exists to validate. A harness restores what it saved, not what
some other process thinks the file should be.

---

## The general form

*An experiment on a working tree has three states, not two: before the fix, after the fix, after the
injection.* A guard or a restore that collapses them into "committed versus not" will be wrong on
exactly the day the run has done something worth proving — and it will be wrong in the direction of
silence, which is the direction that does not get noticed.
