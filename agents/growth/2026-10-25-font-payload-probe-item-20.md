# Item 20, taken from the head — what a reader actually downloads, measured by probe

**2026-10-25.** Queue head: **item 20**, *Four webfont families and 521,408 bytes on an ENGLISH
article*, 8 days, seven displacements. It tied with **item 21** on both clocks — same 8 days, same
seven displacements — so for the second time the 10-05 tiebreak did not select, the 10-11 narrowing
did not select either, and the **10-16 fourth level** decided it: both rows were raised by the same
commit (`330b936`, the 10-17 daily), and item numbers are assigned in raise order, so 20 goes first.

## The instrument, and why it is a probe rather than a reading

Item 20's own row names the proof it wanted: *a server-log probe with nothing injected into the page.*
That is the right shape, because **a woff2 file is not served by the build — it is fetched by a
browser, and only when that browser must paint a glyph out of it.** Nothing the operation owns can
see that. All thirty-eight standing assertions read bytes that exist in `dist` or in the repository.
The bytes a reader actually pays are a product of the page, the font stack, the `unicode-range` carve
and the text that is actually painted — a quantity that exists only at render time and that this
operation has never once measured.

`/tmp/fontprobe/probe.py` serves `web/dist` under `/madar/` on an ephemeral port behind a logging
handler, drives headless Chrome at one URL at a time, and records every `/fonts/*.woff2` the browser
asked for. Nothing is injected. **Control: it reproduced item 20's own median to the byte** —
521,408 on `2026-07-04-kenya-cbe-grade10-pathways` — by a different method from the one that produced
it, which is the only reason the numbers below are worth reading.

A second probe (`who.py` / `italic.py`) answers the cost side: injected into a **copy** of `dist`, it
walks every text node and reports the computed family, style and painted character count out of the
layout engine. The injection is asserted to have changed the file before Chrome is pointed at it
(#35, and the 09-14 trap).

## What the four pages fetch, before any change

| page | font bytes fetched | files |
|---|---|---|
| EN home | **778,376** | 12 |
| AR home | **426,728** | 9 |
| EN article (Kenya) | **521,408** | 8 |
| AR article (Kenya) | **295,628** | 7 |

And the painted-character denominators, which is the half nobody had:

| page | face | bytes | painted chars | bytes per char |
|---|---|---|---|---|
| EN home | Amiri **italic** (Arabic) | 111,720 | **29** | 3,852 |
| AR home | Amiri **italic** (Arabic) | 111,720 | **29** | 3,852 |
| AR home | Cormorant Garamond (latin + latin-ext) | 71,376 | **5** | 14,275 |
| EN article | Newsreader italic (latin) | 146,872 | 196 | 749 |
| EN article | Amiri normal (Arabic) | 108,560 | 92 | 1,180 |

The third row is **item 20's own handed-over datum reproduced independently** — *71,376 bytes to
render the single word `Madār` in the footer* — and the probe adds the denominator the row did not
have: five characters.

## The defect, and it is not the one the item specified

The item names two reductions and declares both out of reach: **subset to the corpus's glyph
inventory** (needs `fonttools` + `brotli`) and **drop a family** (a Designer judgment). Neither was
taken, and the second is still a Designer judgment. But the first is declined on a stated ground that
**is false about the thing it names**: the row says subsetting breaks *"a byte-for-byte mirror of the
response it replaced, which is the property `qa_third_party_origins` and the whole 10-08 design rest
on."* `qa_third_party_origins` asserts **one** thing — that no page fetches automatically from an
origin we do not own. It contains no hash, no byte comparison and no claim about Google's response.
The mirror property is a design choice recorded in `build_font_bundle.py`'s own header, for a
different and better reason (not collapsing the `unicode-range` carve), and no gate holds it. *This
is item 26's question — which check's stated reason for not asserting something has quietly become
false? — pointed at a queue item's reason for not acting.*

*(The real objection to the subset is the one neither the item nor the gate states: a subset computed
over today's 44 pieces is correct the day it is written and silently wrong the next time an article
prints a glyph it does not contain, and the failure mode is a fallback nobody sees. That is the
2026-06-07 rule verbatim — generated artefacts that must mirror the article set are build-generated,
never hand-maintained. It stays declined, on that ground instead.)*

What the measurement found is a third reduction the specification does not contain, and it is the
largest single one available on the Arabic side:

**Two `<em>` tags inside the about paragraph were slanting Arabic.** `قراءاتٍ مختاَرة` and
`تقاريرَ ميدانيّة` — 29 characters, on both home pages — resolved to `Amiri Italic`, a real slanted
Arabic face in the bundle, and so the browser fetched `amiri-italic-400-arabic.woff2` (111,720) plus
`amiri-italic-400-latin.woff2` (19,380) to paint them.

Arabic typography has no italic convention. **This stylesheet already said so, twice** — at
`[dir="rtl"] .pullquote { font-style: normal }`, and again in `SiteFooter.astro` on **2026-10-17**,
the very day item 20 was raised, for the Arabic strapline that was *"being set in Newsreader Italic —
a Latin-only face — so it rendered from the system serif while the browser fetched 146,872 bytes to
draw none of it."* Both were written per component. **Neither reached the `<em>` in the about
paragraph, which had slanted Arabic on both home pages since they were written.**

## The fix, and what it bought

One rule in `global.css`, in the block where the other `[dir="rtl"]` rules live:

```css
[dir="rtl"] em,
[dir="rtl"] i,
[dir="rtl"] cite { font-style: normal; }
```

Re-probed on the rebuilt `dist`, same instrument, same four URLs:

| page | before | after | delta |
|---|---|---|---|
| EN home | 778,376 | **647,276** | **−131,100 (−16.8%)** |
| AR home | 426,728 | **295,628** | **−131,100 (−30.7%)** |

**The Arabic home page lost 30.7% of its font payload to a two-line CSS rule**, and the two files
that disappeared are exactly the two the probe attributed to the 29 characters. The Arabic home was
rendered at 1280 × 2400 in headless Chrome and looked at: the about paragraph is upright throughout,
Arabic shaped and joined, nothing else moved.

## What is handed over rather than taken

1. **The emphasis cue.** Resetting the slant follows the house's own two precedents exactly — both
   reset and neither substituted anything — but it does mean the Arabic edition now carries no visual
   mark where the English carries italic. What replaces italic emphasis in Arabic is a Designer
   judgment and is **not** this lane's to make, so it is queued rather than invented.
2. **Newsreader italic, 146,872 bytes for 196 painted characters on an English article** — 28.2% of
   that page. Legitimate typography (the dek is italic by design), now with a number against it.
3. **The remaining two reductions item 20 named** are still open and still owned by **[WD] + Designer**.

## The structural finding

Eight days apart, in one lane, two defects of the same class were found by hand: a face fetched to
paint **nothing** (10-17, 146,872 bytes) and a face fetched to paint **twenty-nine characters in a
style the script does not have** (today, 131,100 bytes). Both are invisible to every instrument this
operation owns, because every one of them reads a byte that exists rather than a byte that is
requested. That gap is what **standing assertion 39** closes, and the ruling is **#115**.
