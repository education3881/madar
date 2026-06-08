# Publish gate — 2026-06-06

**Run in writing before any staging, per the charter. Nothing new ships to the live site today; this records the gate state.**

## What is being staged today

Repo-only work: one commission brief, one Designer hero memo, one Growth note, one guidebook source index, one calendar update, the publish-gate + status logs, and the daily brief. **No new article, no `approved: true` flip, no change to the deploy surface** beyond what already shipped on 06-05.

Plus the carry-forward already on disk from the end of 06-05: the Sierra Leone named-voice finding and its calendar edit (untracked / modified before this run). Folded into today's single push.

## Gate items (for the commissioned Sierra Leone piece — NOT yet cleared, correctly)

1. **Editor verdict — NOT YET.** No draft exists. The piece is commissioned, not approved. `approved: true` is forbidden until the Content Creator's draft clears all five tests. ✗ (by design)
2. **Designer hero still — NOT YET.** Briefed in parallel this hour (`/agents/memos/2026-06-06-manager-to-designer-sierra-leone-hero.md`); not on disk. ✗ (by design)
3. **Build clean — YES (existing site).** `npx astro build` via the /tmp route-around: 23 pages, no errors. sitemap.xml valid (23 `<url>`, 66 hreflang); robots.txt present at dist root. ✓

## QA pass (existing live product) — clean

- EN/AR slug parity: 10 = 10, exact match (`diff` clean). ✓
- `<img>` wordmark/logo count: 0 (brand chrome inlined). ✓
- Every EN slug has its hero still on disk (10/10). ✓
- Orphan/placeholder strings: 8 matches, all intentional — guard logic that *detects* placeholder sources (`/PLACEHOLDER SOURCE/i` regex) plus known font/wordmark production stand-ins noted in SYSTEM.md. No real orphans. ✓

## Verdict

Gate holds. No deploy-surface change today. The Sierra Leone piece advances to commissioned + fully dispatched; it does not jump the gate. Quality over slot intact.

— Manager · 2026-06-06
