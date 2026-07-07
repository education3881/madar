# Edition 03 — ready to push (founder action)
**Prepared:** 2026-07-07 · Manager staged; founder pushes (standing rule). CI builds + deploys on push.

## What ships
- **Edition 03 "Continuity under disruption" — 10 bilingual pieces** (EN + AR + hero still each): Sudan · Chad · Yemen · Ukraine · Poland · Türkiye · Syria · Lebanon · Gaza · Rohingya. All `approved: true`, `edition: 3`.
- **Ed02 slot-10 closer — Morocco** écoles pionnières (EN + AR + still), Editor-approved.
- **Infrastructure:** `editions.ts` (Ed02 → closed, **Ed03 → current**, July 2026, new "throughline" motif); `edition-03.svg` cover; throughline branch added to both `/editions/` pages.
- **Audit trail:** recon briefs, compose notes, the Ed03 gate verdict + build-verification note, sprint file.

## Verified (see content-drafts/verdicts/2026-07-07-edition-03-gate-verdict.md + -build-verification.md)
Figure gate, route-2 voice (Lebanon/Rohingya gap statements), Gaza guardrails (mechanism-only, zero casualty/ban terms), sibling spacing (Sudan/Chad + Ukraine/Poland de-twins), frontmatter, dek caps incl. tashkeel, parity **10 EN = 10 AR = 10 stills**. Content schema clean (Chile trimmed 201→189). Astro renders Ed03 registry/cover/motif + all pieces.

## Held back (NOT shipping this push)
The 5 Edition 04 EN drafts (India PARAKH, NZ, Chile, Singapore, US-NAEP) + US-NAEP AR are set **`approved: false`** — they stay in the tree but do not build/list/sitemap. Flip to `true` when Ed04 is complete (needs 4 more AR + 10 stills + 5 more pieces).

## Push commands (run on your machine, where git is unblocked)
```bash
cd "/Users/vini/Documents/Claude/Projects/Educational Website"
# clear the sandbox lock if git complains:  rm -f .git/index.lock
git add web/src/content/articles/2026-07-0[67]-*.md \
        web/src/content/articles-ar/2026-07-0[67]-*.md \
        web/public/stills/2026-07-0[67]-*.svg \
        web/public/covers/edition-03.svg \
        web/src/lib/editions.ts \
        web/src/pages/editions/index.astro web/src/pages/ar/editions/index.astro \
        content-drafts/recon content-drafts/verdicts content-drafts/_EDITION_03_04_SPRINT.md
git commit -m "Madār — 2026-07-07: Edition 03 'Continuity under disruption' — 10 bilingual pieces (Sudan·Chad·Yemen·Ukraine·Poland·Türkiye·Syria·Lebanon·Gaza·Rohingya) + Ed02 closer Morocco; editions.ts Ed03 current + throughline motif + cover; gate + build verified; Ed04 drafts held (approved:false)."
git push origin main
```
Then confirm the Actions run goes green and the live site refreshes (recovers the 06-25 stale state + Kenya 404).

## ⚠️ Note on tree state
Mid-session an external process (a concurrent run or your own workflow) **moved** the untracked sprint files out of `web/` into `content-drafts/staged-ed0304/` and reverted the tracked `web/` files to HEAD. I restored `web/` from a build copy; a full backup is also at `outputs/SPRINT_BACKUP_2026-07-07/`. Because the working tree is being touched externally, **pushing soon is the safest way to lock this in.**
