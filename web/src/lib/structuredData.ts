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
    citation: input.sources.map((s) => ({
      '@type': 'CreativeWork',
      name: s.title,
      url: s.url,
    })),
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
}

export function collectionJsonLd(input: CollectionNodeInput) {
  const ar = input.lang === 'ar';
  const url = absolute(input.path);
  const home = absolute(ar ? `${BASE}/ar/` : `${BASE}/`);
  const hub = absolute(ar ? `${BASE}/ar/browse/` : `${BASE}/browse/`);
  const browseLabel = ar ? 'تصفّح' : 'Browse';

  const trail: Record<string, unknown>[] = [
    { '@type': 'ListItem', position: 1, name: ar ? 'مدار' : 'Madār', item: home },
    { '@type': 'ListItem', position: 2, name: browseLabel, item: hub },
  ];
  if (input.isFacet) {
    trail.push({ '@type': 'ListItem', position: 3, name: input.name, item: url });
  }

  return [
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
        itemListOrder: 'https://schema.org/ItemListOrderDescending',
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
