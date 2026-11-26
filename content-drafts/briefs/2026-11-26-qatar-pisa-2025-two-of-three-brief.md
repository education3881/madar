# Editor's brief: Edition 06, piece 3. "Qatar, on two lists of three"

**Slug** `2026-11-26-qatar-pisa-2025-two-of-three` · **Edition** 06 · **Drafter** Content Creator I (GCC/MENA)
· **Arabic** Arabic Content Creator · **Filed** 2026-11-26 · **Cell 1 only. CELL 2 IS BLOCKED, by design.**

## The finding, and the exact shape of its hole
Qatar is on the OECD's **ten-year** science improver list and on its **both-ends** list, and it is **absent
from the three-year list**. That is what the three registers print. The recon's own prohibition is binding
and is repeated here because it is the whole commission: *a piece may say Qatar is absent from the
since-2022 list. It may not say anything about Qatar's 2022 to 2025 change without Qatar's country note.*

So the piece has a spine only once **one** of two registers is read in served text:
1. **Qatar's own authority** on PISA 2025 — the Ministry of Education and Higher Education, or the Planning
   and Statistics Authority, or an Evaluation Institute publication, whichever carries the figures.
2. **The OECD's Qatar country note or country-level table** for PISA 2025.

**Until one of those is read, this piece does not advance past cell 1, and it must not be drafted from the
absence alone.** An absence from a list is the question, not the answer.

## Reachability measured 2026-11-26, recorded so the next run does not re-spend it
| Register | Result from this runner |
|---|---|
| `edu.gov.qa` | **no answer at all** (curl returns 000, not a status code) |
| `etec.gov.sa` (the Saudi comparator) | 200 after redirect, 484 KB — **and its news index carries no PISA text in the served bytes**, so it is JS-rendered and unreadable by the house method |
| `moe.gov.ae` media centre | 200, 37 KB — **same: no PISA text in served bytes** |
| `wam.ae` search | 200, 14 KB — the same shape |
| OECD country notes | **not linked from R1, R2 or R3**; a Wayback CDX domain query for `pisa-2025` URLs returned **504** twice |
| `www.oecd.org` direct | **403**, as it has been all month. Archive snapshots of the three main registers fetch fine from this runner. |

**What that table means for the edition:** every remaining country-anchored candidate on the slate is
blocked on a register this runner cannot read in served text, and every remaining OECD-wide candidate is
blocked on `docs/10_geo_scope.md`'s rule that a piece must be about an in-scope geography rather than about
the institution. **That is the Edition 06 constraint, measured rather than guessed, and it is the research
increment of 2026-11-26.**

## Prohibitions (binding at commission, not at verdict)
- No statement about Qatar's score in any subject between 2022 and 2025, in either direction.
- No inference from the absence. *Absent from a list* is not *fell*, and is not *was excluded*.
- No comparison of Qatar with Jordan, Saudi Arabia or the UAE across different lists — that is comparing
  two questions (piece 1's own finding).
- Every figure carries its scale, its years and whose average it is.

## Cross-link
Follows up `2026-11-26-pisa-2025-three-lists-of-risers` and `2026-05-31-qatar-humanity-spark-strategy`.
Forward edges into both owed at cell 8.

## Length
1,300 to 1,800 words when it is writable. Dek at most 200 code points, measured at compose.
