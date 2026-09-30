# Ruling #72 — a patch is a claim about a file; a repair is a claim about a system

**Filed:** 2026-09-28 · desktop session, workflow-write lane
**Family:** the register that enforces — and the first member whose subject is our own queue
**Extends:** #67 (a rule that names a check and produces no file has produced nothing), #71 (a run cannot observe what happens after it ends), #63 (a validator is not the content), #50 (a correction has a blast radius)
**Cost:** two workflow repairs sat open for eight and four days; both passed every check we own; neither could have landed as written. One of them had already been applied wrongly, in a working tree, three days earlier, and reported in the past tense.

---

## The ruling

`git apply --check` answers one question: *does this diff still fit the file it was cut against?*
That is the whole of its competence. It says nothing about whether the patched step can run,
whether a second open patch contradicts the first, or whether the numbers the patch writes are
still true on the day a hand applies it.

**So a staged repair is verified against three things, and the file is the least of them:**

1. **The file** — `git apply --check`. Necessary, and the only one we were doing.
2. **The job** — does the step still work where it lands? A step that runs a tool out of the
   repository needs the repository. A check that reads the origin needs to run after the origin
   moved. A patch names its own diff; it does not name the preconditions its diff creates.
3. **The queue** — read against **every other open patch**, not only against current state.
   A contradiction between two patches lives in neither patch, so no per-item read can see it.

**And the corollary that makes all three enforceable: a repair is not applied until it is pushed.**
An edit in a working tree has changed nothing about the world. No instrument in this operation
can tell an applied repair from an unpushed one, which is exactly how one got reported as done.

## The origin — three findings, one shape

### 1. Two open patches, mutually exclusive, both green

`agents/patches/` held two workflow repairs this morning. Both applied clean on their own:

| Patch | Filed | What it does to the `verify` feed step |
|---|---|---|
| `2026-09-20-verify-feed-cache-retry.patch` | 09-20 | **rewrites** its seventeen lines, adding a retry |
| `2026-09-24-verify-feed-validators.md` | 09-24 | **deletes** those same seventeen lines |

The second supersedes the first: on 09-24 ruling #63 found the cause was two permanent validators
across replicas, not a transient, so a retry cannot fix it — every attempt still lands on an
independently chosen edge. **They cannot both land.** A hand applying them in filename order would
have written forty-five lines and deleted them in the same push, or hit a conflict and stopped with
issue #7 still open.

The 2026-09-27 review had reconciled this queue the day before, **item by item, for staleness** —
is each patch's prose still true? It refreshed one and did not notice the other contradicted it.
**Reconciling a list member by member does not reconcile the list.**

### 2. The surviving patch was incomplete, and only applying it could show that

The 09-24 patch gave a replacement step and nothing else: *paste over lines 250–266.* The step it
inserts runs `python3 agents/tools/qa_feed_validators.py`. **The `verify` job has never had a
checkout** — it downloaded the artifact and probed the origin with `curl`, and needed no repository
file to do either. Applied exactly as written, it fails on first dispatch with *no such file*.

`git apply --check` passes it. Every assertion we own passes it. Nothing we had could see it,
because all of it reads the file and none of it reads the job.

The checkout also cannot go anywhere: `actions/checkout` cleans the workspace by default, so placed
after the download it deletes `artifact.tar` and the `dist/` the byte-compare depends on. **It goes
first, and that ordering is itself a precondition the patch never mentioned.**

### 3. A move is not a read

That same 09-27 review **moved** this patch from `agents/tools/patches/` to `agents/patches/`,
consolidating a queue that had two homes and no count, and declared the queue reconciled. The file
it moved still said, on the morning it was applied:

> *"the ratio returns to **22 of 24**… Until then it is **21 of 24**"*

True state that morning: **25 assertions, 22 gating, going to 23.** Four assertions had landed since
the patch was written. The review's own standing rule — *every open patch is re-read against current
state* — was written in the same commit that moved this file, and was not applied to it.

**Consolidating a list records that a member arrived at the new address. It does not record that
anyone opened it.** The move is the thing most likely to be mistaken for the read, because it touches
every member and produces a diff.

### 4. The one that hurts — a repair reported before it existed

The 2026-09-25 desktop session applied the feed-validator edit to `astro-pages.yml` and wrote a
growth note, in the past tense:

> *"It was applied in this session. From the next dispatch, **a regression in the reader's poll path
> fails the deploy** instead of failing quietly at the reader."*

It was applied **to a working tree**, on a clone nine days behind `origin/main`, and never committed.
For the three days that followed, the gate was not gating, the sentence read exactly like a finding,
and **no check in this operation is capable of noticing the difference.** It is #71's failure with the
tense reversed: #71 narrated a future it could not observe; this narrated a past that had not happened.

## What changed today

- Both patches left the queue: one applied, one withdrawn with its reason. **The queue is empty for
  the first time**, and the ledger is `agents/patches/WITHDRAWN.md` — a patch is deleted on
  application, so without a ledger the only record it existed is destroyed by the act of using it.
- The `verify` job has a checkout, ordered first, with the ordering's reason in the file.
- `qa_feed_validators` gates from `verify`. **22 → 23 of 25.**
- `CLAUDE.md` reconciled by counting both files, not by remembering: thirteen tool invocations in the
  workflow (twelve build steps plus the new one in `verify`), ten in `postbuild`, two non-gating.

## Standing consequences

1. **The weekly re-reads every open patch against every other open patch**, not only against current
   state. The check is mechanical: any two patches touching the same file are read together, or one is
   withdrawn. Two patches to one file is a finding by default.
2. **A patch states its preconditions**, not only its diff — what the patched step needs from the job
   it runs in, and where in the job it must sit.
3. **A patch carries no counts it does not have to.** Prose about a moving number is the one thing a
   frozen file cannot keep true (#the 09-27 rule); where a count is unavoidable, it is re-derived at
   application and the patch says so.
4. **An applied patch is deleted and ledgered in the same push.**
5. **Nothing is reported in the past tense until it is pushed.** A working-tree edit is described as
   staged, never as applied — and a lane that cannot push says so in the sentence that claims the fix.

## The generalisation

Every one of today's four findings is the same error at a different scale: **a check that reads the
artefact and calls that reading the system.** `git apply --check` reads a file and is taken for a
verdict on a pipeline. A directory listing reads filenames and is taken for a reconciled queue. A
working tree reads as a repository. In each case the narrow instrument was working perfectly and the
claim built on it was one level too wide — which is **#51, a claim inherits the scope of its register**,
arriving for the fourth time and the first time pointed at our own tooling rather than at prose.
