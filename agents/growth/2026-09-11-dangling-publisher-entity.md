# Growth — the publication had no machine-readable identity, and every article credited a pointer to nothing

**Growth + Web Developer · 2026-09-11**
**Action of the day.** Cost: one library function finally called, two front doors, one corrected field, one extended assertion, one CI step.

---

## The finding

Since **2026-08-23**, every one of the 76 article pages has shipped an `Article` node containing:

```json
"author":    { "@id": "https://education3881.github.io/madar/#organization" },
"publisher": { "@id": "https://education3881.github.io/madar/#organization" },
"isPartOf":  { "@id": "https://education3881.github.io/madar/#organization" }
```

**That node was defined nowhere on the site.** `organizationNode()` was written on 08-23, exported, and never called by any page. The home page — the URL the reference points at, and the target of every breadcrumb's first crumb — carried **zero** `application/ld+json` blocks. So did the Arabic home, both editions indexes, About, VALENCE and the 404.

A node object carrying only `@id` is a **reference**, not a description. For **19 days** the corpus credited its author and its publisher to a pointer with no referent, on 76 pages, in two languages — **228 dangling references.**

A second, quieter defect in the same three lines: `isPartOf` also pointed at the Organization. An Article is part of a *WebSite*; it is not part of the company that publishes it. All three fields were aimed at one node and one of them was a category error.

## Why every check we own passed it

This is the instructive part, and it is why the fix came with an assertion.

- **The block parsed.** Assertion 1 satisfied.
- **The `@type` was right**, the required keys present, `inLanguage` agreed with the path. Assertion 3 satisfied.
- **The URL dereferenced.** `qa_jsonld` maps a URL to a file in dist and checks it exists. The reference's document part is the home page — which does exist. The check looked at `.../madar/` , found `index.html`, and counted a success. **It was checking the right string for the wrong thing.** The broken object was not a URL; it was a *node*, and nothing in the tool had ever looked for nodes.

`qa_jsonld` reported **CLEAN** on this build at 09:0x today, an hour before the defect was found by reading the emitted JSON by hand. That is the whole lesson: an assertion that dereferences *documents* cannot see a broken reference *inside* one.

## Why it costs traffic, concretely

The site has **0 of 82 URLs indexed**. The gate target is **11 October**. In that state the single most valuable thing on-page is not a keyword — it is a resolvable **entity**: a crawler needs to know that "Madār" is a *thing*, that it publishes these 76 documents, and that the Arabic and English halves are one publication.

Instead, every article said *"my publisher is that thing over there"* and pointed at a page that described nothing. Specifically:

- **Authorship and publisher were unresolvable.** An Article whose `publisher` cannot be resolved is an Article with no publisher; Google does not fetch a second page to complete it. Consumers resolve `@id` **within a document**.
- **No entity to consolidate onto.** Nothing anywhere declared the name, the alternate Arabic name, the logo, or that the site is bilingual by design — the one genuinely distinctive property this publication has.
- **The breadcrumb led somewhere empty.** Position 1 of every trail named "Madār" and linked to the front door, which then said nothing about itself.

## The fix

1. **`organizationNode()` is now emitted**, plus a new **`websiteNode()`** — `WebSite`, `@id … #website`, `inLanguage: ['en','ar']`, `publisher → #organization`.
2. **Emitted where they are referenced.** Both nodes ship on **every article page in both languages** *and* on **both front doors**. Same `@id` in every document, so consumers merge them into one node rather than seeing duplicates — and, critically, each page's own references now resolve **in-document**, which is the only resolution consumers actually perform.
3. **`isPartOf` corrected** to point at `#website`.
4. **Conservative, per the file's standing posture.** No `sameAs` (the publication holds no verified profile to claim). No `foundingDate` (the first publish date is not a founding date, and asserting the equivalence is exactly the invented precision this operation rules against). **No `SearchAction`** — the site has no search endpoint, and declaring one promises a surface that 404s.

Emitted per page after the fix: `Article` + `BreadcrumbList` + `Organization` + `WebSite`. Front doors: `Organization` + `WebSite`. Nodes site-wide **152 → 308**.

## The assertion, proved both ways (#35)

`qa_jsonld` gains **assertion 4**: *every bare `@id` reference must resolve to a node defined in the same document.* The one exception is named in the code rather than left silent — `workTranslation` / `translationOfWork` are cross-document **by design** and are already dereferenced as URLs.

- **BITE** — the new assertion against the pre-fix build: **FAIL(228)**, each defect naming its page and its field (`author`, `publisher`, `isPartOf` × 76 pages). It found the real, historical defect, not a synthetic one.
- **CONTROL** — the same assertion against the rebuilt site: **silent.** 82 pages, 308 nodes, 608 URL promises, **306 in-document references resolved**, 0 defects.
- **Regression** — all ten standing assertions re-run on the fixed build: green.

## Wired into CI — and a gap named while doing it

`qa_jsonld.py` has existed since **2026-08-29** and was **never added to the workflow**. It ran only by hand, in the daily run, which is why a 19-day defect had 19 days. It is now a build-job step.

**Named for the 09-13 weekly:** three more standing assertions are hand-run only — `qa_a11y_lang`, `qa_ar_language`, `qa_consumer_surface`. Six of ten gate the deploy; four do not. A standing assertion that only runs when someone remembers is a checklist item, not a gate. Recommend all four in CI at the review.

**Push note:** this touches `.github/workflows/astro-pages.yml` — **workflow-scope PAT required.**

## What is not claimed

No traffic figure. The site carries no third-party tracker by design and none is being added. This is a structural fix to the layer search engines read; its effect will show, if it shows, as indexation in the weeks after the wave gate — and it will be reported then as an observation, not forecast now as a number.

---

*Filed by Growth with the Web Developer, 2026-09-11.*
