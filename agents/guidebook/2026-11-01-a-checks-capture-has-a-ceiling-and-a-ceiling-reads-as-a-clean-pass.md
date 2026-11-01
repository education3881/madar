# A check's capture has a ceiling, and a ceiling reads as a clean pass

**Ruling #124** · filed **2026-11-01** at the weekly consolidation · **BINDING**
**Family:** assertion discipline (**forty-fifth member**) · earned by the consolidation itself, not carried into it.

---

## What was found

The assertion-discipline family's bullet in §2 of `agents/guidebook/INDEX.md` ends in a ratio:

> *…by a wide margin the largest and fastest-growing family in the register — **forty-two of one hundred
> twenty-one rulings** …*

On arrival at this review it was **stale by two on both sides**. The true figure was forty-four of one
hundred twenty-three. That is the ordinary fifth-home drift the 2026-10-04 second amendment exists to
catch, and on its own it is a note.

What makes it a ruling is **why nothing caught it.** `qa_register_shape` has asserted that denominator
since **ruling #90** (2026-10-07), on the correct ground that the denominator of *N of M rulings* is the
register's own size and is exactly derivable. Ruling **#106** (2026-10-18) then found the same limb reading
**zero live claims** because the prose had stopped using the form it matched, and fixed it, and added a
silent-pass guard so the fifth home could never again be entirely unread.

**The limb has read zero denominators since 2026-10-15, eighteen days, through two weekly consolidations.**
Measured against the real history of the file rather than asserted:

| INDEX.md as of | denominator the limb read |
|---|---|
| 2026-10-07 | `twenty-eight of ninety rulings` → **90** |
| 2026-10-13 | `thirty-three of ninety-nine rulings` → **99** |
| 2026-10-14 | `thirty-three of one hundred rulings` → **100** |
| 2026-10-18 | *(none)* |
| 2026-10-21 | *(none)* |
| 2026-10-25 | *(none)* |
| 2026-10-30 | *(none)* |
| 2026-11-01 | *(none)* |

The cause is neither scope, nor home, nor control, nor unit — the four things this family's forty-four
prior members are about. **It is the WIDTH of the capture.** The pattern was

```
([A-Za-z][A-Za-z\-]*(?:[ \-][A-Za-z]+)?)\s+of\s+([A-Za-z][A-Za-z\-]*(?:[ \-][A-Za-z]+)?)\s+rulings
```

— at most **two** number-words on each side, which covers every value from *one* to *ninety-nine* and
`one hundred` exactly. The register passed **`one hundred one`** on 2026-10-15 with #101, and three
number-words will not fit a two-word group. `words_to_int` has parsed `hundred` since 2026-10-17, so **the
ceiling was never in the arithmetic; it was in the capture**, one function call upstream of the only place
anybody had thought to look.

**And #106's own guard declined to fire**, for a reason that was right when it was written:

> *The fifth home is not allowed to be entirely unread: zero of BOTH forms is a finding, while zero of one
> form and some of the other is normal and is printed rather than asserted.*

The membership-list form was present and correct, so the guard saw one form of two and held its peace. That
judgment treats the two forms as two independent addresses of one number, which is what they are **only
while both are readable**. From 10-15 one of them was structurally unreadable, and `0 ratio denominator(s)
read` was printed on every run — by the 10-18 and 10-25 reviews among them — and read as the normal half
of a healthy pair.

## The rule

0. **Counting tokens IS the ceiling.** A capture that enumerates how many words a quantity may have has a largest quantity, whatever the enumeration's size; widening it from two to four moves the wall without removing it. Where a check parses a hand-written quantity, the capture delimits and the parser judges.
1. **A check's capture has a ceiling, and the ceiling is reached by the subject growing, not by the subject
   changing.** #106's defect was *the prose stopped using the form I match*; this one is *the prose kept
   using the form I match and the number outgrew it.* The second is harder to see, because every
   surrounding word is still the word the pattern was written for.
2. **A DECLINED match is a finding whenever the declined text carries a number word.** A pattern that
   cannot parse a quantity in quantity position has found its own limit and must say so. Silence is
   reserved for text that is not a quantity at all — the literal `N of M rulings` placeholder in the
   preamble, which carries no number word and is correctly ignored.
3. **A limb that reads a count must state the count it read, and a run that reads `0` must ask when it last
   read more than `0`.** The number was printed faithfully on every run for eighteen days. Printing is not
   asserting (#90), and *a check that finds nothing to check has failed, not passed* (2026-08-16) applies
   to a limb as well as to a whole instrument.
4. **Where a check parses a hand-written quantity, its range is stated at the point of the parse, in units
   of the subject's own growth.** Four tokens reaches 999 — twenty-two months of filing at this rate — and
   that sentence is now in the code beside the pattern, so the next ceiling is a date rather than a
   surprise.

## Proof, both ways (#35), bite first

The bite is **the real published defect, not an injected one** (#115's lesson, and #123's: an injection
wider than its target manufactures the defect it was aimed at, so the safest bite is the one already on
disk).

| # | State | Expected | Result |
|---|---|---|---|
| 1 | **BITE** — widened capture, prose as found (`forty-two of one hundred twenty-one`) | FAIL, naming the real drift | **FAIL** — `the denominator is a count of the whole register and the register holds 123`; `1 ratio denominator(s) read` |
| 2 | **CONTROL** — prose repaired to `forty-five of one hundred twenty-four`, all five homes moved | CLEAN | **CLEAN**, `1 ratio denominator(s) read` |
| 3 | **BITE** — control tree, denominator `one hundred twenty-three` (off by one) | FAIL | **FAIL** — off by one caught at three number-words, which the old capture could not locate at all |
| 4 | **BITE** — control tree, `one hundred twenty-four-ish` | FAIL on the new decline limb | **DID NOT BITE on the first fix: exit 0, `0 ratio denominator(s) read`, indistinguishable from a passing control.** See below. Red after the second fix, naming the phrase it cannot parse |
| 5 | **BITE** — control tree, `one hundred twenty-four thousand` | FAIL on the decline limb | **FAIL** |
| 6 | **CONTROL** — the preamble's literal `N of M rulings` | silent, as designed | silent throughout; the control reads `1`, not `2` |
| 7 | **CONTROL** — old two-word capture, control tree | CLEAN but **for the wrong reason** | CLEAN with `0 ratio denominator(s) read` — the eighteen-day state, reproduced on demand |

**Bite 4 is the expensive half, and it is this ruling's own subject reproduced by this ruling's own fix.**
The first repair widened the capture from two tokens to four. `one hundred twenty-four-ish` splits to
**five** tokens, so the pattern matched nothing at all — and a ratio the pattern cannot *locate* can never
reach the decline limb written to report it. **Counting tokens was the ceiling; the number chosen was
never the point.** The capture is now a lazy run of letters, spaces and hyphens between `of` and
`rulings`, length-bounded only against a runaway, with `words_to_int` as the single judge of whether that
run is a number. *A fix that moves a ceiling has not removed one* — and it exits 0 while it does so, which
is the 2026-09-14 trap (*a bite that fails to change the artefact reads exactly like a passing control*)
arriving through a bite that did change the artefact and still could not be seen.

Row 6 is the one that matters: it is the condition two weekly reviews shipped, and it is indistinguishable
from row 2 in exit code. The only thing that ever separated them was the line that prints how many claims
the limb read — which exists because #106 put it there, and which nobody compared against its own history.

## What it joins, and what it predicts

Assertion discipline, as the **forty-fifth** member, and the first whose defect is the *width* of a
pattern. Its nearest relatives are **#90** (assert the derivable half — the limb this ruling repairs is
#90's own), **#106** (an exemption outlives the reason written beside it — same limb, one cause earlier),
and **#103** (a rule that cannot match is indistinguishable from a rule that matches and does nothing —
the same shape in CSS rather than in Python).

**Forward:** every hand-written quantity this operation parses anywhere has a capture with a ceiling, and
`words_to_int`'s callers are not the only ones. The named next surface is **every regex in
`agents/tools/**` that captures a number in order to compare it** — how many have a width, and which of
them is nearest to its subject's current size? Raised on the standing queue rather than answered here.
