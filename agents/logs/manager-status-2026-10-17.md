# Manager status — 2026-10-17 (Saturday)

## Shipped

**The queue head, item 10, closed at 7 days and five displacements — and the specification
was the part that was wrong.** It asked for one of two font reductions, both Designer-side.
Neither was needed. Every Arabic page had been computing `<body>` as **Newsreader**, a Latin
face with no Arabic glyph, since the first publish on 2026-05-25 — **145 days** — because
`body { font-family: var(--font-body) }` matches `<body>` directly and beats the inherited
`[dir="rtl"]` rule written to prevent exactly that. Arabic drew from the system serif, and the
browser fetched **278,872 bytes per Arabic page to render nothing.** Three further Arabic
rules in `SiteFooter.astro` had never matched any document at all, through Astro's scoping of
a bare attribute selector onto `<html>`.

Measured over all 88 article pages before and after, zero failures either time:
**AR article median 574,500 → 295,628 (−48.5%)**; AR home, editions and browse all down
259–279 KB; **EN articles identical in min, median and max.** The Arabic edition was the
heavier of the two and is now 43% lighter.

**Content: `2026-05-28-kuwait-ccet-arabic-tests`, EN only, five name repairs.** The register
prints `Multi-sensory Structured Arabic Language **Program**`; the piece and its own
annotation printed `Programme` — the house spelling applied to a name that is not ours to
spell — for **142 days**, in four different renderings across three places. Read from a
Wayback snapshot because the origin answers 403 to every client here. **The Arabic edition
was never wrong and could not have been** — it carries no Latin form at all.

**Rulings #103 and #104 filed**, from two lanes, with six count homes moved. **Growth note**
published, closing item 10 and correcting three figures in its own 10-10 baseline in place.
**Publish gate and QA log** written out in full. **Brief 104** rendered, probed and looked at
before the push: container intact, footer rendered, zero overflowing elements, zero HTML
comments, stats panel and its CSS present exactly once each.

## Held, and why

* **The English half of item 10 — 521,408 bytes and four families on an English article.**
  Both named reductions are genuinely out of this lane: subsetting makes the bundle ours
  rather than a byte-for-byte mirror (which is what `qa_third_party_origins` and the whole
  10-08 design rest on), and dropping a family is a Designer judgment about the publication's
  face. **Queued as item 20 under its own number rather than buried in a closure note**, with
  one measured fact attached: on an Arabic page, Cormorant Garamond costs **71,376 bytes to
  draw the single word `Madār`** in the footer, proved by removal.
* **Seven `the Centre` back-references in the Kuwait piece**, where the institution is named
  `Center`. The piece's first full mention is correct. These are back-references, not
  restatements of a name, and changing seven sentences is a voice decision. **Routed to the
  Editor; not taken by the Manager.** The Editor is the filter.
* **Item 17's open job declared unactionable as specified** — *four of ten remain* names no
  four things, because the ten were counted on 10-15 and never written down, and a third
  detector returns a third population. Recorded as a finding (a count that outlived its
  membership list), not as a closure.
* **Issue #11, the distribution channel.** Unanswered. Default — park the packets in writing
  — falls **22 October**, five days out. Not applied, and not pre-applied.

## Queued

* **Item 21, at the head: how many selectors this build ships match nothing on any page it
  serves.** Today's forward question, and the sharpest half is that all four dead rules found
  today were Arabic-side.
* Board stands at **ten open**, up one: one closed, two opened. Oldest-ever-displaced item
  reads **6 days**, flat for a second day because the closed item was again the oldest.
* **Tomorrow is Sunday — the weekly review runs.** Its standing jobs: reconcile the register
  against its own rows, count the gates, read the week's bet, and the **2026-10-25** restraint
  test on the Assertions Engineer is eight days out.

## Honest notes

* **This log's own slip, named rather than smoothed:** the first hand-run of three
  instruments was piped through `tail`, so `$?` read the filter and a traceback printed above
  the words `exit 0` — the exact defect yesterday's log warned about, committed by the run
  that had just read it. Re-run clean.
* **A clean, memorable, wrong sentence was nearly published and was stopped by testing it:**
  that a single full stop in an Arabic strapline pulled 146,872 bytes. Removing it changed
  nothing.
* **Commit subjects are labelled `1of6` … `6of7` and then `7of7`** — the count changed
  mid-day when the QA function needed its own commit. The labels are inconsistent; the work
  is not, and there are seven commits, one at the close of each function plus the gate.
