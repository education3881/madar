// @ts-check
import { defineConfig } from 'astro/config';

// Madār v0.1 — project page at https://education3881.github.io/madar/
// If we later move to a user page (repo renamed to education3881.github.io)
// or a custom domain, set base = '/' and update `site` accordingly.

export default defineConfig({
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
