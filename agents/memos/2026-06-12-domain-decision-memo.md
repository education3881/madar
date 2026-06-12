# Decision memo — custom domain for Madār

**To:** Vini · **From:** Manager, with Web Developer (technical) and Growth (discoverability) · **Date:** 2026-06-12 (Brief No. 15, as requested 2026-06-11)
**Question:** should Madār buy a custom domain and professionalise — with migration impact spelled out?

## Recommendation: BUY NOW — before Search Console and before Issue 01 sends

Not "buy eventually." The reasoning is sequencing, not vanity. Two pending launches — Search Console registration (sitemap packet ready since 06-07, never submitted) and the Substack Issue 01 send (send-ready since 06-01) — each bind permanently to whatever URL exists when they fire. Search Console binds a *property*; Substack binds a *from-address and archive links*. Fire them on `education3881.github.io/madar` and the migration is paid twice: once in redirects, once in re-registration and reader confusion. The site is 18 days old, has 27 indexed-or-indexable URLs and effectively zero inbound links. **Migration cost is at its lifetime minimum this week and steps up the moment either launch fires.** Trust is the moat, and the URL is part of the brand chrome — `education3881.github.io` reads as a throwaway account, which taxes every share, every citation, every byline the publication earns.

## Migration impact (the part you asked for spelled out)

**SEO / discoverability — what moves, what breaks:**
- Near-zero loss *today*: no Search Console property exists, the sitemap was never submitted, inbound links ≈ 0. There is no rank to protect; there is only future rank to site correctly.
- GitHub serves 301s from the github.io origin to the custom domain once configured (docs-confirmed for domain-level; deep-path behaviour for *project* pages is community-documented — Web Developer spot-checks `curl -I` on article paths post-cutover before we declare done).
- Canonical/hreflang: all 27 URLs and their 12 EN↔AR alternate pairs regenerate from one config change — verified today: **no hardcoded `/madar` anywhere in src**; the origin lives only in `astro.config`, the static `sitemap.xml` (105 refs, regenerated), and one `robots.txt` line.
- Clean-cut opportunity: register Search Console on the *new* domain only — no property migration, no dual-property limbo.

**Technical migration (Web Developer's sequence, ~90 minutes of work + DNS/cert wait):**
1. Verify the domain in GitHub (Settings → Pages → verified domains) *before* any DNS points anywhere — prevents takeover.
2. DNS: apex `A` records → 185.199.108/109/110/111.153; `www` CNAME → `education3881.github.io`. Both, so GitHub auto-redirects apex↔www.
3. `CNAME` file into `web/public/` (the Actions deploy must carry it in the artifact — settings-only configuration is overwritten on next deploy).
4. `astro.config`: `site` → the new domain, `base` → `'/'`. **Every internal URL changes** — full rebuild and page-by-page QA pass (the config already anticipates this; comment is in the file).
5. Fold in the standing `@astrojs/sitemap` migration (weekly item since 06-04) — one URL-set change, not two. robots.txt sitemap line updates with it.
6. HTTPS: wait for the Let's Encrypt cert, then toggle Enforce HTTPS — site is plain-HTTP until that second toggle.
7. Post-cutover checks: deep-path 301 spot-checks, then Search Console registration + sitemap submission on the new domain (Growth's packet, finally fired).

**What else "professional" buys:** a real from-address for Substack (deliverability + reader trust — `@madar.tld` instead of a gmail), consistent social handles, and a citable URL for the audience that matters most to us (ministries, researchers, serious educators — people who notice URLs).

**Costs and registrar posture:** .com/.org typically USD 10–15/yr; .education exists but runs ~3–5× that; .edu unavailable (US accredited institutions only). Privacy-respecting registrars with at-cost pricing and free WHOIS privacy: Cloudflare Registrar, Porkbun. Candidates to check, in preference order: `madar.education`, `madar.pub`, `madarmag.com`, `readmadar.com` (assume `madar.com`/`madar.org` are taken or premium — "madar" is a common Arabic word and name). **The purchase is yours** — paid infrastructure sits on the escalation list by design. Availability check happens at the registrar in the moment; we have not run one.

**Risks of buying now:** trivially small. ~USD 15/yr; an afternoon of Web Developer time; a one-time re-crawl of a 27-URL site nobody links to yet. **Risks of waiting:** every published piece, every grid post, every newsletter send from 06-13 onward writes the github.io URL into systems we don't control. The weekly review (Sun 2026-06-14) should ratify; the cutover should not wait past it.

— Manager · 2026-06-12
