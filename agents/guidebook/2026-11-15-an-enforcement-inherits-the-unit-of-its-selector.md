# Ruling #143 — An enforcement inherits the unit of its selector, and the checker inherits it too

**Filed 2026-11-15, from the quality function**, closing standing-queue item 39 at 21 days out of a
three-way tie. Family: **assertion discipline** (fifty-sixth member). Distinguished from #93, #113,
#116, #117, #140 and #142 at the foot.

---

## THE RULING

**A rule about a property is exact only where the unit it SELECTS ON is the unit the property LIVES
IN. Where the selector is coarser, the rule is exact by coincidence — it holds exactly as long as the
coarse unit happens to be homogeneous in the property — and the moment it is not, the rule is
over-broad in a direction nobody chose. And the defect is invisible, because the instrument built to
police the rule is almost always built on the RULE'S unit rather than on the fact's, so it partitions
the world the same wrong way and cannot report the case that is both.**

Operationally, three questions, and they cost one command each:

1. **What is the unit of the fact?** (a script, a claim, a page, an element, a character)
2. **What is the unit of the selector that enforces it?**
3. **If (2) is coarser than (1), what is the population of members of the coarse unit that are NOT
   homogeneous in the property?** Count it. That count is the rule's error, and it is never zero for
   long.

---

## THE INSTANCE THAT EARNED IT

**Ruling #115 (2026-10-25) is right and its enforcement is over-broad.** The fact is *Arabic
typography has no italic convention* — a fact about a **script**. The enforcement is

```css
[dir="rtl"] em, [dir="rtl"] i, [dir="rtl"] cite { font-style: normal }
```

— a selector about a **page**. The two coincide exactly as long as every emphasised run on an Arabic
page is Arabic. Measured over the served corpus on 2026-11-15, inside `.body-main`: **24 Arabic pages
carry `<em>`, 195 elements in all, 139 of them Arabic-bearing — and 56, across 10 pages, contain no
Arabic code point at all.**

They are `Nature`, `Britannica`, `Cambridge`, `Elsevier`, `Scopus AI`, `ScienceDirect AI`, `Reaxys
Predictive Retrosynthesis`, `Common Sense Networks`, `Poynter`, `Kurikulum 2013`, `Kurikulum Merdeka`,
`pembelajaran mendalam`, `Bukanlah tentang Kurikulum Baru.`, `Lan fɔ lan` — **journal titles,
institutions, programme names and foreign-language quotations, where Latin italic is not decoration
but disambiguation.** All 56 have rendered upright and indistinguishable from the surrounding Arabic
for **21 days**, on pages a reader is served.

**Nothing could see it, and nothing was wrong.** `qa_font_payload` limb 1 asks whether a run
*containing an Arabic code point* resolves to a slanted style; these contain none, so the limb is
silent — **correctly**. The limb partitions runs the way the rule partitions them, and the case that
breaks the rule is the case neither partition has a name for.

## AND THE REPAIR IS WHERE THE RULING GETS ITS TEETH

**No CSS-only repair exists, and that is not a shortage of cleverness.** Every candidate sets the
element's computed `font-style` to `italic`, and an `<em>` holding Arabic is the *same element* as an
`<em>` holding Latin — so every candidate reds limb 1 on 139 Arabic runs, and limb 1 is **right** to
red, because the computed style is the only thing CSS can be asked about. **CSS selects elements and a
script lives inside an element's text**, so the finest unit CSS can reach is one step coarser than the
fact. The repair therefore cannot be in the stylesheet at all: the markup must carry the distinction —
the composer marks a foreign-language run with `lang`, which the accessibility family has wanted since
2026-09-13, and the stylesheet keys `:lang()` off it.

*An enforcement whose finest available unit is coarser than its fact does not need a better selector.
It needs the artefact to carry a boundary it currently does not.* That is **#113's and #140's
criterion arriving from the opposite side**: those two say an exact check needs a boundary the artefact
supplies, and this one says what to do when it supplies none — **make it supply one**, rather than
approximating with the next unit up.

---

## THREE MORE INSTANCES, TWO OF THEM FROM THE SAME DAY AND A DIFFERENT FUNCTION

**(a) Item 39's own question, in the other direction.** The row asked *drop a family* — a **corpus**
verb — about transfer cost, which is a **(page, family)** quantity. Neither family is droppable:
Newsreader Italic paints 982 characters on the English home page and Cormorant Garamond 1,507 on the
Editions page, while the same two files paint 196 and 1 character respectively on an article. The
question was unanswerable *as asked* for 21 days, and the moment the unit was corrected the answer was
a column the build had been printing all along — **bytes per painted character**.

**(b) The Editor's Test 1, the same morning.** The England draft's `sources[]` block carries eight
entries and **one of them has no URL**. It is the only register in the piece cited for a property of
the **page** — a standfirst that supplies a gender determination — rather than for a **claim in the
body**. The drafter's discipline (*write the address beside the claim*) is organised on the unit
*claim*, and a member whose unit is *page property* falls outside it. The hand-off lines the standing
ledger enumerates are all claim-shaped for the same reason.

**(c) #117, in retrospect.** Standing-queue item 25 asked for *every served date that has not yet
arrived* — a **date** unit for a property that lives in a **verb attached to a date**. The ruling
rescoped it and the population inverted. This ruling is the general statement of that move; #117 is
its first unrecognised instance.

**Three instances in one day across two functions is a rate, not an anecdote**, and all three were
found the same way: by re-measuring a row's own named instance before taking it (#142).

---

## WHAT THIS ADDS TO THE FAMILY, AND WHAT IT DOES NOT

- **It is not #93.** #93 is about a *threshold* — a floor above today's reality reds every build. This
  is about a *unit*, and a unit error is not relieved by moving a number.
- **It is not #113 or #140.** Those say an exact check needs a boundary the artefact supplies, and
  #140 licenses an instrument that returns *no* answer. This names what happens when a rule proceeds
  with the **next unit up** instead: it returns a confident answer that is right on the homogeneous
  majority and wrong, silently, on the mixed remainder.
- **It is not #142.** #142's detector returns a confident *wrong* answer because a different rule put
  its key there on purpose. Here nothing is in the way; the rule simply cannot address the thing it
  means.
- **It is #116 generalised off an ordering.** #116 said *an ordering rule can express only the
  distinctions its keys can hold*. This says **any** rule can enforce only at the granularity its
  selector can hold — and adds the half #116 did not need: **the checker inherits the same
  granularity, so the rule and its police are blind together.**
- **It is #57 and #70 pointed at a SELECTOR.** Those say a count cannot report a member it cannot
  enumerate and a bucket set cannot report a distinction it cannot hold. A selector is an enumeration
  too, and it cannot exempt a thing it cannot name.

**The one-line form, for the register:** *a rule is exact only where its selector's unit is the fact's
unit, and where it is coarser the error is the count of mixed members — which the rule's own checker
cannot see, because it was built on the rule's unit.*

---

**Raised as standing-queue item 107** (the 56 runs, the board's only DEFECT) and **item 109** (the
forward question: how many served elements in this corpus are mixed in *any* per-script property, and
in how many is the property being decided for the whole by a rule true of a part). The instance is
repaired through the Arabic Editor's gate across ten published pieces; it is not a stylesheet line and
was not improvised at the end of a run.
