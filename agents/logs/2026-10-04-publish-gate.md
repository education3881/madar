# Publish gate — 2026-10-04, in writing, before the commit

**What is being committed editorially:** four `sources[]` edits across three files. **No piece flips.**
**No piece ships.** The held set stays held, 6 slugs / 12 files, and the corpus stays at 38 approved
pairs. This gate is run because the RUNBOOK requires it before committing *anything* editorial, not
because anything is being published.

| Gate item | State |
|---|---|
| Any `approved: false` → `true`? | **No.** 6 held slugs before, 6 after. `qa_held_assets`: 6 held, 38 approved. |
| Editor verdict on file for anything new? | **N/A** — nothing new. The edits are corrections inside annotations, filed as `verdicts/2026-10-04-ed05-cross-edition-named-entity-sweep.md`. |
| Arabic gate | **Arabic Editor is the author of three of the four edits** (the two gender corrections and the title harmonisation) and co-signed the verdict. The fourth is an EN parity clause mirroring an AR one. |
| Named-human transliteration | Unchanged. No name's spelling moved in either edition. |
| Hero stills / og cards | Untouched. 6 held stills and 6 held og cards remain where the build cannot serve them; `qa_held_assets` confirms 88 control assets unaffected. |
| `npm run build` | **exit 0**, run twice — once on the untouched tree, once after the edits. |
| 28 standing assertions | **All green.** 13 `postbuild` CLEAN; the 12 CI build-step assertions run by hand against the same artefact, every one exit 0. |
| `qa_pair_frontmatter` | **CLEAN** — 44 pairs, 38 approved, 6 held, 432 identity fields, 684 source URLs, 338 shared annotations, 3/3 declared asymmetries used and unchanged. |
| Held-slug leak | **Zero.** `qa_held_assets` 6 held slugs contributing no page, no sitemap entry, no feed item, no `lastmod`. |
| Body prose | **Untouched in both editions of all six pairs.** No numeral moved in any body. Word counts unchanged. |
| Commit-message hygiene | Single ASCII line, no `!`, no `$`. |
| Credentials | None added, none present, none logged. |

## The two things worth proving rather than asserting

1. **`qa_ar_language` CLEAN on all 59 Arabic pages** with a French clause and an English pronoun
   quotation newly added to Arabic annotations. That gate bit on **235** Arabic-page fields printing
   English the day it was wired, so its silence was confirmed by running it, not assumed. It is scoped to
   identity fields and not to `sources[]` prose, which already carries Latin register quotations by
   design (#72).
2. **The held set is still invisible.** The four standing assertions that enforce it all ran: a held piece
   contributes no bytes, no `lastmod` above the approved-and-chrome ceiling, no sitemap entry, no feed
   item. Two of today's three edited files are **held**, which is exactly the condition under which a leak
   would show, and none did.

## What this gate does NOT clear, stated so nobody reads it as more than it is

- **Slot 3's and Egypt's confirmation reads** — 4th and 5th of five, both still owed.
- **Ledger Items A, B and C** — all three with the Editor, all three still blocking the flip.
- **The flip rehearsal** — owed in the run that composes the flip commit. 10-01's green is six content
  files old.
- **The packet captions' Arabic gate** and the flip's own publish gate in writing.

**Verdict: CLEAR TO COMMIT. NOT clear to flip, and nothing here moves the wave gate.**

— the Manager, with the Editor, the Arabic Editor and the Web Developer · 2026-10-04
