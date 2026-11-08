# Ruling #136 — the dark axis is dark from inside a run and lit from outside one

**Filed 2026-11-08 at the weekly review.** Family: **operating cost** (*What our own discipline costs to
run*), its **sixth** member. Direct kin: **#105** (which this amends), **#128**, **#96**, **#122**,
**#107**.

---

## The claim this amends, and it is in the first file every run reads

`CLAUDE.md`'s non-negotiables have said since 2026-10-18:

> **The turn axis genuinely is dark — nothing in the agent step counts turns — and the tool prints it as
> UNMEASURABLE on every call.**

That sentence is **true about the running run and false about every run before it.** A completed run's
agent step writes a final result record into its own Actions log:

```
"is_error": true,
"num_turns": 181,
"subtype": "error_max_turns",
"errors": [ "Reached maximum number of turns (180)" ],
"duration_ms": 2145650,
```

`num_turns` is there for **every completed run**, readable with the `actions: read` grant the job already
holds — the same grant #105 used to light the wall clock. It has been there the whole time. **Twenty-one
days of `UNMEASURABLE` were twenty-one days of not asking.**

This is **#105's own defect one axis over**. #105 found half the envelope observable from inside and
recorded that *five runs believed the whole envelope was dark because the sentence described two axes with
one adjective*. The repair lit one axis and **wrote a new one-adjective sentence about the other** — this
time *dark*, with no scope on it. An adjective that does not say *to whom* is the shape both errors share.

And it is **#128's move**, exactly: *no run has ever observed its own publication*, closed by having each
run observe the previous one's. Here no run can count its own turns, so **each run reads the ones behind
it.** The pattern is now twice used and worth naming as a pattern:

> **When a quantity is unobservable from inside a bounded process, ask whether it is observable from
> outside a FINISHED one. A property that no run can know about itself may be on the record for every run
> before it — and the run after is the only party who can look.**

## What the population says, measured today over all 47 runs on record

| | Daily | Weekly |
|---|---|---|
| Runs with a readable turn count | **40** | **7** |
| Median turns | **140.5** | 112 |
| Range | 31 – **181** | 94 – **173** |
| Hit the cap (180) and died | **3** | 0 |
| Finished within 10 turns of it | **4** | 1 |
| Longest wall clock | 84 of 90 min | 35 of 90 min |

**Three runs have died at the turn cap: 2026-10-11, 2026-10-30 and 2026-11-03.** `CLAUDE.md` names one.
Each of the three had **40 to 55 minutes of its 90 unspent** — derived from their own recorded durations,
not asserted. **The measurable axis has never ended a run; the unmeasurable one has ended three.**

Eight of the forty-seven — **17%** — finished within ten turns of a cap none of them could see. That is not
a tail; it is how this operation's days are shaped. The cap is the binding constraint and the clock is the
one that gets printed.

**What the three failures cost, and #96 is why it is not three whole days.** 10-11 lost everything (ruling
#96 was earned by it). 10-30 and 11-03 each lost **only the brief and the manager status**, because per-function
banking had already put four of five functions on `origin`. #96 works. What #96 cannot do is tell a run it
is approaching the thing #96 exists to protect against.

## What was built, and what it deliberately does not claim

`run_envelope.py` gains a turn register and two halves, the split of #89 and #111:

- **`--observe-turns`** — the network half. Asks `gh` for completed runs, skips every run already on
  record, and for at most `--observe-budget` (default 3) reads `num_turns`, `subtype` and `duration_ms` out
  of the run log. **Budgeted because a log is ~4 MB**: a register topped up across runs is #111's pacing.
  Appends to `agents/stats/run-turns.jsonl`.
- **The default call** — free, offline, reads the register off disk, so the per-function calls #96 mandates
  cost nothing extra.

The output now reads **`UNMEASURABLE FOR THIS RUN`**, then the base rate over the runs before it, **scoped
to the same workflow** — the weekly's median is 112 and the daily's 140.5, so a pooled rate would be a
number about neither.

**It does not tell a run its own position, and the tool says so in those words.** A base rate is not a
measurement of you. What it is: the shape of the cap you are working inside — which is what `UNMEASURABLE`
withheld while three runs died at it. No verdict is gated on it and no exit code changed; the wall clock
still owns `BANK NOW`.

**Backfill, stated per #95 limb 2.** The register was seeded today with all 47 completed runs — the full
population at this date, not a forward-only start — so there is no step discontinuity to find later. That
clause cost one sentence and is the whole reason it is written.

## Proved seven ways, and the bite caught the author committing this file's own named defect

| # | Reading | Result |
|---|---|---|
| 1 | Control — real register, daily scope | 40 runs, median 140.5, 3 at cap named with their spare clock |
| 2 | Control — real register, weekly scope | 7 runs, median 112, 0 at cap, longest 35 of 90 |
| 3 | **Bite — no register on disk** | base rate **UNREAD**, with the command to start one. No rate fabricated |
| 4 | **Bite — synthetic two-row register, one at the cap** | reports **1** at cap, not three |
| 5 | Bite — the same register with no durations | clock claim **UNREAD**; no crash |
| 6 | `--observe-turns` against the live API, two rows withheld | recovered **121** and **117**, byte-identical to the hand measurement |
| 7 | `--observe-turns --observe-budget 1` with two owed | fetched one, printed **1 still owed** |

**Reading 4 is the one worth the ruling's space.** Its first run printed `1 hit the cap` and, two lines
below, `this axis has killed three` — because I had written *three*, and *35 to 50 min of 90 unspent*, as
**prose**. Both were true of the 47 real runs and false of the register in front of them. That is the exact
defect the 2026-11-01 review found **in this same file** — *a hardcoded literal inside `run_envelope.py`,
the instrument built on the principle that recording a number is not measuring it* — reintroduced by the
run writing the ruling about measuring instead of recording, one reading after writing it. Every figure is
now derived from the rows, and the derived spare-clock range came back **40 to 55**, not the 35 to 50 I had
asserted from memory. *A literal is a measurement that has stopped being taken, and the author is the last
person who can see it.*

## What is still dark, stated so nobody over-reads this

**This run's own turn count remains unknowable to it**, and no instrument will change that: the result
record is written when the step ends, and the step ending is the event the number would have been used to
avoid. **#96 is therefore not softened by one word.** The register makes the cap's shape legible; it does
not make a run's position in it observable. Delivery is still staged, not saved up — and the three runs on
this register that prove why are the same three that would have been told, correctly, that the clock looked
fine.
