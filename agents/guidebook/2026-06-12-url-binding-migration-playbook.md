# Method — what binds to a URL, and when to move: the migration-cost clock

**Logged:** 2026-06-12 · **Trigger:** the founder's custom-domain decision request (2026-06-11) · **Class:** infrastructure/discoverability method

## The principle

A publication's URL is not an address; it is an accumulating ledger of bindings. Every week of operation, more external systems copy the current URL into places the publication does not control. Migration cost is therefore **a clock, not a constant** — it only goes up, and it steps up discontinuously each time a new system binds.

## The binding ledger (what copies your URL, in escalating cost-to-change)

| Binding | Cost to change later | Madār status 2026-06-12 |
|---|---|---|
| Internal links/config | One config edit + rebuild (cheap, fully owned) | `astro.config` `site`+`base`; static sitemap (105 origin refs); robots.txt (1) — *no hardcoded base in src, verified* |
| Search-engine index | Re-crawl + re-rank; 301s carry most equity but reset takes weeks | **Not yet bound** — Search Console never registered, sitemap never submitted |
| Newsletter platform | From-address + archive links bind at first send | **Not yet bound** — Issue 01 send-ready, unsent |
| Social bios + posted links | Editable bios cheap; posted permalinks immutable | IG grid not yet posted |
| Inbound links (others' sites) | Unfixable without 301s; the true lock-in | ~zero (site is 18 days old) |
| Citations (academic, policy docs, PDFs) | Permanent; 301 is the only remedy | None known |

## The rule of record

**Migrate before the next binding fires, or pay the migration twice.** The cheapest migration day in a publication's life is the day before its first external binding. For Madār, two bindings are pending and both bind to a URL at the moment of first use: Search Console registration and the Substack Issue 01 send. The domain decision therefore *precedes* both in any rational ordering — this is a sequencing fact, not an opinion about whether to buy.

## GitHub Pages specifics (verified against GitHub Docs, 2026-06-12)

- Custom domain on a project site: set DNS (apex `A` 185.199.108/109/110/111.153 + `www` CNAME → `<user>.github.io`), add the domain in Pages settings; with an Actions deploy the `CNAME` file must ship in the build artifact (put it in `public/`).
- Apex + `www` both configured → GitHub auto-redirects between them (docs-confirmed). The old `<user>.github.io/<repo>/` URLs 301 to the custom domain — community-documented for project pages; **spot-check deep paths with `curl -I` post-cutover** before declaring done.
- HTTPS: Let's Encrypt cert provisions after DNS propagates (minutes to ~24h); "Enforce HTTPS" is a second, manual toggle — the site serves plain HTTP until it's on.
- Domain verification (Settings → Pages → verified domains) before binding prevents takeover squatting; do it before DNS, not after.
- Base-path change (`/madar` → `/`) means **every internal URL changes**: full rebuild + page-by-page QA, and the static sitemap must be regenerated — fold the `@astrojs/sitemap` migration (standing weekly item) into the same move; never do two URL-set changes in two pushes.

## Reusable test

Before adopting any external platform or registration, ask: *does this system copy our URL into storage we don't control?* If yes, it is a binding; the migration clock steps up when it fires; sequence accordingly.

— Manager (with Web Developer + Growth) · 2026-06-12
