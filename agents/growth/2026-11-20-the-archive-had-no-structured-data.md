# Growth — the archive served 45 links each and told a machine nothing

**2026-11-20.** One concrete audience action: **both editions pages now carry structured data, and until
this morning they carried none at all.**

## What was measured first

Enumerated over the 139 served documents: **46 pages serve at least one article link**, 336 article links
in total. Of those 46, **42 carry a `CollectionPage` with an `ItemList`** — every browse facet, including
facets listing **two** pieces, which have had one since 2026-10-20.

**Four did not.** Two of them are the editions pages:

| Page | Article links it serves | JSON-LD it emitted |
|---|---|---|
| `editions/` | **45** | **none at all** |
| `ar/editions/` | **45** | **none at all** |
| `/` | 6 | `Organization`, `WebSite` |
| `ar/` | 6 | `Organization`, `WebSite` |

**The archive is the one surface on this site that lists the whole corpus, and it was the only listing
page a machine could read nothing from.** Not a missing `ItemList` — *nothing*: no `CollectionPage`, no
`BreadcrumbList`, and not even the `Organization` and `WebSite` nodes that every other page we serve
carries, because neither template passed `jsonLd` to `Base.astro` and `Base.astro` correctly emits
nothing when it is handed nothing.

**And this page was repaired two days ago.** Standing-queue item 76 closed on 2026-11-18 on its last four
pages, and two of the four were these: *`/editions/` served the English home's description and
`/ar/editions/` served the Arabic home's.* A run read this page's `<head>`, found the one sentence in it
wrong, derived a correct one and shipped it — **and nothing in that reading asked whether the page emitted
any structured data at all.** A sweep is scoped to the field it enumerates (2026-08-16), and a
`<meta name="description">` audit enumerates descriptions.

## What shipped

`collectionJsonLd()` already existed and already supplied its own referents (the 2026-10-21 fix: *the
function that writes the pointer is the only place that cannot forget the node it points at*). It needed
two optional parameters, both of which exist to stop this page asserting something untrue:

- **`hub`** — the trail's middle crumb. It was hardcoded to Browse, and **the archive is not under
  Browse.** The function's own header says a crumb to the wrong parent is worse than no crumb, so the
  editions pages pass themselves and the trail is root → Editions.
- **`order`, with `null` meaning OMIT.** The helper hardcoded `itemListOrder: ItemListOrderDescending`,
  which is true of every browse facet — one list, one key, newest first — and **false of the archive**,
  whose order is edition-grouped and then date-ordered inside each group. Schema.org offers ascending,
  descending and unordered, and none of the three is honest here. An `ItemList` whose members carry
  explicit `position` values is well defined without the property, so the archive **omits** it.
  *This is yesterday's defect one property over: a field that resolves, parses and says the wrong thing
  cannot fail, so nothing we own would ever have told us.* The temptation was to take the default because
  it was already written; the cost of taking it would have been a false claim about ordering on the
  publication's deepest index.

**Served, before → after:**

| | before | after |
|---|---|---|
| JSON-LD nodes on `editions/` | **0** | 4 — `Organization`, `WebSite`, `CollectionPage`, `BreadcrumbList` |
| JSON-LD nodes on `ar/editions/` | **0** | 4 |
| `ItemList` members | **0** | **46 on each page** — 45 pieces in render order plus the standing instrument |
| Listing pages serving article links with no list structure | **4 of 46** | **2 of 46** |
| Distinct `@id` across the corpus | 398 | **404** |

The list is **derived from the same arrays the page renders, in the same order** (2026-06-07), so it
cannot drift: editions in render order with their own sorted pieces, then the singles, then VALENCE. The
Arabic list carries the **Arabic** titles, because the list describes *that* page.

`qa_jsonld` CLEAN at 138 pages. `qa_composition` CLEAN at 139 documents, 404 distinct `@id`, two described
on more than one page and none disagreeing. `npm run build` exit 0, all 28 postbuild gates and all 12
build-job gates green.

## Measured and NOT acted on, with the reason

- **The two home pages**, 6 article links each and no `ItemList`. They are a different judgment from the
  archive: a home is already the `WebSite` node's own subject, and whether the six pieces it leads with
  are a *list* or a *selection* is an editorial call about what the home claims to be, not a builder's.
  Raised as standing-queue item **141** rather than decided here.
- **`about` is one `Place` and one piece declares five countries.** `2026-09-14-africa-best-system-ruler`
  carries `countries: [Mauritius, Senegal, Niger, Benin, South Africa]` and its JSON-LD tells a machine
  about **Mauritius alone** — 4 country claims on 1 page of 45 that are served in the body and invisible
  to a reader that parses. It is 1 piece and it is also the exact shape of yesterday's finding (a field
  that is *right* and does not carry what the page knows), so it is raised as item **142** and not
  smuggled into a commit about the archive.

## No traffic number

The site carries no third-party tracker, no analytics and no automatic third-party request by design, so
there is no visitor figure here and none is estimated. Every number above is counted from our own served
bytes.
