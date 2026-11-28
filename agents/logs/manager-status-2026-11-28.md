# Manager status — 2026-11-28 (daily run)

## What shipped — TWO pieces reached readers today

1. **`2026-11-26-uae-pisa-2025-all-three-lists`** — Edition 06's fifth. It went to `main` at 03:01Z from
   the content run and **was not served**, because that run's own closing commit red the build. This run
   repaired it.
2. **`2026-11-27-saudi-pisa-2025-two-clocks-disagree`** — *Saudi Arabia's reading, up five and down
   eighteen*. Edition 06's **sixth**, flipped by this run in both editions with its rails, still and card.
   Gate: `content-drafts/verdicts/2026-11-28-saudi-pisa-2025-two-clocks-disagree-publish-gate.md`.

**Edition 06 is at 6 of 6 — the founder directive's floor — met on 2026-11-28 with eight days of window
left, against a target of seven.**

## The day's defect, first
`astro-pages.yml` run **46103196013** failed on `npm run build` on the then-current `HEAD`. One stray `|`
inside a prose cell of the standing ledger's in-flight table gave that row six fields against a five-field
header; `qa_register_shape` red; deploy and verify **skipped**; strand **14 commits that no successful
deploy had carried**. Repaired in one character; rebuilt green on all 40 gates; pushed. Raised as queue
**item 168** — the missing thing is not a gate but a *step* between a write and a commit.

## Why the Saudi hold was lifted
Yesterday's run held it for 2026-11-29 and recorded its reasoning so today's would not re-decide it. **The
reasoning was conditional on a board that moved three hours after it was written** — it said the only other
row was at cell 4, five cells from the flag, and the same content run then took Uzbekistan to cells 5 and 7
and Uruguay from 1 to 7. This run closed both their cell 6s. **The guarantee the hold was buying is now
bought twice over.** A recorded decision is applied to the state it names; this one named a state that no
longer exists. The full argument is in the publish gate.

## What was held, and why
- **`2026-11-27-uzbekistan-pisa-2025-only-in-students`, 7 of 8** — cell 6 **FAILED WITH ITEMS on the
  piece's central claim**, repaired in both editions and re-verified PASS in the same run. **Ships
  2026-11-29**, first in the order.
- **`2026-11-28-uruguay-pisa-2025-own-account`, 7 of 8** — cell 6 **PASS with two corrections**. Ships
  **2026-11-30**, second, because its rail names the Uzbekistan slug. The order is derived from the
  corpus, not chosen.
- **`2026-11-22-abu-dhabi-irtiqaa-biennial-yield`** — parked to Edition 10, no run time spent.

**The board is two, one short of the plan's three.** The Editor's standing condition governs the third: a
named human from a reachable non-OECD register, or this edition stops where it is.

## What the two verifications found
- **Uzbekistan:** the chapter prints the score-point change the piece said it does not print — **I.2.12
  girls +85, boys +80; I.2.10 disadvantaged +85, advantaged +87**, the largest row in each. Every figure
  right, every quotation verbatim; the claim was a **negative** one, which has no second operand. **Ruling
  #162.**
- **Uruguay:** PASS. All four Uruguayan registers re-fetched **directly** and all four reproduced — the
  first Ed06 piece verified without an archive in the loop. Two corrections: a stale citation of **our own**
  Uzbekistan title, falsified three hours after composition by this run's own repair (**item 169** — a
  title quoted in a body is the one claim in this corpus with no checker), and a claim about the OECD's
  volume scheme that the piece's own cited index falsifies.

## Queued for tomorrow (Sunday — the weekly review also runs)
1. **Uzbekistan cell 8**, then **Uruguay** on 11-30 → Edition 06 at 8, two above its floor.
2. **A third commission** under the Editor's standing condition. **Eleven doors were measured for it today
   and no commission was made** — `content-drafts/recon/2026-11-28-ed06-seventh-piece-door-test.md`. The
   condition stopped a commission rather than slowed one, which is what it is for. **Two doors are open and
   unwalked and the next step is named in order:** `eec.mn` (Mongolia's Education Evaluation Centre, 200,
   574,232 bytes, no `pisa` on the front page but the link set unwalked) then
   `kemendikdasmen.go.id` (Indonesia). The painful miss is **`naec.ge`**, which answers 200 and is an
   AngularJS wall — 436 characters of served text — while Georgia is second only to Uzbekistan in the
   score-point table.
3. **For the weekly review, handed up rather than answered inside a flip commit:** the edition's opener is
   at six forward rails and the convention caps it there. Saudi's fourth reciprocal edge was **declined and
   recorded** rather than granted or displaced, because a displacement rule invented at a flip is a policy
   nobody can review. One inbound path, one piece, one day.
4. The forward question, at OPEN's head: **count the served sentences that assert an absence, and how many
   state the population they searched.**
5. Edition 07's slate by Thursday 3 December. `moe.gov.cn` answers this runner directly and the ministry
   publishes its own Arabic edition — a configuration ruling #160 has no entry for.

## Honest notes
- **No day was dark.** The content run ran and did good work, and lost a day's publication on one character.
- The plan's housekeeping is complete: issue **#13** closed, **#17** closed, **#7** commented on 11-27.
  No founder decision is owed today.
- **40 of 43 gates green**, publish gate in writing, held-slug leak zero on the two pieces still held.
