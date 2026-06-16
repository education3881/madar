# Publish gate — 2026-06-15 (Monday)

**Run by:** Manager · **Context:** the day's site-facing change (Editions home + covers, `86c4478`) was authored, gated, committed **and pushed by the founder** during the run (local `HEAD` = `origin/main` = `86c4478`). The Manager's staged set today is **agents/ + drafts only — no `web/` files.** Gate runs anyway (deploy-clean-as-staged, every day) and additionally records a **post-ship QA** of the founder's feature.

## Part A — the Manager's staged set (what this push carries)

1. **Editor / Arabic-Editor verdict on any new article** — N/A. No article enters the collection today. Vietnam advanced from recon to **commission-ready** (voice gate closed via one recon pass) but is **not drafted** — quality-over-slot holds; no text ships.
2. **Hero stills on disk** — N/A to this push (no `web/` change staged). Invariant undisturbed: 12 stills match 12 EN articles (unchanged since `86c4478`).
3. **Build clean** — N/A to the staged set (agents/ + Markdown only; nothing compiles). The repo *as a whole* builds clean — see Part B.
4. **No orphaned references** — staged files are guidebook/source-index/QA/growth/gate/status/brief; all internally consistent, links checked.

**Verdict (Part A): PASS for staging.** Agents-only push; no site surface touched by the Manager.

## Part B — post-ship QA of the founder's feature (`86c4478`)

Full review: `/agents/reviews/2026-06-15-editions-home-qa.md`. Summary:

- **Build: PASS** — real `astro build` via the tmpfs/`VITE_CACHE_DIR` route ([[2026-06-15-astro-build-in-sandbox-vite-cache-route]]): **exit 0, 29 pages**, covers serve + inline, EN "Edition 02" / AR «الإصدار الحالي», footer registry-derived, **0 "Issue 01" in `dist/`**, parity 12 = 12, sitemap 29. AR sign-off strings («التوزيع», «الإصدار الحالي») present.
- **One finding (not a regression, not urgent):** the "Issue → Edition" rename reached chrome but **not article content** — the 2 Edition-02 articles' hero `alt`+`caption` still read "Issue 02"/«العدد الثاني» (and surface on the homepage via `alt`), and the Bo founding piece's body says "first issue"/«العدد الأول». Caption taxonomy is itself split (10 register-style vs 2 edition-style). Routed to **Editor + Designer + Arabic-Editor** as a content call; recommended **Option A** (register-style for all, drops "Issue" entirely). Not site-breaking — no park, no same-day fix required.
- **Verified non-issue:** Bahrain AR «العدد ذاته» = common-noun ("the same batch"), correctly left alone.

## Egress / live-render note

Live URL not fetched (egress wall is bash-only; per standing method, git/origin parity is the source of truth and GitHub Actions deploys on push). `86c4478` is on `origin/main`, so the feature is deploying/deployed; render confirmation is a browser check, not a sandbox capability.

— Manager · 2026-06-15
