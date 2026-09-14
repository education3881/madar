# A correction has a blast radius — ruling #50

**Filed:** 2026-09-14 (second run of the day, the first run executed in the cloud)
**Earned by:** Growth, composing the Ed05 wave packet's fourth caption and re-reading the three already in it.
**Family:** the enumeration family (*a green check is scoped to what it enumerates*) — seventh member, and the second to sit outside `dist`. Also a corollary of the non-numeric family named at the 09-13 review.

---

## The rule

**When a verdict changes a piece, it changes every artefact composed from that piece. The correction is not finished when the article is fixed; it is finished when every derived artefact has been re-read against the corrected text.**

A piece is not a leaf. By the time it ships it has descendants: a social caption, a newsletter blurb, an engagement-list note, a brief that summarised it, an edition memo that ledgered it, a review that quoted it. Each was composed **from the piece as it stood on the day**, and each then sits still while the piece keeps moving. The article has a Verifier; the descendants have nobody.

## The case

The Ed05 wave packet (`social-drafts/2026-08-31-ed05-wave-packet.md`) gained its Sudan captions on **2026-09-03**, composed from the piece as drafted. Both languages said the 2014 programme was *"games that teach Arabic and maths"* / *«ألعاب تعلّم العربية والرياضيات»*.

On **2026-09-10** the Verifier's third Edition 05 verdict opened with exactly that claim, as item 1, in the piece's **opening sentence**, in both languages: the owner's register says the 2014 first phase *"start[ed] in 2014 focusing on a numeracy trial… an applied mathematics game"*. Arabic literacy is real and measured — on the *later* programme the evaluation covered. Nothing false about the evaluation; something untrue about 2014. The article was corrected in-run, in both languages, the same day. It now reads *"a set of educational games"*.

**The packet was not corrected, because nothing connects the two.** Four days and four runs later, the caption still carried the sentence the verdict had removed — staged, held, and scheduled to be the first thing about the piece that anyone outside this repository would ever read.

Nothing was published: the packet is held with the wave and the wave has not flipped, so no reader saw it. That is luck arising from an unrelated hold, not a control. Had the wave flipped on schedule, the correction's whole point — that we do not say what the register does not say — would have been undone in the one artefact designed to travel further than the piece.

## Why every existing check was blind to it

- **The Verifier** traces the piece against its sources. The packet is not the piece and has no `sources[]`.
- **The twelve — now thirteen — standing assertions** enumerate `web/dist`. `social-drafts/` is not built, not served, and not in `dist`.
- **The 08-23 rule** (*the QA perimeter includes the artefacts the operation renders for humans*) reached the brief and the review because those are **HTML we render**. A markdown packet is neither published nor rendered; it fell between the two perimeters.
- **The packet's own header** promised the right thing and enforced it in the wrong direction: *"no figure appears here that is not in the shipped piece."* **The defect was not a figure.** It was a noun — the subjects a programme taught — which is ruling #47 exactly, met a second time, one artefact downstream. A promise about figures cannot see a claim.

## The shape, stated generally

The other six enumeration findings asked *what can this check not see?* This one asks a different question: **what does this correction not reach?** A defect class is normally found by widening a sweep. This one is found by following an edit forwards.

**Corollary 1 — the derived artefact is stale by default.** It was true on the day it was written. Every subsequent edit to its parent is a silent divergence, and nothing announces it. Treat any artefact composed from a piece as *provisional until re-read at the moment of use*.

**Corollary 2 — the blast radius is widest for the artefacts that travel furthest.** A caption reaches more people than the paragraph it summarises, and it reaches them without the paragraph attached. Errors propagate in inverse proportion to the number of words carrying them.

**Corollary 3 — re-read at the point of use, don't track at the point of edit.** A dependency ledger listing every descendant of every piece would itself go stale, which is the same defect one level up (2026-06-07: *generated artefacts that must mirror the article set are build-generated, never hand-maintained*). The cheap, durable version is a checklist item at the moment the derived artefact is finally used: **re-read it against the current text of its parent.** Now written into the packet's own flip-day checklist as step 3.

**Corollary 4 — a correction is logged where the piece is, and used where the piece is not.** The verdict files record what changed. Nothing reads them afterwards. When a verdict changes a *claim* rather than a *figure*, say so in the verdict's own summary line in words a later reader can grep — the 09-10 verdict did this well, which is the only reason today's re-read found it in one pass.

## What it costs to obey

One re-read per derived artefact, at the moment it is used rather than at the moment it is written. For this wave: four pieces × two languages of caption, read against eight article files on flip-day. Fifteen minutes, once, against an error that would otherwise be permanent and public.

## Provenance

Ruling #47 (*a description has a date too*), item 1, Sudan verification verdict 2026-09-10 — the parent defect. This is that same defect surviving its own correction, in a different file. Related: #35 (prove both ways — a control that cannot fail is not a control), #41 (supersede, don't resurrect), and the 2026-08-23 RUNBOOK rule on the founder-facing artefact perimeter, which this extends from *rendered* artefacts to *derived* ones.
