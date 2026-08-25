/**
 * sitemapLastmod — a truthful <lastmod> for every URL in the sitemap.
 *
 * ---------------------------------------------------------------------------
 * WHY THIS EXISTS (Growth + Quality, 2026-08-24)
 *
 * The sitemap has carried 82 <loc> entries and ZERO <lastmod> since the
 * hand-patched file was retired on 2026-07-02. A crawler reading it has never
 * had any signal that anything on this site ever changes — which is exactly
 * backwards for a publication that has revised all 76 article pages twice in
 * the last week (the raster og cards on 08-18, the Arabic display layer on
 * 08-23) without a single crawler being told.
 *
 * WHY NOT THE OBVIOUS SOURCES
 *
 *   - Build time for every page. Trivial to emit, and worse than nothing:
 *     every page would claim to change on every deploy. Google states plainly
 *     that it ignores lastmod values it judges unreliable, and "all 82 pages
 *     changed simultaneously, again" is the canonical unreliable pattern. We
 *     would be spending the signal to say nothing.
 *   - The article's frontmatter `date`. That is the PUBLICATION date, and
 *     using it as lastmod asserts the page has not changed since it published.
 *     For every page on this site that assertion is false.
 *
 * WHAT WE USE INSTEAD
 *
 * Git. The last commit that touched the files a page is actually built from.
 * That is a real modification date, not a proxy for one.
 *
 * A page's date is max(its own content file, the newest chrome file), because
 * a change to the layout, a shared component, the i18n display layer or the
 * stylesheet genuinely re-renders every page that includes it. The 08-23
 * Arabic fix edited no article file and changed what all 38 Arabic pages say;
 * a per-content-file-only lastmod would have reported nothing changed.
 *
 * FAIL-LOUD (rulings #16 and the 08-16 silent-pass trap)
 *
 * `actions/checkout@v4` clones at depth 1 by default. In a shallow clone
 * `git log -- <path>` returns an empty string for almost everything, so a
 * naive version of this file would emit no lastmod in CI while passing every
 * check locally — the precise shape of the 07-02 lockfile outage and the
 * reason ruling #16 says verify in the judging environment. So: we assert the
 * repository is not shallow, and we assert the map is non-empty. An assertion
 * that finds nothing to check has FAILED, not passed. The deploy workflow sets
 * fetch-depth: 0 in the same commit as this file.
 *
 * THREE FAILURES, NOT ONE (2026-08-25)
 *
 * The first version of this guard treated every git failure identically and so
 * made the whole site unbuildable outside a git work tree — caught the next
 * morning when the sandbox build (which copies the tree to /tmp to route around
 * the .git/index.lock boundary) died on `git rev-parse`. The conditions are not
 * the same and must not share a branch:
 *
 *   - SHALLOW repo -> the data would be WRONG, silently. Always fatal. This is
 *     the case the guard was actually built for.
 *   - NO repo at all -> the data is ABSENT, and absent is loud by nature: the
 *     sitemap simply carries no lastmod, which is where we stood until
 *     yesterday. Fatal in CI, where a missing lastmod is a real regression;
 *     a loud warning anywhere else, so the tree stays buildable from a copy.
 *   - Repo present and non-shallow but EMPTY map -> malformed. Always fatal.
 *
 * The rule this encodes: a fail-loud guard must distinguish the condition it
 * was built for from the conditions that merely resemble it. Wrong data and
 * missing data are different failures and deserve different answers.
 * ---------------------------------------------------------------------------
 */

import { execFileSync } from 'node:child_process';

const git = (args) =>
  execFileSync('git', args, {
    encoding: 'utf8',
    maxBuffer: 32 * 1024 * 1024,
    stdio: ['ignore', 'pipe', 'pipe'],
  });

/** True when we are inside a usable git work tree at all. */
function hasGitWorkTree() {
  try {
    return git(['rev-parse', '--is-inside-work-tree']).trim() === 'true';
  } catch {
    return false;
  }
}

/**
 * Files that, when changed, change what every rendered page SAYS.
 *
 * `web/src/styles` is deliberately NOT in this list. Google's own definition of
 * lastmod is the date of the last *significant* modification, and it discounts
 * a lastmod it judges unreliable — "all 82 pages changed again" being the
 * canonical unreliable pattern. A stylesheet edit (today's print block, say)
 * changes how a page looks and not one word of what it states, so it must not
 * bump 82 dates. The 08-23 Arabic display layer, which edited no article file
 * and changed what all 38 Arabic pages say, must — and does, via src/lib.
 *
 * The line is: presentation is excluded, rendered content is included.
 */
const CHROME_GLOBS = [
  'web/src/layouts',
  'web/src/components',
  'web/src/lib',
  'web/src/pages',
];

/** repo-relative path -> ISO-8601 date of the most recent commit touching it. */
function buildFileDateMap() {
  if (git(['rev-parse', '--is-shallow-repository']).trim() === 'true') {
    throw new Error(
      'sitemapLastmod: repository is SHALLOW. Git history is the only truthful ' +
        'source for <lastmod>; a shallow clone would emit an empty or wrong one ' +
        'silently. Set `fetch-depth: 0` on actions/checkout.'
    );
  }

  // `:/` is git's repo-root-relative pathspec magic, and it is load-bearing.
  //
  // A bare `web/src` pathspec is resolved relative to the CURRENT DIRECTORY, and
  // both this build and the CI job run from `web/` — where `web/src` matches
  // nothing at all, git exits 0, and the map comes back empty. The workflow sets
  // `working-directory: web`, so the first push carrying this file would have
  // failed the deploy outright. `:/web/src` is anchored at the repo root and
  // resolves identically from any cwd, which is the only property that makes the
  // emitted paths (`web/src/...`, repo-relative) match the keys we look up.
  const out = git([
    'log',
    '--pretty=format:%cI',
    '--name-only',
    '--',
    ':/web/src',
    ':/web/public',
  ]);

  const map = new Map();
  let current = null;
  for (const line of out.split('\n')) {
    const row = line.trim();
    if (!row) continue;
    if (/^\d{4}-\d{2}-\d{2}T/.test(row)) {
      current = row;
      continue;
    }
    // git log is newest-first, so the FIRST time we see a path is its latest change.
    if (current && !map.has(row)) map.set(row, current);
  }

  if (map.size === 0) {
    throw new Error(
      'sitemapLastmod: git produced an EMPTY file/date map. Refusing to emit a ' +
        'sitemap with no lastmod rather than passing silently.'
    );
  }
  return map;
}

/**
 * Pass the commit timestamp through UNTRUNCATED.
 *
 * The first version of this file emitted YYYY-MM-DD; @astrojs/sitemap then
 * normalised it to `...T00:00:00.000Z`, i.e. it invented a midnight. That is
 * precisely the fabrication the 08-23 structured-data work refused when it made
 * `datePublished` a date and not a timestamp. Here we do not have to choose
 * between a truncated date and an invented hour, because git gives us the real
 * one: `%cI` is the actual commit time with its actual offset.
 */
const iso = (d) => new Date(d).toISOString();
const newer = (a, b) => (!a ? b : !b ? a : new Date(a) > new Date(b) ? a : b);

export function createLastmodResolver() {
  if (!hasGitWorkTree()) {
    const msg =
      'sitemapLastmod: not inside a git work tree, so no truthful <lastmod> can ' +
      'be derived. The sitemap will be emitted WITHOUT lastmod.';
    // In CI this is a regression: the deploy is the judging environment and a
    // sitemap that quietly loses its lastmod there is exactly the silent pass
    // ruling #16 exists to prevent.
    if (process.env.CI) {
      throw new Error(
        msg.replace('will be emitted WITHOUT lastmod.', 'would be emitted WITHOUT lastmod.') +
          ' Refusing to build in CI. Check actions/checkout ran and fetch-depth: 0 is set.'
      );
    }
    console.warn(`[sitemapLastmod] ${msg} (non-CI build — continuing.)`);
    return () => null;
  }

  const files = buildFileDateMap();

  let chrome = null;
  for (const [path, date] of files) {
    if (CHROME_GLOBS.some((g) => path.startsWith(g + '/'))) chrome = newer(chrome, date);
  }
  if (!chrome) {
    throw new Error('sitemapLastmod: no chrome file dates resolved — map is malformed.');
  }

  const forContent = (dir, slug) =>
    newer(files.get(`web/src/content/${dir}/${slug}.md`) ?? null, chrome);

  /**
   * @param {string} pathname e.g. "/madar/ar/articles/2026-07-07-sudan-exam-continuity/"
   * @returns {string|null} YYYY-MM-DD
   */
  return function lastmodFor(pathname) {
    const p = pathname.replace(/^\/madar/, '').replace(/\/$/, '') || '/';

    let m;
    if ((m = p.match(/^\/ar\/articles\/(.+)$/))) return iso(forContent('articles-ar', m[1]));
    if ((m = p.match(/^\/articles\/(.+)$/))) return iso(forContent('articles', m[1]));

    // /valence/ is a hand-written static file under public/ — it has its own life.
    if (p === '/valence') {
      const d = files.get('web/public/valence/index.html');
      return d ? iso(d) : null;
    }

    // Index pages (/, /ar, /about, /editions, /ar/editions) list the corpus, so
    // they change when the chrome changes AND when any article changes.
    let newestArticle = null;
    for (const [path, date] of files) {
      if (path.startsWith('web/src/content/')) newestArticle = newer(newestArticle, date);
    }
    return iso(newer(chrome, newestArticle));
  };
}
