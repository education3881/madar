# Guidebook — index of durable working knowledge

**Maintained by:** the Manager (consolidated in the weekly review); **Section 1 owned by the Researcher** from 2026-06-14.
**Last consolidation:** 2026-06-14 (Issue 02 week 2).
**Purpose:** one entry point to everything the team has learned the hard way. The durable manual (`slow-cadence-publication-guidebook.html`) is the *replicable* model for any subject; the files indexed below are *Madār-specific* verified reference and method. A writer should be able to start any piece, or render any asset, without re-running reconnaissance that has already been done and banked.

---

## 1. Verified primary-source indices (Test 1 pre-cleared at the index level) — owned by the Researcher

| File | Subject | What it gives | Status |
|---|---|---|---|
| `2026-06-06-sierra-leone-tsc-source-index.md` | Sierra Leone TSC / GIS teacher-deployment matching | Institutions, four named voices (2024–25) + AR transliterations, the 2024 hard figures with the "source from the technical report not the blog" rule, mandatory counter-texture, live URLs | **Shipped** 2026-06-08; figures traced in full via web tools |
| `2026-06-09-arabic-diglossia-early-literacy-source-index.md` | Arabic diglossia & early literacy (IQRA / Ras Al Khaimah) | Research spine (Saiegh-Haddad 2025; the non-deficit counter-frame), the IQRA intervention as the figure-bearing tier, the two-studies-same-name fence, AR transliteration candidates | **Shipped** 2026-06-10 on the evaluator-on-record tier (J-PAL report follow-up logged) |
| `2026-06-11-korea-aidt-source-index.md` (+ `2026-06-16-korea-aidt-voice-gate-closed.md`) | Korea AI digital textbooks (AIDT), adoption → statutory reversal | Statutory/ministry primaries, named humans by tier, the same-figure-different-scope fence (₩533.3B 2024 allocation vs ₩1T teacher-training 2024–26; $850M dropped as conflation), pilot scope | **SHIPPED** 2026-06-17 (EN+AR, build-verified, 33 pages) — voice gate closed 06-16 (Kim Cha-myung, elementary teacher, *Rest of World* 15 Oct 2025); figures re-verified live at draft. Figure-fence survives as durable reference |
| `2026-06-04-saudi-ece-source-index.md` | Saudi early-childhood (ECE) sourcing landscape | Tiered source map, the GASTAT 2025 data-led inversion route, transliteration rulings for minister + KG director | **Parked** — operational-tier voice not reachable in open primaries |
| `2026-06-14-vietnam-tuition-free-source-index.md` | Vietnam public-school tuition exemption (Politburo 28 Feb 2025 → NA Res. 217/2025/QH15, 26 Jun 2025) | Two-stage instrument named (don't collapse them); scope (preschool→grade-12, public full / private capped support); the *tuition-free ≠ fee-free* fence with HCMC fee figures (Tuoi Tre); fiscal line ~VND 30,600bn/yr (~US$1.2bn); named voices w/ diacritics — incl. **operational** voice Principal Nguyễn Thị Vân Hồng (Tiền Phong, 3 Mar 2025) | **SHIPPED** 2026-06-16 (EN+AR, build-verified, 31 pages) — figure gate closed, voice gate closed; load-bearing URLs re-verified live at draft. Researcher's first commission, carried end-to-end |

Per-draft caveat: Test 1 is re-run per draft. The index pre-clears the *landscape*; the writer/Researcher re-checks each URL at draft time.

## 2. Production / method notes

| File | Method | One-line rule |
|---|---|---|
| `2026-06-05-rendering-stills-to-png.md` | SVG line-art still/tile → PNG via `cairosvg`, no browser | Our stills are pure line-art (`grep -c '<text'` == 0) and the wordmark is path-based, so `cairosvg` renders both exactly — pad to 1:1, never crop; eyeball a 3×3 contact sheet before sign-off |
| `2026-06-11-brand-fonts-via-npm-fontsource.md` | Rendering **text-bearing** assets (esp. Arabic) | **Line-art → cairosvg. Any real text → Playwright headless Chromium** (Chromium shapes Arabic via HarfBuzz; cairosvg silently produces disconnected letterforms — never ship cairosvg-rendered Arabic). Fonts come from npm `@fontsource/*` (GitHub release assets are egress-blocked), `@font-face` via `file://`. Always verify by *looking at the PNG*. |
| `2026-06-08-egress-wall-is-bash-only-use-web-tools.md` | Tracing figures when the primary host fails from `bash` | **The egress wall is bash-only.** `curl`/`wget`/`requests` are restricted; `WebSearch` + `web_fetch` are not. Pattern: `WebSearch` the source (puts the canonical URL in provenance) → `web_fetch` that exact URL. Exhaust this *before* concluding a figure is untraceable or escalating to a founder allowlist action. **Supersedes the operative conclusion of `2026-06-07-sourcing-across-egress-boundary.md`** (retained as the origin note; its "allowlist the hosts" founder ask is **withdrawn — resolved**). |
| `2026-06-12-url-binding-migration-playbook.md` | When to move to a custom domain (the migration-cost clock) | A URL is an accumulating ledger of bindings; migration cost is a *clock, not a constant* and steps up each time a new system (Search Console, newsletter, inbound links, citations) copies your URL into storage you don't control. **Migrate before the next binding fires, or pay twice.** Includes the verified GitHub Pages cutover sequence. |
| `2026-06-15-astro-build-in-sandbox-vite-cache-route.md` | Running a real `astro build` inside the sandbox | The cold build is **not** a capability gap. `node_modules` is present on FUSE; the only obstacle is FUSE's `unlink` ban (Vite dep-cache + `dist/` cleanup). **Build from a tmpfs copy with `VITE_CACHE_DIR` set** → exit 0, 29 pages. Retires the "cold build carried to weekly" caveat. Count pages on tmpfs `dist/`, never on FUSE (stale files inflate it). |
| `2026-06-16-sourcing-one-party-policy-reform-and-vietnamese-transliteration.md` | Sourcing a one-party/parliamentary reform + Vietnamese→Arabic names | **Name BOTH instruments** (Party decision *and* legislature's resolution) with their own dates; never collapse them; distinguish adoption from signing/certification. Carries the *tuition-free ≠ fee-free* fence (source the gap to the country's own press). Includes the reusable **Vietnamese→Arabic transliteration table** and a **frontmatter-key-parity** QA ruling (a missing `hero:` block builds clean, ships broken). |
| `2026-06-17-arabic-dek-character-cap-includes-tashkeel.md` | Capped frontmatter strings (`dek`/`title`) vs Arabic tashkeel | The 200-char `dek` cap counts **Unicode code points**, so each tashkeel mark adds +1 — a fully-voweled AR dek fails at ~150 visible chars. **Keep the body voweled, the dek lightly voweled; count code points before staging** (both languages). Includes a copy-paste check for the pre-stage routine. Surfaced by the real build (Korea AIDT). |

## 3. Durable rulings — the generalizable lessons (apply to every candidate)

These are the transferable rules the source-specific notes paid for. The Researcher applies them at recon; the Editor checks them at verdict.

1. **The operational-not-ceremonial-voice rule (Sierra Leone / Saudi).** When a strategy PDF is the candidate, the unpark hinges on the person who *runs the mechanism*, datelined 2024+ — not the one who *announced* it. Sierra Leone cleared (Marian Abu, on classroom impact, Dec 2024); Saudi and Korea parked (only the launch/announcement tier was reachable). Run this test *before commissioning*.

2. **The tiered-sourcing-asymmetry rule (Saudi).** A government flagship over-documents the minister and the target, under-documents the classroom — in *both* languages. Plan the sourcing around that asymmetry from day one. When the operational tier is unreachable, consider the **data-led inversion** (let an official statistics report carry the why-now, require one named operational voice for dignity) before abandoning the candidate.

3. **The evaluator-on-record trace tier (2026-06-10 ruling — the load-bearing new rule).** A figure may run *without the primary report in hand* only when ALL five hold: (1) the evaluator is on the record by name + affiliation describing the finding; (2) the operator confirms separately by name; (3) the trial design is stated falsifiably (sample/arms/period); (4) every figure carries in-text attribution to the named evaluation, never Madār's own voice; (5) a standing follow-up is logged to re-verify when the report publishes. If any fails: trace to primary or park. A named evaluator describing her own randomised trial *is* a primary source — a person, not a PDF. Verdict checklist line: *Trace tier: ☐ primary in hand · ☐ evaluator-on-record (5 verified, follow-up logged) · ☐ neither → park.*

4. **A program name is not a citation — pin every figure to its report, cycle, and scope.** Two failure modes, same fix (state the discriminator in print next to the number): the **two-studies-same-name trap** (IQRA ~2020 vs 2024–25 J-PAL trial — check year + sample) and the **same-figure-different-scope trap** (Korea ₩533.3B = 2024 project allocation vs ₩1T = teacher training 2024–26; never average or reconcile — fence each to its scope or drop both).

5. **The blocked-tool-is-not-the-unreachable-resource rule (2026-06-08).** A failed `curl` is a statement about `bash`, not about the open web. Re-run through `WebSearch` + `web_fetch` first, not last. Distinguish *the tool that is blocked* from *the resource that is reachable* — it is faster and cheaper than a founder settings change, and it retires most "allowlist" escalations before they're raised.

6. **The render-is-a-method-not-a-gap rule (IG tiles).** Before treating an asset class as a capability gap (a reason to expand the team), confirm it is not simply an un-banked one-time method. Image rendering read as a Designer bottleneck across two runs; it was a `cairosvg` (then Playwright) recipe, now banked.

7. **The URL-binding migration-clock rule (2026-06-12).** Before adopting any external platform or registration, ask: *does this copy our URL into storage we don't control?* If yes, it is a binding; the migration clock steps up when it fires; sequence the domain decision ahead of it.

8. **The dual-instrument rule (2026-06-16, Vietnam).** A reform's *headline is not its legal instrument*. In one-party-plus-legislature systems a reform usually has two distinct instruments — a Party/executive **decision** (direction) and a legislature's **resolution/law** (budget) — and outlets collapse them. Name both with their own dates; distinguish **adoption** from **signing/certification**; conflate neither. The policy-instrument twin of #4. Companion fence: when a reform "removes a cost," establish what that cost legally *is* and what it is *not* (*tuition-free ≠ fee-free*), sourced to the country's own press.

## Consolidation note — 2026-06-14

**Six increments banked since the 2026-06-07 consolidation:** the egress-wall-is-bash-only finding (06-08), the Arabic-diglossia source index (06-09), the evaluator-on-record trace tier (06-10), the brand-fonts-via-npm method (06-11), the Korea AIDT source index (06-11), and the URL-binding migration playbook (06-12).

**Pruning / corrections this week:**
- The **06-07 egress-boundary note is superseded** by the 06-08 finding. Its operative conclusion (figures untraceable; allowlist the hosts) was wrong — the same figures traced in full via the web tools, and the Sierra Leone piece shipped 06-08. The **founder host-allowlist ask is retired as resolved** — it should not be carried into any future review or brief as a live Vini action. (It was erroneously re-listed in the 2026-06-12 manager status; that resurrection is corrected here.)
- The 06-09 (two-studies-same-name) and 06-11 (same-figure-different-scope) rulings are **merged** into a single durable rule (#4 above) — they are one lesson in two dimensions.
- Two parked candidates (Korea, Saudi) keep their source indices as **durable reference**: the figure-fences and source maps survive the park and un-park instantly if a named operational voice surfaces.

**Ownership change:** Section 1 (source indices) passes to the new **Researcher** persona (`/agents/08_researcher.md`, added in the 2026-06-14 weekly review). The Researcher keeps it current and pruned from the week of 2026-06-15.

The durable HTML manual is unchanged this week; nothing this week revised the *replicable* model — only Madār's own working knowledge grew. The team is measurably more capable than a week ago: three of the four indexed source indices now carry a closed figure-trace, and the source-hierarchy rulings have hardened from "source the report not the blog" into a four-part discipline covering time, scope, and the evaluator-on-record tier.

— Manager · 2026-06-14
