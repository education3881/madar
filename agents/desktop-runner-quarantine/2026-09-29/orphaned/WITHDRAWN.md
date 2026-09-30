# Withdrawn and applied patches — the ledger the queue needs to read true

The README says an applied patch is **deleted in the same push**, because a patch that
landed and stayed here reads exactly like one that has not. Deleting it also destroys the
only record that it existed. This file is that record: one line per patch that has left
the queue, and why. It is append-only.

---

## 2026-09-28 — APPLIED: `2026-09-20-issue-6-default-c-gate-register-comment.patch`

Issue #6 stated default C: the gate register has two homes and the workflow now says so.
Regenerated with refreshed counts at the 09-27 weekly, `git apply --check` verified there
and again here before applying. Landed together with the patch below, and its ratio line
was moved 22 -> 23 in the same edit, because the other patch is what moves it.

## 2026-09-28 — APPLIED: `2026-09-24-verify-feed-validators.md` (issue #7, ruling #63)

The `verify` job's feed-cache step was a coin flip; replaced with
`qa_feed_validators.py --attempts 6`. Re-proved on the live origin before landing:
16/16 revalidated 304.

**Two corrections the patch itself needed, found only by applying it:**

1. **Its counts were stale.** It said applying it "returns the ratio to 22 of 24" and that
   until then it is "21 of 24". True state on the day it was applied: **25 assertions, 22
   gating, going to 23**. The 09-27 weekly wrote the standing rule that every open patch is
   re-read against current state, and re-read the *other* patch in this directory — this one
   was **moved** into this directory by that same review and never re-read at its new
   address. A move is not a read.

2. **It was incomplete.** It gave the replacement step and nothing else. The step runs a
   tool out of the repository and the `verify` job **has never had a checkout** — it
   downloaded the artifact and probed the origin with curl, and needed no repository file
   to do either. Applied as written, it would have failed on its first dispatch with
   "no such file". `git apply --check` passed it, and could not have caught this: **a patch
   is a claim about a file; a repair is a claim about a system.** The checkout was added in
   the same edit and ordered FIRST, because `actions/checkout` cleans the workspace and
   would otherwise delete the artifact the byte-compare depends on.

## 2026-09-28 — WITHDRAWN: `2026-09-20-verify-feed-cache-retry.patch`

**Superseded by ruling #63, and it collided with the patch above.** Written on 09-20 to give
the feed-cache step the retry every other origin check in that job already had. On 09-24
ruling #63 found the actual cause — two permanent validators per URL across replicas, not a
transient — so a retry does not fix it: every attempt still lands on an independently chosen
edge. The patch above **deletes the seventeen lines this one rewrites.**

Both were open on 2026-09-28. Both passed `git apply --check` individually. **They cannot
both land**, and a hand applying them in filename order would have written 45 lines and
deleted them in the same push, or hit a conflict and stopped with issue #7 still open.

The 09-27 weekly reconciled this queue **item by item, for staleness** — is each patch's
prose still true? — and that check cannot see a contradiction that lives *between* two
items. **Reconciling a list member by member does not reconcile the list.** From today the
weekly also reads every open patch against every other open patch, and the check is
mechanical: any two patches touching the same file are read together or one is withdrawn.

## 2026-09-28 — WITHDRAWN: `agents/tools/patches/2026-09-25-desktop-tracked-files.patch`

A whole-tree patch of the 09-25 desktop working tree, generated against a clone that was
then 9 days behind `origin/main` and is now 12. It carried the stale version of the
feed-validator edit — including its "22 of 24" and a cross-reference to
`agents/tools/patches/`, the directory retired on 09-27. Applying it would have written
stale counts into the one file the cloud identity cannot correct, which is the exact failure
mode the README names as the worst available. Withdrawn rather than refreshed: the work it
carried has been redone here against current state.
