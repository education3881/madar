# Growth — 2026-08-17: the orphan-page audit, and VALENCE brought onto the map

**Run:** daily, Brief 54 · **Owner:** Growth, with the Web Developer executing · **Bet context:** the standing growth bet is *the first 20 qualified readers*; this is a surface fix that has to land before any of them can arrive by search or by share.

---

## What was found

Yesterday's weekly review codified the **site-chrome link sweep**: enumerate every `href`/`src` the layout emits and assert each resolves in `dist`. It ran green today — **98 unique targets across seven representative pages, zero unresolved.**

Running it exposed the question it does not ask. The chrome sweep checks *links pointing outward*. It cannot see a page that **nothing points to.**

`/madar/valence/` — **VALENCE — The Elements of Good Education**, a 540 KB standalone instrument mapping *58 measurable elements of a young life and 378 verified bonds between them*, shipped 2026-08-08 and revised 2026-08-10 — has been served continuously since that day with:

| Check | State before today |
|---|---|
| Inbound links from anywhere on the site | **0** (grepped across all 82 built pages) |
| Entry in `sitemap-0.xml` | **absent** |
| `<link rel="canonical">` | **absent** |
| Open Graph / Twitter card tags | **absent** — a share rendered as a bare URL |
| `<meta name="robots">` | absent (defaults to indexable, but nothing pointed a crawler at it) |
| Outbound links back into Madār | **0** — a reader who arrived had no route into the publication |
| Feed autodiscovery | absent |

**Cause, and why no existing check caught it.** VALENCE is served from `web/public/` as a static file. `@astrojs/sitemap` enumerates the **Astro route graph**; files in `public/` are copied verbatim and never enter it, so the sitemap omitted them silently. The page count and the sitemap count had been disagreeing by exactly one — **82 pages, 81 sitemap URLs** — since 08-08, and no check compared the two numbers.

**Discoverability consequence, stated plainly:** `robots.txt` points crawlers at the sitemap; the sitemap did not list VALENCE; nothing on the site linked to it. For nine days, the only way to reach the most linkable asset Madār has was to be told the URL by a human.

---

## What shipped today

1. **`customPages` in `astro.config.mjs`** — `/madar/valence/` now enters the sitemap. Sitemap URLs **81 → 82**, matching the served page count exactly. The comment in the config states the general rule so the next `public/` addition does not repeat this.
2. **Head tags on VALENCE** — canonical, `robots`, full Open Graph set (`type`, `site_name`, `title`, `description`, `url`), Twitter summary-large-image card, and RSS autodiscovery pointing at the English feed. A share of this page now renders with a title and a description instead of a bare link.
3. **A route back into the publication** — a discreet closing block: *"A Madār instrument"*, the publication's one-line description, and three links: **Read Madār · Editions · النسخة العربية**. Styled in VALENCE's own palette variables (`--void`, `--ink2`, `--ink3`, `--good`), not the site's, so it reads as part of the page rather than pasted-on chrome.

Verified after the change: build exit 0, **82 pages, 82 sitemap URLs**, both feeds well-formed at 38 items, chrome sweep still zero unresolved.

---

## What is deliberately NOT done, and why

**No nav item was added.** Where VALENCE sits in the site's chrome — a fourth nav item, a homepage block, an editions-adjacent card, or nowhere at all — is an editorial and design decision, not a QA fix. Adding a nav item unilaterally would be the mirror of yesterday's defect: a promise made in the chrome without anyone deciding it should be made.

**Handed forward to the Designer and the founder:**

- VALENCE is bilingual Madār's only English-only surface. Does it get an Arabic edition, an Arabic-language entry point, or an explicit English-only note? Until decided, the AR chrome should not link it.
- No `og:image`. A share currently renders with title and description but no card image — one still would materially change how it travels. **The single highest-leverage remaining item**, and the Designer's call.
- Placement in the chrome, if any.

---

## The rule this earns (RUNBOOK, codified today)

> **The QA pass sweeps links outward *and* pages inward.** The chrome sweep asserts that every link the layout emits resolves. The **orphan sweep** asserts the converse: every page the build serves has at least one inbound path — a link from another page, or an entry in the sitemap, ideally both. The mechanical form is one comparison that had been available all along: **served page count == sitemap URL count**, with any difference named rather than tolerated.

Third member of a family the operation now recognises on sight: the **flag-sweep inversion** (2026-08-09 — an assertion that passes vacuously), the **chrome 404** (2026-08-16 — a check scoped to content never enumerated the layout), and this — **a check that enumerates links can never find a page that has none.** The general form, now stated three ways: *a green check is scoped to what it enumerates.* The counter-discipline is to keep asking what the current sweep structurally cannot see.

---

## Growth read

No traffic numbers, by design — Madār carries no third-party tracker, so there are no visitor counts to report and none will be invented. What changed today is **surface**, which is the precondition for the return-rate measurement the bet actually wants: an asset that was unreachable by search, unrenderable in a share, and a dead end on arrival is now discoverable, shareable, and has three doors back into the publication. The first read comes when Substack sends and attributable inbound exists.

— Growth · 2026-08-17
