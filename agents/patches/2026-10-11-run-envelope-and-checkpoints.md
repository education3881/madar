# Staged patch — the run envelope, and a checkpoint the operation cannot add itself

**Raised 2026-10-11, weekly review. Ruling #96. Carries NO numeric claim about the gate register**
(the #75 rule: a number that lives in three files is asserted from them, never copied into a fourth).

**Why it is staged rather than applied:** every line below edits `.github/workflows/**`, and the
autonomous identity that runs this operation is refused write access to that path. The same refusal
that put seventeen assertions into `web/package.json`'s `postbuild` applies here, and unlike those
there is no second home: a turn cap is an argument to the action, not a step in a build.

---

## What happened

The 2026-10-11 daily run failed with:

```
"is_error": true, "num_turns": 181, "subtype": "error_max_turns",
"errors": ["Reached maximum number of turns (180)"]
```

It had done a full day's work first — the Edition 05 gate judgment that was the edition's last open
blocker, three rulings, a new standing assertion with its proof harness, both editions of a pair
repaired, the edition registry row and cover, and its own brief rendered and inspected. **It committed
nothing.** `ORIGIN_BEFORE` and `origin/main` both read `d837e21` when the job exited, and the workspace
was discarded. The edition did not flip on its own gate date.

## The patch

### 1 — Raise the daily cap, and only the daily

`.github/workflows/madar-daily.yml`, the `claude_args` line:

```diff
-          claude_args: '--model claude-opus-5 --max-turns 180 --allowedTools "Bash,Read,Write,Edit,Glob,Grep,WebFetch,WebSearch"'
+          claude_args: '--model claude-opus-5 --max-turns 260 --allowedTools "Bash,Read,Write,Edit,Glob,Grep,WebFetch,WebSearch"'
```

**260 and not "more":** 181 is the only observation of a run that completed its work and was cut off,
so the honest figure is *the one that bound, plus the margin a day of this shape needs.* The five
standing functions cost ~190 tool calls on 10-11 with the day's work including a gate judgment and a new
assertion; 260 is that plus roughly a third. **Raising it to a number nobody measured would be the same
defect in the other direction** — an envelope chosen by feel is what produced the 180.

`timeout-minutes: 90` is **not** changed. The 10-11 run finished its work in 50 minutes; wall clock was
never the binding constraint, and widening a bound that did not bind buys nothing and hides the next
failure.

### 2 — Record the envelope where the run reads it

Already applied, in the half this identity owns: `CLAUDE.md` now carries both numbers in the
non-negotiables, because **a run cannot pace itself against a limit it has never been told.**

### 3 — What is deliberately NOT in this patch

**A mid-run checkpoint step.** The obvious shape — a workflow step that commits whatever is on disk if
the agent step fails — is wrong, and the reason is this operation's own publish gate. A failed run's
tree is unverified by construction: it may hold a half-composed Arabic twin, a flag flipped for a
rehearsal and not reverted (the 10-10 run had exactly that in its working tree for part of the day), or
an article without its hero still, which is the 2026-06-14 invariant. **A step that commits an
unverified tree would convert a lost day into a published defect**, and the 08-09 flag-sweep rule says
why: an artefact's assertions are scoped to a corpus state, and a dead run leaves the corpus in no
stated state at all.

The fix for that half is therefore a **rule and not a step**, and it is applied, not staged: the RUNBOOK
now requires a commit at the close of every standing function, so what lands has passed a gate at the
moment it landed. **This review ran that way and committed in four stages.**

## Verification owed when this is applied

1. One daily run completes with `num_turns` printed in the QA log, so the operation finally has a
   distribution rather than a single bound. *This costs nothing and was never collected.*
2. The failure issue the workflow files (`run-failure`, seen on #9 and #10) carries `subtype` and
   `num_turns` in its body — on 2026-10-09 and 2026-10-11 it carried neither, and the two failures have
   **different causes with one symptom**, which is precisely what a titled-by-date issue cannot
   distinguish. The 10-10 run read the conclusion and generalised from the wrong column.

## Status

**OPEN.** Blocked on a credential no identity in this operation holds — the same blocker as
`2026-09-24-verify-feed-validators.md`, `2026-09-29-issue-6-default-c-gate-register-comment.patch`,
`2026-10-06-build-served-manifest-check.md` and `2026-10-10-verify-bridge-via-served-manifest.md`.
Re-read against current state at each weekly review per the 2026-09-27 rule. **Raised as GitHub issue
for the founder alongside issue #7**, which has carried the same class of request since 2026-09-20.
