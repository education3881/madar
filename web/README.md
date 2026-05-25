# Web — the publication's site

Astro 5 static site. Deployed to GitHub Pages (free) via GitHub Actions.

## Local development

```bash
cd web
npm install
npm run dev
```

The site runs at `http://localhost:4321`.

## Build

```bash
npm run build       # builds to ./dist
npm run preview     # serves the built site locally
```

## Publishing workflow (for the Editor)

1. Drafts live in `../content-drafts/` while in QA. Vini reviews there.
2. When a draft is approved, move it (preserving filename and frontmatter) to:
   - `src/content/articles/` for English pieces
   - `src/content/articles-ar/` for Arabic pieces
3. Commit and push. GitHub Actions builds and deploys to GitHub Pages.

## Content schema

All articles share one schema, regardless of language. See `src/content.config.ts` for the authoritative version. Required frontmatter:

```yaml
---
title: "Headline"
dek: "One-sentence subhead"               # optional but encouraged
date: 2026-05-25                          # publication date (YYYY-MM-DD)
country: "Sierra Leone"                   # primary country
region: "Africa"                          # MENA | Africa | Asia | LatAm-Caribbean
level: "ECE"                              # ECE | K-12 | Both
themes: ["language preservation", "access"]
type: "essay"                             # curated | short | essay
sources:
  - title: "Ministry of Basic Education statement"
    url: "https://mbsse.gov.sl/..."
arabicVersion: "slug-of-arabic-version"   # optional cross-link
---
```

## Performance budget

Enforced informally; check before each release:

- Lighthouse: Performance ≥ 95, Accessibility = 100, Best Practices = 100, SEO = 100
- Homepage JS: ≤ 30 KB
- Article page JS: ≤ 10 KB
- First Contentful Paint: < 1s on simulated 3G
- Build time: < 30s

## Deployment

See `/.github/workflows/deploy.yml` (added once brand is locked).

One-time setup:
1. Create a public GitHub repo
2. Push this folder
3. Repo Settings → Pages → Source: GitHub Actions
4. Update `site` and `base` in `astro.config.mjs` to match your repo
