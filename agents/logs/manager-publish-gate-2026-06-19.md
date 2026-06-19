# Publish gate — 2026-06-19 — Philippines MTB-MLE reversal (EN + AR) + carry of 06-18 Egypt

Run IN WRITING before staging. **This push folds in TWO ship days** (06-18 was gated GREEN but not pushed by the founder — see State note). Slug today: `2026-06-19-philippines-mtb-mle-reversal`. Sprint piece 6 of 10.

## State note (the honest, load-bearing part)

- Opened on `555f586` (06-17 Korea, deployed clean). **Local HEAD == origin/main == `555f586`.** `git fetch origin` re-checked at gate time: origin unmoved (no founder push landed overnight).
- **The 06-18 Egypt NPDA piece (sprint piece 5) was completed and gated GREEN on 06-18 but never committed/pushed** — it sits, with its brief/logs/growth/guidebook, **uncommitted in the working tree**. So the **live site is still at 06-17 (33 pages, 14=14)**; on disk we are at 37 pages, 16=16. This is **not a missed day** — the work exists and is sound; it is an un-fired push. Today's push therefore lands **both** 06-18 (Egypt) and 06-19 (Philippines) at once. Egypt's 06-18 gate (`manager-publish-gate-2026-06-18.md`, GREEN) stands unchanged and is re-affirmed here; the 06-19 build re-verified both pieces render clean together.
- Push-race invariant honoured: both hero stills + both AR files written before this gate; re-check origin again at the moment the push block is composed.

## Gate items (RUNBOOK §3) — Philippines

- [x] **Editor verdict = APPROVE**, on record: `content-drafts/verdicts/2026-06-19-philippines-mtb-mle-reversal.md`. Five-test rubric passed line by line. The recon's **second-editorial-read sensitivity flag is discharged**: framed as a policy dispute, not a verdict; both camps given their strongest honest case; home language never cast as deficit.
- [x] **Arabic-Editor sign-off**, on record: `content-drafts/verdicts/ar/2026-06-19-philippines-mtb-mle-reversal.md`. Transliterations verified (سوني أنغارا, ريكاردو نولاسكو, ماتاتاغ); policy instruments named cleanly (RA 12027 / RA 10533 / DepEd Order 20 s.2025); **Arzadon dropped in AR too** (parity with EN — no quote we can't stand behind). Second piece on the compose/verify split (Arabic Content Creator composed; Arabic Editor verified).
- [x] **Article md present, `approved: true`** — EN `web/src/content/articles/2026-06-19-philippines-mtb-mle-reversal.md`; AR `web/src/content/articles-ar/2026-06-19-philippines-mtb-mle-reversal.md`. Both deks under the 200-cap (EN 187, AR 162; tashkeel counted).
- [x] **Hero still on disk, same commit as text** — `web/public/stills/2026-06-19-philippines-mtb-mle-reversal.svg` (6.2 KB, valid `</svg>`): an archipelago of many home-language marks threaded by one line resolving into two firm strokes, with the mother tongue left as one kiln-orange mark just off the new path. Asset-with-text invariant honoured (still written immediately after the articles).
- [x] **Clean build** — real `astro build`: **✓ Completed, 37 pages**, both Philippines pages generated, no schema rejection. The exit-1 is the known FUSE post-build `unlink` artifact (thrown after completion); verified by building to a non-FUSE `--outDir /tmp/madar-dist` (37 pages) + confirming static-asset copy in `web/dist/`. GitHub Actions (clean Linux runner) exits 0.
- [x] **QA spot-check** — `agents/logs/qa-2026-06-19.md`. Parity **16 = 16**; still in dist; wordmark inlined (0 `<img wordmark>`); related rail resolves (Egypt + Iqra + Korea, correct `/madar/` base, EN + `/ar/`); new piece appears on EN/AR homepages + editions (collection-iterated). Sitemap well-formed XML.
- [x] **Sitemap mirrors the article set** — hand-patched to **37 urls** (Philippines EN+AR; homepage + editions `lastmod` → 06-19; Egypt's 06-18 lastmods preserved). Parity re-validated; `xml.dom.minidom` parse clean. (6th hand-patch; `@astrojs/sitemap` integration recipe scheduled for the buffer day.)

## Throughput

One fresh piece (EN) + its AR composition. Recon banked 2026-06-16 (recon-precedes-drafting honoured). Sprint rhythm (1/day bilingual) held.

**Verdict: GREEN — cleared to stage (both 06-18 Egypt and 06-19 Philippines).** No push from the sandbox; Vini holds the push.

— Manager · 2026-06-19
