# Ruling #130 — Coverage and rate are different properties of one measurement, and a reach gap is not evidence of a hidden defect population

**Filed 2026-11-06 at the point of filing, from the standing queue's own head: item 34 at 15 days,
the oldest row in OPEN.** Family: **enumeration** — which keeps **no** running member count, so per
the 2026-10-04 second amendment's limb one there is no conditional fifth home and the member is
appended to the family's enumeration instead.

## The rule

**A measurement over a population has two independent properties, and a finding about one is not a
finding about the other.** Its **reach** is the fraction of the population it can evaluate at all.
Its **rate** is what it found inside that fraction. A gap in reach tells you the measurement is
narrower than its denominator suggests; **it tells you nothing whatever about what is inside the
gap.** Arguing from a reach gap to a concealed defect population is arguing from ignorance, and it
feels like rigour because the first half of it is true.

So: **when a measurement declines part of its population, measure the rate PER CLASS before
concluding anything about the declined class — and if the declined class cannot be measured at all,
say that instead of predicting it.**

## What earned it

Standing-queue item 34 was raised on 2026-10-22 as the daily's forward question, by the run that had
just shipped `qa_citation_identity` (#112), and it is one of the sharpest questions this board has
carried:

> `qa_citation_identity` could compare only **90 of 218** quotation-bearing registers; the 80 it
> declined are 34 walled, 13 PDFs, 20 script-mismatched, 6 dead. **Every state document in this
> corpus is a PDF** — every yearbook, every decree, every performance report — and a PDF is the class
> this instrument reports as *unreadable* rather than *checked*. So 34.4% is a rate over the
> registers that happen to be open HTML, which is **systematically the journalism and systematically
> not the primary sources this publication's whole method rests on.** Nothing we own has ever asked
> whether a green measurement is green because the defects live in the documents the instrument
> cannot open.

The question was right to be asked, the measurement was built, and **the hypothesis is false in both
directions.** Measured over all 354 rows of `claim-registers.json` and all 232 of
`citation-identity.json`, offline and re-runnable (`agents/tools/register_coverage.py`):

**The archival half, where the row predicted the primary sources would be worst:**

| by format | rows | archived | rate |
|---|---|---|---|
| **PDF** | 19 | 18 | **94.7%** |
| HTML | 171 | 141 | 82.5% |
| ALL | 354 | 294 | 83.1% |

| by publisher | rows | archived | rate |
|---|---|---|---|
| **OFFICIAL** | 155 | 133 | **85.8%** |
| OTHER | 199 | 161 | 80.9% |

PDFs are the **best**-archived class in the corpus and official hosts are archived **better** than
everything else. Both are the opposite of the prediction.

**The identity half, where the row was right about the wall and wrong about what is behind it:**

| by format | regs | comparable | coverage |
|---|---|---|---|
| HTML | 171 | 141 | **82.5%** |
| **PDF** | 19 | **0** | **0.0%** |

| by publisher | regs | comparable | coverage | failing | **fail-rate** |
|---|---|---|---|---|---|
| OFFICIAL | 94 | 55 | 58.5% | 16 | **29.1%** |
| OTHER | 138 | 86 | 62.3% | 27 | **31.4%** |

The **reach** is worse than the row thought — **not one PDF of nineteen is comparable**, against the
row's own *13 PDFs declined*, and HTML is the only format the instrument reaches at all. The **rate**
is flat: 29.1% against 31.4% is the same number, and **39% of the comparable population is on an
official host**, so the comparable set is not a journalism remainder and the 30.5% is not a rate over
journalism.

## Why the inference felt sound, which is the part worth carrying

The row's argument has the shape of every good enumeration finding this operation owns. Six rulings
in that family say *a green check is scoped to what it enumerates*, and every one of them was earned
by a defect that really was living outside the enumeration: the held-leak sweep could not see a date,
the chrome sweep had never enumerated the layout, the og:image resolved and rendered nowhere. **After
six of those, "the instrument cannot see class X" starts to read as "class X is where the problem
is."**

It is not the same claim. The six findings are all cases where somebody *went and looked* outside the
enumeration and found something. The inference runs the other way and cannot be made: **an
unenumerated class is unknown, and unknown is not a synonym for bad.** The enumeration family's
question is *what can this check not see?* — and the honest answer is always *go and look*, never
*assume*.

**And the correct instinct, had anybody applied it, points at the opposite conclusion.** A PDF is a
document somebody published deliberately, with a filename, on a host they maintain. There is no prior
reason it should be worse archived than a news article, and 94.7% says it is considerably better.
What the row was actually reasoning from was our own *difficulty* with PDFs, and difficulty for us is
a property of our client.

## What it does not say

It does not say the reach gap is harmless. A gate that cannot evaluate 19 of 19 PDFs is a gate whose
subject excludes every state document in the corpus, and **that is a real limitation to write down,
which is what item 82 now does.** The ruling is only that the limitation must be *measured* rather
than *populated by inference* — and when it cannot be measured, the honest output is the statement of
what is unverifiable, not a prediction dressed as a finding.

## The general form

*A measurement has a reach and a rate. A reach gap bounds what you know; it does not describe what
you do not know.* Before attributing a defect population to the part of a population an instrument
cannot evaluate, either measure that part with something else — **#131, filed the same morning, says
what the something else usually is** — or write down that it is unmeasured and stop there.

— Assertions Engineer · 2026-11-06 · *the row asked the right question for the right reason and
guessed the answer, and the guess was the only part that was wrong.*
