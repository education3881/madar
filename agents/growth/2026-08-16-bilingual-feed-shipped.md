# Growth — the publication becomes subscribable without a platform

**Filed:** 2026-08-16 · Growth + Web Developer, commissioned by the Manager at the weekly review · **shipped, build-verified** — rides the push block, no founder action needed

## The finding that started it

The site footer has carried an **RSS** link since the initial publish (`b3b4041`, 2026-05-25). There has never been a feed behind it. No `@astrojs/rss` dependency, no `src/pages/rss.xml`, no `public/rss.xml` — `/madar/rss.xml` has been a hard 404 on every page, in both languages, for **83 days** and **34 QA passes**. The Arabic footer pointed at the English path, which was itself the 404.

Nothing was wrong with the QA check that ran; the wrong thing was its scope. The daily sweep resolves the links the *content* generates (`related:` refs, hero stills, hreflang pairs, article slugs) and had never enumerated the links the *layout* generates. Codified as a prevention rule in the RUNBOOK this week.

## Why this is the growth bet and not just a bugfix

Three consecutive weekly bets have been in-control preparation that stacks up behind the same two founder calls (custom domain, Substack account). Slice 1 and slice 2 of the engagement list — 35 verified targets — cannot be followed because no accounts exist. Issue 01 has been one-click-ready since 2026-08-09 and cannot send. The operation has been getting better and better at being ready.

A feed is the one subscription mechanism that requires **no account, no platform, no founder call**. It lives on our own surface, it is bilingual by construction, and it costs a reader nothing to keep. It also happens to be the mechanism that most suits this publication: slow cadence, no algorithm, no inbox negotiation. Making good on a promise the footer has been printing for 83 days is a better first bet than a fourth week of staging.

## What shipped

| Artefact | What it does |
|---|---|
| `web/src/lib/feed.ts` | RSS 2.0 builder, **hand-rolled and dependency-free** — see the note below |
| `web/src/pages/rss.xml.ts` | EN feed from the `articles` collection, `approved` only |
| `web/src/pages/ar/rss.xml.ts` | AR feed from the `articles-ar` collection, `approved` only — a peer feed, not a translation of the EN one |
| `web/src/layouts/Base.astro` | `<link rel="alternate" type="application/rss+xml">` autodiscovery in every page head, own language first, peer language second |
| `web/src/components/SiteFooter.astro` | Arabic footer now points at the Arabic feed |

**No new dependency, on purpose.** `@astrojs/rss` would mean editing `package.json` *and* `package-lock.json` from the sandbox — and a hand-edited lockfile is exactly what took CI down for four days on 2026-07-02 (`npm ci` EUSAGE). A feed is sixty lines of string building. The cost/risk arithmetic is not close.

## Build verification (route-around recipe, session-unique log path)

- `astro sync` exit 0 · `astro build` exit 0 · **81 pages, Complete!** — unchanged page count (endpoints are not pages)
- `dist/rss.xml` and `dist/ar/rss.xml` both emitted; both parse as **well-formed XML**, RSS version 2.0
- **38 items each** — exactly the published corpus, EN and AR, parity preserved in the subscription surface as well as the reading surface
- Correct `<language>` per feed; `atom:link rel="self"` absolute and correct; **unique permalink GUIDs**; RFC-822 `pubDate` (not ISO 8601 — the RSS spec's own requirement, and the thing most hand-rolled feeds get wrong)
- Autodiscovery present in built HTML on the EN homepage, the AR homepage and an article page; both footer hrefs now resolve
- Regression checks unchanged: dist parity **38 EN / 38 AR**, sitemap **81 URLs**, zero `approved: false` in the build path

## The measurable claim, and how it gets read

This is not a metric that produces a number next Sunday, and pretending otherwise would be the vanity trap the Charter names. What it produces is a **capability**: from the next deploy, any reader or aggregator can subscribe to Madār in either language without an intermediary, and every future piece reaches them automatically.

**Read at the next weekly (2026-08-23):** (1) both feeds resolve on the *deployed* surface, not just in `dist` — verified in the judging environment per rulings #16/#17; (2) both validate against an external feed validator; (3) the weekly URL sweep re-runs against the 2026-08-09 zero-mentions baseline. When the domain lands, the feed URLs migrate with it — and unlike a Substack list, a feed subscriber base is not stored in someone else's system, so the migration-clock ruling costs us nothing here. That is the second reason to have built it first.

— Growth · 2026-08-16
