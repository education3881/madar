# Publish gate — 2026-06-11 (run in writing before staging)

**Scope of this push:** no new piece ships today (recon-or-translate day, per throughput discipline). Staged: the Arabic-language rail cluster (6 frontmatter edits), the Korea AIDT recon bank (brief + source index), the Husseiny IG tile (off-site asset), logs and brief No. 14.

## Gate items

1. **Editor verdict** — N/A for a new piece (none ships). The rail-cluster curation is the Editor's own 2026-06-10 call ("an honest three-node cluster that exists in the catalogue"), executed as queued. **Editorial note on record:** the Iqra rail swaps Bo for the Kuwait CCET + Madrasa pair — rails stay at three, editor-curated; Bo remains one hop away via the Sierra Leone matching node, whose own rail (Bo · Uruguay · Iqra) is untouched. Reciprocity verified in the built output, both languages.
2. **Arabic Editor** — N/A for prose (no new AR composition; rail edits are slug lists, identical in both collections; AR rail headings/labels are component-level and already approved 2026-06-09). The Husseiny tile's Arabic line «البيداغوجيا مهمة.» is the exact rendering the Arabic Editor approved in the 2026-06-10 verdict/packet — no new transliteration introduced. Korean name renderings in the Korea brief are flagged TO BE VERIFIED before any AR ships (لي جو-هو، لي جاي ميونغ، جانغ ها-نا، لي بوم).
3. **Hero stills** — 12/12 on disk, unchanged. New asset (not site-bound): `/design-assets/instagram/issue-02-grid/2026-06-11-tile-husseiny-quote.png` + HTML source.
4. **Clean `astro build`** — YES. /tmp route-around. **27 pages, 0 errors** (unchanged count; no new pages). ✔
5. **QA spot-checks** — rails render on all six edited pages (EN + AR); every rail href resolves to a built page (12/12 OK, scripted check); sitemap stays at 27 URLs (no hand-edit needed — no page-set change); parity 12 = 12; no `[[TRACE]]` markers in output; brand chrome inlined (no `<img src>` wordmark).

**Verdict: GATE PASSES for the staged scope.** Nothing site-facing ships beyond the rail curation, which is build-verified.

— Manager · 2026-06-11
