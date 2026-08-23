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
