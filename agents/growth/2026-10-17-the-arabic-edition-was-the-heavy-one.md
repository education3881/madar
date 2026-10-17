# Growth — the Arabic edition was the heavy one, and nobody had measured it

**Taken:** 2026-10-17, by the daily run, from the standing queue's own head (item 10, raised
2026-10-10 by the growth function, 7 days, five displacements). **Lane:** Growth (reader
experience). **Closes item 10.**

---

## The bet, and what it paid

Page weight is the one reader-experience number this operation can read **without anyone
else's permission** — no tracker, no third party, no account. The CHARTER prefers exactly that
kind of bet. The 2026-10-10 note set a baseline and queued the reduction; this is the
reduction, measured over the whole population rather than one page.

**278,872 bytes removed from every Arabic page in the publication. Nothing removed from the
English pages, and nothing changed about the typefaces.**

| | before | after | delta |
|---|---|---|---|
| AR article — median of all 44 | 574,500 | **295,628** | **−278,872 · −48.5%** |
| AR article — heaviest of 44 | 825,868 | 546,996 | −278,872 · −33.8% |
| AR article — lightest of 44 | 574,500 | 295,628 | −278,872 |
| AR home | 705,600 | 426,728 | −278,872 · −39.5% |
| AR editions | 613,760 | 334,888 | −278,872 · −45.4% |
| AR browse | 521,136 | 261,808 | −259,328 · −49.8% |
| **EN article — min / median / max of all 44** | 487,672 / 521,408 / 703,556 | **identical** | **0 in every statistic** |
| EN home | 778,376 | 778,376 | 0 |

88 article pages probed before and after, **zero failures** both times.

## What the 10-10 item asked for, and why neither branch was taken

Item 10 named two reductions, and both were out of this lane's reach: **subset the faces to our
own corpus's glyph inventory** (needs a dependency and makes the bundle ours rather than a
mirror) and **drop a family** (a Designer judgment about the publication's face). Neither was
needed. The largest reduction available was not in the fonts at all — it was a stylesheet
rule that had never applied, and the whole saving came from **not downloading a face no
Arabic page renders a word in.** Full diagnosis in ruling #103.

Four families still load on an English article and 521,408 bytes is still heavy. **That half
of item 10 is real and is handed on, not closed** — see the new queue item.

## Three corrections to the 10-10 note, because a figure is cited as read

The baseline this item was specified by was wrong in three ways. All three are the same class:
**a figure summed or sampled over one population and labelled with another.**

**1. `2,792,392 bytes` for the bundle on disk is a sum over the wrong population.** It is the
total over the stylesheet's **73 `@font-face` declarations**, counting each file once per
declaration. The bundle on disk is **1,333,968 bytes over 34 files** — and the row printed
`34` beside `2,792,392`, two cells of one row derived from two different populations. The
generator's own code deduplicates by URL and says why in a comment three feet away: *"a
variable font is served once and declared at several weights."* The tool knew. The
measurement did not.

**2. Therefore "the mirror decision was worth roughly 2.29 MB per first-time English reader"
overstates by about 2.75×.** Against the honest proxy for a naive five-rule implementation —
the sum of the distinct files, 1,333,968 — the mirror saves **832,104 bytes**, not 2,290,528.
The 10-08 design decision was right and is still right by a wide margin; it is worth 0.83 MB,
not 2.29 MB.

**3. "EN article · 7 woff2 · 501,864 bytes" is one page reported as a property of 118.** No
English article measures 501,864 today. The population runs **487,672 to 703,556 with a median
of 521,408** — a spread of **215,884 bytes, 43% of the figure itself.** And the sampled page
was English, so the row labelled *"the article page is the one that matters"* measured the
lighter of the two editions: **the Arabic article was the heaviest page in the publication the
whole time, at 825,868 bytes**, and nothing had ever measured it.

*The 10-10 note has been annotated in place rather than rewritten (#41) — the correction
travels with the measurement it corrects.*

## Method

Identical to 10-10's — built pages served over loopback to headless Chrome, observed network
fetches — with one addition forced by the subject. **The injected probe is Latin text in an
element inheriting the body's Latin font stack, so for a font measurement the instrument can
pull the face it is counting.** It was therefore run both ways: the injected probe, and the
loopback server's own access log with **nothing injected at all**. Identical on all four
control pages, file for file. The 10-10 method is cleared.

One reading was discarded: a single run read the English home at 646,408 over 9 files against
778,376 over 12 everywhere else, having dropped exactly the three `latin-ext` subsets. On a
control page that could not have changed, under a fix whose claim was *bytes went down*, **it
had the precise shape of a success.** Three repeats returned the real figure. That is why the
English population is in the table at all.

## Growth reading, per the CHARTER

**Return rate: not measurable, by design, and not estimated.** The site carries no third-party
tracker and none was added here; every figure above was taken from our own files and our own
browser. There is no visitor number in this note and there will not be one.

What this *does* buy, honestly stated: the Arabic edition went from **heavier than the English**
(574,500 against 521,408 at the median) to **43% lighter** (295,628). Arabic is this
publication's distribution advantage rather than its translation cost — the CHARTER says so —
and until today the Arabic reader was paying the most for it, most likely on the slower
connection of the two. Core Web Vitals is a ranking input we cannot observe and can affect;
this is the kind of improvement that compounds quietly or not at all, and we will not pretend
to read it.

**Distribution is still blocked and is still not this lane's to unblock:** GitHub issue #11
(*Founder decision — the distribution channel*), opened 2026-10-15, default **park the packets
if nobody replies by 22 October**. Five days to run. Unanswered as of today.
