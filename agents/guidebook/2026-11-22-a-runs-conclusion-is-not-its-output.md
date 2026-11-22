# Ruling #154 — a run's conclusion is not its output, and both of our run-level reports read the conclusion

**Filed 2026-11-22 by the daily run's research function, out of the state verification that opened the day.**
**Family: operating cost (the register's ninth), member SEVEN.**
**Amends nothing and completes #96 by one hop.**

---

## The rule, in one line

**A RUN'S CONCLUSION IS A TWO-STATE FLAG AND NEITHER STATE DESCRIBES A RUN THAT BANKED EVERYTHING AND
THEN DIED — so a report wired to that flag is wrong about such a run in whichever direction its own
polarity points, and ours are wired to it twice, in opposite directions.**

## What happened

On 2026-11-21 the daily run did a full day's work. It shipped
`2026-11-12-england-ofsted-exempt-cohort` — the first single ever shipped against the standing ledger,
nine days in the gate, eight cells, both editions, every quoted span byte-compared against its register an
hour before the flip — closed standing-queue item 47 at 25 days, repaired the citation graph on 714 nodes,
filed ruling #153, and wrote brief 137. **All five function commits reached `origin`**, exactly as #96
requires. Then it hit the turn cap: **`error_max_turns`, num_turns 181, 43 of its 90 minutes used, 47
unspent.**

**Nobody could read any of it for twenty-four hours.** Both editions of the new piece returned **404** on
the live origin this morning; `ofsted-exempt` appeared **zero** times in the served sitemap; the origin was
still serving the 11-20 build. Observed rather than assumed, by `qa_prior_publication --observe`:
**strand 5**.

The cause is one word. `madar-daily.yml`'s last step:

```yaml
- name: publish what the run pushed
  if: success()
```

and the step before the `if:` was ever written, in the same file, as its own justification:

> *"a step that must happen every single time should not depend on an agent remembering to do it.
> Deterministic, or it is not a gate."*

**The comment states the requirement and the condition contradicts it.** `if: success()` does not make the
step deterministic; it makes it depend on the agent *succeeding*, which is strictly weaker than depending
on the agent remembering. That sentence and that condition have sat four lines apart since 2026-09-14.

## The three limbs, and the third is the one worth carrying

**(1) The predicate has two homes and the wrong copy is the untestable one.** The step's own body already
decides whether to publish: it records `ORIGIN_BEFORE` before the agent step, compares it with
`origin/main` afterwards, and dispatches **only if the origin moved**. That is the correct question — *was
anything pushed* — and it is asked in shell, where any run can read it. The `if:` asks a different
question — *did the run finish* — in YAML, where it is evaluated **only on the runs nobody reads**, because
a passing run never exercises the false branch and a failing run is the one whose log gets skimmed for the
cause of death. **A predicate with two homes is #57's count with two homes**, and the copy that goes wrong
is the one no ordinary day can falsify.

**(2) The same flag is read with the opposite polarity by the failure report, and it is wrong there too.**
`report a failed run` carries `if: failure()` and opened issue **#17**, which says:

> *"This is a dark day unless the next run picks it up."*

2026-11-21 was not a dark day. It was one of the most productive days this operation has had. **So the
founder's two automated records of that day were wrong in opposite directions**: the issue told him nothing
happened, and brief 137 — written by the run, committed and pushed — told him *THE PIECE SHIPS*. Neither
was true. **Everything happened and nothing was served**, and no artefact he could open said so. One bit
was asked to carry two quantities it cannot represent: **what the run produced**, and **whether what it
produced may be published.**

**(3) #96's staging stopped one hop short of the reader.** #96 (2026-10-11) ruled that *delivery is staged,
not saved up*, because a single delivery point converts a cost overrun into total loss. It worked: five
commits, all banked, none lost. **And `origin` is not the reader.** The last hop — origin to published
bytes — remained a *single* delivery point, and it was conditioned on precisely the flag a cap death flips.
So #96 converted total loss of **work** into total loss of **publication for that day**, which is strictly
better and is not finished. *A staged delivery is only staged as far as its last unconditional hop.*

## Measured, three instances, read from the Actions API rather than remembered

| Date | Turns | Commits banked and stranded | What it cost |
|---|---|---|---|
| 2026-10-30 | 181 | 5 | published the next morning |
| 2026-11-03 | 181 | 4 | the origin served the 11-02 build for **two days** |
| 2026-11-21 | 181 | 5 | **a published piece, 404 for a day, while the brief said it had shipped** |

**Fourteen commits and one publication.** And the self-healing is accidental, not designed: the strand
clears when a later run *happens* to succeed and *happens* to push, it is unbounded if two runs fail
consecutively, and it is **invisible in `git log` by construction** — which is why the number had to be
built (#128) before any of this could be counted.

## Why the repair is not ours, and what was done instead

The one-word patch (`if: always()`) is staged at
`agents/patches/2026-11-04-publish-step-must-not-depend-on-the-run.md` with its three proof cases and needs
the `workflows` permission of issue **#7**. **Re-measured this morning rather than inherited:**
`gh workflow run astro-pages.yml --ref main` from inside the agent step returns **403 Resource not
accessible by integration**, so this identity can neither write the file nor substitute for it.

So the run did the three things it can do. **Standing-queue item 77 was re-bucketed from OPEN to BLOCKED**
— its closure needs a credential nobody here holds, which is #116's test, and leaving it OPEN meant it
would eventually take a head no run could close. **Issue #7 carries the measured cost**, with no new
default and no new date, because *a default the operation cannot execute is not a default* (issue #8's
rule). And **the ledger and `CLAUDE.md` now distinguish shipped from served** on the piece itself.

## The family placement, and why it is the operating-cost family rather than assertion discipline

Nothing here is a check. The subject is **the run as a process with a boundary** — the ninth family's own
definition — and this is its third member about the back edge of a run, after #96 (the cliff at the back)
and #136 (the axis you cannot see while standing on it). #94 measured the fixed price at the front, #96 the
total risk after all the work, #105 and #136 the rulers, #107 the position in time, #116 a rule's
throughput. **#154 is the first member whose subject is the hop AFTER the run's own boundary** — what
becomes of finished work once the process that made it has ended.

## And the shape it shares with this week's other two findings, which is the general form

**#152, filed two days ago: *a two-state flag cannot name the state the work is in.*** `approved: true` /
`approved: false` has two values and the gate has eight cells, so a piece six cells in is **absent** rather
than held, and `qa_held_assets` printed CLEAN over an orphan share card in its own `dist`. **This is that
ruling at the run level, forty-eight hours later**: `success` / `failure` has two values and a run has at
least three states — finished, died with nothing banked, and **died with everything banked** — and the
third is the one both of our reports describe wrongly.

**#144, filed seven days ago**, found a derivation that stopped one step short of the number a human
actually reads: the cron band was derived and the Dubai clock column beside it was recomputed by hand.
**This is that, with a publication in place of a number.** The banking is complete and automatic as far as
`origin`; the hop a reader actually experiences was left to a flag.

*General form, and it is the part that outlives this workflow file: **a process's exit status describes the
process, never its output** — so any report, gate or hand-off keyed to that status is making a claim about
the wrong subject, and the direction of its error is set by its own polarity rather than by the facts. Ask
instead what the work itself can be read off: the commits that landed, the bytes that are served, the
origin that moved. Each of those is observable by somebody who was not there.*

---

**Proved by:** the Actions API for three runs' conclusions, turn counts and step outcomes; the live origin
for two 404s and a sitemap absence; `qa_prior_publication --observe` for strand 5; and a fresh 403 from the
dispatch this ruling says is impossible, run this morning rather than quoted from 2026-09-20.

**Queue:** item 77 (BLOCKED, issue #7). **Issue:** #7, third comment. **Kin:** #96, #136, #152, #144, #128, #57, #71.
