# Ruling #36 — a promise must be *derived* from the thing it promises, never declared beside it

**Filed:** 2026-08-26 · **Family:** method / repair-class (sits after #16 and #35) · **Occasion:** the five non-article pages had promised a large share card and shipped none for 93 days, and the 2026-08-18 fix for exactly this defect had not prevented it.

---

## The rule

When markup makes a **claim about an asset** — "a large image follows", "an Arabic document is at the other end of this link", "this page was modified on this date" — the claim must be **computed from the asset**, in the same expression, so that the two cannot be separately true. A claim written as its own literal beside the asset is a claim that will eventually outlive it.

**Corollary — the repair class matters more than the repair.** There are always two fixes available for a broken promise: *supply the missing thing*, or *make the promise underivable without it*. The first fixes today's instance. Only the second fixes the class. Prefer the second, and when you take the first, take the second in the same commit.

## Origin case

`Base.astro` emitted `<meta name="twitter:card" content="summary_large_image">` **unconditionally**, while `og:image` was emitted **conditionally**, `{ogImageAbs && …}`. Two adjacent lines, one guarded and one not, describing the same asset. The consequence: `/`, `/ar/`, `/editions/`, `/ar/editions/` and `/about/` — including **both front doors, the URLs a reader is most likely to actually share** — promised every scraper a large card and gave it nothing, from the first publish on **25 May** until today.

This is the **2026-08-18 defect in a second costume**. That day found that every `og:image` was an SVG, which no social consumer renders, and fixed it by generating 38 raster cards. The fix was correct and it did not prevent this, because it enumerated **articles**, and every article has an image. Sixth statement of *a green check is scoped to what it enumerates* — and the first where the previous member of the family was itself the thing that failed to generalise.

The reason it lasted 93 days is worth naming: `twitter:card` **reads as configuration**, not as an assertion. It looks like a setting for how the site presents itself. It is in fact a per-page factual claim, and every per-page factual claim needs the page's own data behind it.

## Applied today

- `twitter:card` is now `{ogImageAbs ? 'summary_large_image' : 'summary'}` — **derived**. A page without a card can no longer promise one, whatever anybody writes in a template later. `summary` is honest and still renders.
- The five pages were given a card (`/og/brand-card.png`), so the derived value is `summary_large_image` everywhere today — but the guard, not the asset, is the fix of record.
- `qa_consumer_surface` gains two assertions: **every served page has an `og:image`**, and **`twitter:card` and `og:image` agree in both directions** (a card promised with no image, *and* an image shipped under a `summary` card, are both defects — the second wastes an asset we drew).
- Proved both ways per **#35**: against the pre-fix `dist` it reports **10 defects across exactly the 5 known-broken pages**, and is **silent on all 77 pages already known to be correct**. The control held on the first attempt because the control was chosen before the run.

## The card, and a second-order note on #16

The card is drawn **with zero live text**. The first version set a strapline in Newsreader and Amiri; the rasteriser has neither font installed, so the Arabic came out in a fallback sans and the English strapline ran off the right edge. **A share card's judging environment is the flat PNG** — there is no second chance to fall back, because the consumer never sees the SVG. So the card carries only the wordmark, which is real Newsreader + Amiri outlines extracted to paths and therefore pixel-identical in every renderer, on the brand's own orbit motif. *Found by looking at the output*, which remains the cheapest check we own.

## Why it compounds

Every future addition to `<head>` is a claim about something. The rule turns a recurring judgement ("is this tag still true?") into a structural property ("this tag cannot be false"), and it applies well beyond Open Graph: `hreflang` pairs, feed `enclosure`s, `lastmod`, JSON-LD `citation`. Sits with **#16** (verify in the judging environment) and **#35** (prove against a control) as the third member of the *how to trust your own checks* family — #16 governs where you test, #35 governs what you test against, and #36 governs what you should have to test at all.
