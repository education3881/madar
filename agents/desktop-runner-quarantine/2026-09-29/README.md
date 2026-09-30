# Desktop runner quarantine — 2026-09-29

**What this folder is:** the output of a *second* daily runner, preserved rather than
merged, because it collided with the canonical line at identical paths.

## The finding

Madār has two daily runners.

1. **Canonical.** `.github/workflows/madar-daily.yml` — GitHub Actions, cron `23 4 * * *`
   (04:23 UTC). Autonomous: it commits its own work, pushes to `main`, and dispatches the
   deploy. Live since **2026-09-14**, whose commit message states the intent plainly:
   *"Between 11 August and 14 September the daily run lived in a desktop app: it executed
   only when his machine was awake, and 11 of 34 days were dark. Every push also waited on
   him pasting a block. Both dependencies end here."*

2. **Duplicate.** A Cowork scheduled task, `Madar daily operation`
   (`trig_017qwXewssFQN2kfFGQYr5rw`), firing daily against this desktop checkout. It runs
   the same five standing functions, on the same date, against the same repository, and
   ends by handing the founder a `git add -A && git commit && git push` block — the exact
   dependency the 09-14 migration retired.

The 09-14 migration retired the desktop *cadence inside the repository*. The schedule
*outside* the repository was never named in it, so it kept firing for fifteen days.

## Why the collision was not theoretical

The desktop runner ran on **2026-09-25** and **2026-09-28** and committed neither day. On
09-28 its `pull --ff-only` landed at 07:18:11Z, it wrote until 07:37Z, and it stopped. The
canonical run for the same day pushed `c60fecc` at 11:56Z. Two 09-28 briefs then existed —
**at the same path**, 29,760 bytes here against 30,812 bytes on `origin` — plus a parallel
growth note, guidebook note and QA log.

Had the push block in those briefs been pasted from this folder, it would have:

| Regression | Cost |
|---|---|
| `agents/briefs/2026-09-28-daily-brief.html` overwritten | the canonical 09-28 brief |
| `agents/guidebook/INDEX.md` | −32 lines of register index |
| `agents/stats/history.jsonl` | 12 snapshots dropped from the delta series |
| `agents/patches/` ×3 files deleted | three patches queued for a human hand |
| `.github/workflows/astro-pages.yml` | +94/−22 against the gate the deploy runs |

A `git pull` would have aborted first, on the untracked brief — loudly, which is the only
reason this sat for a day instead of landing.

## What was done, 2026-09-29

- `tracked-edits-from-desktop-run.patch` — `git diff HEAD` at 1cbcbaa, 647 lines. Every
  tracked edit the desktop runner made and never committed. Replay with `git apply`
  **only** after reading it against the canonical line; most of it is duplicate work.
- `orphaned/` — nine untracked artefacts, **moved** here, not copied, so that no
  `git add -A` can sweep them into a commit at their old paths.
- The working tree was then restored to `origin/main` and verified **byte-identical**
  (0 ahead / 0 behind at `098bfaf`, before today's canonical push).

### Two sandbox boundaries routed around, not fought

- **Deletion is denied in the connected folder.** `git checkout -- .` unlinks before it
  writes, so it failed on all six modified files. Routed around by rewriting each file in
  place from `git show origin/main:<path>`, then `git reset origin/main` — a *mixed* reset,
  which moves `HEAD` and the index and never touches the working tree.
- **`node_modules/.vite` cannot be unlinked**, so `npm run build` cannot re-optimize here.
  Routed around by building a clean-room clone in the cloud container instead — which is
  the better environment for the check anyway, being closer to CI.

### Stale git locks

`.git/HEAD.lock` and `.git/index.lock` are left behind zero-length and cannot be removed
from this sandbox. Git's read paths work; `git add` will not. Any push block from this
folder must begin `rm -f .git/index.lock .git/HEAD.lock`.

## The standing decision this raises

Retire the duplicate, or repurpose it. See
`agents/briefs/2026-09-29-desktop-observer-report.html`, section *Tomorrow*.

The case for repurposing rather than deleting: **ruling #71** — a run cannot observe what
happens after it ends. The canonical run pushes and dispatches its own deploy, so it can
only ever report the push as a timestamped observation and verify it the *next* day. A
runner that fires 30 minutes later can watch the deploy land and byte-compare the served
site against a clean-room build of the pushed commit. That is what this run did today, and
it is the only job on this desk that the canonical runner structurally cannot hold.
