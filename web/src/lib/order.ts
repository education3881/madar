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
 * The comparison form of a display name. NFD, combining marks dropped,
 * lower-cased.
 *
 * WHY (2026-09-21, ruling #59)
 * ----------------------------
 * Yesterday's note two paragraphs up says `facetsFor` "already broke its count
 * ties on the key" and was therefore the one sort site that needed no fix. It
 * broke them on `a[0].localeCompare(b[0])` — **with no locale argument**, which
 * asks ICU for the default locale, which ICU reads from the environment. Same
 * code, same corpus, two runners:
 *
 *     LC_ALL=en_US  ->  Türkiye, Turkmenistan, Tuvalu
 *     LC_ALL=sv_SE  ->  Turkmenistan, Tuvalu, Türkiye
 *
 * `Türkiye` is already in the corpus (2026-07-07). It is kept out of the
 * rendered facet set today only by the `count >= 2` threshold — that is, by how
 * much we have written about one country, which is not a guarantee of anything.
 * #58 said a build must be a function of its sources; the environment is not a
 * source, and a comparator that consults it has the same defect as one that
 * consults filesystem order, one layer further down.
 *
 * Why not `localeCompare(key, 'en')`, the fix #58 used for slugs: that is
 * deterministic, but it is ICU's answer and `qa_stable_order.py` has to predict
 * it in Python without ICU. On the slug alphabet (`[a-z0-9-]`) the two agree
 * and the assertion is safe. Facet keys are not slugs — they are display names
 * in the schema's vocabulary, diacritics included — so the two orders diverge
 * exactly where this defect lives, and an assertion that cannot state the
 * expected order cannot assert it (#36).
 *
 * So the key is normalised instead, identically in both languages of this
 * repository: `unicodedata.normalize('NFD', …)` with `Mn` dropped is the same
 * three lines in Python. `Türkiye` compares as `turkiye` — between Tunisia and
 * Turkmenistan, which is also where a reader looks for it.
 */
export function collationKey(value: string): string {
  return value.normalize('NFD').replace(/\p{Mn}+/gu, '').toLowerCase();
}

/**
 * Ascending by display name, on the normalised key, ties broken by the raw
 * string so the order is total even when two keys normalise alike.
 */
export function byKeyAsc(a: string, b: string): number {
  const ka = collationKey(a);
  const kb = collationKey(b);
  if (ka !== kb) return ka < kb ? -1 : 1;
  return a === b ? 0 : a < b ? -1 : 1;
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
