# Moving the operation to the cloud — cutover plan

**Filed:** 2026-09-14 · **Manager → Founder** · triggered by the founder's instruction
*"how can I move this project to the cloud? I feel we are missing a lot because of not
running it every day."*

---

## The problem, measured

Since the Africa frame was set on 2026-08-11:

| | |
|---|---|
| Elapsed days | 34 |
| Run days | 24 |
| **Dark days** | **11** |
| Pushes landed | 14, across 13 days |
| Pieces live from the edition | **0** |

Eleven dark days in thirty-four is not a discipline failure. It is where the operation
was running. Two dependencies on one laptop:

1. **The schedule lived in a desktop app.** It fired only when the machine was awake
   and the app was open. No machine, no run, no brief, and no record that a day was
   missed until the next run noticed.
2. **Every push waited on a human paste.** The sandbox cannot reach the founder's
   terminal, so each day ended with a copy-paste block. Blocks went unrun on 08-31,
   09-03, 09-10 and 09-13 — four of them in three weeks, each stranding a full day's
   work on a disk nobody else can see.

Both end here.

## The architecture

| Piece | File | When |
|---|---|---|
| Daily run | `.github/workflows/madar-daily.yml` | 04:00 UTC daily = **08:00 Asia/Dubai** |
| Weekly review | `.github/workflows/madar-weekly.yml` | Sundays 05:00 UTC = **09:00 Asia/Dubai** |
| Founder channel | `.github/workflows/claude.yml` | whenever you write `@claude` on an issue or PR |
| Operating instructions | `.claude/skills/madar-daily/SKILL.md`, `madar-weekly/SKILL.md` | read by the runs |
| Repository standards | `CLAUDE.md` | read on every run |

The migration is cheap for one reason: **this repository already is the operation.**
The charter, the runbook, forty-nine rulings, every QA tool, both content collections
and every brief are already committed. The only thing living outside was the
scheduled-task instruction file, and that is now `.claude/skills/madar-daily/SKILL.md`.

### What changes about how the run behaves

- **It commits and pushes itself.** No push block. No `workflow`-scope PAT — the Claude
  GitHub App carries Workflows: write, which removes the friction that has interrupted
  five of the last eight pushes.
- **The brief goes to the run summary** as well as into the repository, so the day is
  readable from a GitHub notification without opening anything.
- **A failed run opens an issue** labelled `run-failure`. A dark day becomes an event
  with a timestamp instead of a silence.
- **Founder decisions get a real channel.** The run opens an issue labelled
  `founder-decision` with options, consequences, a recommendation, a stated default and
  a stated date. You reply from your phone. `@claude` on the issue reaches the
  operation without a session.

### What does not change

The guard rails are not in these workflows. They are in `astro-pages.yml`, which every
push triggers: twelve standing assertions as build steps, then a `verify` job that
byte-compares the published artifact against the live origin. **An autonomous run that
breaks something fails the deploy and never reaches a reader.** The publish gate still
runs in writing. The Editor is still the filter. Quality over slot still outranks the
calendar.

---

## Your three steps

Everything above is committed and inert until these are done. I cannot do any of them —
credentials are yours by design, and I should never see or handle the token.

### 1. Install the Claude GitHub App

Go to **https://github.com/apps/claude** and install it on `education3881/madar`.

It needs Contents, Issues and Pull requests at read/write; the app asks for its full
permission set and GitHub does not allow accepting a subset.

### 2. Create the token and add it as a repository secret

On your Mac, in a terminal:

```bash
claude setup-token
```

Copy the token it prints. Then in GitHub:

**Settings → Secrets and variables → Actions → New repository secret**

- Name: `CLAUDE_CODE_OAUTH_TOKEN`
- Value: the token

This authenticates against your existing Claude subscription rather than metered API
credit. Do not paste the token into a chat, a file, or a commit — the workflows
reference it only by name.

### 3. Trigger one manual run before trusting the schedule

**Actions → Madār — daily run → Run workflow.**

Leave the optional note blank, or write something like *"cutover smoke test — verify
state, run QA, write a short brief, do not draft"* if you want a cheap first run.

Watch it. The first scheduled run is not the place to discover a permissions problem.

---

## What to check on that first run

| Check | Where | What good looks like |
|---|---|---|
| The run starts at all | Actions tab | No auth error in the first minute |
| Full history is present | run log, checkout step | Not a shallow clone; `lastmod` needs git dates |
| `npm ci` succeeds | install step | Clean, no lockfile complaint |
| The agent can read the repo | run log | It names the current HEAD and the last brief |
| **The push lands** | commit history | A commit authored by the app, not by you |
| **CI fires on that push** | Actions tab | `astro-pages.yml` runs — this is the one to watch |
| The deploy verifies | `verify` job | Byte-compare against the origin passes |
| The brief is readable | run summary | Headline and dek, plus a link to the file |

### The known rough edge

There is an [open issue](https://github.com/anthropics/claude-code-action/issues/814)
where **scheduled** runs can fail authentication in cases where a manually dispatched
run of the same workflow succeeds — the OIDC exchange reports the triggering user as
lacking write access. Scheduled events are attributed to whoever last edited the cron
line, and the action also rejects bot actors to stop trigger loops.

If the 04:00 run fails while your manual run passed, that is this, not a mistake in
these files. Expect to spend one run on it. Mitigations, in order of preference:
re-save the workflow from your own account so the schedule is attributed to you; then
`allowed_bots`; then passing an explicit `github_token` — but note that a run
authenticating with the default `GITHUB_TOKEN` **will not trigger `astro-pages.yml`**,
which would silently stop deploys, so that one is a last resort and needs the deploy
re-checked immediately.

Two smaller things worth knowing: GitHub's cron is best-effort and can drift 10–20
minutes or occasionally skip; and if `main` has branch protection, the app needs to be
allowed to push to it.

---

## Cutover log

### Attempt 1 — 2026-09-14, run `34815261498`: FAILED in 88 milliseconds

**Everything except the prompt worked.** The log is worth keeping because of how
much it proves: the OIDC exchange succeeded, the app token was obtained, git auth was
configured as `claude[bot]`, the actor check passed (*"Verified human actor:
education3881"*), and Claude Code v2.1.270 installed cleanly. Infrastructure: green.

Then:

```json
{ "type": "result", "subtype": "success", "is_error": true,
  "duration_ms": 88, "num_turns": 1, "total_cost_usd": 0, "modelUsage": {} }
```

**Eighty-eight milliseconds, one turn, zero cost, empty `modelUsage`.** The prompt never
reached the model. Cause: the workflow passed `/madar-daily` as the prompt, relying on
slash-command dispatch to find the skill in `.claude/skills/`. It did not resolve, and a
prompt beginning with `/` that is not a known command **fails instantly rather than
falling back to being treated as text.**

A second defect sat behind the first and would have bitten on the next attempt: the
action's own documentation states that a *plain-text* prompt inherits **no** tools —
only a skill invocation picks them up from its `allowed-tools` frontmatter. So switching
to plain text without an explicit grant would have produced a run with no shell, no file
tools and no web access, which would have failed later, slower, and far less legibly.

**Fix (both at once):** the prompt is now plain text instructing the run to *read*
`.claude/skills/madar-daily/SKILL.md` and follow it, and `claude_args` carries an
explicit `--allowedTools` grant covering Bash, the file tools and the web tools.

**The lesson, which is one this operation already owns in another form:** the failure
was not in the work, it was in the *dispatch* — a mechanism chosen because it was
idiomatic rather than because it was verifiable. Reading a file cannot fail for a reason
that has nothing to do with the operation. Same shape as ruling #36 (*a promise must be
derived, not declared*) and ruling #16 (*verify in the judging environment*): the first
version of this workflow was written against the documentation's example rather than
against the environment it would actually run in, and 88 milliseconds is what that costs.

Also cleared in the same commit: `actions/github-script` replaced with the `gh` CLI,
removing a dependency that warns about Node 20 on every run, and the `run-failure` label
is now created idempotently before an issue tries to use it — `gh` refuses to attach a
label that does not exist, so the failure reporter would itself have failed on its first
real failure.

## Cutover sequence

1. Steps 1–3 above. **Do not disable anything yet.**
2. Let the cloud daily run and the desktop schedule coexist for **two or three days**.
   They share no state but the repository, and the run verifies state before planning,
   so a double-run is wasteful rather than dangerous — it will find the day already
   done and say so.
3. When the cloud run has produced **two consecutive green days including a verified
   deploy**, disable the desktop schedules `madar-daily-operation` and
   `madar-weekly-review`. Ask me to do it, or turn them off in the app.
4. Keep the desktop path as the rollback. It has not stopped working; it is just
   dependent on a laptop being open.

## Rollback

Delete or disable the two scheduled workflows in the Actions tab. Nothing else in the
repository depends on them — `CLAUDE.md` and the skills are documentation the desktop
runs benefit from reading anyway, and `astro-pages.yml` is untouched by this migration.

## What this buys, concretely

At ten pieces the Africa edition has roughly two months of daily runs ahead of it. At
the current rate that is about **twenty dark days**. This migration costs one run and
about ten minutes of your time, and its whole job is to make the next twenty days
happen whether or not anyone opens a laptop.

— Manager · 2026-09-14
