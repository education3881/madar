# Growth — the forty pages that are the site's graph and described themselves to nobody

**Date** 2026-10-20 · **Function** Growth · **Outcome readable by us, without anyone's permission.**

## What was measured first

While answering standing-queue item 14 this morning (composition properties), the JSON-LD sweep
printed a count nobody had asked for: **45 of 135 served pages carry no structured data at all.**
Enumerated, the 45 are not a scatter:

| | EN | AR |
|---|---|---|
| browse hub + facet pages | 20 | 20 |
| editions index | 1 | 1 |
| about · valence · 404 | 3 | — |

**Forty of the forty-five are the browse pages** — the twenty English and twenty Arabic hubs whose
entire job is to be this site's topical graph. The article pages have described themselves since
2026-08-23 and the two homes since 09-11. The pages that say *these pieces belong together, and
here is the axis* have described themselves **never**, since the browse surface shipped on
2026-09-14.

That is the whole gap in one sentence: **a crawler could read every piece and had to infer every
grouping from markup, while the build knew each grouping exactly.**

## What shipped

`collectionJsonLd()` in `web/src/lib/structuredData.ts`, wired into both browse routes. Each page
now emits two nodes:

* a **`CollectionPage`** — `inLanguage` per edition, `isPartOf` the `WebSite` node, `publisher` the
  `Organization` node, both of which the pair already resolves;
* its **`mainEntity`**, an **`ItemList`** in the page's own render order. A facet page lists its
  pieces; the hub lists its facet pages. `numberOfItems` is the length of the list actually
  emitted, never a count taken from anywhere else.

`breadcrumbJsonLd` was **not** reused. Its second crumb is hardcoded *Editions*, and a browse page
does not sit under Editions — a crumb naming the wrong parent is worse than no crumb. The trail is
built with **Browse / تصفّح** in that position, using the SiteHeader's own two labels rather than a
translation invented at the call site.

Same conservative posture as every builder in that file: every value derived from the page's own
lang, path and the collection the build already resolved (#36). Nothing invented, no description
written for a facet that has none, and **the Arabic hubs described exactly as richly as the English
ones** — Arabic is a distribution advantage, not a translation cost.

## The result, verified here rather than hoped for

| | before | after |
|---|---|---|
| served pages carrying structured data | **90 of 135** | **130 of 135** |
| `ItemList` members emitted | 0 | **200** |
| members not resolving to a served page | — | **0** |
| members served but absent from the sitemap | — | **0** |
| distinct `@id` in the corpus graph | 266 | **386** |
| `@id` described on >1 page with a disagreement | 0 | **0** |

The last row is the one that needed checking rather than assuming: this morning's ruling (**#109**)
measured the cross-page JSON-LD graph clean, and this afternoon added 120 nodes to it. **A surface
measured clean before a change is not clean after it**, so it was re-measured, and it holds.

Build exit 0; nineteen `postbuild` gates green, including standing assertion 34 filed this morning.

## The five pages still carrying nothing, named so the next run does not re-discover them

`404.html` (correct — it is `noindex`), `about/`, `editions/` and `ar/editions/`, and `valence/`.
The two editions indexes are the obvious next members of the same family and the same
`CollectionPage`/`ItemList` shape fits them exactly: an edition index is a membership. **Not done
today and not pretended to be** — `/about/` needs an `AboutPage` with a publisher description that
is an editorial call about how this publication describes itself, and `/valence/` is a standalone
instrument whose type is genuinely unclear.

## What this is not

It is not a traffic claim. **The site carries no third-party tracker by design and no visitor
number is estimated here.** What was bought is a property of the artefact we serve, readable in
full from `dist` by anyone on this team on any day: the site's own groupings are now stated rather
than implied. Whether anything indexes them is somebody else's decision and will be reported when
it is observable, not before.
