/**
 * taxonomy.ts — the browse surface, derived from the approved corpus.
 *
 * WHY (Growth audit, 2026-09-13; built 2026-09-14)
 * ------------------------------------------------
 * Until today this publication served seven route files and NOT ONE of them
 * grouped articles by anything. A reader who finished the Sierra Leone piece
 * and wanted the rest of what we have written about Africa, or about teachers,
 * had no page to go to. The editions index lists editions chronologically; the
 * related rail carries two or three hand-curated siblings. That was the entire
 * navigation surface of a bilingual publication covering 35 countries.
 *
 * Everything here is DERIVED from the collection at build time (#36, and the
 * 2026-06-07 rule): a hand-kept list of slugs is correct the day it is written
 * and silently wrong the next time an article is added.
 *
 * SELECTION RULES — an index page must discriminate and must not dead-end.
 * The audit found that `government-led programs` sits on 38 of 38 approved
 * pieces: a tag true of everything carries zero information, and a page
 * listing the whole corpus is the editions index with extra steps. It also
 * found three tags holding exactly one piece: a page listing one article is a
 * dead end in the sense `qa_body_links` exists to catch. So:
 *
 *   regions   — every region holding at least one piece (the enum is small and
 *               each value is a genuine division of the corpus)
 *   themes    — tags on FEWER THAN HALF the corpus and on AT LEAST TWO pieces
 *   countries — countries with AT LEAST TWO pieces
 *
 * The thresholds are computed against the live corpus, never frozen, so the
 * set of pages grows as the corpus does — Africa moves 5 → 11 at the Edition
 * 05 flip without anyone editing this file.
 *
 * HELD PIECES ARE INVISIBLE. Callers pass the approved set only; a facet
 * derived over held drafts leaks a slug and a date (RUNBOOK, 2026-09-06).
 */

import { byKeyAsc, collationKey } from './order';

export type FacetKind = 'region' | 'topic' | 'country';

export interface Facet {
  kind: FacetKind;
  /** The frontmatter value, in the schema's own (English) vocabulary. */
  key: string;
  /** ASCII path segment. URLs stay Latin in both languages, as /ar/articles/ already does. */
  slug: string;
  count: number;
}

/** Frontmatter fields this module reads. Kept structural so both collections fit. */
interface PieceData {
  region: string;
  country: string;
  countries?: string[];
  themes: string[];
}
interface Piece {
  id: string;
  data: PieceData;
}

/**
 * ASCII slug for a controlled-vocabulary value. Total on the enums we own.
 *
 * The normalisation step is `collationKey` and not a second spelling of it
 * (2026-09-21): a key's position in a list and its URL are then derived from
 * one function, so they cannot disagree. Without it `Türkiye` — a country this
 * publication has already covered — slugs to `t-rkiye`, because `ü` is not in
 * `[a-z0-9]` and the character class turns it into a separator.
 */
export function facetSlug(value: string): string {
  return collationKey(value.trim())
    .replace(/[’']/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

/** Every country a piece measures: the primary plus the optional list, de-duplicated. */
export function countriesOf(p: Piece): string[] {
  const names = [p.data.country, ...(p.data.countries ?? [])].filter(Boolean);
  return [...new Set(names)];
}

function tally(pieces: Piece[], valuesOf: (p: Piece) => string[]): Map<string, number> {
  const m = new Map<string, number>();
  for (const p of pieces) {
    for (const v of new Set(valuesOf(p))) m.set(v, (m.get(v) ?? 0) + 1);
  }
  return m;
}

export function facetsFor(pieces: Piece[]): Facet[] {
  const total = pieces.length;
  const out: Facet[] = [];

  // Count descending, ties on the normalised key ascending. The tie-break is
  // `byKeyAsc` and not `localeCompare` because localeCompare with no locale
  // argument answers out of the environment rather than out of the data —
  // ruling #59, and the reasoning is in order.ts beside the comparator.
  const push = (kind: FacetKind, counts: Map<string, number>, keep: (n: number) => boolean) => {
    for (const [key, count] of [...counts.entries()].sort((a, b) =>
      b[1] - a[1] || byKeyAsc(a[0], b[0])
    )) {
      if (keep(count)) out.push({ kind, key, slug: facetSlug(key), count });
    }
  };

  push('region', tally(pieces, (p) => [p.data.region]), (n) => n >= 1);
  // Discriminating AND non-trivial. `total / 2` is strict: a tag on exactly
  // half the corpus still splits it, but a tag above that is a beat, not a
  // theme, and the corpus is small enough that the boundary matters.
  push('topic', tally(pieces, (p) => p.data.themes ?? []), (n) => n >= 2 && n < total / 2);
  push('country', tally(pieces, countriesOf), (n) => n >= 2);

  return out;
}

/** Site-absolute path (no base prefix) for a facet page in one language. */
export function facetPath(f: Facet, lang: 'en' | 'ar'): string {
  const prefix = lang === 'ar' ? '/ar' : '';
  return `${prefix}/browse/${f.kind}/${f.slug}/`;
}

/** Site-absolute path (no base prefix) for the browse hub. */
export function browsePath(lang: 'en' | 'ar'): string {
  return lang === 'ar' ? '/ar/browse/' : '/browse/';
}

/** The pieces belonging to a facet, newest first. */
export function piecesIn(pieces: Piece[], f: Facet): Piece[] {
  const match = (p: Piece) =>
    f.kind === 'region'
      ? p.data.region === f.key
      : f.kind === 'topic'
        ? (p.data.themes ?? []).includes(f.key)
        : countriesOf(p).includes(f.key);
  return pieces.filter(match);
}
