import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { renderFeed } from '../../lib/feed';
import { withBase } from '../../lib/urls';
import { countryAr } from '../../lib/i18n-geo';

/**
 * Arabic feed. Peer of the English feed, not a translation of it: it is built
 * from the `articles-ar` collection, so AR/EN parity in the corpus becomes
 * AR/EN parity in the subscription surface. Arabic is a distribution
 * advantage, not a translation cost (Charter, the traffic-growth loop).
 */
export const GET: APIRoute = async (context) => {
  const pieces = await getCollection('articles-ar', ({ data }) => data.approved !== false);

  const body = renderFeed(
    {
      title: 'مدار · Madār',
      description:
        'مجلّةٌ تحريريّةٌ بطيئةُ الإيقاع تتناول التعليم في مرحلتَي الطفولة المبكّرة والتعليم العام، تصدر بالعربيّة والإنجليزيّة. أداةُ بحثٍ، لا مجلّةً.',
      homePath: withBase('/ar/'),
      selfPath: withBase('/ar/rss.xml'),
      language: 'ar',
      items: pieces.map((piece) => ({
        title: piece.data.title,
        path: withBase(`/ar/articles/${piece.id}/`),
        description: piece.data.dek,
        date: piece.data.date,
        // The Arabic feed carried the ENGLISH country as its category from the
        // day it was built (2026-08-16) — Arabic title, Arabic dek, and then
        // "Sierra Leone" as the tag. The data stays English; the display does
        // not (see lib/i18n-geo.ts).
        category: countryAr(piece.data.country),
        cardPath: piece.data.hero?.src
          ? withBase(piece.data.hero.src.replace(/^\/stills\//, '/og/').replace(/\.svg$/, '.png'))
          : undefined,
      })),
    },
    context.site
  );

  return new Response(body, {
    headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' },
  });
};
