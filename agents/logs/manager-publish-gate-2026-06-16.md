# Publish gate — 2026-06-16

**Piece:** "The fee Vietnam waived, and the ones it did not" / «الرسمُ الذي أعفته فيتنام، والرسومُ التي أبقتها»
**Slug:** 2026-06-16-vietnam-tuition-free-public-school · **Edition 02** · curated · Vietnam (Asia) · level Both
**Decision: CLEAR TO STAGE.** First Madār piece on Vietnam; second on Asia. Bilingual ship (EN + AR simultaneous).

This gate ran a **real `astro build`** (the VITE_CACHE_DIR+tmpfs route), not a structural proxy — and the build caught two defects that were fixed before this verdict. Honest record below.

## The four gates

**Gate 1 — Editor verdict (EN).** APPROVE on record: `/content-drafts/verdicts/2026-06-16-vietnam-tuition-free-public-school.md`. All five tests pass; load-bearing URLs re-verified live today (Politburo 28 Feb + NA Res. 217/2025/QH15 26 Jun; principal Nguyễn Thị Vân Hồng via *Tiền Phong*; UNICEF quote tightened to on-record wording). `approved: true` set in the EN frontmatter.

**Gate 2 — Designer hero still.** On disk at `/web/public/stills/2026-06-16-vietnam-tuition-free-public-school.svg` (6.0 KB, valid XML, parses clean). House idiom: one continuous ink line + a single kiln-orange strike through the top ledger entry, closing on a ring; the column stands. Realises the Editor's brief (a line struck, the column still long).

**Gate 3 — Web Developer clean build.** `npx astro build` → **exit 0, "Complete!", 31 pages** (was 29; +2 = EN/AR Vietnam routes). Both routes generated. AR/EN parity **13 = 13**. Related rail resolves to 3 valid slugs in each language. Wordmark renders (inlined; no `<img>` chrome). Homepage (current edition = Ed02) surfaces the new piece in both languages.

**Gate 4 — Arabic Editor verdict.** APPROVE on record: `/content-drafts/verdicts/ar/2026-06-16-vietnam-tuition-free-public-school-ar.md`. Composition (not translation); all Vietnamese named-human + place transliterations verified and fixed in-house (Nguyễn Thị Vân Hồng → نغوين ثي فان هونغ; Nguyễn Kim Sơn → نغوين كيم سون; Trần Thanh Mẫn → تران ثانه مان; Chương Dương → تشونغ دونغ; Hoàn Kiếm → هوان كيم). Teacher-contribution detail attributed to *Tiền Phong*, not our voice. `approved: true` set.

## Two defects the build caught (and the fixes)

1. **EN frontmatter was missing its `hero:` block.** The EN page fell back to a slug-named still but lost its `og:image`, proper `alt`, and caption — a silent parity gap vs. the AR version and the rest of the corpus. **Fixed:** added the hero block (EN alt + caption). Re-build confirms the EN page now renders the still ×2, the caption "Curated 11 · Vietnam", and `og:image` → the Vietnam still. *Lesson for the guidebook: the EN/AR pair must be diffed for frontmatter-key parity, not just body parity — a missing hero block builds clean and ships broken.*

2. **Static `sitemap.xml` did not mirror the new article set** (the known hand-maintained-sitemap drift; RUNBOOK §"Generated artefacts… build-generated, never hand-maintained"). **Fixed:** added the EN + AR Vietnam `<url>` blocks with hreflang alternates; bumped the homepage `lastmod` to 2026-06-16 (its content changed — current edition now leads with this piece). Re-build: sitemap **31 URLs**, both Vietnam locs + alternates present. *This is the third gate in a row to hand-patch the sitemap; the `@astrojs/sitemap` integration is overdue — re-flagged for the weekly.*

## Caption-taxonomy decision (this piece)

Used the **register-style** caption — «سكون · The Still · Curated 11 · Vietnam» / «… كيوريتد ١١ · فيتنام» — **not** "Edition 02". This follows the 2026-06-15 QA recommendation (drop "Issue/Edition" from captions; unify on the register-style) and avoids extending the drift. The **full 14-piece caption unification** (the two live "Issue 02" captions → register-style) remains the weekly's call; this piece does not pre-empt it, it just doesn't add to the mess.

## Not done (deliberate, noted)

- **Reciprocal related-rail backlinks** (Egypt EKB / Sierra Leone TSC / Bo → Vietnam) not added; the rail is one-directional Vietnam → 3, which renders correctly and degrades gracefully. Reciprocity is a nice-to-have, deferred rather than expand the change surface on an autonomous run. Candidate for the next daily.

— Manager · 2026-06-16
