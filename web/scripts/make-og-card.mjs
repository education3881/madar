/**
 * make-og-card.mjs — render an article's hero still into its raster share card.
 *
 * WHY THIS FILE EXISTS (2026-09-14)
 * ---------------------------------
 * Since 2026-08-18 every article has carried a PNG share card derived from its
 * SVG still, because no major social consumer renders SVG and for 83 days every
 * share arrived with no image while the log recorded the image as present. The
 * conversion has been correct ever since — and has lived nowhere. Each run has
 * retyped it, which is how it came to be typed into a stray file at the repo
 * root today. A step that is part of the publish gate belongs on disk.
 *
 * It must run from `web/` so Node resolves `sharp` out of `web/node_modules`.
 *
 *   cd web && node scripts/make-og-card.mjs <slug> [<slug> ...]
 *
 * Reads  public/stills/<slug>.svg
 * Writes public/og/<slug>.png at 1200x600 — the dimensions the article routes
 * promise in og:image:width / og:image:height. Density 200 is what keeps the
 * hairline strokes of the stills from disappearing at raster size; the palette
 * pass is what keeps a two-colour line drawing near the corpus average of
 * ~11 KB instead of the ~60 KB a full-colour PNG of the same image costs.
 *
 * Fails loudly and per-slug: a missing still is an error, never a skip.
 */
import sharp from 'sharp';
import fs from 'node:fs';

const slugs = process.argv.slice(2);
if (slugs.length === 0) {
  console.error('usage: node scripts/make-og-card.mjs <slug> [<slug> ...]');
  process.exit(2);
}

let failed = 0;
for (const slug of slugs) {
  const src = `public/stills/${slug}.svg`;
  const out = `public/og/${slug}.png`;
  if (!fs.existsSync(src)) {
    console.error(`MISSING still: ${src}`);
    failed++;
    continue;
  }
  await sharp(fs.readFileSync(src), { density: 200 })
    .resize(1200, 600, { fit: 'cover' })
    .png({ compressionLevel: 9, palette: true, colours: 32 })
    .toFile(out);
  console.log(`${out}  ${fs.statSync(out).size} bytes`);
}
process.exit(failed ? 1 : 0);
