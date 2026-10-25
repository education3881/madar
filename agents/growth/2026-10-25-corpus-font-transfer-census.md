# Growth — the first corpus-wide transfer-weight census, and the twelve pages the gate could not see

**2026-10-25.** Growth action: **a metrics read**, of a quantity this publication has never once
measured and can read without anyone's permission. No tracker, no third party, no estimate — the
census loads all 134 served pages in headless Chrome against a logging server and records what the
browser actually asked for. *(The site carries no third-party tracker by design; this is a
measurement of what we serve, not of who reads it.)*

Licensed by the morning's instrument: `qa_font_payload` (standing assertion 39, ruling #115) proved
the method on six pages, so extending it to 134 is a read rather than a new build.

## The census

| | pages | min | median | max | corpus total |
|---|---|---|---|---|---|
| EN | 68 | 0 | 521,408 | 658,196 | 35.6 MB |
| AR | 66 | 261,808 | 295,628 | 415,896 | 19.8 MB |
| all | 134 | 0 | 487,672 | 658,196 | **55.3 MB** |

**The Arabic edition is 44% lighter per page than the English one** (295,628 against 521,408 at the
median), which is the opposite of the shape anyone would guess for the edition with the larger
script — and the reason is that the English pages carry four Latin faces in two styles while the
Arabic pages carry one Arabic text face.

`/madar/valence/` fetches **0** font files; it is the standalone instrument and self-contained.

### What costs the most, across the corpus rather than per page

| transferred across 134 pages | pages × size | file |
|---|---|---|
| **14,438,480** | 133 × 108,560 | `amiri-normal-400-arabic.woff2` |
| 9,987,296 | 68 × 146,872 | `newsreader-italic-400-500var-latin.woff2` |
| 8,844,000 | 67 × 132,000 | `newsreader-normal-400-600var-latin.woff2` |
| 5,006,120 | 133 × 37,640 | `cormorant-garamond-normal-400-600var-latin.woff2` |
| 3,845,904 | 114 × 33,736 | `cormorant-garamond-normal-400-600var-latin-ext.woff2` |

**The single largest transfer cost in this publication is the Arabic face on English pages.**
`amiri-normal-400-arabic.woff2` is fetched by **133 of 134 pages — every English one included** —
because the footer prints `مدار` and the English article pages carry a cross-edition teaser in
Arabic. 108,560 bytes, 14.4 MB across the corpus, and on an English article it paints **89
characters**. That is the bilingual chrome's price, stated for the first time. It is a design
property of this publication and is **not** proposed for removal here; it is handed to item 20's
Designer half with a number, which is the thing that half has never had.

Second: **Newsreader Italic at 146,872 bytes reaches every English page and paints 196 characters on
an article** — 28.2% of that page's payload for the dek and one footer line.

And the subsets nobody would guess are live: `newsreader-normal-400-600var-vietnamese.woff2` and
`jetbrains-mono-...-vietnamese.woff2` are each fetched by **exactly one page** — the Vietnam piece.
The Vietnamese carve is not dead weight; it is doing precisely the job it was carved for.

## The finding, and it is about the morning's own gate

The first census was run on the build that already carried the morning's fix, and
`amiri-italic-400-arabic.woff2` **was still being fetched by twelve pages.**

All twelve are Arabic article pages. The cause is one line in the **Arabic article template** —
`.body-main :global(em) { font-style: italic }` — which outranks `global.css`'s `[dir="rtl"] em` at
equal specificity because an Astro-scoped selector carries the component's own
`data-astro-cid` attribute. On `2026-05-28-iraq-mosul-library` it slants **686 characters of quoted
Arabic across six passages**; the page was paying 131,100 bytes for it. And three lines below, the
same file already knew: `p > em:only-child` has reset to `normal` since it was written. **The
template contained both the fact and its contradiction.**

Fixed in the Arabic template rather than by raising specificity from `global.css`, because a
correctness constraint about a script should not have to win a cascade fight with a component's
typographic preference. Measured after: **the Arabic corpus total falls 21,349,860 → 19,776,660,
exactly 12 × 131,100 = 1,573,200 bytes, −7.4%.**

**This is the gate's own stated limitation arriving on day one.** `qa_font_payload`'s header says its
six-page set is a sample and that a defect living only outside it is outside the gate. It said so as
a caveat; twelve hours later it was a measurement. *A sampled gate is not a weaker gate — it is a
gate with a population it has not been shown.*

## One honest caution about every number above

**The payload total is not deterministic.** Three runs of the same probe against the same unchanged
page returned **703,556 / 669,820 / 669,820**; three runs of the gate against one unchanged `dist`
returned `EN article = 487,672 / 487,672 / 521,408`. A `unicode-range` fetch is issued when the
engine reaches a glyph it needs, and whether it does so before the time budget expires is a race.
So the EN corpus total moving **+70,040** between the two censuses, on builds that differ only in an
Arabic template, is **noise and is named as noise** rather than smoothed into a trend. The AR delta
is not: it is exactly twelve times the per-page figure.

This is also the empirical reason a byte ceiling must not be asserted, which is stronger than the
reason the ruling first gave: *assert the shape, print the size.* The two asserted limbs returned the
same verdict on three consecutive runs; the measurement did not.

## Return rate

Unchanged and unmeasurable by design — no tracker, nothing to report, and no estimate offered. What
this read gives the operation instead is a **reader-cost** baseline it can take again any day
without asking anyone: 55.3 MB of webfont across 134 pages, down 1.57 MB today on the Arabic side
alone, with the two largest remaining reductions named and owned.
