# Verification verdict — Australia: "The bar, raised on purpose" (`2026-07-16-australia-naplan-reset`)

**Date:** 2026-07-17 · **Verifier → Editor** · third verdict of the persona
**Drafter:** Content Creator II (drafter ≠ verifier holds) · **Editor five-test verdict:** APPROVE-for-the-wave, 2026-07-16, on file
**Result: FAIL, one item → fixed same-run under Editor routing (both surfaces) → CLEARED.** Ed04 slate: **6 drafted / 5 verified**; only NZ's date-bound scoped re-check remains (NZQA, 20 Jul).

## Method

Figure-by-figure against recon (`recon/2026-07-06-australia-naplan-reset.md`) and the Editor's 07-16 trace list, then live re-trace of the load-bearing subset. Every trace-list item was re-fetched today from a primary or a full-text register mirror per #20 — none accepted from recon alone.

## Figure trace (anchors on file)

| Claim in draft | Anchor (re-fetched 2026-07-17) | Trace |
|---|---|---|
| Reading S+E 68.2% (67.0), NAS 9.3% (10.3); numeracy 66.8% (65.5), NAS 9.2% (9.5) | 30 Jul 2025 release, full text: medianet News Hub wire copy (complete, incl. background) + Mirage mirror | ✓ verbatim |
| Participation 93.8% highest since 2017; Y9 >90% first since 2019; QLD 89.7% through ex-TC Alfred | same release, Gniel passage | ✓ verbatim |
| +20,000 at Exceeding; both Gniel quotes | same release | ✓ word-for-word |
| First two-assessment cohorts (Y5/7/9), growth benchmark | same release | ✓ |
| Indigenous NAS reading **30.8% vs 7.6%** | release **background section** (medianet carries it; the Mirage mirror stops before it) | ✓ verbatim |
| Very remote **22.8%** vs major cities **71.9%** (reading S+E) | release background section | ✓ verbatim |
| Y9 writing girls **69.1% vs boys 53.9%** | release background section **and** 2025 National Results Commentary (blob PDF renders as text — route note below) | ✓ twice |
| Indigenous Exceeding uptrend, writing+numeracy Y7/Y9 since 2023 | release + Commentary (Y7 3.3→4.5%; Y9 writing 4.3→6.6%) | ✓ |
| 2023 first read: ~65% S+E, ~1 in 10 NAS, ~quarter Developing | recon MEASURED (release PDF, 07-06) + stability chain (2024 release: 67.0/65.5 "broadly stable" vs 2023; 2025 release: "broadly stable 2023→2025") | ✓ corroborated |
| 2023 Y9 writing 58.0% meeting | 2023 coverage corroboration + recon primary | ✓ |
| 2023 Indigenous NAS "about one in three" | 2023 Commentary (blob, full text): averages 33.1 / 31.8 / 33.1 / 33.7 across Y3–Y9 | ✓ |
| de Carvalho quote ("…those areas where we need to focus our efforts") | recon-verified verbatim on 23 Aug 2023 release (07-06); context corroborated today | ✓ |
| 2026 calendar: window 11–23 Mar; national results **August 2026** | ACARA key-dates, live today; the "13 August 2026" row confirmed to be the **schools-list** update (the trap the Editor flagged — real) | ✓ |
| "No state or territory has walked the reset back" (negative claim) | absence verified across 2024–26 coverage sweeps; nothing found beyond pre-2023 review history | ✓ absence |
| **2024 volumes: "4.4 million tests sat by *more than* 1.3 million students"** | 14 Aug 2024 release (medianet full text): "A record 4.4 million online tests were submitted by **almost** 1.3 million students in 9,431 campuses" | **✗ FAIL — see item 1** |

## Item 1 (approximation direction, load-bearing in a stillness piece)

Draft ¶4 as submitted: "In 2024, across some 4.4 million tests sat by **more than** 1.3 million students…". The 2024 register says **almost** 1.3 million; it is the **2025** release that says "a record **4.5** million tests… by **over** 1.3 million students." The draft carried 2024's volume with 2025's direction word — two adjacent years, the hedge flipped between them, and the flip travelled. Direction of an approximation is part of the figure (ruling #23, filed today). The error is small and conservative in no direction that matters; it still fails: in a piece whose whole argument is that the ruler must not drift, the prose cannot drift either.

**Fix (same-run, Editor routing):** "more than" → "almost" in ¶4 and in the source-title annotation (frontmatter source 3); **mirrored to the staging copy** (`staged-ed0304/articles/`, per the NZ precedent). Re-checked post-fix: both surfaces agree; build clean (65pp exit 0), zero leakage, parity 30=30.

## Guardrail carriage (#19) — all five recon §6 fences carried in the sentence

1. Series break stated where the comparison would tempt ("not to be compared with earlier years — the authority drew the break-line itself") ✓
2. "1 in 3 below the bar" derivation stated with its denominator; *Developing* defined as working-towards, twice; never rendered as failing ✓
3. AERO figure labelled "a researcher's finding, not an ACARA proficiency figure"; AARE counter carried in-piece ✓
4. August 2026 release named; piece self-fences to 2023–2025 in the closing paragraph ✓
5. AR gloss list carried forward in the Editor's verdict for the AR batch ✓

## Schema and state checks

- Dek **194** code points ✓ (≤200); title 26 ✓ — counted on the file as written.
- `related:` — us-naep (drafted, verified), nz-ncea (drafted), oman (live) — all resolve on disk ✓, no orphan at the wave.
- `approved: false` on both surfaces ✓ (the flag is the hold, #18).
- Hero still **not on disk** — Designer's Ed04 batch of 10 (status memo item 4); alt-text is composed and strong; the still should be drawn to it. Gate item, not a verdict item (Chile precedent).
- `arabicVersion` ref with no AR file — consistent with the other five Ed04 drafts; AR composes as a batch before the gate.

## Observations (per #20 — observations, not verdicts)

- **NAPLAN 2026 platform outage, 11 Mar 2026** (day one of the window) surfaced in coverage during the negative-claim sweep. The draft's only 2026 claims — window sat 11–23 Mar (ACARA's own 27 Mar "testing concludes" release, cited in sources) and results due August — survive it. **Gate action:** re-check the ACARA newsroom at the Ed04 publish gate (already a recon §6 requirement); if the outage shaped the 2026 administration story, that is next cycle's piece, not a hold on this one.
- **Route bank (2 additions):** (a) ACARA's data-portal blob host (`dataandreporting.blob.core.windows.net`) serves the National Results **Commentary PDFs as parseable text** through our fetch path — 2023 and 2025 both read in full today; the acara.edu.au PDFs still render binary. (b) **medianet News Hub** carries ACARA releases **complete** — including the background section where the equity decimals live; the Mirage mirror truncates before it. Both filed to the ACARA source index (row 11).
- Fetch-tool provenance boundary blocked a direct live *article* head-check today (homepage passed — hreflang triple + canonical verified **on live** directly, closing the 07-16 lineage-only caveat). Environment constraint, not a site verdict.

**Verdict: CLEARED for the wave.** The flag stays `false` until the Ed04 gate; this verdict is the piece's flip authority under #18.

— Verifier · 2026-07-17
