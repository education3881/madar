# Madār wordmark — usage

**File:** `madar-wordmark.svg`
**Status:** Placeholder v0.1. Drawn in-house by the design lead using free typeface stand-ins (Cormorant Garamond + Amiri). To be replaced by a commissioned mark from a type designer (Sectra-family Latin + Naskh Arabic, macron set as a heavy slab). Until then, this file ships.

---

## Minimum size

The mark must not appear below **24px tall** on screen (mobile header) and not below **8mm** in print (spine, slipcase, business card). Below those thresholds, the macron slab over the *ā* and the alif madda slab over the م-ا lose their weight and the bilingual balance collapses. Maximum size is uncapped — the mark has been redrafted to hold at 240px+ for the About page and at editorial cover sizes (400mm+) without breakage.

## Clear space

The mark sits inside an invisible rectangle whose padding on all four sides equals **the height of the macron slab** (≈ 0.05× the mark's own height). No other typographic element — no tagline, no kicker, no rule, no menu item — may enter that rectangle. The masthead's ticked rule under the mark sits *outside* this clear space; it is part of the masthead, not part of the wordmark.

## Dark mode

The wordmark ink is drawn with `fill="currentColor"`, so the mark inherits whichever ink colour the surrounding context provides. In a light page (`color: var(--ink)` on `background: var(--paper)`), the mark reads as `--ink`. In a dark mode page (`color: var(--paper)` on a dark `--ink` ground), the mark inverts to paper. The mark never carries its own colour — context decides.

## Bilingual pages

On every Madār surface — web, print, social, email — both scripts always appear together. Latin first, Arabic second, joined by the hairline divider; neither script is ever shown without the other. The two are sized to hold **equal optical weight**, not equal cap-height. If a layout demands a script-stacked variant (e.g., a narrow vertical sidebar), the Arabic sits *under* the Latin with the same hairline as a horizontal rule between them — but the bilingual pairing remains intact.

## What not to do

Do not lock the wordmark to a tagline ("Madār — a research instrument") in the mark itself; the tagline lives in the masthead, never welded to the mark. Do not place the wordmark on photography without a backing wash of `--paper` at full opacity; the mark needs the page's quiet to read. Do not recolour the mark to anything other than `--ink` or `--paper` — never orange, never sage, never gradient. Do not animate the wordmark; the macron is a slab, not a motion. Do not stretch the SVG non-proportionally; the bilingual optical balance is calibrated and will break under skew.
