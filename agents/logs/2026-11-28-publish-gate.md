# Publish gate in writing — 2026-11-28 (daily run)

**Result: NO FLAG FLIPS TODAY, and the gate is run anyway because editorial files moved.**
Two held pairs were edited in this run (a spine repair in both editions of the Uzbekistan pair), so the
gate is owed on the state those edits leave behind, not on a flip.

## A. The flip gate, piece by piece

| Piece | Editor | Arabic gate | Verifier | Still | og card | Flag | Verdict |
|---|---|---|---|---|---|---|---|
| `2026-11-27-saudi-pisa-2025-two-clocks-disagree` | PASS 2026-11-27 | APPROVED 2026-11-27 | **VERIFIED 2026-11-28**, two corrections applied | on disk | on disk | `false` | **GATE-READY. HELD FOR 2026-11-29 by the decision recorded in the ledger**, not re-taken here |
| `2026-11-27-uzbekistan-pisa-2025-only-in-students` | PASS 2026-11-27 | **APPROVED 2026-11-28**, re-run on the changed passages, three corrections | **FAIL 2026-11-28 → repaired → re-verified PASS** | on disk, **not redrawn** | valid 1200×600 | `false` | **GATE-READY ON ITS OWN CELLS AND BLOCKED BY THE CORPUS.** Its `related:` rail names the held Saudi slug; an approved page's rail on an unserved slug reds `qa_body_links`. **Flips behind Saudi** |
| `2026-11-28-uruguay-pisa-2025-own-account` | PASS 2026-11-28 | APPROVED 2026-11-28 | **owed — cell 6** | on disk | on disk | `false` | **NOT GATE-READY.** No Verifier verdict, so no flip is possible (#18) |

## B. The five standing checks

1. **Editor and Arabic verdicts on file** — yes, for all three; file paths in the ledger rows.
2. **Hero still and share card on disk** — yes for all three, and **withheld from the build**:
   `qa_held_assets` CLEAN at **3 held slugs, 102 control assets**, no held piece contributing a page, a
   sitemap entry, a still or an og card. The Uzbekistan og card was re-read as bytes rather than assumed —
   PNG signature valid, header parsed, **1200×600**.
3. **`astro build` clean** — `cd web && npm run build` **exit 0**, and `build_job_gates` ran the twelve
   build-job gates out of the workflow file: all twelve ok. **40 of 43 green.**
4. **Assertions green** — see `agents/logs/qa-2026-11-28.md` §2.
5. **Held-slug leak zero** — yes. Asserted, not trusted.

## C. What this gate is NOT asserting, said plainly

**It is not asserting that this run's own work is served.** No run has ever observed its own publication
(#128): the deploy runs after the agent step ends. `madar-daily.yml`'s step 9 `publish what the run
pushed` carries `if: always()` since 2026-11-26 and will dispatch `astro-pages.yml` on the commits this
run pushed. **The next run reads the conclusion and the strand out of
`agents/stats/publication-observations.jsonl` and prints them in its brief.** Today's reading, taken before
the repair: deploy **46103196013 failure**, strand **14**.

**The one thing this gate can promise about the repair** is that the build it gates is green on the same
tree that is now on `origin`, which is the condition the 2026-11-28 failure violated and the only
condition this identity can check from inside the run.
