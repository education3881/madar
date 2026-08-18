// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Madār v0.1 — project page at https://education3881.github.io/madar/
// If we later move to a user page (repo renamed to education3881.github.io)
// or a custom domain, set base = '/' and update `site` accordingly.

export default defineConfig({
  integrations: [
    // Build-time sitemap (replaces the hand-patched public/sitemap.xml, retired 2026-07-02).
    // i18n block emits hreflang alternates pairing /path <-> /ar/path, matching the
    // hand-patched format so bilingual discoverability is preserved.
    sitemap({
      i18n: {
        defaultLocale: 'en',
        locales: { en: 'en', ar: 'ar' },
      },
      // customPages: pages served from public/ as static files are NOT part of
      // the Astro route graph, so the sitemap integration cannot see them and
      // will silently omit them. Found 2026-08-17: /valence/ (a 540 KB
      // standalone instrument, added 2026-08-08) had been served, unlisted and
      // unlinked, since the day it shipped — no sitemap entry, no inbound link,
      // therefore no discovery path at all. Anything added under public/ that is
      // meant to be found must be listed here in the same commit.
      customPages: ['https://education3881.github.io/madar/valence/'],
    }),
  ],
  site: 'https://education3881.github.io',
  base: '/madar',
  trailingSlash: 'ignore',
  build: {
    inlineStylesheets: 'auto',
    format: 'directory',
  },
  prefetch: {
    prefetchAll: false,
    defaultStrategy: 'hover',
  },
  vite: {
    build: {
      cssCodeSplit: false,
    },
    // Allow overriding the vite dependency cache directory via env var so the
    // build can run in sandboxed environments where node_modules/.vite is
    // not writable. Production deploys (GitHub Actions) leave this unset and
    // vite uses its default location.
    cacheDir: process.env.VITE_CACHE_DIR || undefined,
  },
});
