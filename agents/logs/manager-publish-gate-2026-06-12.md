# Publish gate — 2026-06-12 (run in writing before staging)

**Scope of this push:** nothing site-facing ships today — no `web/` file changes. Staged: the Korea park verdict + source-index figure-fence update, the Vietnam recon brief, the Growth caption packet (Husseiny tile), the URL-binding guidebook ruling, the founder's domain decision memo (the 06-11 ask, delivered on time), yesterday's untracked founder-request memo, gate + status logs, and brief No. 15.

## Gate items

1. **Editor verdict** — the day's editorial action IS a verdict: **Korea PARKS pre-draft** (`/content-drafts/verdicts/2026-06-12-korea-aidt-reversal.md`). Gate 1 (figure trace) closed — scopes fenced in the source index; Gate 2 (named operational voice) did not clear the English-language archive pass. Un-park condition is single and specific: one named in-school/in-agency voice on the record. The Manager backs the park without exception, per standing rule. Vietnam recon opened as the activated second candidate — recon only, no scope commit.
2. **Arabic Editor** — N/A: no AR prose ships. The Husseiny caption's Arabic line and the «نيرة عدلي حسيني» rendering are exactly the 2026-06-10 approved forms — no new transliteration introduced. The Vietnam brief flags Vietnamese-name diacritics + AR transliteration protocol for the Arabic Editor *before* any AR ships, per the named-human rule reaching recon documents.
3. **Hero stills** — 12/12 on disk, unchanged. No new site-bound assets.
4. **Clean `astro build`** — YES. /tmp route-around (fresh `/tmp/mb2`; yesterday's `/tmp/madar-build` was orphaned by the sandbox-user boundary — routed around, not fought). **27 pages, 0 errors.** ✔
5. **QA spot-checks** — every article href in the built output resolves, including the absolute canonical/hreflang set (scripted check, 0 misses); sitemap steady at 27 URLs, no hand-edit (no page-set change); parity 12 = 12; no `[[TRACE]]` markers in output; brand chrome inlined (no `<img src>` wordmark). Live-site fetch remains egress-blocked from the sandbox; state verified via git + origin parity (local = origin = `3d909a5`), per the standing rule.

**Verdict: GATE PASSES for the staged scope.** No site-facing change ships; the build verification confirms the repo remains deploy-clean as staged.

— Manager · 2026-06-12
