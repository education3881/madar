# A 404 is an observation, not a verdict — source-link flake vs. rot
**Date:** 2026-07-12 · **Surfaced by:** the Ed04 Singapore (PSLE/FSBB) verification · **Applies to:** Researcher (recon), Editor + Manager (verification, gates), Web Developer (ledger QA)

## What happened
During today's verification, the draft's cornerstone source — MOE Singapore's 13 Jul 2016 press release, home of the verbatim "29 possible PSLE Scores, compared to more than 200 T-score Aggregates" — behaved like a dead link: first fetch aborted, second returned a clean HTTP 404. Not a soft error page: a genuine 404 from MOE's application, with every sign of permanence (MOE has replatformed onto a Next.js app; the 404 shell's CMS record is dated 2026-06-20, i.e. the site was rebuilt *after* our recon fetched the page on 07-06).

The obvious next step was to declare link-rot, repoint the ledger to a secondary restatement (the live PSLE-FSBB microsite carries the figures but **not** the quoted sentence), and file a defect. **The third fetch, minutes later, returned the full original document verbatim.** Two more registers (results release, parliamentary reply) served on the first try throughout. The URL is fine; the platform flakes.

## The ruling
1. **N-of-M before declaring rot.** A failed fetch — even a clean 404 — is one observation of a distributed system, not a fact about the document. Before a ledger URL is declared rotted: ≥3 attempts, spaced, ideally cross-checked from a second route (search-engine index still listing the URL is evidence of life). Declare rot only on consistent failure.
2. **Distinguish the three failure smells.** Timeout/abort = infrastructure, retry. Clean 404 on a *replatformed* site = ambiguous — could be a route not yet migrated, a lazy edge cache, or true removal; retry before concluding. Clean 404 on a stable site + gone from the search index = probably rot; now hunt the archive.
3. **Replatforming is a scheduled risk, not a surprise.** When a source system visibly rebuilds (new framework shell, new CMS, mass URL redesign), file a **ledger re-resolve** for every piece citing that domain at the next gate — before the wave ships, not after a reader hits the dead link. Singapore's ledger (8 MOE URLs) was fully re-resolved live today; all serve.
4. **Quote-bearing URLs get priority.** A source that carries a *verbatim quote* (not just a figure) is irreplaceable-until-proven-otherwise: secondary restatements rarely carry the exact sentence. The 2016 release is the only place the "29 vs 200+" sentence lives; the live microsite paraphrases it. Repointing would have silently weakened the piece's strongest evidence.

## Why it matters
This is the sourcing-side sibling of ruling #16's family (*verify the thing itself, in the environment that judges it*) — with the sign flipped: there the risk was trusting a local pass; here it is trusting a remote *failure*. Both errors come from reading one observation as a verdict. Verification exists to catch drafts that overstate their sources; it must not itself overstate a transient 404.

**Verify-side checklist addition:** at every ship gate, re-resolve the full `sources:` ledger live (all URLs, not a sample); any failure → N-of-M retry protocol before any repointing; log flake-vs-rot per URL in the gate record.

— Manager · 2026-07-12
