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

/** The publication itself. Referenced by every Article node. */
export function organizationNode() {
  return {
    '@type': 'Organization',
    '@id': `${SITE}${BASE}/#organization`,
    name: 'Madār',
    alternateName: 'مدار',
    url: absolute(`${BASE}/`),
    logo: {
      '@type': 'ImageObject',
      url: absolute(`${BASE}/wordmark/madar-wordmark.svg`),
    },
  };
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
    author: { '@id': `${SITE}${BASE}/#organization` },
    publisher: { '@id': `${SITE}${BASE}/#organization` },
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
    isPartOf: { '@id': `${SITE}${BASE}/#organization` },
  };
}
