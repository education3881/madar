# Manager publish gate — 2026-06-08

**Piece staging for push:** `2026-06-08-sierra-leone-tsc-teacher-matching` (EN + AR) — a NEW article ships live this push (the first since 2026-06-05).

The four gates, run in writing before staging, per the charter.

## Gate 1 — Editor verdict (the filter)
**PASS — 5/5.** Full verdict at `/content-drafts/verdicts/2026-06-08-sierra-leone-tsc-teacher-matching-verdict.md`. Test 1 (sourcing) is the load-bearing one and it clears: every figure (2,341 / 100% / 64% / 57% / 54% / 7%) and every named voice (Marian Abu, Lans Keifala, Gregory Elacqua) traced to the EdTech Hub primary, opened today. The 57%-vs-56/53% discrepancy resolved in favour of the primary's flat 57%.

## Gate 2 — Arabic Editor full pass + transliteration sign-off
**PASS.** Sign-off at `/agents/logs/arabic-editor-2026-06-08-sierra-leone.md`. Named-human transliterations verified (ماريان أبو / لانس كيفالا / غريغوري إلاكوا / بو / فالابا / بونثي / سيبال); TSC rendered هيئة خدمة التدريس consistent with the Bo AR piece; AR is composition, not calque; dek under the 200-char cap.

## Gate 3 — Hero still on disk
**PASS.** `/web/public/stills/2026-06-08-sierra-leone-tsc-teacher-matching.svg` present and referenced by both EN and AR frontmatter. House visual system held (continuous calligraphic line, paper ground, ink + single kiln-orange gesture, no fills/filters/gradients). All 11 slugs have a still (11/11).

## Gate 4 — Clean build + QA
**PASS.** Build via the /tmp route-around (the recurring `node_modules/.vite` FUSE boundary — copied node_modules with `cp -a` after rsync dropped files; routed around, not fought).
- 25 pages built, 0 errors.
- EN/AR slug parity exact: **11 = 11**, `diff` clean.
- Every slug has its hero still (11/11); brand wordmark remains inlined SVG (no `<img>` wordmark hits; the 23 `<img>` hits are editorial hero stills, by design).
- Rendered EN carries the figures (spelled in house style: "Sixty-four percent", "Fifty-seven percent", 54/7 percent), Marian Abu, Falaba/Bonthe, the 14% school-ID limit. Rendered AR carries the anchor voices and 2,341.
- **Sitemap fix applied:** the hand-built `public/sitemap.xml` was stale (missing the 2 new URLs). Added both EN + AR entries with hreflang alternates; validates as XML; now **25 `<url>`** in dist. robots.txt at root.

## Carried infra item (to the weekly, not blocking)
Replace the hand-built sitemap with `@astrojs/sitemap` before it drifts again — today's manual patch is the second time the static file needed hand-editing on a ship. The 06-07 host-allowlist request is **withdrawn** (the egress wall was bash-only; the web tools reach the sources — see today's guidebook entry).

**Verdict: all four gates PASS. Cleared to stage.**

— Manager · 2026-06-08
