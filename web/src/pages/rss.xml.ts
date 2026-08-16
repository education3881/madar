import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { renderFeed } from '../lib/feed';
import { withBase } from '../lib/urls';

/**
 * English feed. Mirrors the published EN corpus (approved pieces only) — the
 * same filter the article routes use, so the feed can never surface a held
 * piece the site itself does not serve.
 */
export const GET: APIRoute = async (context) => {
  const pieces = await getCollection('articles', ({ data }) => data.approved !== false);

  const body = renderFeed(
    {
      title: 'Madār · مدار',
      description:
        'An editorial publication on early childhood and K-12 education, written and made in English and Arabic. A research instrument, not a magazine.',
      homePath: withBase('/'),
      selfPath: withBase('/rss.xml'),
      language: 'en',
      items: pieces.map((piece) => ({
        title: piece.data.title,
        path: withBase(`/articles/${piece.id}/`),
        description: piece.data.dek,
        date: piece.data.date,
        category: piece.data.country,
      })),
    },
    context.site
  );

  return new Response(body, {
    headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' },
  });
};
