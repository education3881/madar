# Inlining dissolves the scope a file was composed in

**Ruling #99** · filed 2026-10-13 (daily run, the Edition 05 flip) · **enumeration family**

---

## The ruling

**An artefact composed as a self-contained file carries a private namespace only while it stays a
file. The moment a build *inlines* it into a page, every name inside it — a class, an id, a CSS
custom property, a gradient or filter name — joins one shared namespace with everything else inlined
beside it, and the last declaration wins.** So a page assembled from artefacts that are each correct
can be wrong, and the defect exists in **no file** — which means no check that reads files can find
it.

## What happened

Edition 05's flip added a fifth cover to `/editions/`. The page was rendered and looked at before the
commit (the 2026-08-23 rule), and the new cover printed its kicker in **Edition 01's vermilion**
rather than its own green.

Measured rather than eyeballed — computed `fill`, read out of a real browser through an iframe, on the
built page:

| Cover | Registry accent | Computed `fill` BEFORE | AFTER |
|---|---|---|---|
| Edition 05 | `#2D6A4F` | `rgb(217, 79, 42)` | `rgb(45, 106, 79)` |
| Edition 04 | `#9C5B3A` | `rgb(217, 79, 42)` | `rgb(156, 91, 58)` |
| Edition 03 | `#2E4C63` | `rgb(217, 79, 42)` | `rgb(46, 76, 99)` |
| Edition 02 | `#2F6F6A` | `rgb(217, 79, 42)` | `rgb(47, 111, 106)` |
| Edition 01 | `#D94F2A` | `rgb(217, 79, 42)` | `rgb(217, 79, 42)` |

`inlineCover()` injects each cover's markup — *including its own `<style>` block* — into the page.
All five covers use the same five class names (`.wm`, `.ar`, `.kick`, `.th`, `.thm`). Five `<style>`
blocks in one document are one cascade; render order is current-first then descending, so the last
block in document order has always been Edition 01's. **Every edition's cover type except Edition 01's
has rendered in Edition 01's accent since the second cover was inlined.**

Fixed in the same commit: each cover's root carries `class="ed-cover ed-cover-NN"` and each of its
five rules is scoped under it. The file stays self-contained and renders identically when fetched
standalone.

## Why it survived four editions of looking at that page

**Because the figures were right.** The line work in every cover is drawn with `stroke="…"`
*presentation attributes on the elements themselves*, which no stylesheet in the page overrides. Only
the **type** leaked. So each cover looked individually plausible — right ground, right drawing, right
proportion, a kicker in *an* accent — and the thing that was wrong was a relationship between five
artefacts that nobody holds in view at once.

## Why no instrument could see it

All 29 gating assertions read **files**: `dist`, or the repository root. Four of them render
(`qa_render`, `qa_arabic_shaping`, `qa_arabic_joining`, `qa_feed_direction`) and all four ask about
**type and direction** — is it blank, is it legible, does Arabic shape, does a field carry its own
direction. None asks whether an element kept the identity its own file declared.

And the defect is not in any file. Each of the five SVGs is correct. `edition-05.svg` served
standalone prints green. The wrong artefact is the **composition**, which exists only after the build
assembles it and only in a browser that resolves the cascade.

## The general form, and the family

A member of the **enumeration family** — *a green check is scoped to what it enumerates* — and the
first one where the thing to enumerate **is not a file at all**. *(The family keeps no running member
count, so none is written here: a number nobody maintains is the defect #57 exists to stop.)* The family's earlier members widened
the scope from content to chrome (08-16), from links out to pages in (08-17), from "resolves" to
"usable by the consumer" (08-18), from the publication to the founder-facing artefacts (08-23), from
the served set to the held one (09-06). Each of those found a *file* nobody was reading. This one
finds a **property that belongs to no file**, and the generalisation is:

> **Ask of every claim: is this a property of a file, or of an assembly?** A claim about an assembly
> can only be checked after the assembly exists — in a render, or in a build-time pass that reads the
> page rather than its parts. Checking each part harder will never reach it.

## What it binds

1. **An artefact that will be inlined is composed as if its names were public**, because after
   inlining they are. Scope every rule under a root class unique to the file; never rely on a `<style>`
   block being private.
2. **A build-time inline is a merge, and a merge of named things is checked for collisions** — classes,
   ids, custom properties, `<defs>` names. Checked today across the rest of the surface and recorded so
   it is not re-checked blind: **no still carries a `<style>` block (0 of 45), the wordmark carries
   none, and no built page duplicates an `id`** (EN home 4, editions 5, zero collisions).
3. **A render is a measurement, and the measurement is a computed value, not a screenshot.** The
   screenshot showed an orange kicker; what proved it was reading `getComputedStyle().fill` on all five
   covers and finding one value where there should have been five.

**Standing-queue item 13** is the gate this ruling does not itself provide: for each cover on the
editions page, the computed kicker `fill` equals its registry accent. The repair is shipped; nothing
yet stops the sixth cover reintroducing it.

**Related:** [[2026-10-12-a-blast-radius-is-traced-where-the-instruments-are]] — that ruling says a
correction's radius stops where the instruments are; this one says some radii have no file to point an
instrument at.
