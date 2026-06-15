/**
 * Read an edition cover SVG from /public/covers/ at build time and return it as
 * a string so it can be inlined into a page with `set:html`. Inlining (rather
 * than <img src>) lets the cover inherit the page's CSS and brand fonts so the
 * baked-in wordmark/label render correctly.
 *
 * Astro builds from the `web/` directory, so cover files resolve against
 * `process.cwd()/public/covers/<file>`.
 *
 * Returns the SVG markup with any leading <?xml ...?> declaration stripped, or
 * null if the file is missing.
 */
import { readFileSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';

export function inlineCover(file: string): string | null {
  if (!file) return null;
  const p = resolve(process.cwd(), 'public/covers', file);
  if (!existsSync(p)) return null;
  try {
    return readFileSync(p, 'utf-8').replace(/^<\?xml[^?]*\?>\s*/, '');
  } catch {
    return null;
  }
}
