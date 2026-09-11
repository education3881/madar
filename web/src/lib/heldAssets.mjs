/**
 * heldAssets — a held piece contributes no BYTES to the published site.
 *
 * ---------------------------------------------------------------------------
 * WHY THIS EXISTS (Quality, 2026-09-09 — the 09-08 forward question, answered)
 *
 * Ruling #18 makes `approved: false` the hold. The 09-06 review extended it:
 * *a held file is not part of the publication — nothing derived from the
 * content set may read it* — and 09-08 closed the last known path, the
 * sitemap's `<lastmod>`. After that fix a held piece contributes no page, no
 * sitemap entry, no feed item and no date.
 *
 * It still contributed FILES. Its hero still and its raster share card live in
 * `web/public/`, and everything in `public/` is copied wholesale into `dist`.
 * Measured on the 09-09 build: **six assets, ~48 KB, for three unpublished
 * Edition 05 pieces**, with **zero references** to any of them from any served
 * HTML or XML.
 *
 * "Unreferenced" was the argument for leaving them, and it is the wrong test —
 * the same wrong test as the 08-18 og:image defect, where a file that resolved
 * perfectly was useless to the consumer that fetched it. The right test is what
 * a stranger can GET. Every one of those paths is derivable from the slug
 * pattern the rest of the site publishes, so:
 *
 *     /madar/og/2026-09-01-sudan-cant-wait-to-learn.png      -> 200
 *     /madar/articles/2026-09-01-sudan-cant-wait-to-learn/   -> 404
 *
 * A share card is a derivable promise (#36) and this one promises an article
 * that does not exist. Worse, the still is an SVG and carries its own
 * `<title>` in plain text — "The Still · Sudan — the classroom that left home,
 * and the returning arc" — so the withheld piece's SUBJECT is served in
 * readable text at a guessable URL. An edition that ships as one gated wave
 * was pre-announcing its contents to anyone who typed the pattern.
 *
 * DECISION (Manager + Web Developer, in writing, 2026-09-09): **withhold.**
 * Ship-early's only benefit was a smaller flip commit; the flip commit is a
 * one-line flag change either way, because the assets stay on disk in
 * `public/` — where the publish gate already checks for them — and are removed
 * from `dist` at the end of the build. Nothing about the gate changes; the
 * bytes simply stop being served a wave early.
 *
 * HOW, AND WHY THIS SHAPE
 *
 * A build-time hook, not a hand-kept exclude list: anything that must equal
 * "the current set of held pieces" is generated from the content collection or
 * it is correct on the day it is written and silently wrong the next day
 * (RUNBOOK, 2026-06-07). The hold is read through `heldContentFiles()` — the
 * SAME parser the lastmod resolver uses — so the two can never disagree about
 * what "held" means.
 *
 * Fail-loud, per the module it borrows from: if the slug's assets are missing
 * from `public/` entirely we say so rather than silently succeeding, because
 * "nothing to remove" and "nothing was there" are different facts and only one
 * of them is fine. An asset sweep that finds nothing to check has failed, not
 * passed (08-16 silent-pass trap).
 */

import { readdirSync, rmSync, existsSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join, dirname, resolve, basename } from 'node:path';
import { fileURLToPath } from 'node:url';

import { heldContentFiles } from './sitemapLastmod.mjs';

/** Directories under `public/` that carry per-slug assets. */
const SLUG_ASSET_DIRS = ['stills', 'og'];

/**
 * The path that proves a candidate is the repo root — the first of the content
 * directories `heldContentFiles` will read. A root is accepted only if the
 * thing we intend to read from it actually exists there.
 */
const CONTENT_PROBE = 'web/src/content/articles';

/**
 * Locate the repo root WITHOUT making git a precondition of the build.
 *
 * ---------------------------------------------------------------------------
 * DEFECT FOUND 2026-09-10 (Verifier's QA pass, one day after this hook shipped)
 *
 * The first version of this hook opened with a bare `git rev-parse
 * --show-toplevel` and used its output unchecked. In CI that works. Outside a
 * git work tree it does not merely degrade — it throws, and takes the whole
 * build with it:
 *
 *     [madar:withhold-held-assets] Command failed: git rev-parse --show-toplevel
 *     fatal: not a git repository
 *
 * This is the SAME defect the sitemap lastmod resolver carried on 2026-08-25
 * and the same lesson (#16, verify in the judging environment): a build step
 * that reaches for git makes the site unbuildable anywhere git is not, and
 * `heldContentFiles` never needed git at all — it does filesystem reads. The
 * hold was being read through a tool that has nothing to do with the hold.
 *
 * Two rules restored here, both already in the guidebook:
 *  - **Wrong data and missing data get different answers** (08-25). A missing
 *    git binary or a non-repo directory is not by itself a defect; a root we
 *    cannot find the CONTENT in is.
 *  - **Derive it from the thing itself** (#36). The primary route is this
 *    module's own location, which is deterministic, needs no external process,
 *    and is correct in a shallow clone, a worktree, an export or a copy. git is
 *    consulted LAST and only as one more candidate, never as an authority —
 *    and even its answer must pass the existence probe, so a git root that
 *    points somewhere without content cannot silently aim the sweep at nothing.
 */
function resolveRepoRoot() {
  const moduleDir = dirname(fileURLToPath(import.meta.url));
  const candidates = [
    // web/src/lib/heldAssets.mjs -> repo root
    resolve(moduleDir, '..', '..', '..'),
    // the astro project's parent (build cwd is `web/` in CI), then cwd itself
    resolve(process.cwd(), '..'),
    process.cwd(),
  ];

  try {
    candidates.push(
      execFileSync('git', ['rev-parse', '--show-toplevel'], {
        encoding: 'utf8',
        stdio: ['ignore', 'pipe', 'ignore'],
      }).trim()
    );
  } catch {
    // Not a work tree, or no git on PATH. Not fatal on its own.
  }

  for (const candidate of candidates) {
    if (candidate && existsSync(join(candidate, CONTENT_PROBE))) return candidate;
  }

  throw new Error(
    `heldAssets: could not locate the content set. Probed for "${CONTENT_PROBE}" ` +
      `under: ${candidates.filter(Boolean).join(', ')}. Either the content ` +
      'directories moved — in which case this sweep is checking nothing and the ' +
      'hold is unenforced — or the build is running somewhere it cannot see the ' +
      'repo. Both are defects; neither is a silent pass.'
  );
}

export function withholdHeldAssets() {
  return {
    name: 'madar:withhold-held-assets',
    hooks: {
      'astro:build:done': ({ dir, logger }) => {
        const repoRoot = resolveRepoRoot();

        // heldContentFiles returns repo-relative content PATHS; the slug is the
        // filename. Both language files of a held pair yield the same slug.
        const slugs = new Set(
          [...heldContentFiles(repoRoot)].map((p) => basename(p, '.md'))
        );

        const distDir = fileURLToPath(dir);
        let removed = 0;

        for (const slug of slugs) {
          let foundForSlug = 0;
          for (const sub of SLUG_ASSET_DIRS) {
            const subDir = join(distDir, sub);
            if (!existsSync(subDir)) continue;
            for (const name of readdirSync(subDir)) {
              // Match the slug as the filename STEM, not as a substring: a
              // future slug that merely contains a held slug must not be swept
              // away with it.
              if (name === slug || name.startsWith(`${slug}.`)) {
                rmSync(join(subDir, name), { force: true });
                removed += 1;
                foundForSlug += 1;
                logger.info(`withheld ${sub}/${name} (approved: false)`);
              }
            }
          }
          if (foundForSlug === 0) {
            throw new Error(
              `heldAssets: held slug "${slug}" has NO assets in dist. Either its ` +
                'hero still and share card were never generated — which the publish ' +
                'gate requires before the wave flips — or the asset directories ' +
                'moved and this sweep is now checking nothing. Both are defects; ' +
                'neither is a silent pass.'
            );
          }
        }

        if (slugs.size === 0) {
          logger.info('no held pieces; nothing withheld');
        } else {
          logger.info(
            `withheld ${removed} asset(s) for ${slugs.size} held piece(s) — a held ` +
              'piece contributes no bytes to the published site'
          );
        }
      },
    },
  };
}
