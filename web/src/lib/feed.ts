/**
 * RSS 2.0 feed builder — hand-rolled, deliberately dependency-free.
 *
 * Why not @astrojs/rss: adding a dependency means touching package.json AND
 * package-lock.json from the sandbox, and a hand-edited lockfile is what took
 * CI down for four days on 2026-07-02 (npm ci EUSAGE). A feed is ~60 lines of
 * string building; it is not worth a lockfile edit. No new dependency is
 * introduced by this module.
 *
 * Emits one channel per language. Both feeds are built from the same article
 * schema (see content.config.ts) and carry only `approved` pieces — the feed
 * is a mirror of the published corpus, never of the staging layer.
 *
 * Added 2026-08-16 (weekly review) to make good on the footer's RSS link,
 * which had pointed at a non-existent /rss.xml since the initial publish
 * on 2026-05-25.
 */

import { statSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';

import { newestFirst } from './order';

/**
 * Real byte size of a share card, read from `public/` at build time.
 *
 * A missing card is not an error here: `cardPath` is only set when the piece
 * declares a hero, and `qa_held_assets` already governs which cards exist in
 * dist. But a card that is present and mis-measured is exactly the defect this
 * function was written to end, so a stat failure yields 0 and is caught by
 * `qa_feed_enclosures.py`, which asserts against the served file rather than
 * against this computation.
 */
function cardBytes(cardPath: string): number {
  const here = dirname(fileURLToPath(import.meta.url));
  const pub = resolve(here, '../../public', cardPath.replace(/^\/madar\//, ''));
  try {
    return statSync(pub).size;
  } catch {
    return 0;
  }
}

export interface FeedItem {
  title: string;
  /** Site-absolute path INCLUDING the base prefix, e.g. /madar/articles/slug/ */
  path: string;
  description?: string;
  date: Date;
  /** Country, used as the item category — in the CHANNEL's language. */
  category?: string;
  /** Site-absolute path of the raster share card, if one exists. */
  cardPath?: string;
}

export interface FeedChannel {
  title: string;
  description: string;
  /** Site-absolute path of the channel's home page, including base prefix. */
  homePath: string;
  /** Site-absolute path of this feed document, including base prefix. */
  selfPath: string;
  language: 'en' | 'ar';
  items: FeedItem[];
}

/** XML text-node / attribute escaping. Applied to every interpolated value. */
function esc(value: string): string {
  return value
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

/** RFC 822 date, as RSS 2.0 requires (not ISO 8601). */
function rfc822(date: Date): string {
  return date.toUTCString();
}

function abs(site: URL | undefined, path: string): string {
  return new URL(path, site ?? 'https://education3881.github.io').href;
}

/** Right-to-left mark, U+200F. */
const RLM = '‏';

/**
 * BIDIRECTIONAL TEXT IN A FEED (added 2026-08-23).
 *
 * "Well-formed" is to a feed what "resolves" was to the og:image — it says the
 * document parses, not that a reader can read it. Two separate problems, and
 * RSS 2.0 gives each a different lever:
 *
 *  - `<title>` is PLAIN TEXT by spec. No markup, so no `dir` attribute. A
 *    reader drops the string into its own paragraph, whose base direction is
 *    the reader's UI language — LTR for most subscribers. Under an LTR base,
 *    trailing punctuation and runs of digits ("2026", "12,348") resolve to the
 *    WRONG SIDE of an Arabic string. The only available lever is to prefix the
 *    value with U+200F, which sets the paragraph base direction to RTL.
 *
 *  - `<description>` is HTML by universal convention, so it takes real markup:
 *    a `<div dir="rtl" lang="ar">` wrapper, which is both stronger and more
 *    explicit than a control character.
 *
 * 27 of our 38 Arabic deks mix Arabic with Latin or digits, and before today
 * not one character of direction metadata appeared anywhere in either feed.
 */
function feedTitle(value: string, language: 'en' | 'ar'): string {
  if (language !== 'ar') return esc(value);
  return esc(value.startsWith(RLM) ? value : RLM + value);
}

function feedDescription(value: string, language: 'en' | 'ar'): string {
  if (language !== 'ar') return esc(value);
  // Escaped, then wrapped: the wrapper is markup we intend, the content is not.
  return `&lt;div dir="rtl" lang="ar"&gt;${esc(value)}&lt;/div&gt;`;
}

export function renderFeed(channel: FeedChannel, site: URL | undefined): string {
  const items = [...channel.items]
    .sort(newestFirst<FeedItem>((i) => i.date, (i) => i.path))
    .map((item) => {
      const link = abs(site, item.path);
      return [
        '    <item>',
        `      <title>${feedTitle(item.title, channel.language)}</title>`,
        `      <link>${esc(link)}</link>`,
        `      <guid isPermaLink="true">${esc(link)}</guid>`,
        item.description
          ? `      <description>${feedDescription(item.description, channel.language)}</description>`
          : null,
        item.category
          ? `      <category>${feedTitle(item.category, channel.language)}</category>`
          : null,
        // The share card, so an item carries its art into a reader. Only ever
        // a raster path — the 2026-08-18 rule (no consumer renders SVG) binds
        // the feed exactly as it binds og:image.
        //
        // 2026-09-20: `length` was hard-coded to "0" from the day enclosures
        // shipped. In RSS 2.0 it is the size of the file in bytes, and it is
        // how a reader decides whether to fetch or show the thing at all — so
        // for 38 pieces in two languages every card was resolvable, correctly
        // typed, and declared empty. The 08-18 defect exactly (the URL was
        // never the problem; the promise about it was), on the surface 08-18
        // named as the next one to check. Measured from the file on disk, so
        // it cannot drift from what is served.
        item.cardPath
          ? `      <enclosure url="${esc(abs(site, item.cardPath))}" length="${cardBytes(item.cardPath)}" type="image/png" />`
          : null,
        `      <pubDate>${rfc822(item.date)}</pubDate>`,
        '    </item>',
      ]
        .filter(Boolean)
        .join('\n');
    })
    .join('\n');

  const selfHref = abs(site, channel.selfPath);
  const latest = channel.items.reduce<Date | null>(
    (acc, item) => (acc === null || item.date > acc ? item.date : acc),
    null
  );

  return `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>${esc(channel.title)}</title>
    <link>${esc(abs(site, channel.homePath))}</link>
    <description>${esc(channel.description)}</description>
    <language>${channel.language}</language>
    <atom:link href="${esc(selfHref)}" rel="self" type="application/rss+xml" />
${latest ? `    <lastBuildDate>${rfc822(latest)}</lastBuildDate>\n` : ''}${items}
  </channel>
</rss>
`;
}
