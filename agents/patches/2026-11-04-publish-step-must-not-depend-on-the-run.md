# Staged patch — the publish step must not be conditional on the run's own conclusion

**Raised 2026-11-04 (standing-queue item 77). Owner: whoever holds write access to
`.github/workflows/**`, which this identity does not — founder issue #7 / standing-queue item 22.**
**This patch carries NO COUNT of any kind**, deliberately, per the 2026-09-27 rule: a staged patch is
frozen prose about a moving tree, and the issue-#6 patch sat for seven days asserting numbers that had
moved. There is nothing here to go stale. *(And that sentence was false twice before it was true. The draft quoted a hard-coded count of `astro-pages.yml`'s build-job assertions; `qa_patch_queue` refused the commit; the count was replaced by a pointer at the derivation — **and the note recording that refusal quoted the refused figure back, so the gate refused the note too.** A record of a rejected number is a second copy of it. The gate caught this patch twice, in the exact shape the patch's own first paragraph is about.)*

## The defect, measured twice

`madar-daily.yml`'s last step is `publish what the run pushed`, and it reads:

```yaml
      - name: publish what the run pushed
        if: success()
```

Ruling **#96** moved this operation to per-function commits so that an overrun run banks its work
instead of losing it. It does that. **It cannot bank the publication**, because the step that dispatches
the deploy is gated on the agent step having succeeded. Ruling **#122** wrote the corollary down on
2026-10-31 in these words: *a per-function commit discipline proves the work survived and says nothing
about whether anybody can read it.*

Observed twice since:

* **2026-10-30** — `error_max_turns` at 181 turns, five of six commits landed, no deploy dispatched.
  The strand closed the next morning when the 10-31 run succeeded and dispatched a deploy carrying both
  days.
* **2026-11-03** — `error_max_turns` at 181 turns, four of five commits landed and pushed, no deploy
  dispatched. **The origin served the 2026-11-02 build until 2026-11-04**, with four commits on `main`
  the whole time.

**The self-healing is accidental.** Nothing dispatches the deploy except a *successful* run, so the
strand lasts until the next run happens to finish — one day in the 10-30 case, two in the 11-03 case,
and unbounded if a run fails repeatedly. **And the strand is invisible in `git log`**: the repository
looks complete, every commit is pushed, and only the origin disagrees.

## The change

```diff
       - name: publish what the run pushed
-        if: success()
+        if: always()
```

## Why `always()` is right and not merely convenient

The step is **already idempotent and already conditional on the thing that matters.** Its own body
compares `origin/main` before and after the run and dispatches **only if the origin moved**:

```bash
if [ "$ORIGIN_AFTER" = "$ORIGIN_BEFORE" ]; then
  echo "Origin unchanged … there is nothing to publish."
else
  gh workflow run astro-pages.yml --ref main
fi
```

So the guard that stops a held day spending a deploy is in the script, not in the `if:`. The `if:`
adds exactly one behaviour: **work that was pushed is not published when the run that pushed it
overran.** That is not a safety property. A bad commit cannot reach a reader through this path either
way — `astro-pages.yml` runs its own build-job assertions (the register is derived by
`qa_patch_queue`, and is deliberately not quoted here) and a `verify` job that
byte-compares the published artifact against the origin, and a red build deploys nothing. **The
deploy's safety is the deploy's gates, not the agent step's exit code.**

The one argument for the current form is that a failed run might have left a half-finished editorial
state on `main`. Three things answer it: a flag change is committed in the turn it is finished (#96b),
an article's assets ship in the same commit as its text (2026-06-14), and the held-leak assertions fail
the build on a partially-shipped piece. A half-finished state does not reach a reader; it fails a gate.

## How to prove it

* **Control:** a successful run that pushed — the deploy must still be dispatched exactly once.
* **Control:** a run that pushed nothing — the step must still print *origin unchanged* and dispatch
  nothing, whatever the run's conclusion.
* **Bite:** a run that pushes and then fails — the deploy must be dispatched. Reproduce by failing the
  agent step deliberately after a commit, or by reading the 2026-11-03 run, where `ORIGIN_BEFORE` and
  the four pushed commits are both on file.

## Until it lands

The next successful run carries every strand ahead of it, because the step's own origin comparison
spans whatever accumulated. That is what happened on 2026-10-31 and again on 2026-11-04. **It is a
recovery, not a design**, and it is written here so no run has to rediscover it from a stale origin.
