# Madār v0.1 — Web Developer Handoff

**Date:** 2026-05-25
**Build status:** `npm run build` succeeds. All six pages render from a clean tree.

## What's wired

- **Design system** — `src/styles/global.css` carries the Field Atlas tokens (paper / ink / orange / sage / sand) and the type stack (Newsreader, Cormorant Garamond, JetBrains Mono, Amiri, Cairo via Google Fonts in `Base.astro`). Logical properties throughout — RTL works without override sheets.
- **Layouts & chrome** — `Base.astro` is the shell; `SiteHeader.astro` (home + article variants) and `SiteFooter.astro` are the masthead and footer. Both pull in the wordmark SVG when present and fall back to a typographic Madār · مدار pair if it's missing.
- **Home (`/`)** — bilingual masthead with the wordmark SVG inlined, bilingual tagline, "This week" section with the three pieces, About mini-block (EN + AR side by side), macron-divided sections. Matches `_HOME_mockup`.
- **Article template (`/articles/<slug>/`)** — title block, drop cap, mid-article Still (the painterly SVG loaded via `<img>`), pull-quote treatment, marginalia rail, sources list, and a **"Draft — pending source verification"** pill that auto-appears when any source URL is a placeholder. Detects `[PLACEHOLDER SOURCE]` in source titles.
- **About (`/about/`)** — Editor's prose embedded directly with proper headings and the bilingual section markers. Arabic close line at the foot.
- **Arabic home (`/ar/`)** — RTL masthead, Arabic-first chrome, surfaces the Arabic excerpts from Piece B (Jordan) until the full `articles-ar` collection is populated. Links back to `/` for English pieces.
- **Three articles** — moved from `/content-drafts/inbox/` to `/web/src/content/articles/` with the Editor's frontmatter remap applied: `standfirst` → `dek`, sources restructured as `{title, url}` objects, `region` + `level` added, `editorial` → `short` on Piece A, `hero_brief_for_designer` stripped, `contains_composites` preserved (schema extended in `content.config.ts`). All three set `approved: true` per the brief.
- **Stills** — extracted from the Designer's mockups and saved to `/public/stills/<slug>.svg`. Wordmark copied to `/public/wordmark/madar-wordmark.svg`.

## How to run dev locally

```bash
cd web
npm install
npm run dev
```

Open the URL it prints (usually `http://localhost:4321`). `npm run build` produces the static site in `dist/`.

## What's placeholder

- **Wordmark** — v0.1 stand-in per Designer (Cormorant Garamond + Amiri); to be replaced by a commissioned mark. Site still works when it's swapped in.
- **Source URLs on the three pieces** — Editor flagged that real URLs land in the next QA pass. The schema requires valid URLs, so all source entries currently use `https://example.com/placeholder-*` URLs and the article template renders these as plain text (no `<a>`) plus a footer note explaining the situation. The two curated pieces also display the "Draft — pending source verification" pill on the home card and at the top of the article.
- **About-page contact email** — `hello@madar.example` is a placeholder per the Editor's copy.
- **Arabic article collection (`src/content/articles-ar/`)** — empty by design. The schema and glob loader are wired; when Arabic-original or Arabic-translated pieces land, drop the markdown files in and they render at `/ar/articles/<slug>/` (a corresponding `[...slug].astro` under `/ar/articles/` can be added later — for v0.1 only the Arabic home is built).

## What Vini must do before GitHub Pages deploy

1. **Create the repo** under GitHub username `education3881`.
2. **Update `astro.config.mjs`** — set `site` and `base`:
   - Project page (`https://education3881.github.io/<repo>/`): `site: 'https://education3881.github.io'`, `base: '/<repo>'`
   - User page (`https://education3881.github.io/`): `site: 'https://education3881.github.io'`, `base: '/'`
   - Custom domain: `site: 'https://<domain>'`, `base: '/'`
3. **Add a GitHub Actions workflow** for Pages (Astro's standard `astro-pages.yml` works as-is).
4. **Push** and enable Pages → "Build and deployment: GitHub Actions" in repo settings.

## Compromises I made

- The Editor's source URLs are placeholders (`example.com/placeholder-*`). The schema enforces valid URLs, so this is the cleanest way to keep the schema strict while letting v0.1 ship. The article template detects these and renders them as non-links plus a footer note. When Editor returns real URLs, just replace the URL field in each piece's frontmatter — no template change needed.
- The Colombia dek was 14 characters over the schema's 200-char limit. I tightened the phrasing without changing the editorial sense; the Editor can refine further if needed.
- The "Draft — pending source verification" pill is keyed off the string `PLACEHOLDER SOURCE` appearing in a source title (case-insensitive). When the Editor swaps in real titles, the pill disappears automatically.
- The Arabic article pages (`/ar/articles/<slug>/`) aren't wired yet — only the Arabic home. v0.1 deliberately ships English-first with Arabic excerpts; the Arabic full-article route is a v0.2 task once the Arabic collection has content.
- The article template uses `<img src="/stills/<slug>.svg">` rather than inlining the SVG. This costs one extra request per article but keeps the markdown frontmatter clean and lets Designer swap a Still file without touching the template.

— Web Developer

---

## 2026-05-25 (afternoon) — geography-rule scrub + editorial hierarchy

Applied Editor's nine public-copy patches: home now leads with Sierra Leone (Piece A, pinned by slug for v0.1) at `<article class="lead">` with the wide 800×500 Still and the editorial "Read this issue's lead" label, with Jordan and Colombia under a `<section class="also">` register; About page rewritten to drop the country enumeration entirely and replace *Where we look* with *How we choose what to cover*; the new tagline ("Education, written slowly, in two languages" / "التعليم، بتأنٍّ، بلغتين") is live in both languages, the wordmark is now loaded via `<img src="/wordmark/madar-wordmark.svg">` so the Designer's path-outlined v0.2 mark renders directly, and the new line-drawing Stills (chalkboard / textbook / schoolhouse) come through automatically via the existing `/stills/<slug>.svg` convention. `npm run build` succeeds; grep across `/src` for *underrepresented*, *places others*, *twelve countries*, etc. is clean.
