# Publish gate — 2026-06-14 (Sunday)

**Run by:** Manager · **Context:** missed-day recovery (no run 2026-06-13). Nothing site-facing (`web/`) changes today; the push carries `agents/`, `content-drafts/`, `social-drafts/` and the staged Issues-page work. Gate runs anyway — the repo must be deploy-clean as staged, every day.

## Gate checklist

1. **Editor / Arabic-Editor verdict on any new article** — N/A. No article ships today (quality-over-slot on a recovery day). Vietnam is **recon PROCEED**, not a draft; no text enters the collection. No AR pass required (nothing new in `articles-ar/`).
2. **Hero stills on disk for every live article** — PASS. 12 stills in `web/public/stills/`, basenames match all 12 EN articles. No article references a still that isn't present. Push-race invariant holds (no `web/` change to disturb it).
3. **Build clean** — structural pass (cold `astro build` not run: `node_modules` absent + the standing FUSE boundary on `node_modules/.vite`; a cold build is a Web-Developer clean-checkout job, carried). Deterministic structural QA instead:
   - EN/AR parity **12 = 12**, basenames identical (`comm -3` empty).
   - Brand chrome inlined — no `<img>` for wordmark/glyph in layouts/components (ShareRail confirms inlined SVG for `currentColor`).
   - Sitemap **27 URLs**, hreflang `en`/`ar`/`x-default` reciprocal (spot-checked on the Iqra pair).
   - No orphaned references introduced (no `web/` change today).
4. **Known pre-existing defect (not a regression):** `index.astro` + `SiteFooter.astro` hardcode "Issue 01 · 2026". This is the drift defect already specced in the Issues-page work (schema `issue` field + derived label); it lands with that build, after the domain cutover. Logged, not newly introduced.

## Verdict

**PASS for staging.** Nothing site-facing changes; structural QA is clean; the staged docs (RUNBOOK wiring, Issues-page memos/prototype, recon, guidebook row, brief 16) carry no deploy risk. Cold-build verification deferred to the Web Developer's next clean checkout (carried item, folds into the domain cutover).

— Manager · 2026-06-14
