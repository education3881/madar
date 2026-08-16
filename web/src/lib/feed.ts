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

export interface FeedItem {
  title: string;
  /** Site-absolute path INCLUDING the base prefix, e.g. /madar/articles/slug/ */
  path: string;
  description?: string;
  date: Date;
  /** Country, used as the item category. */
  category?: string;
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

export function renderFeed(channel: FeedChannel, site: URL | undefined): string {
  const items = [...channel.items]
    .sort((a, b) => b.date.getTime() - a.date.getTime())
    .map((item) => {
      const link = abs(site, item.path);
      return [
        '    <item>',
        `      <title>${esc(item.title)}</title>`,
        `      <link>${esc(link)}</link>`,
        `      <guid isPermaLink="true">${esc(link)}</guid>`,
        item.description ? `      <description>${esc(item.description)}</description>` : null,
        item.category ? `      <category>${esc(item.category)}</category>` : null,
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
