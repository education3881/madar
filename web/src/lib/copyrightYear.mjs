/**
 * copyrightYear — the footer's year, derived from the repository rather than from
 * the clock the build happened to run on.
 *
 * Added 2026-10-27 by the growth function, from standing-queue item 43's
 * enumeration: *which served claims live in code rather than in content?*
 *
 * `SiteFooter.astro` read `new Date().getFullYear()` from 2026-05-25 until today.
 * That is a claim about **when the build ran**, served on all 134 pages, and it has
 * the one property no instrument this operation owns can see: it agrees with
 * itself. Every comparison we make — `qa_live_drift`, the verify job's
 * byte-compare, `qa_date_identity`, `qa_served_manifest` — puts one byte beside
 * another byte, and two builds run in the same calendar year produce identical
 * bytes here no matter what the repository says. On 1 January 2027 every page
 * served from a December-2026 build silently begins carrying a wrong year, and
 * nothing goes red, because nothing changed. It is ruling #117's general form
 * (*a served artefact is read in the reader's present*) arriving through the
 * build clock instead of through a tense.
 *
 * The fix is the one `articleJsonLd` took on 2026-10-26: use the resolver the
 * sitemap already uses, so the year is a fact about the newest commit touching an
 * approved file or the chrome. Two properties follow, and both are the point:
 *   - **deterministic** — the same tree produces the same byte, on any day;
 *   - **falsifiable** — the value can now disagree with the repository, which
 *     means an instrument can be pointed at it. A build-clock year cannot be
 *     wrong in a way anything can detect.
 *
 * Memoised at module scope on purpose: `createLastmodResolver()` walks git
 * history, and this is called from a component that renders on every one of the
 * 134 pages.
 */
import { createLastmodResolver } from './sitemapLastmod.mjs';

let cached = null;

export function copyrightYear() {
  if (cached) return cached;
  // The site-wide notice takes the site's own index date, not the page's: a
  // copyright line is one claim about the publication, never 134 claims about
  // 134 pages.
  cached = createLastmodResolver()('/').slice(0, 4);
  if (!/^20\d\d$/.test(cached)) {
    throw new Error(`copyrightYear: resolver returned ${cached}, not a four-digit year`);
  }
  return cached;
}
