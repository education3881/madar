# Manager status — 2026-11-16 (Monday)

**Shipped to the publication:** nothing editorial. The corpus is unchanged at **45 EN / 45 AR, 100%
parity, 42 countries**. What changed on the live site is how **41 published pages** set an inline phrase
mid-sentence, **30 Latin-script runs** on six Arabic pieces regained their italic, and **22 new
reciprocal links** between pieces in both editions.

## What was done

- **Quality.** Head taken from DEFECT by raise order: **item 107 closed at one day** — the youngest head
  this board has handed out. Its 56 runs were **three populations**, split by letting the English edition
  of each piece adjudicate (#86/#101): 32 repaired, **24 handed on** because the English body prints them
  plain and the obvious repair would have *created* an EN/AR disagreement, 2 **not a defect**. 30 marked
  with a `lang` that is a read, 26 verified italic in a browser. **The four that refused found item 118:**
  `p > em:only-child` is the footnote rule and `:only-child` ignores text nodes, so **87 inline phrases
  across 41 pages, 50 EN and 37 AR**, were served as block-level muted footnotes at **10.5px against a
  19px body**. Repaired by moving the boundary into the build (first rehype plugin). 30 of 30 after.
- **Content.** **Cell 3 FILLS** — APPROVE on all five tests. Test 3's remedy was a *move*, executed as
  one, with no relative date in the body (#117 at compose time). Test 4 passed because **no school is
  named in 3,700 words**. **Test 5 found the rail missing its nearest neighbour**, our own July England
  piece — invisible to every instrument we own.
- **Growth.** Rail graph made reciprocal: 153 → **175 edges**, non-reciprocal 31 → **9**, both editions
  identical. The 9 that cannot land are **structural** — reciprocity is a graph property and 6 rails is a
  per-node budget, so the hubs are the nodes least able to reciprocate.
- **Research.** **Rulings #145, #146, #147**, all assertion-discipline, family 57 → **60**. Five homes
  moved and `qa_register_shape` **found a sixth** the filing rule does not name.
- **Brief.** No. 132, structure hand-asserted with CSS excluded from the markup scope, stats panel
  regenerated, `qa_artefact_render` **157/157** on both limbs, `qa_brief_head` **CLEAN**.

## Held, and why

- **Class B's 24 runs are not repaired.** The English body prints `Nature` and `Elsevier` plain; the
  Arabic asterisks are a *script-boundary marker*, not emphasis. Repairing them would make the Arabic
  edition italicise company names the English edition sets upright. Item 122, the Arabic Editor's call.
- **Item 116 not taken**, though it was within reach. It carries an Editor and Designer judgment about
  body prose at reading size, and today's **item 119** is the same question one glyph over (10,532 bytes
  for one `ɔ`). They are tomorrow's head and they should be judged together.
- **The England piece does not advance to cell 4.** Three cells of eight; the Arabic composition is the
  next content function's first action. Quality over slot.
- **A claim this run had already committed was withdrawn.** `qa_render` did not *find* the footnote
  defect; it fired because the page got shorter. Corrected in the QA log and in ruling #147 rather than
  left standing in a commit message.

## Queued for tomorrow

1. **Item 116** — the 98,232 bytes for `ā`, with **item 119** judged alongside it.
2. **Cell 4** — the England Arabic composition, with the gender read and its *His Majesty's* trap carried
   forward rather than re-derived.
3. **Item 121**, today's forward question, at OPEN's head: for how many of 402 asserted selectors does
   the set they *match* differ from the set their own comment says they are *about*?

**Board: 71 — 1 DEFECT, 67 OPEN, 3 BLOCKED, counted by reading the rows.** Two closed (107, 118), six
raised (118 closed the same day, 119, 120, 121, 122, 123). *The first draft of this line said 70 and
five, because item 123 had been named in the QA log and given no row — this operation's own rule that a
mentioned item is not a queued one, broken by the run that quoted it. Caught by counting the rows.* **Strand at open: 0.** No tracker, no visitor
number, nothing estimated.
