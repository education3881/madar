# `agents/patches/` — changes the autonomous run wrote and is not permitted to push

The cloud identity that runs `madar-daily.yml` authenticates with the Actions token. That
token **may not create or update anything under `.github/workflows/`** — GitHub refuses the
push outright:

```
! [remote rejected] HEAD -> main (refusing to allow a GitHub App to create or update
  workflow `.github/workflows/astro-pages.yml` without `workflows` permission)
```

This is a correct design and not a misconfiguration (ruling of 2026-09-14, clause 4). It is
also not a `permissions:` block away: `workflows` is not among the keys a workflow can grant
itself.

So a workflow change the run needs is written here as a patch instead of being abandoned,
and named in that day's brief. **A patch in this directory is unapplied work**, not history.

## Applying one

From a checkout whose credentials carry the `workflow` scope (the founder's terminal, or a
run using a PAT):

```bash
git am agents/patches/<file>.patch     # keeps the original message and authorship
git push
```

Then delete the patch file in the same push — a patch that has landed and stayed here reads
exactly like one that has not, which is the failure mode this directory would otherwise
create for itself.

## The queue is reconciled at every weekly review, and here is why that is not tidiness

**Found 2026-09-27:** the `2026-09-20-issue-6-default-c…` patch below had been sitting here
for seven days asserting, into the one file every run is told to read first, that the
operation owns **21 standing assertions of which 19 gate the deploy, seven of them from
`postbuild`**. Four assertions landed while it sat unapplied. Had the founder applied it on
any day after 09-22, it would have written **stale counts into `astro-pages.yml`** — which
is precisely the drift the 2026-09-20 review spent its budget repairing in `CLAUDE.md`.

**A staged patch is frozen prose about a moving count.** Every other artefact here that
carries a number is now reconciled weekly; a patch was reconciled by nobody, ages silently,
and its failure mode is the worst available — it injects stale state *at the moment of
application*, by a hand that trusts it, in a file the autonomous run cannot then correct.
Both entries below were re-read and the counts refreshed on 2026-09-27; the patch was
regenerated from a real diff and re-verified with `git apply --check`.

**Standing rule from today: the weekly review re-reads every open patch in this directory
against current state, and refreshes or withdraws it.** A patch that cannot be re-verified
is withdrawn rather than left to rot — an unapplied patch is unapplied work, but a *wrong*
unapplied patch is a trap.

## Open

| Patch | What it does | Why it matters |
|---|---|---|
| `2026-09-20-verify-feed-cache-retry.patch` | Gives the `verify` job's feed-cache step the retry every other origin check in that job already has, and makes it record `x-cache` / `x-served-by` on a miss | **That step has failed the deploy twice in nineteen days** (2026-09-09 and 2026-09-19), both times on a conditional GET issued ~12s after publish, both times while the site itself was serving correctly. Until this lands, the deploy stays liable to a red run that means nothing about the publication — and the third occurrence will be as undiagnosable as the first two, because the current step records nothing about which edge node answered. The shell is proved both ways against the live origin; see `agents/logs/qa-2026-09-20.md` §1. |
| `2026-09-24-verify-feed-validators.md` | Returns `qa_feed_validators` (standing assertion 24) to the `verify` job, where its reason belongs. **Moved here from `agents/tools/patches/` on 2026-09-27**, when the review found the queue had two homes and no count. | Assertion 24 is one of the three that do not gate the deploy, and the only one whose *reason for being ungated* cannot be written where the other two are — it belongs to the `verify` job, which this identity cannot write. Applying it makes the ratio **23 of 25**. Counts re-verified 2026-09-27. |
| `2026-09-20-issue-6-default-c-gate-register-comment.patch` | Adds the comment block that makes issue #6's option C honest: `astro-pages.yml` names all **ten** `postbuild` gates in `web/package.json`, prints the total (**25**) and the ratio (**22 gating**), names the three that do not gate and why, and says why the register is split in two. **Counts refreshed 2026-09-27 — see the section above; as staged on 09-20 it read seven / 21 / 19 and would have written all three wrong.** | **Issue #6 carried a stated default dated 2026-09-20 — apply C — and the date passed unanswered, so C applies.** The circularity the issue itself warned about then bit: applying C means editing the one file this identity may not write, and the push was refused on exactly the error quoted at the top of this README. Comment-only; changes no step and no gate. Until it lands, a reader of the workflow gets *twelve* as the answer to "what gates the deploy?", which is an incomplete answer — the honest total lives in `CLAUDE.md` and in each weekly review's printed ratio. |

## A note on the second entry, because the shape is worth keeping

The 2026-09-20 weekly review attempted this push knowing it would probably fail, and staged
it as a **separate final commit** so the refusal cost that commit and nothing else. It was
refused, the commit was dropped, the rest of the block landed, and the work is here. That is
now the standing shape for any workflow change: *write it, stage it last, attempt it, and
preserve it with its reason rather than abandoning it or not trying.* An attempt that is
cheap and recorded is better than a prediction — the 09-14 ruling said this would be refused,
and it is worth re-proving on a different day rather than assuming a constraint has held.
