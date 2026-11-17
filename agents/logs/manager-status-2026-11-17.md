# Manager status — 2026-11-17 (Tuesday)

**State verified before anything was planned.** `HEAD == origin/main` at `e0e0ea3`, clean tree. Deploy
43879692641 **success** on that exact SHA, origin serving the tip, **strand 0** — yesterday's close asked
whether its eight commits would be carried and they were. No missed day.

## What shipped

**Nothing editorial.** The corpus is unchanged at **45 EN / 45 AR, parity 100%, 42 countries**. Said
plainly, not absorbed.

**What changed on the live site**, in both editions:

- **284,492 bytes removed across the six measured pages** with the rendered output provably unchanged —
  0 differing pixels of 3,120,000 on a full-page comparison, and 0 differing pixels in three faces at
  three sizes. EN home 613,540 → 515,308. EN editions 636,664 → **495,764**. AR editions −33,736. EN
  article −11,624.
- **All 139 served pages stopped claiming to be Edition 05 at page level.** The EN home's `<title>` and
  `og:title`, both home top bars and the footer's issue line on every page. One mention of *Edition 05*
  remains and it is the edition block's own, which is correct.

## What was held, and why

- **The three published article bodies that still spell `Madār` the expensive way** (~86,608 bytes each).
  The repair is proved and the prose is published, so it is the **Editor's** call and not mine. Queue item
  **125**, with the proof attached. The other four body instances (`fuṣḥā`, `ʿāmmiyya`, `Māori`,
  `pāngarau`) **cannot be made cheaper at any price** and are recorded as a price.
- **`qa_font_payload`'s flaky gated limb.** Met again, same page and same file as yesterday; five
  immediate re-runs clean; pooled **2 reds in 11 readings, ~18%**. Not fixed — a fix to an assertion is the
  Assertions Engineer's and the day's head was already spent. The **rate** is now on the row (item 124),
  because that is what makes it urgent: in the deploy's build job it is a deploy skipped roughly one push
  in five.
- **Item 119 was not deferred, it was decided.** `ɔ` is kept and the 10,532 bytes are a price we pay. A
  row that has been waiting for a judgment gets one.

## Queued

**Board 73, counted against the rows: ZERO DEFECT · 70 OPEN · 3 BLOCKED.** Two closed (116, 119), three
raised (125, 126, 127).

- **Tomorrow's head: the oldest OPEN row**, the DEFECT bucket being empty for the first time since 11-12.
  Item **124** is the sharpest row on the board and is **named rather than promoted** — raised yesterday,
  therefore the youngest; if the oldest-first rule is to be broken it is broken in writing by the run that
  breaks it.
- **Content: the Arabic Editor's gate** on `2026-11-12-england-ofsted-exempt-cohort` — cell 5 of 8, with
  two items the composition handed up rather than settled: the **eleven grade renderings**, to be judged
  as a set because the regulator publishes nothing in Arabic and so every one is ours; and the **editorial
  future owed as a correction on the English pair**, whose hand-off line 6 reads zero.
- **Issue #13 stays open.** Nothing today pre-empted it; one boolean carries every edition label.

## Rulings filed

**#148** — a cost is a defect only where an equivalent exists; otherwise it is a price, and which one it is
is decided mechanically. Closed items 116 and 119 together.
**#149** — obligatory morphology makes the composer a detector for exactly the property a string-matcher
cannot see. **Amends #117 clause 4.**

Register at **#1–#149**, all four range homes plus both family counts and the ratio moved at the point of
filing; `qa_register_shape` CLEAN — after failing twice on my own edits.

## Verification at the close

Build **exit 0**, all **42** assertions and all **12** build-job gates green. `qa_brief_head` CLEAN across
135 briefs and 22 reviews. `qa_artefact_render` 158 artefacts on both limbs, today's brief included.
Brief 133 structure hand-asserted: 3 sections, beats Yesterday/Today/Tomorrow in order, one `html`/`head`/
`body`/`main`, every pair balanced, stack empty, no nested `.container`, 4 stat tiles, 5 stats rows, no
unescaped angle bracket.

**No tracker, no analytics, no third-party request, and no visitor number anywhere in brief 133.**

## Envelope

Five functions, each committed and pushed as it closed (#96) — none saved for the end. Wall clock well
inside 90 minutes; the turn axis printed **UNMEASURABLE FOR THIS RUN** on every call, beside its base rate
over the 47 daily runs behind it.
