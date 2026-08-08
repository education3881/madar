# Publish gate (in writing) — Edition 04, "The measurement question" — 2026-08-08

**Decision authority:** Founder (Vini), 2026-08-08, interactive: *"lets just publish it, later we decide about the channels."* Scope = 8 (locked 2026-08-02). Channels (Substack/custom domain) explicitly deferred — do not block the site.

**Gate run by:** Manager/CEO. **Verdict: PASS — all 8 pieces cleared for the wave; 16 files flipped `approved: true`; build-verified.**

## The wave (8 pieces, each EN+AR)
| Piece | Country | Editor 5-test | Verifier verdict | AR gate |
|---|---|---|---|---|
| us-naep-honesty-gap | United States | APPROVE | CLEARED 07-09 | composed 08-02 |
| india-parakh-hpc | India | APPROVE | CLEARED 07-11 | composed 08-03 |
| singapore-psle-sbb | Singapore | APPROVE | CLEARED 07-12 | composed 08-04 |
| chile-simce-return | Chile | APPROVE | CLEARED 07-15 (fixed→re-cleared) | composed 08-05 |
| nz-ncea-corequisite | New Zealand | APPROVE | CLEARED 07-21 (scoped re-check) | composed 08-06 |
| australia-naplan-reset | Australia | APPROVE | CLEARED 07-17 (fixed→re-cleared) | composed 08-02 |
| netherlands-doorstroomtoets | Netherlands | APPROVE | CLEARED 07-27 | composed 08-07 |
| england-report-cards-first-term | United Kingdom | APPROVE | CLEARED 07-29 | composed 08-08 |

All eight verified drafter≠verifier (persona #11); verdicts on file in `content-drafts/verdicts/`. Rulings #21–#28 all originated in this wave's verification.

## Gate checklist
1. **Editor + Verifier verdicts:** 8/8 on file, all CLEARED. ✓
2. **Arabic Editor:** 8/8 composed at register; all named-human transliterations CONFIRMED-by-convention (name-routing conventions filed as guidebook rows 12–14 + #28 family); institutional acronyms Latin-tagged + glossed per #28a. ✓
3. **Stills ×10 → delivered as ×8:** the standing gap. **8 bespoke hero stills drawn today** (the wave is 8 pieces, so 8 stills, not 10) in the house ink-line language — pure line, one kiln-orange accent, paper ground, no fills/filters/gradients — each built from its piece's hero alt-text spec. All 8 present in `web/public/stills/` and resolve in `dist/stills/`. **No broken hero chrome.** Founder brief: "visually stunning and still elegant, better than other times" — elevated craft (faint underdrawing, luminous companions, orange echo/focal). Contact sheet reviewed. ✓
4. **`editions.ts`:** Ed04 registry entry added (period Aug 2026, theme "The measurement question", motif `horizon`, accent `#9C5B3A`, ground `#E9E5DB`, cover `edition-04.svg`); Ed03 flipped `current`→`closed`; Ed04 `current`. Cover SVG `edition-04.svg` created + resolves in dist. Editions page renders "Edition 04 · The measurement question" as current. ✓
5. **England moved into the build path:** EN + AR copied from `staged-ed0304/` into `web/src/content/articles{,-ar}/` (staging mirror retained, per the other 7). ✓
6. **Flip:** all 16 build-path Ed04 files `approved: false`→`true`. Verify: 38 EN / 38 AR `approved: true`; zero Ed04 `approved: false` remaining in build path. ✓
7. **Build:** `astro build` → **81 pages, Complete!, exit 0** (was 65; +16 Ed04 article pages). ✓
8. **Dist parity:** 38 EN / 38 AR article pages. ✓
9. **Hero integrity:** every Ed04 article's referenced still exists in `dist/stills/` — all 8 resolve, no broken images or share cards. ✓
10. **Share cards / SEO:** og:image + twitter:image absolute on Ed04 pages; hreflang reciprocal (en/ar/x-default) on Ed04 pages. ✓
11. **Internal links:** England `related:` (oman, us-naep, netherlands) all resolve to live pages; the 08-07 orphan-ref fix holds across the wave. ✓
12. **Brand chrome:** wordmark inline (0 external `<img wordmark>`) on Ed04 pages. ✓
13. **Stats:** live corpus goes to **38 EN / 38 AR / 100% parity / 35 countries** (Ed04 adds US, Australia, India, Singapore, Chile, NZ, Netherlands, UK; new regions Oceania + N-America) with this push.

## Not in scope (founder-deferred)
Distribution — Substack Issue 01 (Ed04-launch) and the custom-domain migration — remains parked on the two founder calls. The site goes live independent of both.

## Verdict
**PASS. Edition 04 is cleared and staged for the founder's push.** Ships whole (8 pieces, 16 files, 8 stills, edition wiring) in one commit. Once pushed + deployed (Pages Source = GitHub Actions since 07-07), Ed04 is live.
