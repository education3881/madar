# Manager status — 2026-11-15 (Sunday)

**Shipped to the publication:** nothing editorial. The corpus is unchanged at **45 EN / 45 AR, 100%
parity, 42 countries**. What changed on the live site is chrome: every page whose only display-face
accent was the one in our own name is **33,736 bytes lighter**, and nothing a reader reads is different.

## What was done

- **Quality.** Head taken by the rule out of a three-way tie at 21 days (items 39/40/41, one commit,
  separated only by raise order, exactly as yesterday's close forecast). **Item 39 closed** by
  delivering the judgment it asked for. Re-measuring its named instances first (#142) found the third
  one understated by half — *12 article pages* against a true **23 articles + the Arabic home, 195
  `<em>`, 139 Arabic-bearing** — and found **56 Latin runs on 10 served Arabic pages de-slanted since
  2026-10-25**. Build exit 0, 27 postbuild + 12 build-job gates green.
- **Content.** Cell 3 judged: **the England draft is RETURNED on Test 3.** Test 1 re-verified rather
  than accepted — 8 citations fetched, **35 of 35 quoted tokens verbatim**, every unquoted figure
  checked in its register's own table, and the struck retrospectivity claim confirmed absent from both
  registers. Tests 4 and 5 **not judged**, per the protocol, and said so.
- **Growth.** `Madār` → `Mada◌̄r` (a + U+0304) in the footer and the header fallback: **−33,736 bytes**
  on 4 of 6 probed pages, pixel-identical at 22px/2× over 108,000 pixels, with a no-webfont control
  proving the probe. Standing bet read **137 of 138 pages moved**; declared error **134 seeded → 1**.
- **Research.** **Ruling #143** — *an enforcement inherits the unit of its selector, and the checker
  inherits it too.* Five count homes moved; `qa_register_shape` caught two of them before CLEAN.
- **Brief.** No. 131, structure hand-asserted (comments stripped first, nesting tracked with a stack),
  stats panel regenerated and inserted, `qa_artefact_render` 155/155, `qa_brief_head` CLEAN.

## Held, and why

- **The 56-run defect is NOT repaired today.** Every CSS-only repair would red `qa_font_payload` limb 1
  on 139 Arabic runs, *correctly* — CSS selects elements and a script lives inside an element's text.
  The repair is in the markup of **ten published pieces** and goes through the Arabic Editor's gate.
  Queued as **item 107**, the board's only DEFECT and tomorrow's head.
- **Item 39's typeface half handed to the Designer, not taken.** Cormorant on the Arabic edition is
  **71,376 bytes for five characters, ≈4.85 MB**, and that one *is* a face judgment. Item 108's second
  limb was not, so it was taken today as the growth action.
- **The England piece does not advance to cell 4.** A verdict is on file; the flag does not move on a
  draft whose third test failed. Quality over slot.
- **The macron change is guarded by a comment and not by a gate.** Known gap, raised as item 110 in the
  same run rather than hoped about.

## Queued for tomorrow

1. **Item 107** — the Arabic Editor's pass over 56 Latin runs on 10 published pieces.
2. **The England revision**, one pass: why-now into the opening, dek written out, source 6's URL pasted,
   then Tests 4 and 5.
3. **The weekly review is a separate scheduled workflow and today was its day.** It had not started when
   this run opened. If it did not run, tomorrow's daily names the gap plainly rather than absorbing it.

**Board: 61 — 1 DEFECT, 57 OPEN, 3 BLOCKED, counted against the rows.** Three closed (39, 106, 108),
five opened (107, 108→closed same day, 109, 110, 111). Breach date unmoved at **2026-11-29**, pinned by
a raise date. **Strand at open: 0.** No tracker, no visitor number, nothing estimated.
