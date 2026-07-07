# Publish gate — 2026-07-07 · Morocco (Edition 02, piece 10)

Run **in writing before staging**, per the standing 3-gate rule. This gate covers **Morocco only**. Ed03 and Ed04 drafts are **NOT** gated this run — explicitly held (see QA log + sprint file).

## Gate 1 — Editor verdict (five tests): PASS
Recorded in `content-drafts/verdicts/2026-07-06-sprint-triage.md` §C, in writing:
1. Figure gate PASS — 13-source ledger, every figure MEASURED/ANNOUNCED/DERIVED-labeled; World Bank co-financier interest disclosed inline; 10,000-MAD bonus flagged not-yet-verified-in-BO.
2. Voice gate PASS at full bar — Hassan El Bilali (provincial director, Berrechid) + Abdeslam Derrari (school director), Médias24 03-04-2025, direct quotes, translation disclosed.
3. Mechanism-first PASS — minister unnamed; no vendor framing.
4. Firewall PASS — MEL +0.9 SD (labeled preliminary/pilot) never blended with CSEFRS 79/100 (ruling #12b).
5. Sibling spacing PASS — rails Brazil + Egypt-NPDA; distinct motif and closing aphorism.
- **Defect caught and fixed at the gate:** title/dek over-asserted the DERIVED one-in-six ratio; retitled **"The label that can be refused"** / **«العلامةُ التي يمكنُ أن تُحجَب»**, both deks recomposed around the decree-documented refusability mechanism (EN 186/200; AR ≈157/200 incl. tashkeel). The gate did its job.

## Gate 2 — Arabic Editor sign-off: PASS
Per triage §C: البلالي (MAP rendering, not البيلالي) CONFIRMED · مدراري CONFIRMED for AR while EN keeps "Derrari" per its cited outlet (cross-language outlet-fidelity) · علامة as label-noun CONFIRMED · pan-Arab month forms CONFIRMED. **Morocco APPROVED.**

## Gate 3 — build + assets: PASS (this run)
- Hero still on disk: `web/public/stills/2026-07-06-morocco-ecoles-pionnieres.svg` ✓
- EN + AR both present, `arabicVersion`/`approved: true` set ✓
- **astro build CLEAN** in the Actions-exact `/tmp` environment: 45 pages, `sitemap-index.xml` (45 URLs), Morocco EN + AR render, parity **20 = 20** ✓

## Verdict
**Morocco APPROVED to stage** as Edition 02, piece 10 — closing the edition at 10 and satisfying founder decision #1 (slot 10 = first banked deployment-theme piece). Will not go **live** until the deploy P0 (Pages config, ruling #17) is fixed; the commit queues it for the first successful publish.

— Manager · 2026-07-07
