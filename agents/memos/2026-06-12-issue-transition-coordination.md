# Coordination memo — issue-to-issue transitions + the Issues page

**From:** Manager → Designer + Web Developer (joint), cc Editor, Growth
**Date:** 2026-06-12 (founder directive, same day)
**For:** founder discussion 2026-06-13; ratification at the weekly 2026-06-14
**Deliverable today:** a discussable prototype (`/design-assets/issues-page/2026-06-12-issues-page-prototype.html`) + the Designer's visual-language proposal

## The founder's ask, decomposed

Vini asked for three connected things: (1) a worked plan for how the publication transitions from issue to issue — he has noticed the visual pattern change between the May and June pieces; (2) a new page that clearly shows the **current issue** and gives access to **previous issues' content**; (3) a per-issue visual identity — "slightly different visual guidance" per issue, potentially including color.

## What recon established (today, before any design)

- **The drift he noticed is real and measurable:** all nine Issue 01-era stills (05-26 → 05-31) sit on a **sand `#E8E2D0`** ground; both June stills (Sierra Leone TSC, Iqra) sit on **paper `#FAFAF7`**. Nobody decided this; it happened. The work is to make it *intentional* — the Designer's proposal turns the accident into the system.
- **"Issue" does not exist in the codebase.** No `issue` field in the content schema; the homepage hardcodes `Issue 01 · 2026 · 05 · 25` in the section meta — exactly the hand-maintained-label drift defect the RUNBOOK's prevention rule names. The Issues page work fixes this at the root.
- **The design system's five-token rule binds.** "No more than five colors, non-negotiable." Per-issue identity must come from *deployment* of the tokens, not new hexes — or from a formally amended, pre-approved ground ladder (Designer's Phase-2 option, below). We do not improvise palette per issue.

## Work split

**Designer** (proposal delivered today, `/agents/memos/2026-06-12-designer-issue-visual-language.md`):
- The per-issue visual grammar: ground color, motif, numeral treatment, and the *transition ritual* — what visually happens when an issue closes.
- Phase-2 option: a pre-approved neutral ground ladder for future issues, with contrast verification, framed as a SYSTEM.md amendment for the weekly to ratify or reject.

**Web Developer** (implementation spec; build AFTER founder discussion + weekly ratification):
1. Schema: add `issue: z.number().int().positive().optional()` to the shared article schema; backfill all 24 frontmatters (10 EN + 10 AR = Issue 1; 2 + 2 = Issue 2). One-time hand edit at approval-time thereafter — per-article metadata, not a generated artefact, so the prevention rule is not violated.
2. Pages: `/issues/` (EN) + `/ar/issues/` (AR) — current issue hero + previous issues, **iterating the collection grouped by `issue`**, never naming slugs (RUNBOOK rule). Per-issue tokens via a small `issues.ts` registry (number, period, theme line, ground token, motif id) — the only hand-kept piece, one line per issue, added at issue open.
3. Homepage: replace the hardcoded `Issue 01 · …` meta with the derived current-issue label from the same registry. Nav link "Issues · الأعداد".
4. **Sequencing constraint (binding):** this page lands *with or after* the domain cutover, never straddling it — one URL-set change at a time. If the domain is ratified Sunday, order is: cutover (incl. @astrojs/sitemap) → issues page in the next push.

**Editor** — owns the issue boundary itself: an issue closes by editorial declaration (recorded in calendar.md), never by date arithmetic. The page renders the declaration; it does not make it.

**Growth** — once live, the Issues page becomes the canonical "start here" link for newsletter and grid bios (one URL that always shows the current issue — no per-issue bio edits).

## Tomorrow's discussion agenda (2026-06-13)

1. Does the prototype's reading of "current vs. archive" match what Vini imagined? (Especially: orange-marks-now / past-recedes-to-sand semantics.)
2. Per-issue color: deployment-only (Phase 1, no system change) vs. the ground-ladder amendment (Phase 2)?
3. Naming: "Issues" vs "Editions" vs Arabic-led «الأعداد»?
4. Sequencing sign-off: after domain cutover, agreed?

## The publish gate applies in full

Nothing in this memo ships to the site today. The prototype is an off-site artefact for discussion. Implementation goes through Editor sign-off on labels/copy, Arabic Editor on all AR strings, build + QA, gate in writing.

— Manager · 2026-06-12
