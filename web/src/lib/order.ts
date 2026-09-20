/**
 * The publication's canonical reading order.
 *
 * Every list surface Madār serves — both home pages, both editions pages, every
 * browse facet, both feeds — answers the same question: which piece comes first?
 * Until 2026-09-20 each of them answered it with `b.date - a.date` and nothing
 * else, which is a comparator that returns 0 for two pieces published on the
 * same day. `Array.prototype.sort` is stable, so a 0 does not randomise the
 * pair — it delegates the decision to whatever order `getCollection()` handed
 * the entries over in, which is filesystem enumeration order, which is nobody's
 * decision at all.
 *
 * That is not hypothetical: 24 of the 38 approved English pieces sit in a tie
 * group (16 share 2026-07-07 alone), and a byte-compare of this build against
 * the live origin — the same commit, built twice on two runners — found five
 * sitemap pages and both feeds serving the same pieces in a different order.
 * Ruling #58.
 *
 * The fix is one comparator, exported once, used everywhere, because the defect
 * is not that any single site got it wrong — it is that each site was free to
 * decide separately, and eight of the nine chose the same incomplete answer.
 * (The ninth, `facetsFor` in taxonomy.ts, already broke its count ties on the
 * key. The shape was known here; it was simply never carried across.)
 *
 * The tiebreak is the slug, ascending. Any total order would make the build
 * deterministic; the slug is chosen because it is stable under everything the
 * editorial process does to a piece — a retitled piece keeps its position, and
 * the leading date in our slug convention means the tiebreak reads as a
 * secondary sort on the rest of the name rather than as noise.
 */

/**
 * Newest first, ties broken by a caller-supplied stable key.
 *
 * Generic on purpose: content-collection entries carry their date at
 * `.data.date` and their key at `.id`, while feed items carry `.date` and
 * `.path`. One comparator, two accessors, no second implementation to drift.
 */
export function newestFirst<T>(date: (x: T) => Date, key: (x: T) => string) {
  return (a: T, b: T) =>
    date(b).valueOf() - date(a).valueOf() || key(a).localeCompare(key(b), 'en');
}

/**
 * The canonical order for a content-collection entry, EN or AR. Structurally
 * typed rather than tied to `CollectionEntry<'articles'>` so the Arabic
 * collection uses the identical comparator instead of a parallel one.
 */
export const byDateThenSlug = newestFirst<{ data: { date: Date }; id: string }>(
  (p) => p.data.date,
  (p) => p.id
);
