/**
 * schema.org JSON-LD builders.
 *
 * WHY (Growth, 2026-08-23)
 * ------------------------
 * Until today not one of the 82 pages carried structured data. The `<head>` is
 * otherwise strong — canonical, reciprocal hreflang + x-default, absolute
 * raster og:image, twitter card, robots — but every one of those describes the
 * page's IDENTITY. None describes what the page IS, who made it, what language
 * it is in, or what it stands on.
 *
 * That last one is the expensive omission. Madār's whole claim is that every
 * piece rests on named primary sources — ministry registers, statutes,
 * assessment bodies — and `schema.org/citation` is precisely the field that
 * makes a bibliography legible to a machine. We were shipping the evidence and
 * hiding it. The 08-18 brief recorded that a search for the publication by name
 * and by URL surfaced nothing of ours; structured data is the highest-leverage
 * on-page lever we control while the domain question is still open, and it
 * costs nothing per page because the data is already in frontmatter.
 *
 * Deliberately conservative:
 *  - Only fields we can populate TRUTHFULLY from frontmatter. No invented
 *    author names, no fabricated `datePublished` precision, no `aggregateRating`.
 *  - `inLanguage` is real and load-bearing here: a bilingual corpus that does
 *    not declare per-page language asks a crawler to guess, and today's ruling
 *    (#33) is about exactly that class of guess.
 *  - Both language editions get the SAME builder, so the Arabic corpus is
 *    described as richly as the English one — Arabic is a distribution
 *    advantage, not a translation cost (Charter, traffic-growth loop).
 */

const SITE = 'https://education3881.github.io';
const BASE = '/madar';

const absolute = (path: string) => new URL(path, SITE).href;

export const ORG_ID = `${SITE}${BASE}/#organization`;
export const SITE_ID = `${SITE}${BASE}/#website`;

/**
 * The publication itself. Referenced by every Article node.
 *
 * WHY THIS IS EMITTED, NOT JUST DEFINED (Growth, 2026-09-11)
 * ----------------------------------------------------------
 * This function existed from 2026-08-23 and was never called. Meanwhile every
 * one of the 76 article pages shipped
 *
 *     "author":    { "@id": ".../madar/#organization" }
 *     "publisher": { "@id": ".../madar/#organization" }
 *     "isPartOf":  { "@id": ".../madar/#organization" }
 *
 * — three bare `@id` REFERENCES to a node defined nowhere on the site. A node
 * object carrying only `@id` is a pointer, not a description; for 19 days the
 * corpus credited its author and its publisher to a dangling pointer, and the
 * breadcrumb's first crumb named "Madār" and linked to a front door that
 * declared nothing at all.
 *
 * The correction that matters is WHERE the node is emitted. Consumers resolve
 * `@id` references within a single document; none of them fetches the home page
 * to complete an article's publisher. So the node is emitted on every page that
 * references it — the article pages themselves — and on both front doors, which
 * is where the entity belongs anyway. Same `@id` in every document means one
 * node, merged, not duplicates (ruling #36: the claim is derived from the thing
 * it describes; #37: a reference is a declaration, and a declaration is checked).
 *
 * Conservative, as the rest of this file: only fields that are true and
 * verifiable from what we ship. No `sameAs` (the publication holds no verified
 * social profile), no `foundingDate` (the first publish date is not a founding
 * date and inventing the equivalence is the kind of precision this operation
 * rules against), and deliberately no `SearchAction` on the WebSite node —
 * the site has no search endpoint, and declaring one would promise a surface
 * that 404s.
 */
export function organizationNode() {
  return {
    // Every node in Base.astro's jsonLd ARRAY is serialised as a top-level
    // object, so each carries its own @context — matching articleJsonLd and
    // breadcrumbJsonLd rather than relying on a sibling's context.
    '@context': 'https://schema.org',
    '@type': 'Organization',
    '@id': ORG_ID,
    name: 'Madār',
    alternateName: 'مدار',
    url: absolute(`${BASE}/`),
    knowsLanguage: ['en', 'ar'],
    logo: {
      '@type': 'ImageObject',
      url: absolute(`${BASE}/wordmark/madar-wordmark.svg`),
    },
  };
}

/**
 * The site as a work, distinct from the organization that publishes it.
 *
 * An Article `isPartOf` a WebSite; it is not "part of" an Organization — that
 * was a category error in the 08-23 builder, and it is fixed here rather than
 * carried. `inLanguage` is a list because the site genuinely is one bilingual
 * publication, not two sites: the same editions index, the same edition
 * numbering, reciprocal hreflang on every page.
 */
export function websiteNode() {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    '@id': SITE_ID,
    name: 'Madār · مدار',
    url: absolute(`${BASE}/`),
    inLanguage: ['en', 'ar'],
    publisher: { '@id': ORG_ID },
  };
}

/**
 * The pair every page needs in order for its own references to resolve.
 * Spread into the `jsonLd` array of any page that names ORG_ID or SITE_ID.
 */
export function publisherNodes() {
  return [organizationNode(), websiteNode()];
}

export interface ArticleNodeInput {
  title: string;
  dek?: string;
  /** Site-absolute path INCLUDING base prefix. */
  path: string;
  date: Date;
  /**
   * The last commit that touched the files this page is built from, from the
   * SAME git-derived resolver the sitemap's <lastmod> uses (2026-10-26, growth).
   * Not a build timestamp and not the frontmatter `date` — both of those were
   * rejected for <lastmod> in 2026-08-24 for the same two reasons, and they are
   * the same two reasons here: a build timestamp says every page changed on
   * every deploy, and the publication date asserts the page has never changed.
   * Omitted rather than guessed when the resolver cannot answer, because a
   * fabricated freshness signal is worse than none (#1, and the whole of
   * `sitemapLastmod.mjs`'s own header).
   */
  dateModified?: string | null;
  lang: 'en' | 'ar';
  country: string;
  themes: string[];
  /** Absolute or base-prefixed path to the raster share card. */
  cardPath?: string;
  sources: { title: string; url: string }[];
  /** Path of the same piece in the other language, if it exists. */
  translationPath?: string;
}

/**
 * BreadcrumbList (Growth, 2026-08-28).
 *
 * WHY: the Article node describes what a page IS; nothing yet describes where
 * it SITS. A crawler that arrives at an article URL (the likeliest entry point
 * once indexing starts — articles outnumber hubs 76 to 6) learns the page's
 * position in the site only by walking links. BreadcrumbList states it in the
 * head, and search results render it as a readable trail instead of a raw URL —
 * which matters more than usual while the URL still carries a github.io host.
 * Same conservative posture as articleJsonLd: every value is derived from the
 * page's own lang + path (ruling #36 — a claim about a page is computed from
 * the page), labels reuse the SiteHeader's own nav strings, and both language
 * editions get the same builder.
 */
export interface BreadcrumbInput {
  lang: 'en' | 'ar';
  /** Site-absolute path INCLUDING base prefix. */
  path: string;
  title: string;
}

export function breadcrumbJsonLd(input: BreadcrumbInput) {
  const ar = input.lang === 'ar';
  const url = absolute(input.path);
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    '@id': `${url}#breadcrumb`,
    itemListElement: [
      {
        '@type': 'ListItem',
        position: 1,
        name: ar ? 'مدار' : 'Madār',
        item: absolute(ar ? `${BASE}/ar/` : `${BASE}/`),
      },
      {
        '@type': 'ListItem',
        position: 2,
        // The SiteHeader's own nav labels — not a translation invented here.
        name: ar ? 'الإصدارات' : 'Editions',
        item: absolute(ar ? `${BASE}/ar/editions/` : `${BASE}/editions/`),
      },
      {
        '@type': 'ListItem',
        position: 3,
        name: input.title,
        item: url,
      },
    ],
  };
}

export function articleJsonLd(input: ArticleNodeInput) {
  const url = absolute(input.path);
  return {
    '@context': 'https://schema.org',
    '@type': 'Article',
    '@id': `${url}#article`,
    headline: input.title,
    ...(input.dek ? { description: input.dek } : {}),
    url,
    mainEntityOfPage: { '@type': 'WebPage', '@id': url },
    // Date only — the corpus records a publication date, not a timestamp, and
    // inventing an hour to satisfy a richer format would be a fabrication.
    datePublished: input.date.toISOString().slice(0, 10),
    // A correction a machine cannot see is a correction that did not travel.
    // On 2026-10-26 nine served sentences were repaired across four pieces
    // (#117) and the sitemap's <lastmod> moved for all eight affected URLs
    // while every article's own structured data went on declaring only its
    // publication date — so the one consumer class that reads JSON-LD rather
    // than the sitemap was told nothing had changed since July.
    ...(input.dateModified
      ? { dateModified: input.dateModified.slice(0, 10) }
      : {}),
    inLanguage: input.lang === 'ar' ? 'ar' : 'en',
    isAccessibleForFree: true,
    // The publication is the author of record. Pieces are bylined
    // «هيئة التحرير» / the editorial desk, never an individual, so naming a
    // person here would invent one.
    author: { '@id': ORG_ID },
    publisher: { '@id': ORG_ID },
    ...(input.cardPath
      ? {
          image: {
            '@type': 'ImageObject',
            url: absolute(input.cardPath),
            width: 1200,
            height: 600,
          },
        }
      : {}),
    about: { '@type': 'Place', name: input.country },
    keywords: input.themes.join(', '),
    // The point of the whole exercise: the bibliography, machine-readable.
    //
    // 2026-11-19, GROWTH, standing-queue item 87. This block emitted
    // `name: s.title` for every source, and `s.title` is OUR WHOLE ANNOTATION
    // about the document rather than the document's name: median 274
    // characters, longest 3,237, and 663 of 714 over the 110 characters at
    // which a consumer stops showing a title. A machine was being told that a
    // press release is TITLED with our commentary on why we opened it. That is
    // the 2026-08-18 share-card defect one surface over and strictly worse — a
    // promise that resolves, renders and says the WRONG THING cannot 404, so
    // nothing can notice.
    //
    // The one-line repair item 87 proposed was measured and REFUSED there:
    // cutting at the first ' (' improves 503 entries and DAMAGES 163, because
    // a parenthesis is as often part of a name as the start of a gloss
    // ('Free Quality School Education (FQSE)'). Re-measured 2026-11-19 with a
    // narrower rule and it got worse, not better.
    //
    // So the fix is structural rather than a cut, and schema.org already draws
    // the line we need: `name` is a NAME and `description` is prose about the
    // thing. The annotation moves to `description`, where long text is
    // legitimate, and `name` is emitted ONLY where the drafter MARKED a
    // document name — a quoted or italicised span, which is a boundary the
    // ARTEFACT supplies rather than one this builder has to guess (#113).
    // 120 of 714 entries carry one, median 62 characters. The other 594 get
    // url + description and no name at all, because telling a consumer nothing
    // about a title is strictly better than telling it something false.
    citation: input.sources.map((s) => {
      const name = markedName(s.title);
      return {
        '@type': 'CreativeWork',
        ...(name ? { name } : {}),
        description: s.title,
        url: s.url,
      };
    }),
    ...(input.translationPath
      ? { workTranslation: { '@id': `${absolute(input.translationPath)}#article` } }
      : {}),
    // A piece is part of the SITE, not of the organization that publishes it.
    // Corrected 2026-09-11; the 08-23 builder pointed all three of author,
    // publisher and isPartOf at the same Organization node.
    isPartOf: { '@id': SITE_ID },
  };
}

/**
 * The document name a drafter MARKED inside a source annotation, or null.
 *
 * Standing-queue item 87, 2026-11-19. Three conventions are in use across both
 * editions and all three mark the same thing — the register's own title:
 * single quotes (straight or curly), double quotes (straight or curly), and
 * markdown emphasis. Whichever appears FIRST within the annotation's opening
 * 400 characters is taken, because a later quoted span is a quotation FROM the
 * register rather than the register's name — which is the distinction
 * `qa_citation_identity` (#112) exists to work on, from the other side.
 *
 * Deliberately returns null rather than guessing. An unmarked annotation has no
 * boundary this builder can supply, and 594 of 714 go unnamed today.
 */
function markedName(annotation: string): string | null {
  // Window measured rather than chosen, 2026-11-19. A marked span is ambiguous
  // between the register's TITLE and a QUOTATION FROM it — #112 found 529
  // quoted tokens over 218 registers in these same annotations, so quotations
  // are the MAJORITY of marked spans in the corpus as a whole. What separates
  // them is position: a title sits immediately after the publisher, a quotation
  // sits later in the gloss. Measured across all 714 entries, the first marked
  // span within the opening N characters yields 191 names at N=400, 163 at 200,
  // 120 at 120 and 75 at 90 — and hand-sampling twelve at N=120 returned twelve
  // genuine document titles, where N=400 returned a courtroom quotation among
  // them. 120 is taken: PRECISION OVER RECALL, because a false title is the
  // defect this whole change exists to remove and no title is merely a silence.
  const head = annotation.slice(0, 120);
  // The delimiters must be QUOTE MARKS and not POSSESSIVE APOSTROPHES, and the
  // difference is positional rather than in the character: U+2019 is the same
  // code point in `the release's own words` as in `'Results of Government
  // Schools Reviews'`. An opening mark is preceded by the start of the string,
  // a space or an opening bracket; a closing mark is followed by the end, a
  // space or punctuation — never by a letter. Written this way because the
  // first version of this function was NOT, and the measurement caught it
  // naming a citation `s founding figure On the gender attributed to…`, a span
  // running from one possessive to the next. Third firing in one day of the
  // family ruling #150 names: a matcher wrong about a character class.
  const m = head.match(
    /(?:^|[\s(\[\u2014-])[\u2018']([^\u2019'\n]{6,160})[\u2019'](?=$|[\s,.;:)\]\u2014])|(?:^|[\s(\[\u2014-])[\u201c"]([^\u201d"\n]{6,160})[\u201d"](?=$|[\s,.;:)\]\u2014])|(?:^|[\s(\[\u2014-])\*([^*\n]{6,160})\*(?=$|[\s,.;:)\]\u2014])/,
  );
  if (!m) return null;
  const name = (m[1] ?? m[2] ?? m[3] ?? '').trim();
  return name.length >= 6 ? name : null;
}

/**
 * CollectionPage + ItemList for a browse facet page (Growth, 2026-10-20).
 *
 * WHY. Measured today over the built site: **45 of 135 served pages carry no
 * structured data at all, and 40 of those 45 are the browse facet pages** — the
 * twenty EN and twenty AR pages whose entire job is to be this site's topical
 * graph. The article pages have described themselves since 08-23; the hubs that
 * say *these pieces belong together, and here is the axis* have described
 * themselves never. `ItemList` is the one schema.org type that states a
 * membership, and a membership is exactly what a facet page knows and a crawler
 * has to infer from markup.
 *
 * Same conservative posture as every builder above: every value is derived from
 * the page's own lang, path and the collection the build already resolved
 * (#36 — a claim about a page is computed from the page). No `numberOfItems`
 * that is not the length of the list we actually emit; no description invented
 * for a facet; `inLanguage` real and per-edition, because the Arabic hubs are
 * described exactly as richly as the English ones.
 *
 * `breadcrumbJsonLd` is NOT reused: its second crumb is hardcoded *Editions*,
 * and a browse page does not sit under Editions. A crumb that names the wrong
 * parent is worse than no crumb, so the trail is built here with Browse in that
 * position, using the SiteHeader's own two labels rather than a translation
 * invented at this call site.
 */
export interface CollectionNodeInput {
  lang: 'en' | 'ar';
  /** Site-absolute path INCLUDING base prefix, with trailing slash. */
  path: string;
  /** The page's own visible heading — the facet key, or the hub's own word. */
  name: string;
  /** Members, in the order the page renders them. */
  items: { name: string; path: string }[];
  /** False for the /browse/ hub itself, which has no parent facet. */
  isFacet: boolean;
  /**
   * The crumb between the site root and this page. Defaults to Browse, which
   * is where every caller lived until 2026-11-20.
   *
   * Added by the growth function that gave the two EDITIONS pages their first
   * structured data: they serve 45 article links each and emitted NO JSON-LD at
   * all — not a CollectionPage, not an ItemList, not even the Organization and
   * WebSite nodes every other page on the site carries — because neither
   * template passed `jsonLd` to `Base.astro`. The archive is not under Browse,
   * so a trail hardcoded to Browse would have been a crumb to the wrong parent,
   * which this function's own header already says is worse than no crumb.
   */
  hub?: { path: string; label: string };
  /**
   * `itemListOrder`, or `null` to OMIT it.
   *
   * Defaults to descending, which is true of every browse facet: one list, one
   * key, newest first. It is NOT true of the editions page, whose order is
   * edition-grouped and then date-ordered inside each group — neither ascending
   * nor descending, and schema.org offers no third value that is honest here.
   * An `ItemList` whose members carry explicit `position` values is well defined
   * without the property, so the archive omits it rather than asserting an order
   * it does not have. *A field that resolves and parses and says the wrong thing
   * cannot fail* — yesterday's citation-name defect, one property over.
   */
  order?: 'descending' | null;
}

export function collectionJsonLd(input: CollectionNodeInput) {
  const ar = input.lang === 'ar';
  const url = absolute(input.path);
  const home = absolute(ar ? `${BASE}/ar/` : `${BASE}/`);
  const hub = input.hub
    ? absolute(input.hub.path)
    : absolute(ar ? `${BASE}/ar/browse/` : `${BASE}/browse/`);
  const browseLabel = input.hub ? input.hub.label : ar ? 'تصفّح' : 'Browse';

  const trail: Record<string, unknown>[] = [
    { '@type': 'ListItem', position: 1, name: ar ? 'مدار' : 'Madār', item: home },
    { '@type': 'ListItem', position: 2, name: browseLabel, item: hub },
  ];
  if (input.isFacet) {
    trail.push({ '@type': 'ListItem', position: 3, name: input.name, item: url });
  }

  // The referents ship with the references (fixed 2026-10-21). The 10-20 growth
  // commit gave these 40 pages `isPartOf` and `publisher` pointers and did not
  // spread `publisherNodes()` at either call site, so every browse page served
  // two dangling @ids — 80 defects, and `qa_jsonld` failed the deploy on them.
  // Supplying them HERE rather than at the call sites is deliberate: the
  // function that writes the pointer is the only place that cannot forget the
  // node it points at.
  return [
    ...publisherNodes(),
    {
      '@context': 'https://schema.org',
      '@type': 'CollectionPage',
      '@id': `${url}#collection`,
      name: input.name,
      url,
      inLanguage: input.lang,
      isPartOf: { '@id': SITE_ID },
      publisher: { '@id': ORG_ID },
      mainEntity: {
        '@type': 'ItemList',
        '@id': `${url}#itemlist`,
        ...(input.order === null
          ? {}
          : { itemListOrder: 'https://schema.org/ItemListOrderDescending' }),
        numberOfItems: input.items.length,
        itemListElement: input.items.map((it, i) => ({
          '@type': 'ListItem',
          position: i + 1,
          name: it.name,
          url: absolute(it.path),
        })),
      },
    },
    {
      '@context': 'https://schema.org',
      '@type': 'BreadcrumbList',
      '@id': `${url}#breadcrumb`,
      itemListElement: trail,
    },
  ];
}
