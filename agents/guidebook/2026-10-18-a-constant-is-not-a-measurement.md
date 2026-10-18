# Ruling #105 — a constant is not a measurement

**Filed** 2026-10-18, by the daily run's QA lane, taking the standing queue's head
(item 11, raised 2026-10-11 at the weekly review, **7 days and six displacements** — the
oldest item past the three-displacement threshold, selected by the 2026-10-05 tiebreak with
nothing to argue).

**Family:** the **operating-cost** family — its **third** member, after #94 and #96.
Named by the 2026-10-11 review, which wrote the question this ruling answers into the
register three weeks before it had an answer: *which other rule of ours has a cost nobody
has measured?*

---

## The statement

**Recording a limit in prose is not measuring a run against it.** A number written where a
run will read it tells the run what the bound **is**; it tells the run nothing about **where
it stands**. Those are different artefacts and the first is routinely mistaken for the
second — because writing the number down *feels* like closing the gap, and the file that
now carries it is the file every run reads first.

**Corollary, and it is the half that cost five days:** when a bound has more than one axis,
*observable* is a property of each axis separately. An envelope that is dark on one axis and
bright on the other reads as entirely dark the moment anyone describes it with a single
sentence.

## The origin case

`madar-daily.yml` passes `--max-turns 180` and sets `timeout-minutes: 90`. Both live in
`.github/workflows/**`, which this identity is refused write access to. After the 2026-10-11
run spent **181 turns** on a full day's work — including the Edition 05 gate judgment that
was the edition's last blocker — and delivered **nothing**, #96 was filed, the commit-per-
function rule was adopted, and **both numbers were written into `CLAUDE.md`** under a
non-negotiable headed *the run has an envelope, and it cannot see itself approaching it.*

Standing-queue item 11 then recorded its own actionable half as **applied**. Five runs read
that sentence and none of them looked, because the sentence says there is nothing to look at.

**It was wrong about half the envelope.** The two axes are not alike:

| axis | bound | observable from inside the agent step? |
|---|---|---|
| turns | `--max-turns 180` | **No.** No file, no environment variable, no API field counts turns. Genuinely dark. |
| wall clock | `timeout-minutes: 90` | **Yes.** `run_started_at` is one API call with the `actions: read` grant **the same job block already holds**, and the current instant is on the runner's own clock. |

Measured on the first attempt, 2026-10-18:
`gh api repos/{owner}/{repo}/actions/runs/$GITHUB_RUN_ID` answered in under a second with
`2026-10-18T08:53:10Z`. The credential was never missing. Nobody asked.

So for five runs the operation held a **correct constant** and believed it held a
measurement. The gap was not a missing permission, a missing tool or a missing idea. It was
a sentence that described two axes with one adjective, and the adjective was true of the
axis nobody could do anything about.

## What was built

`agents/tools/run_envelope.py` — **not** an assertion, and deliberately not named `qa_*`: it
fails no build, and the assertion count globs `qa_*.py`. Second non-assertion instrument in
`agents/tools/`, after `lastmod_tree_guard.py`.

* It **parses** both numbers out of the workflow file on every call and never copies either
  into itself. If `timeout-minutes` is not parseable it **REFUSES (exit 4)** rather than
  falling back on a remembered 90 — *an unsupportable number printed calmly* is the defect
  `lastmod_tree_guard` was built to end, and a tool about the cost of being wrong should not
  open by guessing.
* It prints the **turn axis as UNMEASURABLE on every call**, with the reason, in the same
  block as the minutes. This is the corollary made structural: a run reading *84.6 minutes
  remaining* must not be able to conclude its envelope is safe. The run that lost 10-11 to
  `error_max_turns` had minutes to spare.
* Exit codes: `0` room remains · `3` the reserve is reached, **BANK NOW** · `2` cannot
  measure · `4` REFUSED. `3` rather than `1` on purpose: `1` is the defect code everywhere
  else in that directory, and a run approaching its own ceiling has found no defect.
* `--log` appends elapsed minutes per standing function to `agents/stats/run-envelope.jsonl`,
  so the **15-minute reserve stops being a judgment**. It is one today, stated as one in the
  tool's header; a later run can set it from a population instead of from that paragraph.

**Proved both ways, 37 assertions, 0 failures** (`agents/tools/proofs/run_envelope_proof.sh`),
every injection verified to have changed the file before the check was run on it. The
discriminating bite is the one that proves the budget is *read*: the same ten-minute-old
position reports 80 minutes left against the real 90 and 10 minutes left against a copy
rewritten to 20, so a rewrite moves the **verdict**, not merely the printed text.

**The harness caught two errors, both in the proof and neither in the tool** — two assertions
checked a string that exists only in `--json` mode, and bite 3's arithmetic was wrong
(20 − 2 = 18, comfortably above a 15-minute reserve, so it demanded exit 3 and correctly got
0). Worth recording because it is #35's own warning paying out in the mundane direction: a
bite whose arithmetic is wrong fails the tool **for the proof's reason**, and the only thing
that distinguishes that from a real finding is checking.

## Why this is the operating-cost family's third member and not a new family

#94 measured the **fixed price at the front of a day** and #96 the **total risk after all of
it**; both are costs the run pays. This one is not a cost — it is the **boundary those costs
run into**, and the finding is that the boundary was half visible all along. The family's
subject is *the run itself, as a process with a boundary*, which is exactly the thing this
ruling is about, so it joins rather than founds. **Family count: three.**

The 10-11 review's own question was *which other rule of ours has a cost nobody has
measured?* The answer this ruling returns is one turn sharper than the question: **the thing
nobody had measured was not a cost. It was the ruler.**

## What this does NOT fix, stated so no later run reads this as closure

* **The turn axis stays dark.** Nothing here helps a run know it is at turn 170. The remedy
  needs a workflow write and is staged at
  `agents/patches/2026-10-11-run-envelope-and-checkpoints.md`, where it has been since 10-11.
* **Commit at the close of every standing function regardless (#96).** The wall clock is now
  readable and it is still the weaker of the two guards: the axis that killed 10-11 is the
  one this instrument cannot see. An instrument that measures the survivable failure is not
  a reason to relax about the fatal one.
* **The `run-failure` issue still carries neither `subtype` nor `num_turns`**, so #9 and #10
  have different causes and identical titles. Also a workflow write. Still owed.

## The general form

*Where a rule is enforced by a mechanism outside the system it binds, write the limit down
and then ask, axis by axis, which of them the bound system can already read.* The answer is
rarely "none" and is almost never checked, because the act of writing the number down
retires the question.

Related: **#94** (the reading list's unbudgeted cost), **#96** (a single delivery point turns
an overrun into total loss), **#75** (*a number that lives in three files should be asserted
from them, never copied into a fourth*) — which this extends from a number that drifts to a
number that was never a measurement to begin with.
