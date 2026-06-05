# Guidebook — rendering stills and tiles to PNG (deterministic, no browser)

**Banked:** 2026-06-05
**Why this exists:** The IG opening-grid tiles were "on deck" for two runs because image *rendering* read as a capability gap (weekly signal, 2026-06-04). It is not a gap — it is a one-time method. This is that method, so no Designer task slips again for "we can't render PNGs."

---

## The method

Our stills are SVG (`viewBox 1200×600`) and almost always **pure line-art with no `<text>` and no font dependency** — verify with `grep -c '<text' file.svg` (expect 0). When that holds, no headless browser is needed; `cairosvg` renders them exactly. The wordmark (`/design-assets/wordmark/madar-wordmark.svg`) is **path-based** (outlines extracted from Newsreader + Amiri), so it too renders with no fonts installed.

### Setup (sandbox)
```
pip install cairosvg pillow --break-system-packages
```

### Still → 1080×1080 IG tile (pad, never crop)
The stills are 2:1; the grid wants 1:1. The brief's rule is **pad with paper, don't scale to bleed.** Render the still at 1080×540, composite centred on a 1080×1080 `#FAFAF7` canvas:
```python
import cairosvg, io
from PIL import Image
PAPER = (250, 250, 247)  # #FAFAF7
png = cairosvg.svg2png(url=svg_path, output_width=1080, output_height=540,
                       background_color="#FAFAF7")
still = Image.open(io.BytesIO(png)).convert("RGBA")
canvas = Image.new("RGBA", (1080, 1080), PAPER + (255,))
canvas.alpha_composite(still, (0, (1080 - still.height)//2))
canvas.convert("RGB").save(out_path, "PNG")
```

### Net-new tiles (wordmark, divider)
Build a 1080×1080 wrapper SVG: a paper `<rect>` plus either the wordmark inner markup nested in a sized `<svg>` (preserve its `viewBox 0 0 520 120`, place at ~60% width), or pure geometry for the divider (hairline `<line>` at `#0E1B2C` opacity 0.18 + an orange `#D94F2A` slab). Render with `cairosvg.svg2png(bytestring=...)`.

## Verification step (do not skip)
Composite the outputs into a 3×3 contact sheet and **look at it** before sign-off — fidelity, centring, and grid coherence are visual properties a build log can't confirm.

## When this method does NOT apply
If a still ever contains real `<text>` with brand fonts (Cormorant Garamond / Newsreader / Amiri), `cairosvg` will fall back to a default serif. In that case either (a) outline the text to paths first, or (b) render via a headless browser that can load the web fonts. For the current catalogue, every still is line-art, so (a)/(b) are not needed.

## Palette constants (canonical)
`paper #FAFAF7 · ink #0E1B2C · orange #D94F2A · sage #7A8471 · sand #E8E2D0`

— Designer / Web Developer · 2026-06-05
