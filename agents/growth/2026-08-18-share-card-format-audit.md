# Growth audit — the share card that was never there

**Date:** 2026-08-18 · **Growth → Manager (Web Developer + Designer briefed inline)** · **Status: FIXED IN-RUN**
**Prompted by:** yesterday's forward question — *the sweeps check that a link resolves and that a page is reachable; neither checks that the thing at the other end is usable by the consumer that fetches it.*

---

## The finding

Every Madār article, in both languages, has declared an `og:image` since the first publish on 2026-05-25. The value was the article's hero still — **an SVG**.

- The file exists.
- The URL is absolute (fixed by an earlier Growth audit precisely so scrapers could resolve it).
- It resolved on every QA pass we have ever run.
- **It renders on no major social consumer.** Facebook, X, LinkedIn and Slack accept PNG, JPEG, WEBP and GIF. None accepts SVG.

So for **83 days**, every share of every piece — 76 article pages — travelled as a bare title-and-description with **no card image**, while the QA log recorded the image as present and resolving. The pages additionally declared `twitter:card = summary_large_image`: a promise of a large image, kept with nothing.

**Why this is a growth finding and not only a QA one.** The card is the entire visual surface of a link outside our own site. Madār's distribution plan is Substack plus a small, deliberate engagement list — i.e. **links pasted into other people's feeds**. The one asset that had to work in someone else's product was the one asset never tested there. Our stills are the best thing we make; they have never once been seen by a reader who did not already visit the site.

---

## The fix

| Item | Detail |
|---|---|
| Cards rendered | **38** PNGs, one per still, at `public/og/` |
| Size | **1200×600**, native 2:1 — no crop, no padding bars |
| Weight | **452 KB total, ~10 KB each** (line art) |
| Renderer | sharp / librsvg 2.61 (density 144, `#FAFAF7` flatten, palette PNG) |
| Wiring | both article routes derive `/stills/x.svg` → `/og/x.png`; reason written into the source comment |
| Verification | Arabic shaping checked **by looking at the PNG** (harfbuzz + fribidi present; سكون renders joined) |
| New assertion | **no `og:image` may end in `.svg`** — runs every QA pass. This run: 39 og URLs, 0 SVG, 0 unresolved |

**Why 1200×600 and not 1200×630.** X crops `summary_large_image` to 2:1 regardless; Facebook's 1.91:1 recommendation tolerates 2:1. Padding to 630 put visible paper bars across the stills with a sand ground. Native 2:1 needs neither a crop nor a bar.

**VALENCE's card, also shipped** — the item flagged yesterday as the highest-leverage one left. A bespoke line-art still in the house palette (a lattice of elements; one bond in kiln orange), rendered to PNG and wired into the VALENCE head with dimensions, alt text and `twitter:image`. One defect caught by inspecting the render: `letter-spacing` broke the Arabic wordmark's joins (مدار → م د ا ر). Tracking is never applied to Arabic — re-rendered, re-inspected at 3× zoom.

---

## What this does not fix

- **Placement and the Arabic question for VALENCE** stay with the founder. A card makes a share legible; it does not decide where the instrument sits in the chrome, or whether it gets an Arabic edition, an Arabic entry point, or an explicit English-only note.
- **Nothing is retroactive.** Links already shared stay cardless in the caches that hold them; the scrapers re-fetch on next share.
- **Discoverability is still the open wound.** A web search for the publication by name and URL this morning surfaced nothing of ours. That is what an unindexed site on a borrowed path looks like, and it is the standing argument for the two decisions that have been waiting since June: **the custom domain** (memo 12 June — every day binds more URLs to the GitHub Pages path) and **Substack** (until it exists, Growth is preparation, not operation).

## Standing lesson

**A promise in the metadata is a promise to a machine we do not own.** Verifying it means checking against *that machine's* accepted formats, not against our own filesystem. The next surface with the same shape is the **feeds**: both are well-formed and carry 38 items, and nothing has ever checked that an item renders legibly in a reader, that Arabic items carry their direction, or that links resolve from outside our origin.

— Growth · 2026-08-18
