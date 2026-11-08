# Publish gate — 2026-11-08

**What is going to the origin tonight:** no new piece and no flag change. **Eight annotation edits
across four published pairs** (`2026-06-20-oman-school-performance-ratings`,
`2026-05-28-iraq-mosul-library`, `2026-07-07-singapore-psle-sbb`, `2026-05-27-uae-madrasa-tiktok`),
each written into **both** editions, closing the first taking of standing-queue item 85. **No body
sentence changed in either language.** Plus a ruling, a growth note, a recon record, the logs and the
brief, which serve no article bytes.

| Gate | State |
|---|---|
| Editor verdict on file | **n/a — no commission, no flag change.** These are annotation repairs to pieces whose pair verdicts, Verifier verdicts and Arabic gates are already on file from Edition 02/03/05 and unaltered by an addition to `sources[]` provenance |
| Arabic Editor verdict | **n/a as a gate, discharged as a read.** Every Arabic edit is a provenance clause written beside a determination the Arabic edition had already made; four of the ten determinations are now attributed to a morpheme the register prints, two are declared as this edition's own with today's date, and none changes a transliteration or a named human's spelling |
| Hero still on disk | unchanged, all four already served |
| Share card on disk | unchanged, all four already served |
| `npm run build` | **exit 0** |
| 27 postbuild assertions | **green** |
| 12 build-job assertions | **green locally** via `npm run gates` → `build_job_gates` — all 39 of 42 gating assertions green on this tree |
| `qa_pair_frontmatter` | CLEAN, 44 pairs, 704 source URLs, 348 shared annotations — the one declared asymmetry (Sudan) unchanged |
| `qa_citation_identity` | CLEAN, 233 quotation-bearing registers, **100 confirmed**, and the two registers this run quoted for the first time (`gov.om`, `stomp.sg`) both read today, **all seven tokens found in the served bytes** |
| `qa_patch_queue` | CLEAN, 39 of 42 gating, derived from three homes |
| `qa_register_shape` | CLEAN, §3 1 → 134 contiguous, all four range homes agreeing, fifth home read |
| `qa_prior_publication --check` | **OK, limb 5 satisfied** — this run observed before it built |
| Held-slug leak | **VACUOUS** per the 2026-08-09 inversion: 0 held pieces, 44 approved. The inverse assertion is the live one and `qa_held_assets` reports it green |

## Two things this gate records rather than smooths

**1 · The ordering was wrong again, for the second consecutive day, and it is now a queue row.**
Ruling #96 says *commit and push at the close of every standing function, never once at the end*, and
the publish-gate rule says *run the gate in writing before committing anything editorial.* On a day
when the content function changes a served byte, those two pull in opposite directions, and #96 wins by
force because a staged block in this cadence is a lost block. So this gate was written **after** the
content commit, exactly as it was on 2026-11-07. Nothing would have been caught by the right order
today — the build was green before the commit and every assertion above is green now — **which is
precisely why it is written down**: a conflict that costs nothing on the day it is noticed is the one
that is still unresolved on the day it costs something. **Raised as standing-queue item 88.**

**2 · Two served Arabic determinations now go to the origin declared as this edition's own rather than
as reads, and that is the honest state rather than a defect.** `الدكتورة` for Dr. Anna-Christine Janke
and `الدكتور` for Dr. Waleed Al Ali stand on registers that print `Dr.` and no pronoun. #86 clause 2
says exactly what to do with that — write it down in the annotation as this edition's own, with its
date — and both now do, in both languages, with the single settling fetch named in each. The
alternative was to de-gender the Arabic, which Arabic grammar does not permit for a role noun about a
person, so there is no silent option here: the edition either commits and says so, or cannot write the
sentence.

**Signed:** Manager, 2026-11-08. Nothing editorial is held today.
