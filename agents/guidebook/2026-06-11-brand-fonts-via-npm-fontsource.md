# Guidebook — brand-font rendering: fonts come from npm, render via Chromium

**Banked:** 2026-06-11 · **Extends:** `2026-06-05-rendering-stills-to-png.md` (which covers the line-art/no-text case)

## The finding

Two facts, discovered making the first text-bearing tile (Husseiny quote):

1. **GitHub release assets are now egress-blocked.** `github.com` is allowlisted, but release downloads 302-redirect to `release-assets.githubusercontent.com`, which is not. Any "download the font zip from the project's GitHub releases" path fails with curl exit 56. Do not fight it.
2. **The route-around is npm.** `registry.npmjs.org` is allowlisted and the `@fontsource/*` packages carry the same SIL-OFL font files as woff2: `@fontsource/amiri`, `@fontsource/cormorant-garamond`, `@fontsource/jetbrains-mono` (Newsreader also exists as `@fontsource/newsreader`). `npm install` them anywhere, point CSS `@font-face` at the files with `file://` URLs.

## The render rule for text-bearing assets

- **No text / line-art only** → cairosvg (the 2026-06-05 method, unchanged).
- **Any real text, especially Arabic** → Playwright headless Chromium (`pip install playwright && python3 -m playwright install chromium` — works without `--with-deps`, which needs sudo and fails). Chromium shapes Arabic via HarfBuzz: guillemets mirror in RTL, lām/tāʾ marbūṭa shaping and diacritics come out right. cairosvg does NOT shape Arabic — it will silently produce disconnected letterforms. Never ship cairosvg-rendered Arabic text.
- **Verification is visual, always** — render, then look at the PNG (the 2026-06-05 "look at it" rule). Shaping errors are invisible to build logs and obvious to eyes.

## Why this matters beyond tiles

This unlocks every future text-bearing brand asset (quote tiles, OG/social cards, AR-first graphics) without a capability-gap slip like the 2026-06-03→05 grid delay. The fonts ARE the brand; now they render in the sandbox, both scripts.

— Designer / Web Developer · 2026-06-11
