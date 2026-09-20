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

## Open

| Patch | What it does | Why it matters |
|---|---|---|
| `2026-09-20-verify-feed-cache-retry.patch` | Gives the `verify` job's feed-cache step the retry every other origin check in that job already has, and makes it record `x-cache` / `x-served-by` on a miss | **That step has failed the deploy twice in nineteen days** (2026-09-09 and 2026-09-19), both times on a conditional GET issued ~12s after publish, both times while the site itself was serving correctly. Until this lands, the deploy stays liable to a red run that means nothing about the publication — and the third occurrence will be as undiagnosable as the first two, because the current step records nothing about which edge node answered. The shell is proved both ways against the live origin; see `agents/logs/qa-2026-09-20.md` §1. |
| `2026-09-20-issue-6-default-c-gate-register-comment.patch` | Adds the comment block that makes issue #6's option C honest: `astro-pages.yml` names all seven `postbuild` gates in `web/package.json`, prints the total (21) and the ratio (19 gating), and says why the register is split in two | **Issue #6 carried a stated default dated 2026-09-20 — apply C — and the date passed unanswered, so C applies.** The circularity the issue itself warned about then bit: applying C means editing the one file this identity may not write, and the push was refused on exactly the error quoted at the top of this README. Comment-only; changes no step and no gate. Until it lands, a reader of the workflow gets *twelve* as the answer to "what gates the deploy?", which is an incomplete answer — the honest total lives in `CLAUDE.md` and in each weekly review's printed ratio. |

## A note on the second entry, because the shape is worth keeping

The 2026-09-20 weekly review attempted this push knowing it would probably fail, and staged
it as a **separate final commit** so the refusal cost that commit and nothing else. It was
refused, the commit was dropped, the rest of the block landed, and the work is here. That is
now the standing shape for any workflow change: *write it, stage it last, attempt it, and
preserve it with its reason rather than abandoning it or not trying.* An attempt that is
cheap and recorded is better than a prediction — the 09-14 ruling said this would be refused,
and it is worth re-proving on a different day rather than assuming a constraint has held.
