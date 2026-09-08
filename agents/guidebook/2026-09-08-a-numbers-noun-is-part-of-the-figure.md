# A number's noun is part of the figure

**Ruling #45 · Section 1, row 40 · filed 2026-09-08 by the Verifier**
**Family:** the figure-trace axes (#12/#12b coverage, #14 funnel stage, #21 vintage,
#22 scope, #23 direction, #24 position, #25 condition) — this adds the eighth: **type.**

---

## The rule

**A figure is a value *and* a noun, and the noun is checked like the value.**
*Price*, *saving*, *budget*, *target*, *reached*, *planned*, *pledged*, *estimated*,
*avoided* — these are not framing around the number, they are part of it. Two sentences
carrying the same digits and different nouns carry different figures, and a draft that
substitutes one noun for another has misquoted its source while transcribing it perfectly.

**Corollary 1 — a saving is not a price.** They are related by an arithmetic the source
usually does not print, and inferring the missing term is adjudicating a source against
itself (#38). Carry the noun the source uses and let the reader do the subtraction, or
carry both terms only if the source prints both.

**Corollary 2 — the word *unambiguously* is a claim, and it is checked.** When a draft
tells the reader a figure is beyond dispute, the draft has taken on a burden the source
may not carry. Any sentence that vouches for a figure's clarity must be traced *harder*
than the figures around it, not waved through on the strength of its own confidence.

**Corollary 3 — two channels of *figure* checking cannot catch a *type* error.** #27 says
a clean figure is confirmed by two independently-routed reads. Both reads return the same
digits, because the digits are right. Only a read of the source **sentence** — its verb
and its noun — catches this class. The trace must therefore quote the source clause, not
record the number.

---

## Where it bit

**Zambia, *The law that moved the finish line*, verified 2026-09-08** — Edition 05's first
verification verdict, and the piece failed on exactly one item, this one.

The piece said the Examinations Council built its results-processing system
> for **K4.7 million**, against an estimated K15 million to procure it externally

The source (ZANIS, re-fetched as served 09-08, ¶408) says
> at a cost of 4.7 Million Kwacha, **a move that has saved Government about 15 Million
> Kwacha** that would have been spent on procuring an external system.

The source states a **saving**. The piece states a **price**. They coincide only under one
of the sentence's two readings:

| Reading | External system | Net saving | Piece |
|---|---|---|---|
| A — the 15m that *would have been spent* was avoided | K15m | K10.3m | correct |
| B — the saving itself is 15m | K19.7m | K15m | wrong by K4.7m |

Reading A is the likelier parse. *Likelier* is not the standard, and the piece had
introduced the paragraph with **"One number in that announcement is unambiguously an
achievement"** — vouching for the clarity of the one figure on the page whose source
sentence is unclear.

**Both languages carried the price reading independently.** The Arabic composed
*«مقابل تقديرٍ بخمسةَ عشرَ مليونًا لشرائه من الخارج»* — "against an estimate of fifteen
million to buy it from abroad." A pair wrong in parallel is wrong twice; the AR gate and
the Editor's numeral-multiset test both passed it, correctly, because **the multiset test
compares values and this defect lives in the noun.**

**Why every existing instrument missed it.** The value is right, so the figure trace
passed. The digits match across languages, so the multiset test passed. It is not a
vintage, scope, direction, position, condition, coverage or funnel-stage error, so none
of the seven axes named it. It is not an arithmetic failure, so the sums passed. The
defect had no axis until now.

## The fix, and its shape

Rendered in the source's own grammar in EN, in AR, and in **both** `sources[]` titles —
a saving, attributed to the named Executive Director, hedged with the source's *about*.
K19.7m was **not** computed: that is reading B asserted, which is the error inverted.

## Applied to our own method, same run

The Verifier's figure-trace table gains a **type** column beside the register column
(#43) and the scale column (#44). The question the trace now asks at every row:
**what noun does the source attach to this number, and is it the noun in our sentence?**

The pair returns to the queue for a confirmation read at the wave gate rather than
flipping on the verdict — the fix is ours, so the check on the fix cannot also be ours in
the same breath.

## Where else to look first

Anywhere the operation converts a comparison into a level. Candidates already in the
corpus and in recon: *cost avoided* vs *cost*, *gap closed* vs *gap*, *additional* vs
*total* (the deficit-is-a-ratio family, row 20), *allocated* vs *filled* (this same piece
handles it correctly, twice, at the 30,000 posts), *targeted* vs *reached* vs *completed*
(Sierra Leone's rare downward drift, handled correctly). The Zambia piece got the noun
right everywhere it was a funnel stage and wrong the one place it was an accounting term.

— Verifier · 2026-09-08
