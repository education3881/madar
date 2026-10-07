# The corpus's claims about WHERE — a complete census of 772 annotations, and the Arabic edition makes more of them

**2026-10-07 · Growth · the audit this run could read without anyone's permission**

Today's confirmation read on Edition 05 row 4 found an annotation that was **right about what and wrong
about where**: it placed Alexis Le Nestour's two PASEC advisory years *"on the served page"*, and the
served page — the CGD blog — carries a byline and no biography. The fact is true and lives on the
author's own expert profile. The body leans on it in both languages, and it is **the piece's entire
warrant for using a secondary's ruler at all.**

A reader who goes to check the warrant goes to the URL the annotation gives, and the warrant is not
there. **That is a discoverability and trust defect, not a bookkeeping one** — the publication's whole
claim about itself is *named primary sources read in served text*, and an annotation that mis-places a
source is the one failure mode that punishes exactly the reader who checks.

So the question for growth was not *is this one fixed* but **how many more of these do we own?**

---

## The census

Every annotation in the corpus, both editions, held pieces included — read out of `sources[]` rather
than out of `dist`, because a held piece's annotation is what the flip commit will serve.

| | EN | AR | total |
|---|---|---|---|
| Files | 44 | 44 | **88** |
| Annotations | 386 | 386 | **772** |
| Annotations carrying a *mode* claim — "read in served text" / "as served" / "كنصٍّ مُتاح" | 44 | 42 | **86** |
| *Position* phrase matches | 8 | 15 | **23** |
| …of which false positives on the phrasing | 3 | 7 | **10** |
| **Genuine claims about WHERE on a page** | **5** | **8** | **13** |

*The mode row counts **annotations carrying at least one** such claim, not phrase occurrences. The first
pass counted occurrences and double-counted every *"read in served text"* as also *"in served text"*,
reporting 75 for the English side against a true 44 — **a substring counted as two findings**, caught by
recomputing before it was published rather than after. Which is this operation's own #34 (*a total must
be added*) committed against itself in the act of auditing.*

**The false positives are instructive and were not discarded silently.** Seven of the Arabic fifteen
matched `فوق` — *above* — used numerically (*"47.9% at or above the proficiency threshold"*, *"410 and
just above the global median"*), and three of the English eight matched *"above the"* and *"beside the"*
the same way, plus one that was a piece's own **title** (*The finish line above the starting line*).
A positional word used numerically is 2026-09-14's input-side trap in its purest form: **the right
string for the wrong reason.** A census that reported 23 would have been wrong by ten.

---

## The finding: the Arabic edition makes MORE claims about where than the English one

**Eight against five, on the identical corpus, by the identical sourcing.** That is ruling #86's bound
landing in a second place — *the Arabic is composed and not translated, so it is a second channel on our
own annotations, and nothing we own compares them* — and #86 was filed on a count of named humans. It
turns out to hold for a second claim class nobody was looking at.

**One of the eight is single-channel: a claim only the Arabic edition makes, about a third party's user
interface.** The Sudan pair's UNICEF press release carries, in Arabic only:

> *لا طبعةَ عربيةً له على المنصّة: زرُّ «العربية» على الصفحة يعود إلى النصِّ الإنجليزي نفسِه، فالمُسمَّى
> العربيُّ للبرنامج أدناه تفسيرُنا لا تسميةُ المالك*
>
> (*no Arabic edition of it on the platform: the «العربية» button on the page returns to the same English
> text, so the Arabic name for the programme below is our interpretation and not the owner's naming*)

**Checked today, because #86 says the single-channel claims go first.** The page serves 200 at 180,492 B;
its «العربية» link resolves to **the identical English path**, with no `/ar/` segment; and the only
`hreflang` the page declares is `en`. **The claim is exactly right**, and so is the conclusion it
carries — the Arabic programme name is disclosed as ours. *An edition that invents a claim its peer
cannot check also invented the disclosure that makes it safe.*

**The other ruler-piece position claim was also checked and also holds.** The HSRC press release names
its Principal Investigator verbatim as *"Dr Vijay Reddy, Principal Investigator of TIMSS 2019 and
Distinguished Research Specialist at the Human Sciences Research Council"*, which is what both editions
say it says. So on the piece that produced today's defect, **one position claim was wrong and two were
right** — and the wrong one was the only one about a *person's biography* rather than about a page's
furniture.

---

## What this is worth to growth, stated without a traffic number

The site carries **no third-party tracker by design**, so there is no visitor figure here and none is
estimated. What is measurable without anyone's permission is **the proportion of our own promises that
survive being checked**, and that is the number this publication actually competes on:

- **13 position claims across 772 annotations** — 1.7%. Small, and every one of them is a claim a
  checking reader can falsify in one click.
- **Four checked today: three right, one wrong and repaired in both editions.**
- **Nine remain unchecked** — three on Sierra Leone and Rwanda whose own confirmation reads covered the
  surrounding prose, and six on published pieces.

**The cheap instrument is named rather than promised**, because this operation has learned what a
promise costs: a position claim is not mechanically checkable the way a URL is — *"on the same page"*
needs a human to look. But the **census** is mechanical, it took one pass, and it is the thing that was
missing. **A phrase list plus a count turns an unbounded worry into a nine-item list.**

---

## Carried to the queue, and the limit named

**Added to the standing queue as part of item 5's territory, not as a new item:** the six unchecked
position claims on **published** pieces sit beside the five dead citations already queued there, because
both are served bytes on published pieces and both are the Web Developer's with an editorial
disposition. **Rushing nine annotation re-reads into the tail of a run four days before a wave flip is
how a correction becomes the next defect** — the same reasoning the 10-05 run gave for not fixing the
dead citations the day it found them, and it was right then.

**The limit, named because the first pass had it and would have reported a clean half-corpus:** the
phrase list was **English-only on its first run**, and it was extended to Arabic idiom only because the
operation has a ruling about exactly this. An English phrase list over a corpus whose Arabic is
*composed* would have found 5 claims and reported the census complete, missing the 8 that matter more —
**and missing the one claim that has no second channel at all.** A census is scoped to its vocabulary,
which is *a green check is scoped to what it enumerates* with the enumeration hidden inside a word list.
