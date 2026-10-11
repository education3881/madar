# A run with one delivery point stakes the whole day on reaching the end of it

**Ruling #96.** Filed 2026-10-11 at the weekly review. **Family: the operating-cost family —
named today, second member** (first member **#94**, whose placement was owed to this review).
Earned by the 2026-10-11 daily run, which did a full day's work and delivered none of it.

---

## The claim

**Where a run is bounded by an envelope it cannot observe, and commits once at the end, the
envelope deletes the entire run rather than its tail.** The loss is not proportional to the
overrun. A run cut off one turn short of its commit delivers exactly as much as a run that never
started — and it costs the same as one that finished.

**The corollary is the operating rule:** *commit when a unit of work is done, never when the day
is done.* A run that commits after each standing function and then dies has delivered four
fifths of a day. A run that commits once has delivered a day or nothing, decided by something it
cannot see.

## What happened

The 2026-10-11 daily run started 10:51:53Z and failed at 11:42:24Z:

```
"is_error": true, "num_turns": 181, "subtype": "error_max_turns",
"errors": ["Reached maximum number of turns (180)"]
```

`.github/workflows/madar-daily.yml` passes `--max-turns 180`. The run used **181 turns, 314
assistant messages and roughly 190 tool calls over 50 minutes**, and it was not a run that
wandered. Read from its own log (run `38133474743`, which is the only place any of this now
exists), it had:

- taken **the Edition 05 gate judgment** — the packet captions' Arabic gate, the edition's last
  remaining blocker, 9 days old and named in the 10-10 ledger as *"an Arabic Editor judgment,
  which this run deliberately did not take"* — and written the verdict file;
- filed **three guidebook rulings**, including one on caption vocabulary that the gate earned;
- built **a new standing assertion** (`qa_stats_history.py`), with a proof harness and its
  `postbuild` wiring — which would have been the operation's thirty-third, and which closes
  standing-queue item 6, the board's oldest;
- repaired **both editions** of the Africa ruler pair;
- added the **Edition 05 registry row and cover asset**, and found a defect doing it — a growth
  note titled *the front door did not know*;
- written the publish gate, the QA log and the brief, **and rendered the brief to PNG and looked
  at it**, per the 2026-08-23 rule.

`ORIGIN_BEFORE` and `origin/main` both read `d837e21` when the job exited. **Nothing was
committed. The runner's workspace was discarded.** Zero of it reached disk, and the edition did
not flip on its own gate date.

## Why the 10-10 remedy did not prevent it

Yesterday's **#94** diagnosed the 2026-10-09 failure — *a mandated reading list every run must
append to is an unbudgeted operating cost* — and acted: `CLAUDE.md` 22,559 → 16,140 → 17,835
bytes, net −21%. The diagnosis was right about 10-09 and **too narrow by one step.**

The two failures are not the same failure:

| | 2026-10-09 | 2026-10-11 |
|---|---|---|
| Cause | `usage_limit_reached`, HTTP 429 | `error_max_turns`, cap 180 |
| Turns | 31 | **181** |
| Duration | 7m 15s | **50m** |
| Where it died | inside **step one**, on `RUNBOOK.md` | at the **end**, after the whole day's work |
| Work existing at death | none | **a full day, including the edition's last blocker** |
| Delivered | nothing | **nothing** |

**#94's remedy addresses the first column only.** Shrinking what a run must read buys turns at
the front of the day; it cannot help a run that read everything successfully and then spent 175
turns doing excellent work with no way to bank any of it. *The reading list was the cost. The
delivery point is the risk, and they are different defects with one indistinguishable symptom:
a red run and an unchanged origin.*

Which is why both days read as "the same dark day" from the outside, and why 10-10 — reading
only the conclusion, not the log — generalised from one. **Two failures with one symptom will be
diagnosed as one failure by any run that does not open the evidence.** The first thing this
review did was download both runs' raw logs; `gh run view --log` truncated today's 4.1 MB log to
1,637 lines, which made it look exactly like 10-09's — six tool calls and death on `RUNBOOK.md`.
*The truncation preserved the beginning, which is where the previous diagnosis already was.*

## What this generalises

This is the shape the operation already knows twice, with a human in the slot:

- **2026-08-16** — *a push gap escalates; it does not simply roll forward.* "The founder's
  proof-of-work contract is delivered by the push, not by the file on disk — an unpushed brief
  is an *undelivered* brief."
- **2026-08-30** — *founder-push availability is a capacity constraint, not a compliance
  failure.* Every escalation the rule prescribed targeted the operation, and the operation was
  never the constraint.

Both rules treat a *staged* block as the safe state and the push as the risk. **That premise is
now wrong.** In the cloud cadence the staged block is not safe: there is no disk that survives
the run. The 08-16 rule's own sentence — *the risk is not loss, it is contamination* — inverts.
**The risk is loss, and it is total.**

## Binding

1. **Commit at the close of every standing function**, not once at the end of the run. Five
   functions, up to five commits, each one a line of its own. A run's work is not *done* when it
   is written; it is done when it is on `origin`.
2. **Any judgment that closes a blocker, any ruling, any new assertion, and any content flag
   change is committed in the turn it is finished** — these are the artefacts whose loss cannot
   be re-derived by a later run from the repository, because the repository is where they were
   going.
3. **A run never plans a push for its own last turn.** The brief and the log are written against
   work already landed, and a final commit carries only them.
4. **The envelope is stated where the run can read it.** `--max-turns 180` and
   `timeout-minutes: 90` live in `.github/workflows/*.yml`, which this identity is refused write
   access to; they are therefore recorded in `CLAUDE.md` and the remedy is staged at
   `agents/patches/2026-10-11-run-envelope-and-checkpoints.md`.
5. **A failed run is read from its raw log, never from its conclusion** — and never from
   `gh run view --log`, which truncates silently. `gh api .../logs` and unzip.

## The family this opens

**The operating-cost family — what executing our own discipline costs, and what happens when the
cost exceeds the envelope.** Ninth family in the register, and the first whose subject is neither
the publication nor an instrument but **the run itself as a bounded process.**

- **#94** (2026-10-10) — the mandated reading has no budget; its cost is paid before any work.
- **#96** (2026-10-11) — the delivery has one point; its risk is paid after all the work.

Together they bracket a run: a fixed price at the front and a cliff at the back, with the day's
actual work in between. **Kin, deliberately not reassigned:** **#88** (*a per-unit bound is not a
total bound*) is the same question asked of a check's duration rather than a run's, and stays in
assertion discipline where it was filed.

**Count line: TWO members, #94 and #96, reconciled against its own membership at the moment of
naming, 2026-10-11.** It applies from today; there is no backward window, because the family is
two days old and both members are in it. *(Limb 1 of the 10-04 second amendment: a rule that puts
a count onto the faster clock states the date from which it applies and whether it was reconciled
at that date. Both stated.)*

---

*Kin: #89 (an invariant needs one place that holds both its sides — "a run cannot observe its own
past"; this is a run unable to observe its own **future**) · #94 · the 08-16 and 08-30 push-gap
rules, whose premise this inverts · [[delivery-is-not-authorship]].*
