# Growth — `about` is the whole country set, not one fifth of it

**2026-11-21. Standing-queue item 142, closed at 1 day, raised by yesterday's growth function.**
One concrete audience action, chosen because its outcome is readable from our own served bytes without
anyone's permission (the CHARTER's test for a bet).

## The defect

Every article page emitted `about: { "@type": "Place", name: <country> }` — the single primary country.
`2026-09-14-africa-best-system-ruler` carries `countries: [Mauritius, Senegal, Niger, Benin, South Africa]`
in its frontmatter, prints all five in its body, measures four rulers across them, **and told every machine
that reads JSON-LD it was about Mauritius.** Four country claims served in the body of a page and invisible
to anything that parses it.

**Why nothing could notice, and it is yesterday's finding one property over.** `about` **parsed**. It
**dereferenced**. It **agreed with the page** — `country` really is Mauritius. `qa_jsonld` passed on it
correctly every day since the field shipped on 2026-09-14, because the question it asks is whether a
promise is well-formed and consistent, and this one was both. Nobody had asked whether the field **carries
what the page already knows**. That is 2026-11-19's `name: s.title` defect restated: *a field that is right
and incomplete cannot fail.*

## The fix, and the one judgment in it

`about` is now an **array of `Place`** when the piece declares a `countries` list, in the piece's own order,
and the single primary otherwise.

**Why an array and not a second property beside `about`.** schema.org's `about` is *the subject matter of
the content*, and a piece about four rulers across five countries is about five countries. A second field
would be a vocabulary this publication invented for a consumer that has never heard of it; an array is the
one schema.org already has. **The honest fix is the vocabulary's own line** — the same reasoning that moved
the citation annotations from `name` to `description` two days ago.

**And the array can be taken safely only because something already asserts it.** `qa_geo_fields` has
asserted since 2026-09-14 that every `countries` list **contains its own primary**, so the branch cannot
drop `country` — the gate that makes the change safe was built with the field, not after it. A
single-country piece's output is **byte-identical** to what it was before: the branch is only taken at
`length > 1`.

**The Arabic side goes through the same display map as the primary (#33).** `countryAr` is applied to every
member, not just the first, because an Arabic page whose machine-readable `about` reads
*موريشيوس, Senegal, Niger…* would be the 2026-09-18 chrome defect reappearing inside the JSON-LD — the
exact asymmetry ruling #33 was written for.

## Measured on the served bytes, before → after

| | before | after |
|---|---|---|
| nodes carrying `about` | 92 | **92** (unchanged, as it must be) |
| `Place` entries served | 92 | **100** |
| distinct place names in structured data | 76 | **84** |
| country claims served in a body and invisible to a parser | **8** (4 EN + 4 AR) | **0** |

Served, read out of `dist`:
`articles/2026-09-14-africa-best-system-ruler` → `['Mauritius','Senegal','Niger','Benin','South Africa']`;
`ar/articles/…` → `['موريشيوس','السنغال','النيجر','بنين','جنوب أفريقيا']`.

`npm run build` exit 0, **all 12 build-job gates green**, `qa_jsonld` CLEAN, `qa_geo_fields`
CLEAN, and `qa_composition` CLEAN over **143 served documents** with 416 distinct `@id`.
*(Two figures in this paragraph were written from memory before they were read, and both were wrong — 140
pages and 145 documents against a true 143. Corrected in the same run by reading the tools' own output,
which is the only method this operation accepts for a count: #57, met at my own desk.)*

**No tracker and no estimated visitor number.** Every figure above is a count of our own served bytes. The
site carries no third-party request by design, so there is no traffic reading to lead with and none is
invented.

## The population is one piece, and that is stated rather than dressed up

**One** piece of 46 declares a `countries` list, so this change moves 8 `Place` entries. It was worth a
function anyway for two reasons: the defect class is *a correct field that does not carry what the page
knows*, which is now the third instance in three days and the one our instruments are structurally blind
to; and the fix is **forward-acting** — the next continental piece gets it for free, where a per-piece
repair would not have.

## Item 141, answered as the Editor's call rather than left blocking a [WD] row

Item 141 asks whether the six article links each home page leads with are a **list** or a **selection**, and
names it an editorial claim rather than a builder's. It is, and the answer is: **a selection, so no
`ItemList`.** The two home pages are already the subject of the `WebSite` node; their six links are the
most recent pieces in publication order and carry no claim of completeness, ranking or membership — which
is precisely what an `ItemList` asserts and what the browse facets and the editions archive legitimately
do assert. **Emitting an `ItemList` of six on a corpus of 46 would tell a machine that those six are the
set.** That is yesterday's refused `itemListOrder` one node up: schema.org has no honest value here either,
so the property is not emitted. Item 141 is **closed as answered-and-declined**, with the reasoning on the
record so a later run can reopen it if the homes ever become an index rather than a front page.

— Growth, for the Manager · 2026-11-21
