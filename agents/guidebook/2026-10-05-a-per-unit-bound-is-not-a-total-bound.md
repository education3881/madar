# Ruling #88 — a per-unit bound is not a total bound, and a check that cannot state its duration cannot be scheduled

**Filed:** 2026-10-05 · **Lane:** Assertions Engineer (QA) · **Family:** assertion discipline (26th member)
**Earned on:** standing queue item 1, open 18 days, displaced three times, the Edition 05
flip's only queue dependency — closed today by the one-queue rule rather than by anyone
remembering it.

## The rule, in one line

**A per-unit timeout bounds a unit, never a run — and a sweep whose worst case cannot be
stated is not a slow check, it is an unschedulable one.**

## What was actually wrong

`qa_sources_alive` had carried a per-URL `TIMEOUT = 20` since 2026-09-10, plus `flush=True`
since the 09-16 P1. Both are correct and neither bounds the **sweep**. Measured today rather
than reasoned:

- **59 held-cited URLs** × HEAD-then-GET, with the TLS path adding a second HEAD+GET inside
  `_still_served` → **4 × 20s × 59 = 79 minutes** of socket budget.
- And 79 minutes is the *optimistic* reading. `timeout=` on a urllib request is a
  **per-socket-operation** deadline, not a per-request one. A host dribbling one byte every
  19 seconds holds the connection open indefinitely. **The true worst case is unbounded.**

Demonstrated against a local black-hole server (accepts TCP, answers nothing, never closes):
the unbounded sweep was **killed at 45 seconds having completed 1 of 6 URLs**. That is the
measurement that makes this a ruling rather than a preference.

## Why it mattered, and why it sat for 18 days

The Edition 05 ledger names the full held sweep as **the last step before the flip commit**.
A step whose duration cannot be stated **cannot be placed in a sequence** — so the only
instrument standing between the wave and a dead source link was the one step nobody could
schedule. Eighteen days, three displacements from the queue head, and it closed only because
the 2026-10-04 one-queue rule put it first *by rule*. **The rule worked on its first Monday.**

## The design, and the half that is the actual lesson

A ceiling checked **between** units is not a ceiling. It bounds the loop and inherits the
unboundedness of whatever is in flight — which is precisely the thing being bounded. So:

- **The main thread owns the deadline; a daemon worker owns the socket.** The main thread
  consumes results against a monotonic deadline and returns when it expires. A daemon thread
  does not hold interpreter exit, so a wedged read is **abandoned rather than waited on**.
- **Per-attempt timeouts are clamped to the remaining budget**, so the tail of the budget is
  not spent inside one read that cannot finish.
- **Still sequential.** One worker, same order, same traffic. Going parallel would have made
  it fast *and* rude; 59 concurrent requests at UNESCO is a different decision from bounding
  our own run.

**Proved both ways (#35), and the bite proved as carefully as the control (#74):**

| | Result |
|---|---|
| **Bite is real** (unbounded, black-hole host) | killed at 45s, **still running**, 1 of 6 done — the injection demonstrably changes the artefact before the ceiling is tested |
| **Bite** (`--budget 25`, same host) | returned in **25.0s**, `checked 0 of 6 · TRUNCATED`, all 6 named `unchecked` |
| **Bite, exit limb** (`--require-complete`) | **exit 2** |
| **Control** (healthy host, ceiling 25s) | `checked 6 of 6 in 0.0s · complete`, **exit 0** — a non-binding ceiling changes nothing |
| **Control, mixed** (3 healthy + 3 hanging) | the 3 that answered reported as answered; only the 3 unreached marked `unchecked` |
| **Control, no `--budget`** | byte-identical behaviour to before; the ceiling is opt-in |
| **The real population** | **59 of 59 held URLs in 153.2s under a 300s ceiling, complete, exit 0** |

## The half that generalises beyond timeouts

**Truncation must be louder than failure**, because a truncated sweep's silence is
indistinguishable from a clean one *in the direction that hurts*: it reports a held source as
fine when it was **never opened**. So unreached URLs get their own `unchecked` bucket, are
named individually, and carry a note that says in words: *this is a finding about this run,
not about the source; nothing is known either way.* And `--require-complete` gives the flip a
**different exit code** for *"everything answered"* versus *"we ran out of clock"* — two facts
that must never share one.

> **General form:** *a bound is only a bound at the layer that owns the clock.* A per-item
> limit, a per-retry limit and a per-connection limit all leave the aggregate free. **And
> whenever a run can stop early, the output must distinguish *checked and clean* from *never
> checked* — otherwise the ceiling converts a slow honest check into a fast dishonest one.**

This is the 08-16 silent-pass trap with a clock attached, and the sixth time the enumeration
family has been restated: **a green check is scoped to what it enumerates** — and a truncated
sweep silently *shrinks its own enumeration at runtime*, which no previous member covers.

## Binding

1. **Any check that touches a network or an unbounded population takes a total wall-clock
   ceiling**, enforced where the clock is owned, not between units.
2. **A ceiling defaults to off.** Existing invocations must not change behaviour on the day
   the ceiling lands.
3. **A truncated run names every unit it did not reach** and never summarises them beside the
   units that answered.
4. **"Complete" and "incomplete" get different exit codes** wherever a gate consumes the
   result — `--require-complete` at the flip.
5. **The scheduled figure is measured, not estimated:** the full held sweep is **~154s**; the
   flip step is specified at a **300s** ceiling with `--require-complete`, roughly 2× headroom.

*Five counts moved in this commit per the four-count rule and its conditional fifth (RUNBOOK,
2026-10-04): §3's range, §3's heading, §1's count line, `CLAUDE.md`'s non-negotiable range, and
the assertion-discipline family's own running member count — TWENTY-FIVE → TWENTY-SIX.
Reconciled by counting rows, never against yesterday's number (#57).*
