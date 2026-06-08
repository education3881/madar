# Publish gate — 2026-06-07

**Run in writing before any staging, per the charter. Nothing new ships to the live site today; this records the gate state.**

## What is being staged today

Repo-only work: one research dossier, one Growth packet, one guidebook method entry, one calendar update, the publish-gate + status logs, and Brief No. 10. **No new article, no `approved: true` flip, no change to the deploy surface** beyond what already shipped on 06-05.

**Plus the entire un-pushed 06-06 day** (commission brief, Designer memo, source-index guidebook entry, Growth note, calendar edit, Brief 09, 06-06 gate + status logs, history.jsonl). Origin `main` = `8231af0` (06-05); the 06-06 push was never run. Folded into today's single commit.

## Gate items (for the commissioned Sierra Leone piece — NOT yet cleared, correctly)

1. **Editor verdict — NOT YET.** No draft exists; dossier delivered. `approved: true` forbidden until a draft clears all five tests with figures traced. ✗ (by design)
2. **Designer hero still — NOT YET.** Briefed 06-06; not on disk. ✗ (by design)
3. **Source-trace gate — BLOCKED ON ACCESS.** The seven hard figures + two named-human attributions cannot be traced to the primary (DOI .1115) from the sandbox: `edtechhub.org` / `docs.edtechhub.org` / `documents1.worldbank.org` are outside the network allowlist. Spine corroborated independently; figures quarantined. A `[[TRACE]]`-placeholder draft is permitted; an `approved` piece is not. ✗ (by design — and the unblock is named)
4. **Build clean — YES (existing site).** `npx astro build` via /tmp route-around: 23 pages, no errors. sitemap.xml valid (23 `<url>`, 66 hreflang); robots.txt at dist root. ✓

## QA pass (existing live product) — clean

- EN/AR slug parity: 10 = 10, exact (`diff` clean). ✓
- `<img>` wordmark/logo count: 0 (the single grep hit is a comment confirming inlined SVG glyphs). ✓
- Every EN slug has its hero still on disk (10/10). ✓
- Placeholder/TODO strings: 28 matches, all intentional — `PLACEHOLDER SOURCE` guard regex, empty-state CSS/JSX, `.gitkeep` notes, the known wordmark TODO stand-in (SYSTEM.md). No real orphans. ✓

## Verdict

Gate holds. No deploy-surface change today. The Sierra Leone piece advances from commissioned → dossier-complete; it is blocked only on source access, and the unblock is a single named Vini action. Quality over slot intact.

— Manager · 2026-06-07
