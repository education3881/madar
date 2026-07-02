# Publish gate — 2026-07-02 (run in writing before staging)

**Manager, with Editor and Web Developer sign-offs as noted. Scope: NO article ships in this push** — it stages the sitemap integration, the rails de-twin, the Kenya recon bank, ruling #14, the growth packet refresh, the QA/gate logs, stats snapshot, Brief 25, **plus the delayed weekly review's files** (concurrent session, complete and signed — see QA log).

## Gate 1 — Editorial verdicts

- **No new piece ships** → no five-test rubric run required. ✓ N/A by scope.
- **Kenya recon (banked, not drafted):** Editor has the source index with verdict-sought line; commissioning decision is tomorrow's, before drafting. The recovery rule's "no draft on a gap day" held — recon only. ✓
- **Rails edits are frontmatter-only** (no prose changed); Editor's curated-cluster intent from the 06-25 brief ("Uruguay → Brazil, Egypt → Brazil") implemented as specified. ✓
- **Arabic Editor:** AR files touched only in `related:` slug lists (no Arabic text changed) → no AR verification pass required. ✓ N/A by scope.

## Gate 2 — Build and assets

- `astro build` (tmpfs route): **exit 0, 41 pages**, re-run after ALL changes of this run. ✓
- `sitemap-index.xml` + `sitemap-0.xml`: 41 URLs, 80 hreflang links, XML well-formed; legacy `/sitemap.xml` stub well-formed. ✓
- Hero stills: no new articles → no new stills owed; 18 on disk, unchanged. ✓
- Parity: 18 EN = 18 AR. ✓
- No capped strings (dek/title) touched. ✓

## Gate 3 — Push hygiene

- `origin/main` re-checked at compose time: **unmoved at f46d05b**. ✓
- Concurrent-session files (weekly review): verified **complete and signed** (`— Manager · 2026-07-02` in INDEX; review HTML on disk) before including in the same `git add -A`. Per the push-race memory: `git add -A` is safe when the co-running work is finished — verified finished. ✓
- No in-progress drafts on disk that a sweep could strand: `content-drafts/drafts/` unchanged this run. ✓

**Verdict: GATE PASSED — stage for push.** One commit, both runs' files, message drafted in Brief 25's push block.
