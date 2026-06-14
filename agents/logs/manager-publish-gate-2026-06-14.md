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

**PASS for staging** (first run, daily/weekly). Nothing site-facing changed; structural QA clean.

— Manager · 2026-06-14

---

## Second gate — the Editions feature (founder-directed, same day)

After the first push landed (`692e3a4`), Vini authorised building the **Editions** feature now (see `memos/2026-06-14-editions-decisions-and-palette.md`). This is a **site-facing** change, so the gate ran a real cold build.

1. **Cold build — PASS.** `node_modules` install + `astro build` via the /tmp route-around: **29 pages, 0 errors** (27 baseline + `/editions/` + `/ar/editions/`). The FUSE boundary was routed around, not fought.
2. **Schema + backfill** — `edition` field optional (no break risk); backfill verified 10 + 2 EN, 10 + 2 AR; build passed schema validation. Parity holds **12 = 12**.
3. **Rendered content verified in built output** — both edition pages: numerals 01/02, May/June periods, both theme lines, "Current"/«العدد الحالي» tag on Edition 02 only, all 12 piece links per language, per-edition accents (`#2F6F6A` current / `#D94F2A` Edition 01) + grounds present via inline custom properties. Nav link resolves on interior pages.
4. **Sitemap** — updated by hand to **29** URLs incl. the two editions entries with reciprocal hreflang; valid XML (the build-generated sitemap migration is still carried).
5. **Sandbox hygiene** — `.fuse_hidden*` FUSE leftovers from rewriting 24 frontmatters added to `.gitignore` so `git add -A` cannot sweep them. Stray `.git/index.lock` present (sandbox can't unlink — `Operation not permitted`); the push block clears it on Vini's side.
6. **Sign-offs still pending before this is "done":** Editor on EN theme lines; **Arabic Editor on all AR strings** (الإصدارات / periods / theme lines / «العدد الحالي» / empty-state) — drafted, flagged in `editions.ts`. The AR word for "placement" («الإسناد») is explicitly queued for the Arabic Editor's ruling.

**Verdict: PASS for staging** — the build is clean and the pages render correctly. Caveat logged honestly: AR strings are draft-pending-AR-Editor, and the homepage still frames everything as "Issue 01" (deliberately out of scope; teed up for Vini's editorial call on whether the homepage becomes current-edition-only).

— Manager · 2026-06-14 (second gate)
