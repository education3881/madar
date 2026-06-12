# Founder request — custom domain decision memo (due in Brief No. 15, 2026-06-12)

**From:** Vini, 2026-06-11, after pushing `3d909a5`.
**Ask, verbatim in spirit:** should Madār buy a custom domain and professionalise? He wants a recommendation **with the migration impact spelled out** — not just a yes/no.

## What tomorrow's run must deliver (Manager + Web Developer + Growth, jointly)

A one-page decision memo inside the daily brief covering:

1. **Recommendation** (buy / hold / buy-but-migrate-later) with reasoning in Madār's frame: trust is the moat; the URL is part of the brand chrome.
2. **SEO / discoverability impact** — what moves and what breaks: indexed-page reset, `<link rel=canonical>`, 301 behaviour on GitHub Pages (custom domain redirects project-pages URLs automatically or not — verify), hreflang pairs (we have 27 URLs, EN/AR alternates), Search Console re-registration (the 06-07 sitemap packet was never submitted — a clean-cut opportunity: register the new domain instead of the github.io property), and the fact that the site is ~2.5 weeks old with near-zero inbound links — **migration cost is at its lifetime minimum right now**.
3. **Technical migration on GitHub Pages** — CNAME file, DNS (apex A/ALIAS + www), enforce-HTTPS cert wait, `site`/`base` change in `astro.config` (the `/madar/` base path goes away — every internal URL changes; the build must be re-verified page by page), sitemap regeneration (ties into the @astrojs/sitemap weekly item — do both in one move, not two).
4. **What else "more professional" buys** — email on the domain (Substack from-address deliverability), social handles consistency, the wordmark already carries the brand.
5. **Costs & registrar posture** — typical .com/.org ~USD 10–15/yr; flag .edu is unavailable; note privacy-respecting registrar options; name candidates (madar.* availability check) — **the purchase itself is Vini's action** (paid infra = escalation list).
6. **Risks of waiting** — every week adds indexed URLs and inbound links that will need redirecting; the Substack launch and Search Console submission are both pending and both bind to a URL — do the domain BEFORE either fires, or pay the migration twice.

## Constraint reminders
- No third-party trackers regardless of domain.
- The github.io origin keeps working as redirect source once a custom domain is set (verify exact behaviour for *project* pages vs user pages — known nuance).
- Weekly review (Sun 14 June) should ratify whatever the memo recommends; the memo itself ships tomorrow per the founder's ask.
