# Method — running a real `astro build` inside the sandbox (the cold-build is NOT a gap)

**Banked:** 2026-06-15 · **Owner:** Web Developer / Manager · **Type:** production method
**Supersedes the operative caveat** repeated in several recent gates and briefs ("cold `astro build` not run: `node_modules` absent + the FUSE boundary; carried to the weekly"). That caveat was **half-wrong** and cost us verification we could have had. This note retires it.

---

## The finding

A full, clean `astro build` **does run in this sandbox today** — 29 pages, exit 0. Two separate facts were conflated into one false blocker:

1. **`node_modules` is present.** It is committed-absent from git but **materialised on the FUSE mount** (216 MB, 75 top-level packages, `node_modules/.bin/astro` present). No `npm install` is needed. (Recent gates asserted "node_modules absent" — that was not true on inspection.)

2. **The only real obstacle is the FUSE mount's `unlink` ban**, which bites Vite/Astro in two places:
   - **Dep-optimise cache** at `node_modules/.vite` → `EPERM: operation not permitted, unlink … .vite/deps/*.js` on the *re-optimise* step.
   - **SSR temp cleanup** under `dist/` → `EPERM … unlink dist/pages/**/*.astro.mjs` *after* pages are generated.

   Neither is a compiler error. The first is pre-build; the second is post-generation cleanup of a throwaway file (`dist/` is git-ignored). The pages are produced correctly in both cases.

## The recipe (definitive, repeatable — exit 0, accurate page count)

`astro.config.mjs` already exposes the cache override: `cacheDir: process.env.VITE_CACHE_DIR || undefined`. Use it, and move the **whole build off FUSE** by building from a tmpfs copy so `dist/` cleanup is writable too:

```bash
SRC="/sessions/.../mnt/Educational Website/web"; B=/tmp/mbuild
rm -rf "$B" /tmp/vmad; mkdir -p "$B"
cp -a "$SRC/src" "$SRC/public" "$SRC/astro.config.mjs" "$SRC/package.json" "$SRC/tsconfig.json" "$B/"
ln -s "$SRC/node_modules" "$B/node_modules"        # symlink, don't copy 216 MB; reads work over FUSE
cd "$B" && VITE_CACHE_DIR=/tmp/vmad npx astro build  # cache + dist both on tmpfs → exit 0
find dist -name '*.html' | wc -l                     # accurate count; dist is fresh, no stale files
```

Why each step:
- **Copy `src public astro.config.mjs package.json tsconfig.json`** — the build inputs. Small and fast.
- **Symlink `node_modules`** — avoids a 216 MB copy; package resolution only *reads*, which FUSE allows.
- **`VITE_CACHE_DIR=/tmp/vmad`** — dep-optimise cache lands on tmpfs, not `node_modules/.vite`.
- **`cwd = /tmp/mbuild`** — `dist/` is created on tmpfs, so the post-generation `unlink` cleanup succeeds → exit 0.
- The wordmark loader resolves `../../public/wordmark/…` first, so the copied `public/` satisfies it without the repo-root `design-assets/` fallback.

## Refinement — 2026-06-25 (Brazil ship; folded in at the 2026-07-02 consolidation)

Three environment drifts surfaced on a real build and their fixes are now part of the recipe:

1. **`cp -a` into `/tmp` can fail** ("preserving times: Operation not permitted") and a stale `/tmp/mbuild` from a prior session can be un-clearable. Fix: **`B=$(mktemp -d)`** for a fresh build dir every run, and **`cp -RL`** (no archive/preserve flags) for the inputs.
2. **Invoke the binary directly** — `./node_modules/.bin/astro build` — rather than `npx astro build`; `npx` may try to resolve/install a newer astro against the network and the FUSE boundary.
3. **FUSE leaves `.fuse_hidden*` ghosts** of files replaced this session in the content dirs (the unlink-ban artifact). A build over a copy that includes them emits spurious `[WARN] Duplicate id … later items overwrite earlier`. They are gitignored and invisible to `git status`/`git add -A`, and the GitHub Actions clean checkout never sees them → production is unaffected. For a warning-free honest local build: **`find "$B/src" -name '.fuse_hidden*' -delete` after the tmpfs copy.**

Updated core sequence:

```bash
SRC="/sessions/.../mnt/Educational Website/web"; B=$(mktemp -d)
cp -RL "$SRC/src" "$SRC/public" "$SRC/astro.config.mjs" "$SRC/package.json" "$SRC/tsconfig.json" "$B/"
find "$B/src" -name '.fuse_hidden*' -delete
ln -s "$SRC/node_modules" "$B/node_modules"
cd "$B" && VITE_CACHE_DIR=/tmp/vmad ./node_modules/.bin/astro build
find dist -name '*.html' | wc -l
```

## Why it matters / how to use it

- **Build verification is now a daily capability, not a weekly clean-checkout job.** Any `web/` change — ours or founder-directed — can and should be build-verified the same run. The QA gate's "build clean" line can be a *real* build, not a structural proxy.
- **Counting:** never `find <FUSE>/web/dist` for a page count — FUSE can't unlink, so stale HTML from old builds accumulates and inflates the count. Count the **tmpfs** `dist/`, or read the route list the build prints.
- **In-place is acceptable for a quick check**: `VITE_CACHE_DIR=/tmp/vmad npm run build` from `web/` will *generate* every page (you can grep them) and only fail on the final `dist/` cleanup (exit 1, cosmetic). Use the tmpfs recipe when you need a clean exit code or an honest count.

## Widening — 2026-07-04 (Kenya ship; written at the 2026-07-06 weekly consolidation)

*(The 07-04 QA log recorded this as "banked to the guidebook", but the note was never written — the weekly caught the log-vs-artifact drift and writes it now.)*

The FUSE `unlink` ban has **widened beyond the two known spots**: on the 07-04 build it bit *any* end-of-build unlink on the mount — `dist/_noop-middleware.mjs`, then `.astro/_noop-middleware.mjs` — **including files created in the same session**. Two consequences supersede parts of the text above:

1. **The "in-place is acceptable for a quick check" paragraph (§ Why it matters, item 3) is retired.** An in-place build on the mount can no longer *complete* at all; the mounted tree cannot host a finishing build. The tmpfs clean-checkout recipe is the **only** honest local build.
2. **`node_modules` may need restoring per-sandbox**: a package installed in one session's environment (e.g. `@astrojs/sitemap`, installed 07-02) can be absent from the next sandbox's `node_modules`. Restore with `npm install --cache /tmp/npm-cache` before building — and note the 07-06 finding: that same real `npm install` is what silently **repaired the hand-edited lockfile desync** that had been killing CI (ruling #16, `2026-07-06-local-build-is-not-the-deploy.md`). A real install is both the package restore *and* the lockfile truth-maker; never hand-edit the lock.
3. Stale `.astro-stale-*` / `.vite-stale-*` rename-asides accumulate on the mount (FUSE blocks their deletion); they are gitignored as of 07-04 and swept by any clean checkout.

## Cross-refs
- [[edu_website_sandbox_lock]] — the recurring FUSE/index.lock boundary this operationalises.
- `2026-06-08-egress-wall-is-bash-only-use-web-tools.md` — same shape of lesson (a blocked *bash* operation is not an unreachable *capability*). The cold build was the build-side twin of that error.
- `2026-07-06-local-build-is-not-the-deploy.md` — ruling #16; the deploy-side twin (a *passing* local build is not a passing deploy).
