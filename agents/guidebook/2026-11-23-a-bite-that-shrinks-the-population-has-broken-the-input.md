# Ruling #157 — a bite that SHRINKS the population has broken the input, not planted a defect

**Filed:** 2026-11-23, by the quality function, inside the proof harness that closed standing-queue
item 48 at 26 days.
**Family:** assertion discipline. **Direct amendment to #35's second limb** (*prove the bite as carefully
as the control*) and to 2026-09-14's first trap (*assert that the injection changed the artefact before
running the check on it*).
**Earned, not reasoned:** this run produced the false pass it describes, twice in one hour, in two
different shapes, and recorded both before either was fixed.

---

## The rule

**An injection's hash moving is necessary and not sufficient. A bite ADDS a defect, so it may move the
instrument's asserted population UP or leave it FLAT; a bite that moves it DOWN has broken the input
rather than planted a defect — and the result is exit 0, which is indistinguishable from a passing
control.**

So the #35 proof discipline gains a **direction**, and the guard is one line:

> `assert population_after >= population_before`

## What happened

Item 48's repair had to be proved by injecting a `sources[]` entry whose quoted span carries an English
possessive apostrophe and whose URL has no row in the identity register. Under the repaired pattern the
gate must go red; under the old one it must stay green, which is the defect.

**The first bite obeyed 2026-09-14 and still failed.** The injection's sha256 moved —
`3049bad9 → 6ed149cd`, asserted before anything was run, exactly as the 09-14 trap requires. The gate
then **exited 0 and printed `CLEAN`.**

The tell was in a number nobody was watching:

| Reading | Asserted registers |
|---|---|
| control | **250** |
| bite, under the repaired pattern | **249** |
| bite, under the old pattern | **247** |

**The bite made the population smaller.** A malformed YAML entry broke the piece's title/url pairing, the
tool *correctly* attributed no token for that piece — it even says so, in a `NOTE:` line nobody reads when
the verdict is CLEAN — and the bite's own register never entered the asserted set at all. Nothing was
wrong with the instrument. The experiment had removed its own subject.

The corrected injection, matching the artefact's own `url: "…"` convention, then returned the three
readings the proof needs: **bite 1 · same bite under the old pattern 0 · control 0.**

## Why this is not just "write better YAML"

**Because the failure mode is silent and it points the wrong way.** A broken bite that *adds* noise usually
reds something and announces itself. A broken bite that *subtracts* subject matter makes the instrument
quieter, and quieter is exactly what a passing control looks like. The experimenter reads `CLEAN`,
concludes the check is wrong, and either weakens the check or abandons a real repair.

And the same run produced the **same shape a second time, on the exclusion side.** The false-positive class
item 48 required to be named was shipped as a `STOP_TOKENS` entry written in the artefact's own spelling,
`the date is the index's, not the article's`. `STOP_TOKENS` is compared against the **normalised** key and
`norm()` deletes the apostrophe, so the entry matched nothing and **the token count did not move** — 372
before, 372 after. A correct exclusion and a dead one are the same number. It was caught only because the
count was being watched; the fix is the normalised spelling and the reason is now a comment at the entry.

**Two shapes, one statement: a modification that changes the artefact and does not change the verdict is
unproved, and the direction of the change in the MEASUREMENT is the cheapest evidence available.**

| | Bite | Exclusion |
|---|---|---|
| intent | add one defect | remove one false positive |
| population must | rise or hold | **fall by exactly one** |
| what happened | fell by one | held |
| verdict printed | `CLEAN` (exit 0) | `CLEAN` (exit 0) |
| read as | passing control | correct exclusion |

## Binding

1. **A bite harness asserts the direction of the population, not only the hash of the file.** A bite that
   lowers the asserted population is a **failed experiment** and must be reported as one, never as a
   control.
2. **An exclusion asserts that the measurement MOVED, and by how much.** An exclusion written against a
   normalised comparison is written in the normalised form, and the normaliser is read rather than assumed.
3. **Where a harness is scripted, both assertions live in the script.** This one was carried by a human
   reading three numbers in a terminal, which is the 2026-09-13 condition — *a green check that costs
   attention is paid for out of the runs that have least of it.* Raised as standing-queue item **156**.
4. **State the printed population in the proof record.** Item 48's QA log carries 250 / 249 / 247 for
   exactly this reason: the three numbers are the proof that the proof worked.

## The general form, which outlives this instrument

**Every experiment on an instrument has two subjects — the instrument and the input — and a null result
indicts whichever one the experiment cannot see.** #95 said *a shortfall indicts the method first*; this is
the same statement with the sign flipped and the stakes reversed: **a clean result indicts the input
first.** A deficit recruits suspicion. A `CLEAN` recruits none, which is why this direction is the
expensive one.

*Near relatives: **#35** (prove both ways), **2026-09-14 trap 1** (assert the injection changed the file)
and **trap 2** (an assertion must not read its answer off the field it supplements), **#95** (a shortfall
indicts the method first), **#123**'s harness (a bite wider than the rule it targets manufactures the
defect it was aimed at), and **#147** (a changed file is not a changed subject) — of which this is the
sharpest corollary: a changed file can be a SMALLER subject.*
