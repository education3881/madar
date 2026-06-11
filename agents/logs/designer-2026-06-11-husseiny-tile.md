# Designer log — Husseiny pull-quote tile (Issue 02 grid)

**From:** Designer → Manager / Growth
**Date:** 2026-06-11
**Brief:** Growth launch packet 2026-06-10 §3 ("One tile, both languages, no figures")
**Output:** `/design-assets/instagram/issue-02-grid/2026-06-11-tile-husseiny-quote.png` (1080×1080) + reproducible HTML source in `source/`.

## What it is

The first Issue 02 grid tile: the Husseiny line in both languages — «البيداغوجيا مهمة.» set large in Amiri 700 (RTL, the lead surface, per the packet), the English continuation in Cormorant Garamond italic below an orange macron slab, attribution in JetBrains Mono (named human + affiliation + dateline context), path-based wordmark bottom-right. Paper/ink/orange palette, site grain texture. No figures on the tile, per the brief.

## Method note (extends the 2026-06-05 rendering guidebook)

This is the catalogue's first tile with **real text in brand fonts**, which the 2026-06-05 method explicitly does not cover (cairosvg cannot shape Arabic). The working path, now banked in the guidebook (`2026-06-11-brand-fonts-via-npm-fontsource.md`):

- **Fonts:** GitHub *release assets* are no longer reachable from the sandbox (they redirect to `release-assets.githubusercontent.com`, not on the allowlist). Route-around: `@fontsource/amiri`, `@fontsource/cormorant-garamond`, `@fontsource/jetbrains-mono` from npm (allowlisted) — same OFL fonts, woff2.
- **Render:** Playwright headless Chromium (allowlisted CDN), 1080×1080 viewport, `@font-face` with `file://` URLs, screenshot. Chromium shapes the Arabic correctly (HarfBuzz) — guillemets mirror, lām-shaping and diacritic placement verified by eye on the output, per the "look at it" rule.

## Verification

Rendered PNG inspected visually: Arabic shaping correct, RTL punctuation correct, EN column balanced at four lines, slab/wordmark/grain on brand, kicker legible at thumbnail size. Ship-ready; joins the Issue 02 grid queue behind the opening grid (still one Vini-action from launch).

— Designer · 2026-06-11
