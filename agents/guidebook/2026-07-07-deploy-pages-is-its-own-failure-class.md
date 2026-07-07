# Ruling #17 — `deploy-pages` is its own failure class (origin-commit-is-not-the-deploy-either)

**Filed:** 2026-07-07 · Manager (Quality) · extends **ruling #16** (`local-build-is-not-the-deploy`, 06-25)

## The finding
Ruling #16 said *a passing local build is not a passing deploy*, and pointed the runner-side suspect at the founder's push. This run followed that pointer and found the rule was only half the lesson. The 07-06 push (`f217a0f`) landed at origin, and the live site **still** served the 06-25 edition — Kenya (piece 9) 404, `sitemap.xml` newest entry Brazil 06-25.

Reading the Actions jobs API split the run into its two jobs and settled it:

- **`build` job — SUCCESS.** Every step green, including `npm ci` (4s) and `npm run build` (4s) and `upload-pages-artifact`. **The lockfile fix from 07-06 worked.** The build is healthy.
- **`deploy` job — FAILURE.** The single step `actions/deploy-pages@v4` failed in ~6s. Check-run annotation: **"Deployment failed, try again later."**

This is not the lockfile. It is not code. It is the **publish** step — the one that hands the built artifact to GitHub Pages — and it has failed on **four consecutive runs** (07-02, 07-02, 07-06 Kenya, 07-06 fix). Last successful live deploy: `f46d05b`, 2026-06-25. Four straight failures over five days is a **configuration state**, not a transient.

## The rule
**A deploy has two independent gates, and either can be green while the other is red:**
1. **Build** (code / lockfile / schema) — owned by the repo; fixed by a commit.
2. **Publish** (`deploy-pages@v4` → Pages) — owned by the repo **Settings**; a commit cannot fix it.

So the ladder of "is it live?" now has three rungs, not two:
- local build green → **not** the deploy (ruling #16)
- origin commit landed → **not** the deploy either (ruling #17)
- **a marker only the new deploy can serve resolves live** → the deploy (the only proof)

`deploy-pages@v4` returning **"Deployment failed, try again later"** on a setup that deployed via Actions before almost always means a **Pages settings state**, most likely:
- **Settings → Pages → Build and deployment → Source** is no longer **"GitHub Actions"** (flipped to *Deploy from a branch*, or Pages disabled). A stale **`gh-pages` branch exists in this repo** — a standing red flag that the source may be pointed at a branch.
- or **Settings → Environments → `github-pages`** gained a protection rule that blocks `main`.

**No push repairs either of these.** The fix is a founder settings change; until it lands, every commit builds a perfect artifact that is never published.

## Diagnostic method (banked, reusable — works from the sandbox)
`api.github.com` GET endpoints **are** reachable via `web_fetch` (the "unreachable" note in prior logs was about writes / rate-limited paths). The recipe:
1. `GET /repos/OWNER/REPO/actions/runs?per_page=6` — **large**; `grep`/read for `head_sha` + `conclusion` to see the failing streak. (Response is ~90k chars — read it from the saved file, don't inline.)
2. `GET /repos/OWNER/REPO/actions/runs/{id}/jobs` — **compact**; this is the money endpoint. It splits `build` vs `deploy` and shows which **step** failed. A run that fails in <60s total has failed *early* (setup/ci) — a multi-minute run that then fails is later (deploy).
3. `GET /repos/OWNER/REPO/check-runs/{job_id}/annotations` — the human-readable failure message.

Job durations are themselves evidence: run #37 was 37s total — build 09:36:44→09:37:04 (green), deploy 09:37:08→09:37:16 (failed). The build genuinely ran; the deploy genuinely tried and was refused.

## Correction of record
Brief 27 (07-06) said *"your one push repairs the pipeline."* **It did not, and could not.** The push healed the build (which was the 07-02 diagnosis) but the deploy has a *second, independent* failure that predates and outlives the lockfile fix. Filed as the fourth instance of the meta-pattern (sitemap 06-07, dek-count 07-04, lockfile 07-06, **publish-config 07-07**): *verify the thing itself, in the environment that judges it* — and know that the environment has **more than one** judge.
