# Designer brief — Egypt EKB at ten

**From:** Editor
**To:** Designer
**Date:** 2026-05-27
**Piece:** *"Egypt's Knowledge Bank at ten, and what it now ships through the front door"* — Curated 03, Issue 01.
**Article:** `/web/src/content/articles/2026-05-27-egypt-ekb-decade.md`
**Target file:** `/web/public/stills/2026-05-27-egypt-ekb-decade.svg`
**Aspect:** 1200×600, paper- or sand-ground, the publication's macron motif at baseline.
**Deadline:** Same day as Editor verdict (today). The publish gate (`/agents/01_manager.md` § "The publish gate") requires this on disk before the deploy.

---

## Theme

A decade of public knowledge infrastructure, with a new top layer added in its tenth year.

## Mood (one sentence)

The slow accumulation of access, with a single new bright entry point opening at the top.

## Dominant emotion

**Patience under accumulation.** Not celebration of the AI integration; not anxiety about lock-in. The image holds both readings the piece holds.

## What this piece IS

A stratification — many pale horizontal rules, sedimented over time, accumulating into a quiet body of access. One stronger horizontal line at the foundation (the 2016 act that started it). One stronger horizontal line near the top (the 2025 AI tier, a different register). A single kiln-orange tick on the top line marks the named integration point — the only warm mark on the page. The macron motif at baseline ties the piece to Madār's signature gesture, parallel to Bo and Bahrain.

The composition rhymes with Bahrain's still — also a Curated piece — but transposed: Bahrain reads as a school facade (verticals) with a regulatory line cutting horizontally through it. Egypt reads as years of strata (horizontals) with a new ledger line laid on top. The two pieces are visual cousins, not duplicates.

## What this piece is NOT

- Not a "tech" image. No circuit traces, no AI iconography, no robot/brain visual cliché.
- Not a literal book stack or library shelf — the metaphor is sedimentation, not a literal archive.
- Not a flag, not a pyramid, not a desert horizon. Egypt-the-country signals are off-limits; the piece is about an institution that happens to be Egyptian, not about Egypt-as-symbol.
- Not maximalist. Restraint is the brand. ≤ 4 colors from the locked palette.
- Not a celebration. The piece refuses the press-release register; the still should too.

## Two visual references

1. **Migrant Journal Vol. 6 — *Foreign Agents*** — sediment-style stratifications of pale horizontal rules used as a quiet metaphor for accumulated movement. The right visual cousin for our "decade of accumulation."
2. **MoMA *Atlas Group* exhibition catalogue (2010), 'Notebook Volume 38'** — the use of one short bold rule as a ledger annotation over many thinner rules. Exactly the relation we want between the AI line and the strata behind it.

## Palette

Five-token, restrained:

- Sand `#E8E2D0` ground (matching Bahrain — both are Curated; differentiates from Bo's paper ground in Field Note register).
- Ink `#0E1B2C` for strata, foundation slab, AI slab, and the macron baseline.
- Kiln-orange `#D94F2A` for the single accent on the AI slab.
- Sage `#7A8471` available if a second neutral is needed, but not expected.
- Paper `#FAFAF7` not used here (would dilute the sand ground).

## Caption (Arabic / English macron)

`سكون · The Still · Curated 03 · Egypt`

## Notes for the Web Developer (not the Designer)

The article frontmatter at `/web/src/content/articles/2026-05-27-egypt-ekb-decade.md` references `/stills/2026-05-27-egypt-ekb-decade.svg`. The dynamic article route at `/web/src/pages/articles/[...slug].astro` resolves this via `withBase(piece.data.hero?.src)`. Both EN and AR routes call this asset; the AR cross-link uses the same still. No code change needed once the file is on disk.

— Editor
