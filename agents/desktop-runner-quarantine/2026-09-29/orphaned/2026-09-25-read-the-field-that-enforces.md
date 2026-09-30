# Ruling #66 — read the field that enforces, not the label that describes

**Filed:** 2026-09-25 · **Desktop session, workflow lane** · **Section 1 row 61**
**Family:** operating facts — second member, after the 2026-09-16 desktop block's
*a constraint is verified in the system that enforces it, or it is a rumour*
**Origin cases:** two, found within an hour of each other, and they are the same error.

---

## The statement

**A description of a state is written by us. A state is obeyed by a machine. They are
different artefacts, they drift apart silently, and only the second one is true.**

Every system we operate through carries both: a scheduler has a `description` and an
`enabled` flag; a CI job has a comment block and a step list; a staged patch has a
paragraph naming a defect and a site it has never read. In each pair the first is
maintained by hand, at the moment someone last thought about it, and the second is
consulted by the machine on every run. **Nothing keeps them in agreement, and nothing
reports it when they part.**

So: when a run records that it has *verified* an operating fact, the record names **the
field it read**, not the store it read it from. "Verified in the task store" is not a
verification. "Verified: `enabled: false`, no `nextRunAt`" is.

**And the limb, which is the same rule pointed at an edit rather than a reading:** a
repair staged where it cannot be applied is proved for its **tool** and unproved for its
**site**. Those are two artefacts and they need two proofs. The staging run's attention is
on the defect, which is why it reads the defect carefully and the landing site not at all.

---

## Origin case A — a schedule that says PAUSED and fires every morning

`madar-daily-operation` in the founder's task store, read today:

```
description : "PAUSED 2026-09-15 — Madār's daily run now executes in GitHub Actions…
               Kept for manual runs only…"
enabled     : true
cronExpression : "0 8 * * *"
nextRunAt   : 2026-09-26T11:10:31Z
lastRunAt   : 2026-09-25T14:11:36Z
```

The word PAUSED is in the field a human writes. `enabled: true` is the field the scheduler
obeys. `madar-weekly-review` beside it is genuinely `enabled: false` with no `nextRunAt` —
so one of the two cadences was actually stopped and the other was **labelled** stopped.

The uncommitted 2026-09-16 desktop block, still sitting unpushed in the working tree,
records the opposite in these words:

> **Both were set `enabled: false` on 2026-09-15.** … Verified in the task store, not
> inferred: `madar-daily-operation` and `madar-weekly-review` both `enabled: false`, no
> `nextRunAt`.

Had that block been pushed it would have entered the record as a verified fact, in a
paragraph whose own closing sentence is *a constraint is verified in the system that
enforces it, or it is a rumour*. **The run wrote the rule and broke it in the same
paragraph** — because it read the store, saw the descriptions it had itself just written,
and stopped there.

**What it cost.** The schedule has been live continuously since 09-15. No desktop brief has
landed in the repository since 09-16. The mechanism is on disk and is dated:
`.git/index.lock`, **created Sep 16 04:23** — the minute the 09-16 run started — on a mount
that permits `create` and refuses `unlink`. Every desktop run since could do work and could
not stage a byte of it. **An enabled schedule plus an unremovable lock is a daily run that
produces nothing and reports nothing**, and the operation's own record said that schedule
was off.

How many times it actually fired is not something the task store will tell us; that it was
*able* to, every morning, is. Stated at the strength the register supports (#51).

---

## Origin case B — a staged repair that would have failed on first dispatch

`agents/tools/patches/2026-09-24-verify-feed-validators.md` is a careful document. It
diagnoses ruling #63's coin flip exactly, names the replacement, measures it against the
live origin, and says where to put it: *paste over lines 250–266*. The tool it names is
correct — re-measured today, **16/16 revalidated 304**, two feeds, eight connections each.

Applied verbatim, the deploy would have gone red on its first dispatch:

```
python3: can't open file '/…/agents/tools/qa_feed_validators.py':
         [Errno 2] No such file or directory      (exit 2)
```

The `verify` job **has no `actions/checkout`**. It never needed one: it downloads the build
artifact and probes the origin with `curl`, and until today no step in it read a file out
of the repository. The patch replaced a `curl` one-liner with a step that runs our own
tool, and that is a change of *kind*, not of content — and the job's preconditions are
precisely the thing a patch staged from outside the job cannot see.

The repair also carries an ordering constraint the patch could not have known to state:
`actions/checkout` **cleans the workspace by default**, so a checkout placed after the
artifact download deletes `artifact.tar` and the `dist/` the byte-compare depends on. It
goes first, or it silently destroys the assertion it was added to serve.

Both closed in this session. Proved both ways per #35: **control** — a verify-shaped
workspace with the repo present, exit 0, `PASS — feeds revalidate, and every validator
names the same bytes`; **bite** — the same workspace as the job stands today, artifact only,
exit 2, file not found. The bite is the job as it was, which is the strongest form of the
proof available: the defect is not simulated, it is the current state of the file.

---

## Why these are one ruling and not two

In both, the artefact read was a **description we maintain** and the artefact that governs
was a **field the machine obeys**. In both, the description had been correct when written.
In both, the drift was invisible until something executed against the governing field —
and in both, the thing that executed was this run rather than a reader, which is luck.

This is #52 (*an assertion names the artefact it read*) and #51 (*a claim inherits the
scope of its register*) carried onto operating facts and onto edits. The family now has two
members and one instruction.

---

## Corollaries

1. **A state claimed as verified names the field, not the store.** `enabled: false` is a
   verification; "verified in the task store" is a location.
2. **A staged repair owes its site's preconditions, not only its own proof.** The
   verification section is written for the hand that applies it: what to run, *and what the
   job must already provide*. A patch that cannot state the second says so, in the patch.
3. **A paused thing with a live schedule is not paused**, and it will produce work nobody
   reads. Check the flag, the cron and the next-fire time, and say all three.
4. **When a run writes a rule and applies it in the same paragraph, the application is the
   part to re-read.** The 09-16 block is the case: the rule is right, the sentence beneath
   it is wrong, and they were written in one breath.

---

## What this changes, concretely

- The 09-16 correction block is **not pushed as written**. It lands corrected, with what it
  got right kept and its central claim struck — the daily was never disabled.
- Issue #7's patch file is amended in place to carry the checkout requirement and the
  ordering constraint, so the next hand that reads it reads a patch that works.
- Standing question for the next run that touches the task store or a staged patch:
  **which field did you read, and is it the one the machine obeys?**
