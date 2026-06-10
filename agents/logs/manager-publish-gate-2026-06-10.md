# Publish gate — 2026-06-10

This gate covers the full Iqra/diglossia ship. **Note on sequencing:** the gate below was run, in writing, against the complete change-set *before staging* — but at 08:24, mid-run, the founder's push of brief No. 12's block landed (`feb98b1`) and its `git add -A` carried the two article files (text final, verified no drift) to origin ahead of the hero still, sitemap, reciprocal links and verdicts. The gate's verdict therefore stands for the change-set as a whole, and the remaining 12 files are staged as the completion commit — which is time-sensitive, because until it lands the live Iqra pages reference a hero still that 404s.

## Gate checklist (in writing, before staging)

1. **Editor verdict** — **APPROVED**, in writing, all five tests, at `/content-drafts/verdicts/2026-06-10-rak-iqra-arabic-diglossia-verdict.md`. The sourcing judgment of record: figures run on the **evaluator-on-record tier** (J-PAL's Husseiny + Al Qasimi's Mohammed/Ridge, named, quoted, datelined 2026-05-22; trial design stated falsifiably; every figure attributed in-text; follow-up logged to re-link the J-PAL report when it publishes). Ruling banked as a guidebook entry. ✔
2. **Arabic Editor verdict** — **APPROVED**, in writing, at `/content-drafts/verdicts/ar/2026-06-10-rak-iqra-arabic-diglossia-ar.md`. Six named-human renderings verified (Mohammed, Ridge, Husseiny, Abadzi, Saiegh-Haddad, Al Nowais); AR is composed, not translated; quote provenance (English, The National) named in-text. ✔
3. **Hero stills on disk** — 12/12 present, including `/web/public/stills/2026-06-10-rak-iqra-arabic-diglossia.svg` (house line-art discipline: ink + kiln-orange on paper-cream, no fills/filters, `<text>`-free). ✔
4. **Clean `astro build`** — YES. Built via the /tmp route-around (node_modules FUSE boundary). **27 pages, 0 errors** (25 → 27: the new EN + AR pages). ✔
5. **QA spot-check** — verified in built HTML:
   - New EN page: hero resolves; related rail links to Sierra Leone matching + Bo resolve; bilingual close renders (`dir="rtl"` present); wordmark inlined. ✔
   - New AR page: `اقرأ أيضًا` rail resolves to AR Bo + AR Sierra Leone; EN↔AR cross-links resolve both directions; canonical URL correct. ✔
   - Reciprocal: Sierra Leone EN + AR pages now show the new piece in their rails. ✔
   - Parity 12 = 12 exact; deks under the 200-char schema cap (both checked at write time — the 2026-05-28/06-08 failure mode); no `[[TRACE]]` markers anywhere in built output; sitemap at 27 URLs with hreflang alternates. ✔
6. **Stats panel** — `madar_stats.py --log` run clean; snapshot appended to `/agents/stats/history.jsonl`; panel pasted into brief No. 13 with its CSS present once. ✔

## Verdict

**PASS** for the change-set as a whole. The mid-run race (founder push between article-write and still-write) is a *process* finding, not a quality one: every item above was verified before staging, and the completion commit restores the invariant the gate exists to protect (no article live without its hero). Queued for the weekly: the push block's `git add -A` is unsafe whenever a founder push can overlap an agent run — propose explicit pathspecs or a push-window convention.
