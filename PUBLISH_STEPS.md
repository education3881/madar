# Publish steps — Madār v0.1

This file is the precise, ordered sequence Vini runs **once** to publish v0.1. It's safe to delete after the first successful deploy.

## Context (the state I left things in)

I configured everything I could from the sandbox:

- `web/astro.config.mjs` — `site` and `base` set for `https://education3881.github.io/madar/`.
- All internal links and asset references are now base-aware via a new `web/src/lib/urls.ts` helper. Every `href` and `src` rewrites to `/madar/...` at build time.
- `.github/workflows/astro-pages.yml` — GitHub Actions Pages workflow, builds from `web/` and uploads `web/dist`.
- `.gitignore` — at the repo root, ignores `node_modules`, `dist`, `.astro`, `.DS_Store`, env files.
- `npm run build` was run against the new config in a sandbox copy and produced clean output with every URL correctly prefixed.

What I could not finish: the actual git init + push. My sandbox can't fully manage `.git/` internals on your mounted folder — a partial `.git/` directory was left behind that needs deleting before you re-init.

## Run these commands in your terminal

```bash
cd "/Users/vini/Documents/Claude/Projects/Educational Website"

# 1. Remove the partial .git directory my sandbox left.
rm -rf .git

# 2. Fresh init on the main branch.
git init -b main
git config user.email "education3881@gmail.com"
git config user.name "Madār"

# 3. Stage everything; .gitignore will skip node_modules/dist/.astro.
git add -A
git status              # sanity check — should list ~65 files, no node_modules, no dist

# 4. First commit.
git commit -m "Madār v0.1 — initial publish

- Astro static site under /web, builds to /web/dist
- Three approved pieces (Sierra Leone, Jordan, Colombia)
- Bilingual (EN + AR) with RTL Arabic home
- GitHub Actions workflow for Pages deploy
- Configured for project page at https://education3881.github.io/madar/"

# 5. Set the remote and push. GitHub will prompt for auth on first push.
#    Use a personal access token (PAT) as the password, not your account password.
#    Create one at: https://github.com/settings/tokens — scope "repo" is enough.
git remote add origin https://github.com/education3881/madar.git
git push -u origin main
```

## Then in the GitHub UI (one time)

1. Open `https://github.com/education3881/madar/settings/pages`.
2. Under **Build and deployment** → **Source**, select **GitHub Actions**.
3. Save. The Actions tab will show the first workflow run starting automatically (or on the next push if it didn't trigger).
4. After ~30–60 seconds the run completes and the site is live at:

   **https://education3881.github.io/madar/**

## If anything goes wrong

- **Push fails with "authentication"** — you used your account password instead of a PAT. GitHub stopped accepting passwords for git operations in 2021. Create a PAT at the link above and use it as the password.
- **Workflow run fails on build** — open the failed run, expand the "Build Astro site" step, look for the actual error. Most likely cause is a missing source URL or an Arabic content file with a schema mismatch; the Editor can fix and you re-push.
- **Site loads but CSS / images broken** — almost certainly means `base` in `astro.config.mjs` doesn't match the URL the site is served at. Double-check the repo is named `madar` exactly and the URL is `education3881.github.io/madar/` (trailing slash).

## After it ships

Delete this file. The HANDOFF.md in `/web/` keeps the long-term notes.
