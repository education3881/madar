# Publish gate (retroactive) — 2026-07-07 · Edition 03 "Continuity under disruption" (10 pieces)

**Context:** Edition 03 went live via the founder's `git add -A` push before the verification wave ran (the sandbox staging that would have held it did not reach the working tree — bash file-moves don't persist to the founder's git; Write-tool files do). Founder decision on discovery: **keep live, verify in place.** This gate is that verification, run after publication.

## Method — drafter ≠ verifier
Three independent auditors, each cross-checking a subset against the research record only (compose-notes figure/voice ledgers + recon briefs + frontmatter `sources:`), no re-drafting:
- A: Sudan, Yemen, Syria
- B: Ukraine, Türkiye, Gaza (+ Gaza guardrail audit)
- C: Poland, Lebanon, Chad, Rohingya (+ route-2 gap-statement audit)

Checks per piece: every body figure traceable to the record (flag untraceable/contradictory); named humans match name/role/date/outlet + transliteration; internal arithmetic; dek not stronger than body; route-2 gap statement present; Gaza sensitivity.

## Result — 10 / 10 PASS
- **Figures:** every figure in all 10 pieces traces to the compose-notes/recon ledgers. No untraceable or contradictory number found. Internal arithmetic reconciles where checked (e.g., Syria Damascus remainder 65,111−28,559−29,287=7,265 = branch splits; Yemen 39,047/193,668≈1-in-5; Poland 111,726+54,089=165,815; Chad 5,919 passed < 12,348 sat).
- **Named operators:** all match the record; disclosed-translation and implementer-vs-independent-voice conventions honored; transliterations verified at source in compose-notes.
- **Route-2 gap statements (Lebanon, Chad, Rohingya):** all THREE present in the Oman pattern. Rohingya (flagged suspect) has an explicit statement (para 6) disclosing its only named operator reaches the page in paraphrase, no quotation marks — correct.
- **Gaza guardrails:** held — exactly one damage-context sentence (UNICEF 91.8% / >740 schools), zero casualty counts, zero ban-politics, ceasefire as a single neutral clause.
- **Mechanical gates:** all 10 EN + 10 AR deks ≤200 incl. tashkeel; 10 stills on disk; EN/AR parity 10=10; no orphaned related refs.

## Two items for Editor awareness (NOT defects — no fix required)
1. **Gaza — the ~658,000 "two+ years without in-person schooling" sentence:** a borderline second damage-context line, but defensibly a continuity/access denominator (schooling interruption, not physical destruction). Holds at the one-sentence limit under that reading. Left as-is.
2. **Poland — 195,288 "children incl. preschools, end-Sept 2024":** the weakest-supported figure; the drafter self-flagged it as personally un-re-verified and offered to strike. It traces to the recon ledger, is denominator-labeled in-piece, and carries nothing load-bearing. Left as-is; strike candidate if the Editor wants maximum conservatism.

## Verdict
**Edition 03 publish gate CLEARED. All 10 pieces verified-and-live.** The fast-drafted sprint batch held up under independent scrutiny — the bar held even though the process order was scrambled by the premature push.

## Housekeeping (for the next daily run) — NON-URGENT
- **Edition 04 (5 pieces: chile, india-parakh, nz-ncea, singapore, us-naep) are committed in `web/src/content/` but correctly HELD** via `approved: false` frontmatter. The article route builds only `approved !== false` (`web/src/pages/articles/[...slug].astro`), so they do not generate pages, are absent from the sitemap, and 404 (confirmed) — **this is the intended held state, not a risk.** They publish only when someone deliberately flips `approved: true` after Ed04 is complete (10/10) and gated. No `git rm` needed. (Edition 4 is also absent from `editions.ts`, a second gate.)
- Duplicate copies of the 10 now-live Ed03 drafts remain in `content-drafts/staged-ed0304/` — harmless clutter; dedupe whenever convenient.
- The Ed03 verification record (this file) is uncommitted; it rides the founder's next push, no urgency.

— Manager / verification wave · 2026-07-07
