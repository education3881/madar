# QA review — Editions home + covers feature (commit 86c4478), post-ship

**Reviewer:** Manager (QA pass) · **Date:** 2026-06-15 · **Subject of review:** `86c4478` "edition art covers + homepage rebuild"
**Method:** real `astro build` via the tmpfs/`VITE_CACHE_DIR` route ([[2026-06-15-astro-build-in-sandbox-vite-cache-route]]) + residual-drift grep across `dist/`. Live URL not fetched (egress wall — git/origin parity is the truth; Actions deploys on push).

## Context (state, honestly)

This feature was **built, committed, and pushed by the founder during today's run** (local `HEAD` = `origin/main` = `86c4478`). I did **not** author any `web/` file — I watched the tree change under me (covers 09:46, footer registry-wiring ~09:58, `ar/index` +187) and deliberately stayed out of `web/` to avoid a collision while it was live-editing. This review is therefore a **post-ship verification**, not a pre-push gate. It records that what shipped is sound and names the one class of drift that survived.

## Build verdict — PASS

- **Clean build, exit 0, 29 pages** (27 baseline + `/editions/` + `/ar/editions/`). No compiler/type/schema errors.
- **Covers** `edition-01.svg`, `edition-02.svg` serve from `dist/covers/` and inline on both editions pages + the homepage current-edition block.
- **Homepage rebuild verified in built output:** EN home renders **"Edition 02"** and scopes to the current edition's pieces (lead + 1 secondary) with a previous-editions strip; AR home renders **«الإصدار الحالي»**. **Zero "Issue 01" anywhere in `dist/`.** Footer derives from the registry on every page (EN "Edition 02 · 2026" / AR «الإصدار ٠٢ · ٢٠٢٦»).
- **AR sign-off present:** «التوزيع» (placement) and «الإصدار الحالي» in the built editions pages — matches the Arabic-Editor ruling.
- **Parity:** 12 = 12 holds; sitemap steady at 29.

## One real finding — branding drift survived in CONTENT, not chrome

The commit says "all hardcoded 'Issue 01' removed." True for chrome. But the **"Issue → Edition" rename did not reach article content**, and it now ships live in three places:

1. **Hero `alt` + `caption` of the two Edition-02 articles** (`2026-06-10-rak-iqra…`, `2026-06-08-sierra-leone…`): `"…The Still · Issue 02 · …"` (EN) and «…العدد الثاني…» (AR). Because the homepage lead/secondary `<img alt>` pulls article hero `alt`, **"Issue 02" also appears on the homepage** (8 EN occurrences across the three pages).
2. **The founding Bo piece body prose** (`2026-05-25-bo-teacher-chalk`, EN + AR): "in this **first issue** of Madār" / «في هذا **العدد الأول**». Self-referential serial language in published copy — only this article.
3. **Caption taxonomy is internally inconsistent** (this is the root cause): **10** articles caption by *register* — "Field Note 01 / Curated 02…10" — while **2** caption by *edition* — "Issue 02". So even a pure word-swap ("Issue"→"Edition") would leave two schemes side by side.

**Not drift (verified, do not touch):** Bahrain AR «العدد ذاته» = common-noun "the same batch/number" of inspection reports — correct Arabic, unrelated to the serial unit.

## Recommendation (Editor + Designer + Arabic-Editor — a content call, not a chrome patch)

Pick one caption taxonomy and apply it to all 12:

- **Option A (cleanest): register-style for everyone.** Drop the edition number from the 2 June captions → "Field Note / Curated · UAE", matching the other 10. Captions stop encoding the edition (which the editions pages + homepage now do far better). Smallest change; removes the word "Issue" entirely.
- **Option B: edition-style for everyone.** Re-caption all 12 with "Edition NN" / «الإصدار NN». Most consistent with the new model but touches 24 frontmatters (EN+AR) and re-opens transliteration.

Separately, the **Bo founding-piece self-reference** ("first issue" / «العدد الأول») is a one-line Editor + Arabic-Editor copy decision — change to "first edition" / «الإصدار الأول», or keep deliberately as period-voice from launch. Low urgency, but it's live.

**Suggested owner/cadence:** Option A is a ~30-minute Web-Developer/Editor change, build-verifiable via the route above. Not a same-day emergency (no broken render, no parity break) — fold into the next content run or the weekly. Logged here so it isn't re-discovered cold.

## Durable pre-push checklist for any "Edition language" change (reuse)

1. Build via the tmpfs/`VITE_CACHE_DIR` route → exit 0, expected page count (count on **tmpfs** `dist/`, not FUSE).
2. `grep -rl "Issue 0" dist` → **0**, and `grep -rl "العدد" dist` → triage each hit (serial-unit = fix; common-noun "number/count" = leave).
3. Check **content** surfaces, not just chrome: hero `alt`, hero `caption`, and **article body prose** — the rename hides there and leaks onto the homepage via `alt`.
4. Confirm footer + homepage labels derive from `currentEdition` (no literals); AR strings match the Arabic-Editor ruling (الإصدار, never عدد-as-serial).
5. Parity 12 = 12; sitemap count unchanged unless routes added.
