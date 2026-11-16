# Ruling #147 — a partial window is not a comparison, and a changed file is not a changed subject

**Filed:** 2026-11-16, by the growth function, from correcting `qa_render`.
**Family:** Assertion discipline (member **sixty**).
**Sharpens #35 in its second clause. Amends nothing.**

## Clause 1 — a window that is not the size of its ruler is not a measurement

**A measurement partitioned into fixed windows and judged against a floor calibrated on a full window
must not judge the REMAINDER, because the verdict is then a function of `size mod window` — a number
that is not a property of the thing being measured.**

`qa_render` asserts per-band ink at `BAND = 900` rows with `BAND_INK_FLOOR = 0.006`, and iterated
`range(0, height, BAND)`. The Arabic article page is **5450** rows, so the final band was **50 rows** —
the footer's bottom padding, **legitimately blank**, reading ink exactly **0.0000** — and it failed the
build after the growth function added four `related:` rails. **Nothing was wrong with that page.**

**It fired twice in one run, and the second firing is what proved it.** The first, that morning, was a
130-row remainder on the English article while a real defect *was* present (#146's sign-off). **So the
earlier claim that the gate "found" that defect is wrong, and the correction is the point of this
ruling:** the band fired because the page got **shorter**. A tripwire that answers *did the height
change* is not an instrument for *is the page right*. The defect was found by **reading a count**. The
Arabic case settles it, because there the height moved for an entirely correct reason.

**Fixed, not weakened:** every band is now a full `BAND` rows, the last **anchored at `height - BAND`**.
It overlaps its predecessor deliberately — these are measurement windows, not a partition — and the
bottom of a page now receives a **full screenful** of scrutiny instead of whatever is left over.
Control: CLEAN, 22 bands of 900px, worst band ink **0.0141**. Bite: a 1,200px empty block before
`</body>` → **FAIL on two full bands, both 0.0000**.

**The temptation this ruling exists to refuse:** the artefact had once coincided with a real defect, and
that is the standard argument for keeping a noisy check. *Keeping an artefact because it once coincided
with a defect is how a gate becomes a habit* — the 2026-09-13 lesson arriving from the opposite side,
where a check that costs attention is paid for out of the runs that have least of it.

## Clause 2 — a changed file is not a changed subject

**#35 requires that a bite be shown to have changed the artefact. That is not sufficient. It must be
shown to have changed the artefact THE ASSERTION READS.**

The first bite injected 1,000 blank pixels into `ar/articles/2026-07-04-kenya-cbe-grade10-pathways` and
`qa_render` returned **byte-identical band figures and exit 0** — because its `TARGETS` list names
**`bo-teacher-chalk`** as the AR article. The sha256 comparison ran, proved the file had changed, and
**proved the wrong thing.** A passing control and a mis-aimed bite are indistinguishable in the output,
which is 2026-09-14's trap with the hash discipline already in place — *the discipline was satisfied and
the proof was still void.*

**Binding:** a bite names the artefact the assertion reads, proves that artefact changed, and where the
assertion has a target list the bite is aimed **by reading the list**, never by choosing a
representative instance. An assertion with a fixed probe set is a **sampling** instrument, and a bite
aimed outside the sample measures nothing — the same blindness that let this change's own byte cost go
unmeasured until the probe was re-pointed (#145's cost table; item 39's *cost is a `(page, family)`
pair*).

## General form

*Clause 1: check that your ruler and your window are the same size before you believe a reading.
Clause 2: check that your experiment touched your subject before you believe a result.* Both are the
same error at different ends of one instrument — **a comparison between two things that are not
comparable** — and both were invisible while every number on the page looked plausible.

**Evidence:** `agents/logs/qa-2026-11-16.md` (addendum); `agents/tools/qa_render.py` (`band_tops`);
queue item 123.
