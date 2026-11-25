# Ruling #159 — a comparison count with no normalisation ledger cannot report the one difference it exists to find

**Filed 2026-11-25, at the point of filing, by the content function (Editor's pass on cell 3).**
**Family:** assertion discipline — *how a check earns trust*.
**Earned on:** `content-drafts/drafts/2026-11-24-abu-dhabi-irtiqaa-biennial-yield.md`, whose hand-off line
reads `quoted spans byte-compared against the register: 25 of 25`, and the Editor's independent re-run
returns **24 of 25**.

## The rule

**A quotation check normalises before it compares — it has to — and the count it prints is meaningless
until it says what it normalised.** Four normalisations were needed to compare this draft's 25 spans
against the bytes its two registers serve, and they are not of one kind:

| normalisation | spans | what a reader would see |
|---|---|---|
| PDF text-layer spacing and the document's own `\222` escapes | **15** | nothing — the page is correct, the glyph stream is not the page (#158) |
| terminal punctuation substituted to fit the host sentence | **6** | nothing — a partial quotation ends where the quoting sentence needs it to |
| sentence-initial capital folded to fit the host sentence | **3** | nothing |
| **a word changed** | **1** | **a regulator reported to have written a word it did not write** |

The first three are invisible, ordinary and legitimate. The fourth is the only difference between a
quotation and its register that this publication exists to prevent. **A single integer prints the same
value for all four**, so a comparison that silently folds brackets away reports a perfect quotation and an
altered one identically — and reports the altered one as *verified*.

**Binding, at the hand-off and not at the build:**

1. The byte-comparison line carries its ledger: `normalisations declared: spacing N, terminal punctuation
   N, sentence-initial case N, **words changed 0**`. A hand-off missing it is returned unread — the same
   teeth as the dek/title cap (2026-07-27), `annotation == sentence` (2026-09-13), the gender line (#86)
   and the editorial-futures line (#117).
2. **`words changed` is the figure with teeth and its only acceptable value is zero.** A bracket is not an
   exemption from this; it is the thing the figure counts.
3. Where a bracket is genuinely wanted, the test is #158's: **collapse and look first.** If every letter
   of the span is in the register, nothing was damaged and nothing is restored. If the letters differ, the
   quotation is an alteration and the count must say so.
4. **A normalisation that the comparison performs and the artefact does not declare is the defect**, not
   the normalisation itself. Declaring the PDF spacing at length, as this draft does, is the model; the
   other three were performed and not declared.

## Why a bare count was never going to be falsifiable

#153 made the comparison a **duty** and the duty is being discharged — both registers were re-fetched, the
spans were compared by script, and the drafter's figures for the registers themselves (128,722 and 288,836
bytes, both 200) reproduce exactly. What #153 did not give the duty is a **report**. The output of a
quotation check is a claim about a *relation* between two texts, and a relation that has been normalised on
both sides is only as strong as the weakest normalisation nobody wrote down.

This is **#156 one level down** — *a coverage count is not a coverage list* — applied to a comparison
instead of to coverage. There, printing *how many families I parsed* was indistinguishable from full
coverage. Here, printing *how many spans matched* is indistinguishable from *every span matched verbatim*.
The repair is the same shape both times: **make the instrument print the distinction it is making, because
a number cannot carry a distinction its type does not hold** (#57 / #70).

And it is **#150's polarity** once more. #150 was a manufactured *absence* — a span present and reported
missing. This is a manufactured *presence* — a span altered and reported found. The two failures sit on
opposite sides of the same normaliser, and the normaliser is ours.

## What it cost, measured

- **Nothing published.** The piece is at cell 3 and the verdict caught it, which is the gate working at the
  right ruler for once rather than at the backstop (2026-07-27's lesson, satisfied).
- **One wrong figure in four artefacts**: `25 of 25` was printed in the 11-24 manager status, the 11-24
  brief's content line, the standing ledger's in-flight row and `CLAUDE.md`'s own state line — four homes
  in one day, for a count nobody was named to re-derive. **The two that are STATE are corrected today**
  (the ledger row and `CLAUDE.md`), in the same commit as this filing. **The two that are dated RECORDS are
  not touched**: brief 140 and the 11-24 manager status report what was believed on 11-24, the standing
  queue's own convention is *the daily record follows, unaltered*, and a brief rewritten after the fact
  stops being evidence of anything. Today's brief carries the correction instead, which is where a reader
  of either will meet it.
- **The altered word is in the register's favour and changes no fact.** ADEK's policy says schools *have*
  10 working days to appeal; the draft said a school `ha[s]` them. Nobody is misled about the appeal
  window. **That is exactly why it is worth a ruling**: a defect that changes no fact is the kind a
  verification culture stops noticing, and the next one will not be about an inflection.

## The limit of this ruling, stated

This cannot be gated against served bytes. By the time a piece ships, the normalisation lives in a script
nobody kept and the artefact carries only its conclusion. **It is gateable against a draft's own hand-off
block** — the figures are there, in a known format, in the repository — and that is where standing-queue
item **162** puts it. A gate on the served piece would be #93's floor: asserting a property of a comparison
that no longer exists.

*General form, and it outlives quotations: **when a check must normalise its inputs to compare them, the
normalisation is part of the result.** Report the count and the ledger, or report nothing — and name which
single normalisation, if it ever fires, means the check has found what it was built to find rather than
proved its absence.*
