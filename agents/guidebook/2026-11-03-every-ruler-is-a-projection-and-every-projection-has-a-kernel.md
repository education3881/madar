# Ruling #126 — Every ruler is a projection, and every projection has a kernel

**Filed** 2026-11-03 · **earned by** standing-queue item **28**, raised 2026-10-19 as the daily's
forward question, closed today at **15 days** from the OPEN head · **family** assertion discipline
(**forty-seventh member**) · **instrument changed** `qa_render`, standing assertion 14.

---

## The rule

**A ruler is a projection. Every projection has a kernel — a set of distinct states it maps to one
output — and a defect inside the kernel is invisible no matter how much the check enumerates.**

Six standing rulings say *a green check is scoped to what it enumerates* (08-09 flag inversion, 08-16
chrome 404, 08-17 orphan sweep, 08-18 consumer format, 08-23 founder-facing artefacts, 09-06 held
dates). **All six ask what entered the measurement. None asks what the measurement cannot distinguish
once it is in.** Those are different questions with different remedies, and conflating them is how an
instrument gets widened in the only direction that cannot help it.

**Binding, in three clauses:**

1. **An assertion's header states its ruler and its kernel in the same sentence.** Not the target list
   — the arithmetic, and what the arithmetic collapses. *A count collapses position. A ratio collapses
   locality. A sign collapses dimension. A computed style collapses the layer below it.*
2. **A kernel is closed by changing the ruler or by constructing the geometry in which it is empty —
   never by enumerating more.** Adding targets to a check whose defect is in the kernel buys nothing
   and reads like diligence.
3. **Where neither remedy is available, the kernel is printed with the ruler change that would empty
   it**, as a decline under #93 and written per #125. It is a row on the standing queue and not a
   watch, because this class of decline does **not** expire by arithmetic (item 71) — only by somebody
   changing the arithmetic.

## What the question was asked of, and the four answers

| # | instrument | the ruler | its KERNEL | remedy taken |
|---|---|---|---|---|
| 14 | `qa_render` | pixel population count over a raster | **extent** + **position** | ruler changed |
| 17 | `qa_arabic_shaping` | computed-style string | **the layer below** | already changed — assertion 18 |
| 18 | `qa_arabic_joining` | one scalar width ratio over one run | **locality** | printed; item 74 |
| 26 | `qa_feed_direction` | pairwise sign of Δx | **dimension** | geometry constructed — kernel EMPTY |

### `qa_render` — the only instrument this operation owns that looks at a pixel, reading one screenful

**Extent.** `--screenshot` under `--headless=new` captures the **viewport**, not the document. Old
headless captured the full page; **the flag name did not change when the behaviour did.** Every raster
this tool had ever read was **1200×900**, against documents 2,559 to 5,648 px tall — the ruler held
**29.6% / 35.2% / 15.9% / 16.9%** of its four targets, while the output printed one line per *page*.

**It was never a regression**, and that is the part worth keeping. The floors were calibrated on
2026-09-15 from `--report` values of ink 0.0216–0.0506, and the viewport numbers measured today
reproduce that range to the digit. **The instrument was calibrated inside its own kernel**, which is
why forty-nine days of green said nothing about it — and why the crop sat exactly where the properties
cannot fail, over the masthead and the opening of the article, the most reliably-inked part of any page.

**Position.** Widening the raster **alone would have reduced sensitivity.** A pixel count has no
coordinates and the lower page is less ink-dense: the EN home's dark fraction *falls* from 0.0095 to
0.0053 when the ruler is widened. The decisive pair is this — the EN home's whole-page dark is
**0.0053 and passes the 0.003 floor**, and **its own last band reads 0.0006, five times below that
floor and invisible to the average.** So both kernels had to be closed in one change or neither.

**What shipped.** The shot is taken at the document's own height, and **P1 NOT BLANK is asserted per
900 px band**. The property is now *no screenful of any page is blank* — which is what the 2026-08-16
edge-to-edge defect actually was — rather than *the page as a whole drew something*, which no page with
a masthead can fail. The height is **verified rather than assumed**: measured at a 900 px viewport,
re-measured at the height about to be shot, and the page **refused** if the two disagree, because a
layout that depends on viewport height cannot be captured in one raster. Floors chosen from measurement
before anything was asserted (#93): band ink 0.0114–0.0612 across all 21 bands, floor 0.006.

### `qa_arabic_joining` — the kernel the ruler's own dynamic range forces

The SERVED half takes the page's **longest** Arabic run and compares its advance width against its own
ZWNJ-de-joined self, failing above 0.90. Measured by injecting N evenly-spaced ZWNJ into the real run:
**one broken join is invisible to three decimals on three of four targets**, **128 broken joins of 511
reads 0.742**, and 79% of the AR home's run broken reads 0.863 and **passes**. It reads **1 of up to 49**
eligible runs per page.

**And the two limits cause each other.** A ratio over a short run has no dynamic range — the tool's own
header records `مدار` at 0.972 shaped and says no threshold can separate it — so `SERVED_MIN_LEN = 12`
and the longest run is selected, and **the longest run is the one in which a single broken join is most
diluted.** *The ruler's dynamic range and its locality trade against each other, and a single scalar
admits no other resolution.* This is the sharpest form of the rule: the kernel was not an oversight,
it was the price of the ruler having any range at all.

### `qa_feed_direction` — the kernel is empty, and that is the template

`signature()` pushes `b.left` and **discards `b.top`**, so a line wrap and a direction flip are the same
symbol. The projection is one-dimensional over a two-dimensional layout — **and it loses nothing**,
because the probe pins `white-space: pre; width: 60000px` so no field can wrap, with the reason written
in the comment at the point of construction. **This is the only one of the four whose author
interrogated the ruler**, and the method is clause 2's second half: where you cannot widen a ruler,
construct the geometry in which its kernel is empty. The residue is named rather than asserted — that
geometry is **ours, not the consumer's**, and a subscriber's reader wraps (item 75).

### `qa_arabic_shaping` — already interrogated, and the interrogation is why 18 exists

Its header states the kernel in one sentence: *"computed style reports what was ASKED FOR, never what
the font DELIVERED."* Written into the 2026-09-17 QA log as a forward question and shipped as assertion
18 the next day. **One of four, and it took a day** — which is the evidence that clause 1 is cheap.

## The proof, and the harness that failed first

Proved per #35 with every injection asserted to have changed the artefact before either ruler read it
(the 09-14 discipline). Control green on both rulers. **Bite A — a screenful below the fold blanked —
exit 1 RED on the new ruler and exit 0 GREEN on the old**, which is not a formality: the old ruler's
green is the measurement of what the widening bought. Its message carries both halves at once:
*`rows 4500-5400 carry ink 0.0010, below floor 0.006 (whole raster 0.0385 passes)`*. Bite B
(`min-height:300vh`) fires the height guard; its first run did so as an **uncaught traceback**, fixed to
fail with a sentence, because a stack dump in CI reads as a broken tool and gets switched off.

**And the harness was wrong before the code was.** Both bites first reported GREEN on the new ruler
with the injections verifiably applied — a passing control's exact signature. The check was right;
`if cmd; then …; fi; rc=$?` captures the exit status of the `if`, not of `cmd`, so every verdict was
recorded as 0. ***A harness that projects {0, nonzero} onto {0} has a kernel too*** — this ruling's own
thesis, committed inside the proof of this ruling, which is #124's class on 11-01 and #125's on 11-02
making three consecutive filings whose gate or harness failed in the shape the filing was about. The
only reason it was caught is that the per-band numbers were **printed and read** (0.0295 → 0.0010)
rather than trusted.

## Cost

**8.0 s → 32.2 s**, 1.08 Mpx per target to 3.1–6.8 Mpx, plus two `--dump-dom` height passes per target.
Stated rather than hidden. **No sampling was introduced to pay for it:** item 41 asks which gating
assertions read a sample rather than a population, and closing an extent gap by reading every fourth row
would have answered that question in the wrong direction.

## Where it sits

Beside **#93** (a floor above today's reality reds every build — which is why two limbs are printed),
**#125** (how a decline must be written — the printed limb names no sibling because there is none),
**#116** and **#123** (*a bucket set is an enumeration too, and it cannot report a distinction it cannot
hold* — the same statement about an **ordering** and a **classification**; this is it about a
**measurement**), and the six enumeration rulings it is the complement of. Related: **#55** (the layer
question), **#16** (judge in the environment that judges — turned on our own probe at item 75).

## See also

* `agents/logs/qa-2026-11-03.md` — the full measurement tables and the displacement line.
* `agents/tools/qa_render.py` — the ruler, its kernel and the printed limbs, in the header.
* Standing-queue items **73**, **74**, **75** — the three kernels not closed today, each with the ruler
  change that would empty it.
