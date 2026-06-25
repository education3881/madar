# Manager publish gate — 2026-06-25 (Brazil, sprint piece 8 of 10)

**Decision: PASS — cleared to stage.** Run in writing before any `git add`, per charter. One fresh bilingual piece (EN+AR); no override-mode.

## The piece
- **Brazil — "The literacy target, made national"** (Compromisso Nacional Criança Alfabetizada / Indicador Criança Alfabetizada; the self-administered-vs-external seam). Edition 02, `curated`, EN+AR. First Edition-02 Latin-America piece.

## Gate 1 — Editorial verdict + approval, on record
- **Editor verdict: APPROVE** — `content-drafts/verdicts/2026-06-25-brazil-crianca-alfabetizada.md`. Five-test rubric all PASS. Figure gate (closed at recon) **re-verified live this run** to named primary surfaces; the seam figure (Indicador 56% vs Saeb 49.3%, 2023) printed with both numbers attributed and the census-vs-sample caveat carried. Voice gate **seated at the system-operator tier** (Eliana Estrela, Seduc-Ceará, Mar 2026) — not a route-2 gap-statement case like Oman; announcement/ceremonial tiers (Santana, Lula) excluded by name; classroom-voice upgrade path logged, non-blocking.
- **Arabic Editor verdict: APPROVE** — `content-drafts/verdicts/ar/2026-06-25-brazil-crianca-alfabetizada.md`. Named-human transliterations verified (إليانا إستريلا · سيارا · سوبرال · برازيليا); Saeb/INEP/Todos Pela Educação kept Latin with AR gloss; composition (not translation); register on-voice; dek under cap incl. tashkeel.
- **`approved: true`** set on both EN and AR frontmatter.

## Gate 2 — Assets on disk (push-race invariant respected)
- **Hero still:** `web/public/stills/2026-06-25-brazil-crianca-alfabetizada.svg` — present; pure line-art (paper-cream / ink / kiln-orange; an ascending three-year figure, the external-audit shadow beneath, the 7-point gap in orange). Written **immediately after the article text**, before this gate — no asset deferred to a "completion commit." Referenced by both EN+AR via `<img src="/madar/stills/…">`; wordmark stays inline `<svg>`.
- **Sitemap:** `web/public/sitemap.xml` hand-patched to **41 URLs** (Brazil EN+AR with hreflang alternates); XML re-validated well-formed.

## Gate 3 — Build clean + parity (see qa-2026-06-25.md)
- **Build: exit 0, 41 pages** via the tmpfs route (full corpus, not reduced — completed in 2.21s this run). Both Brazil pages generated. Schema validation clean **with no gate-stage fix** — the dek cap was enforced at compose (EN 196 / AR 193), the first sprint ship where the cap didn't bite at the gate.
- **Brand chrome:** 1 inline `<svg>` (wordmark) + 1 `<img>` (hero still); zero brand-via-`<img>`.
- **Related rails:** resolve to Uruguay (LatAm sibling) + Egypt (literacy-measurement sibling), both in collection.
- **EN/AR parity:** 18 = 18 (stills 18, sitemap 41). Stats panel regenerated deterministically for the brief (`madar_stats.py --log`).

## Throughput / standing-rules check
- Quality-over-slot: held — gates were closed before drafting (banked 06-24), figures re-verified live, nothing unverified shipped. 1 fresh bilingual/day rhythm intact.
- Manager did **not** adjudicate the gate — the Editor did, on record; Manager routed and backs the verdict.
- **Sprint state after this ship: Edition 02 = 8 of 10 live. Two slots (9, 10) remain** — Researcher's wave-2 recon (Kenya CBC / Africa-beyond-Sierra-Leone + one more) is the gating dependency; no draft until banked gate-closed. Finish line ~end of W26 (≈06-29/30), bar over date.

— Manager · 2026-06-25
