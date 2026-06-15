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

---

## Third gate — edition covers + homepage rebuild (founder-directed, 2026-06-15)

Vini approved the cover art direction and asked that the homepage mirror the editions organisation (current edition in its colours, with a browse link) and that **every edition carry an elaborate art cover**.

1. **Cover art — DONE.** Two complete SVG covers authored in the brand's line-art register: Edition 02 = astrolabe + 12-point woven thread-rosette, pine on paper; Edition 01 = surveyor's compass rose + horizon, terracotta on sand. Siblings in structure (frame, ticked azimuth ring, wordmark, bottom motif), distinct in instrument + palette — "different look, same style." Text-bearing but inlined into pages so brand fonts resolve. Files: `web/public/covers/edition-0{1,2}.svg`.
2. **Cold build — PASS.** 29 pages, 0 errors. Parity 12 = 12.
3. **Editions pages** — each block now inlines its cover above the masthead (`inlineCover()` via `process.cwd()`), constrained to 320px. Verified: both covers inlined on EN + AR (`#2F6F6A` + `#D94F2A` present).
4. **Homepage rebuilt (EN + AR)** — current edition is the hero, themed with its own ground/accent (no hardcoded orange), its cover inlined (~360px), pieces scoped to the current edition (lead = most recent), a "Previous editions" strip with cover thumbnails, and a "Browse all editions →" link. **Every hardcoded "Issue 01" is gone** (verified: 0 in built output anywhere, incl. the footer, which now derives the edition label from the registry). EN themeEn aligned to "deployment" to match the AR ruling + the cover.
5. **AR** — homepage mirrored over `articles-ar`; labels «الإصدار الحالي» / «إصدارات سابقة» / «تصفّح كل الإصدارات». RTL-correct.

**Open / honest caveats:** (a) no headless browser in the sandbox, so visual confirmation was by content-grep + the inline cover previews Vini approved in chat — final pixel check is the live deploy; (b) the AR theme strings carry the 2026-06-14 Arabic-Editor sign-off; the new UI labels are standard MSA and low-risk but a glance at the live AR home is worth it; (c) Edition 02 has 2 pieces, so the homepage is intentionally sparse — on-brand for a slow publication.

**Verdict: PASS for staging.** Build clean at 29; covers + homepage verified in built output.

— Manager · 2026-06-15 (third gate)
