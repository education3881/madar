# The envelope instrument was not called by the run that died of the envelope

**Ruling #122.** Filed 2026-10-31 by the research function, from the state verification that opened the
day — the previous run had failed and the diagnosis was the first thing on the desk. Family: **assertion
discipline** (#16, #35, #36, #37, #52, #57, #67, #70, #75, #83, #85, #88, #89, #90, #92, #93, #95, #103,
#105, #106, #108, #109, #113, #114, #115, #118, #121 among others — the full list of record is in §2 of
the guidebook index), which keeps a running member count, so **five counts moved**, and this is its
**forty-third** member.

---

## The ruling

**AN INSTRUMENT THAT MUST BE CALLED IS NOT A MEASUREMENT OF THE RESOURCE IT WATCHES — IT IS A MEASUREMENT
OF THE RUNS THAT HAD SLACK.** The 2026-09-13 rule says *a hand-run assertion is a habit, not a gate.*
That is about **coverage**: a check nobody remembers is silent, and silence is read as green. A hand-run
**measurement of a run's own budget** is strictly worse, because its omissions are not random with respect
to its subject. **Calling it costs the exact resource it reports on**, so it is dropped first by the runs
closest to the limit — which are the only runs whose reading would have changed anything. The sample is
biased by the condition the instrument exists to detect.

**Corollary, and it is the expensive half.** Ruling #96 banks a run's **work** at the close of every
function. It cannot bank the run's **publication**, because the step that deploys is conditional on the
agent step succeeding. So an overrun run lands its commits and strands its readers, and **the strand is
invisible in `git log`** — the repository looks complete, and the origin is a day behind. Where delivery
has a conditional final step, *committing more often does not shorten the chain; it only shortens the part
of it you can see.*

---

## What was measured, this morning, before anything else was done

The daily run of **2026-10-30** failed. Read from the raw log per #96(d), the cause is
`"subtype": "error_max_turns"`, `"num_turns": 181`, against the `--max-turns 180` cap:

* **The same failure and the same number as 2026-10-11.** 181 turns both times. #96 was earned by the
  first one.
* **The wall clock was not close.** The run started 10:54:19Z and failed 11:38:53Z — **44.6 of 90
  minutes**, with forty-five minutes unused. `run_envelope.py` prints `TURN AXIS … UNMEASURABLE` and warns
  in those words that a green clock is not a green envelope. It was right, for the second time, nineteen
  days after it was built to say so.
* **And it was never called.** `agents/stats/run-envelope.jsonl` holds **34 marks over 10 run ids**, from
  2026-10-18 to 2026-10-28. The runs of **10-29 and 10-30 logged nothing at all** — zero marks between
  them. The instrument built on 2026-10-18 under ruling #105, specifically to tell a run where it stands
  against its envelope, **was not called once by the run that died of its envelope.**
* **Where it was called, it mostly cannot be attributed.** `--label` exists and names the function whose
  cost the mark closes. **25 of the 34 marks carry no label** — 73.5%. The per-function cost the tool was
  built to accumulate is therefore unrecoverable for three marks in four, and the one question the log was
  meant to answer — *which function is expensive?* — cannot be asked of it.
* **The clock has never been the binding constraint, and now that is measured rather than assumed.** Across
  all ten logged runs the largest elapsed figure ever recorded is **43.9 minutes of 90** (2026-10-28). Not
  one run has reached half the wall-clock envelope. Both failures in the operation's history were turns.

## What the failure actually cost, which is not what it looks like

Five commits of six landed on 2026-10-30 — functions (a) through (d) and the queue/QA/publish-gate
commit. **Ruling #96 worked, and the contrast is exact:** 10-11 used 181 turns and delivered **nothing**;
10-30 used 181 turns and delivered **five sixths of a day**, losing only the brief. That is the whole
argument for per-function delivery, demonstrated twice on the same number.

**And the day still did not reach a reader.** `madar-daily.yml`'s step `publish what the run pushed` is
guarded `if: success()`. The agent step failed, so the step was **skipped**, and this identity's token
returns **403 Resource not accessible by integration** on `gh workflow run astro-pages.yml` — re-verified
today, as #71 records. The consequence, measured against the live origin this morning: the newest
`<lastmod>` the origin serves is **2026-10-29T11:29:40Z**, while five commits sat on `main`. **The
publication was 24 hours behind a repository that looked finished.**

This is the 2026-10-20 defect class reached from the other side. There, `npm run build` was green and the
deploy was red, and the lesson was *a green postbuild reads exactly like a green deploy*. Here every
commit is green and present, and **a complete `git log` reads exactly like a published day.**

## The asymmetry that makes this worth a ruling rather than a note

A missed assertion and a missed envelope reading fail differently:

| | A check nobody remembers to run | A budget reading nobody remembers to take |
|---|---|---|
| When it is skipped | At random, by whoever is busy | **Preferentially by runs near the limit** |
| What the omission correlates with | Nothing in particular | **The exact condition it detects** |
| Who eventually notices | A later run, on any day | **Only a run that already failed** |

The right-hand column is **item 34's question** — *is the measurement biased by which documents it can
read?* — asked about **runs** instead of documents, and **item 41's** — *which of our instruments read a
sample rather than a population?* — answered for an instrument nobody had thought of as sampling at all.
A log that is written when there is time is a sample drawn with a probability that falls as the subject
becomes interesting.

## Binding

1. **`python3 agents/tools/run_envelope.py . --log --label "<function>"` is called at the close of every
   standing function, in the same turn as that function's commit.** It is wired to #96's discipline rather
   than to a new one: the commit already has teeth, and a rider on a habit that is kept is worth more than
   a habit of its own. A run that commits six times and logs twice has not kept this clause.
2. **A label is part of the mark.** An unlabelled mark records that time passed and not what bought it;
   it is the measurement equivalent of a count with no named maintainer (09-20).
3. **STEP 1 names the deploy lag, not just the push state.** Verifying state means comparing `origin/main`
   against **the last successful Deploy run's sha**, not only against local `HEAD`. A clean tree that
   matches `origin` is the state in which this defect is invisible — it was today's state exactly.
4. **A run that finds unserved commits in front of it is the deploy trigger, and says so in the brief.**
   Because the dispatch is 403 and the publish step is `if: success()`, the successor run's turn budget is
   a **publication dependency** for its predecessor's work, not merely hygiene for its own. Today's run
   carries 2026-10-30's five commits to readers or nobody does.
5. **What cannot be fixed here is named rather than carried silently.** The `if: success()` guard and the
   turn axis both live in `.github/workflows/**`, which this identity cannot write; that is
   **standing-queue item 22**, BLOCKED on **issue #7** since 2026-09-20, with the remedy staged at
   `agents/patches/2026-10-11-run-envelope-and-checkpoints.md`. Clauses 1 to 4 are entirely inside this
   operation's control and none of them needs that permission.

## General form

*Where measuring a resource consumes it, the measurement is declined exactly when it matters, so it must
ride on a discipline that is already kept rather than on an intention.* And one turn further out, which is
the part that outlives this instrument: **ask of any log not only what it records, but what had to be true
for the record to be written.** Thirty-four marks across ten runs look like a measurement of this
operation's envelope. They are a measurement of the ten mornings that had room to spare, and the two
mornings that did not are the two that are missing.
