# Designer brief — UAE Madrasa × TikTok

**From:** Editor
**To:** Designer
**Date:** 2026-05-27
**Piece:** *"The Arabic STEM library that decided to live inside the algorithm"* — Curated 04, Issue 01.
**Article:** `/web/src/content/articles/2026-05-27-uae-madrasa-tiktok.md`
**Target file:** `/web/public/stills/2026-05-27-uae-madrasa-tiktok.svg`
**Aspect:** 1200×600, sand or paper ground, the publication's macron motif at baseline.
**Deadline:** Same day as Editor verdict (today). The publish gate requires this on disk before the deploy.

---

## Theme

A curriculum sequence unbundled into a feed. Order, becoming scatter — but a particular kind of scatter, the kind a vetted feed produces.

## Mood (one sentence)

The same set of units, twice: once arranged in a column the platform composed; once redistributed across a field the algorithm composed.

## Dominant emotion

**Studied curiosity.** Not anxiety about the algorithm, not celebration of the reach. The image holds the piece's posture: this is something to read, not something to take a side on.

## What this piece IS

A composition built from one small unit (a thin ink rectangle, the visual stand-in for a single educational video) repeated many times in two arrangements that share the canvas:

- **A column or tight grid in the left or upper portion** — the platform's own sequence: units arranged in close rows, ordered, sized identically, the spacing of a curriculum.
- **A scatter across the rest of the field** — the same units redistributed, slightly rotated or off-axis, varied in spacing, no longer in sequence. A feed.

A single kiln-orange small unit somewhere between the two arrangements — the moment of the partnership, the single hinge between the two compositions. The macron motif at baseline ties the piece to Madār's signature gesture, parallel to Bo, Bahrain, and Egypt.

The composition rhymes with Egypt's still but reads differently: Egypt is sedimentation (horizontal strata accumulating); UAE is redistribution (the same units, arranged twice).

## What this piece is NOT

- Not a phone screen. No screen icons, no TikTok bird, no play button. Literal social-media iconography is the cliché.
- Not "Arabic letters becoming pixels" or any disintegration metaphor — those read as anti-tech editorial, and the piece is not that.
- Not a tree, branches, or any "spreading" metaphor — the piece argues redistribution, not growth.
- Not maximalist. ≤ 4 colors from the locked palette.
- Not a celebration; not a critique. Restraint matches the piece.

## Two visual references

1. **Karel Martens, *Counterprint* (2013)** — small repeated units arranged in two registers on the same field, with one anomalous unit serving as the visual hinge. Almost exactly the structural model we want.
2. **MoMA's typographic-grid exhibition catalogues (Müller-Brockmann tradition)** — the discipline of a small unit used as both the building block of a sequence and the inhabitant of a field. The same atom, two arrangements, restraint as the bond.

## Palette

Five-token, restrained:

- Sand `#E8E2D0` ground — consistent with Bahrain (Curated 02) and Egypt (Curated 03); the curated series shares a ground.
- Ink `#0E1B2C` for both the column and the scatter (the same color across both arrangements is the point — same content, two distributions).
- Kiln-orange `#D94F2A` for the single hinge unit. The only warm mark on the page.
- Sage `#7A8471` not used here.
- Paper `#FAFAF7` not used.

## Caption (Arabic / English macron)

`سكون · The Still · Curated 04 · UAE`

## Notes for the Web Developer (not the Designer)

The article frontmatter references `/stills/2026-05-27-uae-madrasa-tiktok.svg`. The dynamic article route resolves it via `withBase(piece.data.hero?.src)`. No code change needed once the file is on disk.

— Editor
