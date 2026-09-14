import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Shared schema — applies to both English and Arabic articles.
const articleSchema = z.object({
  title: z.string().min(1),
  dek: z.string().max(200).optional(),
  date: z.coerce.date(),

  // Geography (validated against /docs/10_geo_scope.md by editorial process)
  country: z.string().min(1),

  // OPTIONAL, added 2026-09-14 for the first continental piece (Editor's
  // decision 3, commission 2026-09-04). `country` stays the single primary —
  // the byline, the feed category and the related rail all read it and none of
  // them changes. `countries` is the full set a continental piece measures, in
  // the piece's own order, and it MUST contain `country`. It exists because a
  // piece whose honest deliverable is "four rulers, four crowns" is not a
  // Mauritius piece, and because the stats panel counts distinct countries and
  // would otherwise under-count it by four. Rendered in the marginalia when
  // present (both languages, through the i18n-geo display map); asserted by
  // agents/tools/qa_geo_fields.py, which lands in the same commit as the field
  // and the first file to use it — a field with no consumer is a promise to
  // nobody (#37).
  countries: z.array(z.string().min(1)).min(2).optional(),

  region: z.enum(['MENA', 'Africa', 'Asia', 'LatAm-Caribbean', 'Europe', 'N-America', 'Oceania', 'Other']),

  // Education level (per /docs/20_topics.md)
  level: z.enum(['ECE', 'K-12', 'Both']),

  // Thematic tags (free-form but should map to /docs/20_topics.md)
  themes: z.array(z.string()).min(1),

  // Editorial format
  type: z.enum(['curated', 'short', 'essay']),

  // Edition number (monthly issue). Optional so non-edition drafts never break
  // the build; backfilled across the published corpus.
  edition: z.number().int().positive().optional(),

  // Sources — at least one is required by /docs/30_quality_bar.md
  sources: z
    .array(
      z.object({
        title: z.string(),
        url: z.string().url(),
      })
    )
    .min(1),

  // Optional cross-link to the same piece in the other language
  arabicVersion: z.string().optional(),
  englishVersion: z.string().optional(),

  // Optional editor-curated "related reading" — slugs (article ids) in the
  // SAME language collection. Unknown/unapproved slugs are filtered at render
  // time, so a parked or renamed piece degrades gracefully (no build break).
  related: z.array(z.string()).optional(),

  // Hero visual reference (filled in by Designer)
  hero: z
    .object({
      src: z.string().optional(),
      alt: z.string().optional(),
      caption: z.string().optional(),
    })
    .optional(),

  // Set to true once Vini has approved the draft for publication
  approved: z.boolean().default(false),

  // Editorial audit trail — true when the piece uses composite characters.
  // The dagger footnote in the body is what readers see; this flag is for editorial review.
  contains_composites: z.boolean().optional(),
});

const articles = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/articles' }),
  schema: articleSchema,
});

const articlesAr = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/articles-ar' }),
  schema: articleSchema,
});

export const collections = {
  articles,
  'articles-ar': articlesAr,
};
