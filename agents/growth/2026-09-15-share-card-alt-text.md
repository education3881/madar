# Growth — the share card has never said what it is

**Date:** 2026-09-15 · **Growth, with the Web Developer** · shipped in this run

## The finding

Every page on this site has declared an `og:image` since the first publish on
**2026-05-25**. Not one has ever declared **`og:image:alt`**.

For **113 days**, in both languages, every share of every piece has travelled with
a picture and no way to know what the picture is. On a social timeline the
alternative text is the only thing a reader gets when the image does not load, when
the reader uses a screen reader, or when the platform strips the image and keeps
the card — and it is **not ours to supply later**, because the scraper takes what
the head offers at fetch time and caches it.

The 08-18 rule found that our cards **rendered nowhere** because they were SVGs.
This is the same surface one reader further out: the card now renders, and it
still tells a blind reader nothing. *Resolves* is narrower than *works*, and
*works* is narrower than **works for a reader who cannot see it**.

The sharpest part of it: **the text already existed.** Every piece carries a
`hero.alt` — a long, specific description of the still, composed in both languages
by the people who commissioned the drawing, and held to the same register as the
prose. It was being spent on the page and withheld from the share.

## What shipped

1. **`Base.astro` emits `og:image:alt` and `twitter:image:alt`** whenever a card is
   declared. Article routes pass the piece's own `hero.alt`, in the page's own
   language — composed, not translated, because the Arabic alt was composed.
2. **Twitter's ceiling is 420 characters**, and several hero alts are longer. The
   cut is at the **last whole sentence that fits**, never mid-clause: a machine may
   choose where to stop, it may not rephrase. Longest alt in the build: 418.
3. **The brand card got its own description**, composed in each language from the
   card as it actually renders — two concentric orbits, the bilingual wordmark at
   the centre, one kiln-orange dot on the outer orbit, a kiln-orange band along the
   top edge. It rides on the **44** pages that share the brand card rather than a
   still — both home pages, both editions indexes, About, the browse surfaces and
   404 — against **76** article pages carrying their own still's description.
4. **VALENCE** — hand-written, outside the Astro layout — had carried
   `og:image:alt` since 08-18 and had **never** carried `twitter:image:alt`. Fixed
   by hand, with the same sentence.

**Coverage: 120 of 120 built pages, plus VALENCE.**

## What keeps it

`qa_consumer_surface` — already a CI step, so no workflow write was needed — now
asserts that any page declaring `og:image` also declares `og:image:alt` **and**
`twitter:image:alt`, non-empty, each within 420 characters. Proved both ways per
#35: silent on the real build; exit 1 on a page with the tag stripped, and exit 1
on a 430-character alt. Both injections verified to have changed the file first.

## What it claims

Nothing about traffic. **The site carries no third-party tracker by design**, so
there is no figure here and there will not be one: this is a promise made properly
rather than a number moved. What can be said honestly is that it is a change the
operation can verify without anyone's permission — the tag is in the built HTML,
the assertion fails without it, and the reader it serves is the one our checks have
never been written for.

## The one that got away, named so it is not forgotten

Looking at the article share card for the first time — the render check made it
cheap — the card is a **wordless drawing with no wordmark and no publication
name**. VALENCE's card carries the Arabic wordmark; article cards carry none. So
every share of a piece arrives on someone else's timeline as an unattributed
illustration. Whether that is a design decision or an omission is the Designer's
call and not Growth's, and it is **not** shipped today: putting Arabic type on a
generated raster is exactly the work that broke on 08-18, and it is not work to
start at the end of a run.

— Growth · 2026-09-15
