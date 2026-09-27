# Ruling #71 — a run cannot observe what happens after it ends, and must not narrate it

**Filed:** 2026-09-27 · daily run, state-verification lane
**Family:** which register speaks for the owner — and the first member of it whose subject is **us**
**Extends:** #69 (the cause of an absence is a claim), #70 (a 200 is not a connection a reader can make), #41 (fetched-on-date)
**Cost:** six daily briefs told the founder the opposite of what was happening, in the one document he opens.

---

## The ruling

**An autonomous run's last act is not the system's last act.** A run observes what is true while it is
running and nothing after; if the pipeline does anything once the agent step exits, that part of the
world is structurally invisible to the agent, and **an invisible part of the world is not an empty one.**

So: a run reports **an observation with a timestamp**, never a state of affairs. *"At 10:02Z no deploy
had started for today's push"* is true, checkable, and useful. *"The work sits on main until a human
clicks Run workflow"* is a forecast about a period the run cannot reach, and it is the kind of sentence
that gets copied forward for six days because it reads like a finding.

**And where the claim is about our own automation, the automation is read.** Not the symptom.

## The origin

Since 2026-09-21 every daily brief and every addendum commit has carried some form of:

> *"the push that started no deploy and the 403 that refused one… Nth consecutive day the work sits on
> `main` until a human clicks Run workflow."*

Checked today against the Actions API rather than against yesterday's brief:

| Deploy run | Event | Fired | Final commit of that run | Gap | Result |
|---|---|---|---|---|---|
| `36234253156` | **workflow_dispatch** | 09-26 09:56:01Z | 09-26 09:55:34Z | **27s** | success |
| `36121527064` | **workflow_dispatch** | 09-25 09:59:48Z | 09-25 09:59:23Z | **25s** | success |
| `35982998240` | **workflow_dispatch** | 09-24 09:43:46Z | 09-24 09:43:24Z | **22s** | success |
| `35712971901` | **workflow_dispatch** | 09-22 09:53:53Z | 09-22 09:53:07Z | **46s** | success |

**Twenty-two to forty-six seconds. That is not a human clicking Run workflow.**

The mechanism is in our own repository, in the same file the claim is about. `madar-daily.yml` grants
the job `actions: write` — *"read the last deploy's result, AND dispatch the next one (issue #6,
2026-09-14)"* — and carries a step named **`publish what the run pushed`**, at line 187, after the agent
step at line 89, which compares the origin before and after and runs `gh workflow run astro-pages.yml`
when it moved. Its comment block explains precisely why it exists and why it lives in the workflow
rather than in the run's instructions: *"a step that must happen every single time should not depend on
an agent remembering to do it."*

**Issue #6 was closed by that step on 2026-09-14, and it has worked every day since.** The 403 that six
briefs reported is real and its cause was correctly diagnosed on 09-20 — the **agent step** runs as a
different identity from the **job**. That is a fact about one token. It was generalised into a fact
about the publication.

**Verified today, so that this ruling is not one more inherited narrative:** the 09-26 deploy is green
on `e531d38`, which is `HEAD` and `origin/main`; and `qa_live_drift` reports **CLEAN — origin matches
dist: 120 URLs, 0 lastmod drift, 4 sampled heads identical.** The publication is current and served,
and has been throughout.

## Why it survived six days — and this is the part worth keeping

The 09-26 brief contains **both** of these:

- *"the 09-25 deploy green and its bytes served (`36121527064`)"* — a verified observation, correct,
  with the run ID attached.
- *"the work sits on `main` until a human clicks Run workflow"* — an inherited narrative, false.

They contradict each other and they sat two paragraphs apart for six days. **The narrative won because
it was the prose and the observation was a parenthesis.** Every run did check the previous deploy, as
the state-verification rule requires; every run recorded that it was green; and not one asked what had
made it green, because the answer was already "known".

> **An inherited narrative outranks a fresh observation unless something forces them into the same
> sentence.** The state-verification rule says *check the last deploy*, and six runs did. It does not
> say *reconcile what you checked against what you are about to write*, and so six runs did not.

## The corollaries

- **A refusal to one of our identities is not a refusal to the operation.** #70 said this of the
  reader's client and ours; this says it of two tokens inside one workflow file. Name the identity in
  the record: *"the agent step's token is refused"* — not *"we cannot dispatch a deploy."*
- **Where a run reports on machinery it is part of, it reads the machinery.** The mechanism here was a
  commented step in a file every run is told to read the QA consequences of, added by the run that
  diagnosed the problem, and no later run opened it.
- **A per-run claim that recurs verbatim has stopped being an observation.** The sixth identical
  sentence is not six confirmations; it is one claim copied five times. When a line in the brief has a
  day counter attached to it, the counter is the signal to re-derive it, not to increment it.
- **The addendum commit pattern is the artefact of the error.** Six runs pushed a second commit whose
  sole purpose was to explain an unserved state that was served twenty-seven seconds later. The
  addenda were locally honest — at the moment of writing, no deploy *had* started — and globally
  wrong, because the run necessarily ends before the step that deploys it.
- **State verification has a second half.** The rule reads *never plan a day off a brief — verify state
  from git and the live site.* It now also reads: **verify the claims you are about to repeat, not only
  the state you are about to plan from.** A brief is yesterday's artefact in its assertions as much as
  in its facts.

## What changed on disk

- `CLAUDE.md`, `agents/RUNBOOK.md` — the 09-14 rule's clause *"work committed by an autonomous run sits
  on `main`, unserved, until a human pushes anything or clicks Run workflow"* is **superseded**, dated,
  and replaced with what the pipeline does.
- The brief's standing "unserved state" line is replaced by a **verified** deploy line: the previous
  run's deploy ID, its conclusion, and a `qa_live_drift` result.
- Nothing about the *editorial* consequence changes: the wave gate, announcements and anything binding
  an external system to a URL still schedule onto **origin-confirmed** state (08-30, restated 09-14).
  That rule was right for a reason that survives this correction — it just is not waiting on a human.

Related: [[2026-09-26-the-cause-of-an-absence-is-a-claim]] · [[2026-09-27-a-200-is-not-a-connection-a-reader-can-make]]
