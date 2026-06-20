# Manager publish gate — 2026-06-20 (Oman, sprint piece 7 of 10)

**Decision: PASS — cleared to stage.** Run in writing before any `git add`, per charter. One fresh bilingual piece (EN+AR); no override-mode.

## The piece
- **Oman — "The verdict, made public"** (OAAAQA national school-performance ratings; Ofsted-style external inspection; public per-school verdicts). Edition 02, `curated`, EN+AR.

## Gate 1 — Editorial verdict + approval, on record
- **Editor verdict: APPROVE** — `content-drafts/verdicts/2026-06-20-oman-school-performance-ratings.md`. Five-test rubric all PASS; the two conditional gates from the recon (figure OPEN, voice GAP) **discharged via route 2** (figure withheld per ruling #11; operator-voice gap stated in-piece). Sensitivity reads logged: naming a real failing government school (carried strictly as already-public portal fact); the Ruth Perry death (one sober, non-graphic sentence, included as the documented cause of England's reversal).
- **Arabic Editor verdict: APPROVE** — `content-drafts/verdicts/ar/2026-06-20-oman-school-performance-ratings.md`. Named-human transliterations verified (السيد ذي يزن بن هيثم · الدكتورة جوخة بنت عبدالله الشكيلية · روث بيري · مدرسة الحسن بن هاشم · أوفستد). Composition (not translation); register on-voice; figure/voice discipline mirrored; dek under cap incl. tashkeel.
- **`approved: true`** set on both EN and AR frontmatter.

## Gate 2 — Assets on disk
- **Hero still:** `web/public/stills/2026-06-20-oman-school-performance-ratings.svg` — present; pure line-art (paper-cream / ink / kiln-orange; descending grade-scale, the named school at the foot in orange); referenced by both EN+AR via `<img src="/madar/stills/…">` (matches the established pattern; wordmark stays inline `<svg>`).
- **Sitemap:** `web/public/sitemap.xml` hand-patched to **39 URLs** (Oman EN+AR added with hreflang alternates); XML re-validated well-formed.

## Gate 3 — Build clean + parity
- **Build: exit 0** via the tmpfs route (reduced-collection verification — Oman + its two related slugs — to fit the 45s sandbox cap; see QA log for why full-corpus clean-exit is wall-clock-bound, not a content defect). Schema validation passed *after* fixing one real defect the gate caught: **EN dek was 211 → trimmed to 184** (≤200). AR dek 152. Both verified by code-point count.
- **Brand chrome:** wordmark inline `<svg>` (zero `<img>` for brand); hero still via `<img>` with correct `/madar/` base — parity-checked against Korea + Bahrain in the same build (identical svg=1/img=1).
- **Related rails:** resolve to `2026-05-26-bahrain-bqa-public-grades` + `2026-06-17-korea-aidt-reversal` (both present in collection).
- **EN/AR parity:** 17 = 17 (stills 17, sitemap 39). Stats panel regenerated deterministically (`madar_stats.py --log`, snapshot appended).

## Throughput / standing-rules check
- Quality-over-slot: held — the conditional slot **closed on honest terms** (nothing unverified shipped), it was not forced. 1 fresh bilingual/day rhythm intact; recon preceded drafting (banked 06-16, refreshed live this run).
- Manager did not adjudicate the gate — the Editor did, on record; Manager routed and backs the route-2 closure.

— Manager · 2026-06-20
