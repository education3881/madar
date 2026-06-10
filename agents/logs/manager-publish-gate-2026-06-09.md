# Publish gate — 2026-06-09

No new article shipped today (throughput discipline: yesterday shipped a fresh piece). This gate covers the one change that goes live on push: the **related-reading rail** (schema + component + both article templates + 6 frontmatters).

## Gate checklist (in writing, before staging)

1. **Editor / AR verdict** — N/A for article content (no new piece). The rail surfaces only already-approved pieces; its content is editor-curated `related` slugs, not new prose. AR rail label (`اقرأ أيضًا`) is a standing UI string, not a translated article — no AR-Editor article pass required. ✔
2. **Hero stills on disk** — unchanged; 11/11 present (no new piece). ✔
3. **Clean `astro build`** — YES. Built via the /tmp route-around (node_modules/.vite FUSE boundary). **25 pages, 0 errors.** ✔
4. **QA spot-check** — verified in built HTML:
   - EN matching page → related links to Bo + Uruguay resolve. ✔
   - EN Bo page → related link to matching resolves. ✔
   - AR matching page → `اقرأ أيضًا` heading + related links to Bo + Uruguay resolve. ✔
   - Negative check: bahrain (non-cluster) page renders **0** related rails — graceful degradation confirmed (resolver filters unknown/unapproved slugs; no dead links, no build break). ✔
   - Parity 11 = 11 exact; stills 11/11; wordmark inlined; sitemap unchanged at 25 urls. ✔

## Verdict
**PASS.** Safe to stage. The change is additive, build-verified, and degrades gracefully. Risk if mis-shipped (schema/template change breaking the build) was retired by the route-around build, not assumed away.
