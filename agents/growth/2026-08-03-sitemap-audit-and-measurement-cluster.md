# Growth — 2026-08-03 · live sitemap re-audit + measurement-cluster growth

**Action (discoverability integrity):** Re-audited the built sitemap in the judging environment after composing India's Arabic.

- `sitemap-0.xml` = **65 URLs** = 60 live corpus (30 EN + 30 AR) + 5 structural. Unchanged from 08-02 — correct: nothing new *shipped*, India AR was added held.
- **Zero held-Ed04 slugs in the sitemap** (scanned all 8 wave slugs: india, australia, us-naep, singapore, nz-ncea, chile, netherlands, england — none present, EN or AR). The `approved !== false` route filter holds on the sitemap surface as well as the article/edition/home routes.
- India's EN article correctly renders **nowhere** in `dist` (the whole Ed04 wave is held, EN included) — so there is no dangling EN→AR hreflang to leak. hreflang reciprocity is a wave-gate concern, not a live one, and stays clean.

**Cluster growth (staged for the wave gate, not yet live):** With India AR composed, the bilingual **"measurement question"** internal-link cluster now has three of its spine pieces bilingual — us-naep ↔ australia ↔ india — plus the standing EN cross-links to england (report cards) and brazil (alfabetizada). At the wave gate the `related:` blocks resolve reciprocally across EN+AR so a reader who lands on any one measurement piece can walk the whole set in their language. India's EN already cross-links england + brazil; the AR mirrors those slugs. Nothing to push now; logged so the gate inherits a complete cluster map rather than rebuilding it.

**Distribution still founder-gated:** Substack announce + custom domain remain the two founder calls; neither blocks the site. No third-party tracker by design — return rate will be the metric once Substack is live; no visitor numbers invented.
