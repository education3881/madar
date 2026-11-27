# Manager status — 2026-11-27 (daily run)

## Shipped
- **`2026-11-26-qatar-pisa-2025-two-of-three`** — *Qatar's decade and its three years*, EN + AR, all eight
  gate cells closed in this run (cells 3 through 8), hero still and share card drawn and inspected, two
  forward rails written in the same commit as the flag. Publish gate in writing at
  `agents/logs/2026-11-27-publish-gate.md`.
- `2026-11-27-thailand-pisa-2025-fourth-list` shipped this morning from the content run and is serving.
- **Edition 06: 4 of 6**, ten days of window left. Two pieces served today — the first time on a day that
  was not an edition's opening day. The directive's floor of one a day: met on all three days.

## Held
Nothing held. **The corpus now contains zero `approved: false` pieces**, so the held-leak assertion is in
its vacuous mode and the 2026-08-09 inversion was applied — the positive checks were run in its place.

## In flight — three rows, the plan's floor met for the first time
| Row | Cell | Next |
|---|---|---|
| `2026-11-26-uae-pisa-2025-all-three-lists` | 1 of 8, re-briefed today | **cell 2.** Angle moved: ten-year reading trend −6 against a three-year +15 |
| `2026-11-27-saudi-pisa-2025-two-clocks-disagree` | 1 of 8, commissioned today | **cell 2.** Reading +5 on one clock, −18 on the other |
| `2026-11-22-abu-dhabi-irtiqaa-biennial-yield` | 2 of 8, **parked to Edition 10** | 28 December, costs no run time |

Neither live row is blocked. Every register both need is read, hashed and indexed at
`agents/guidebook/2026-11-27-oecd-pisa-2025-volume-i-chapter-2-source-index.md` (§1 row 156).

## What went wrong, stated plainly
1. **A provenance triple this operation published this morning does not reproduce** — the recorded snapshot
   date named a capture the byte count did not belong to, and the hash matched no capture of that page.
   Found at the Editor's desk, **repaired in both editions of the already-shipped Thailand piece**, filed as
   **ruling #161**. Nothing was fabricated and nothing was stale; the only wrong thing was the evidence that
   the row could be re-checked.
2. **`qa_claim_registers --emit` destroyed four register rows while I was using it to test yesterday's
   forward question.** The Wayback availability endpoint answers 200 and reports its own timeout in the
   body; the tool read that as *no snapshot* and overwrote four positive observations. The guard against
   outages existed and a success-code failure walked around it. Fixed, proved with two controls and two
   bites, four rows restored. Raised as item **167** because the register now holds a known error of
   **unknown** size — earlier emits ran the same code unwatched.
3. **Three red builds before green**, on three different gates, each catching something a reading would not.
   All named in `agents/logs/qa-2026-11-27.md`.

## Decided today, so nobody re-decides it
- **A self-citation is cited per language.** The pair gate's own note said the corpus held two rival
  conventions and only one could be the house rule. Settled; the one older pair that does it the other way
  is left as it shipped and the step is recorded rather than smoothed.
- **The rail step is amended**: forward edges are derived at cell 8 from the piece's own final `related:`,
  not read from the list frozen at cell 1 — because a commissioning brief cannot name a piece that does not
  exist yet, and under the directive something ships every day.

## Queued
Items **166** (no Arabic body marks a Latin run with its `lang`, against a standing prohibition that says it
must — raised with its real population, not with the one piece that found it), **167** (above), and the
forward question: *every citation gate checks a row we wrote and none re-fetches what the row describes —
of the 297 rows claiming a snapshot, how many still resolve?*

## Not done
No Arabic `lang` markup applied — it changes served bytes, it is the Web Developer's line, and the pattern
has never been proved against the three Arabic gates. No UAE draft; the content run has it next with
everything it needs on disk.
