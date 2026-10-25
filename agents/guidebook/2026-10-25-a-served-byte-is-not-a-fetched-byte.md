# Ruling #115 — a served byte is not a fetched byte, and nothing we own reads the second kind

**Filed 2026-10-25**, daily run, QA lane, closing **standing-queue item 20** from the head at 8 days
and seven displacements. Family: **assertion discipline — the fortieth member.**

---

## The selection, because this is the first time the ladder needed its last rung twice

Items **20** and **21** arrived at this morning tied on **both** published clocks: 8 days each, seven
displacements each. The 10-05 tiebreak (*oldest past threshold goes first*) did not separate them.
The 10-11 ANSWER 1 narrowing (*finer clock, but only when displacements also tie*) did not either,
because both were raised by **the same commit** — `330b936`, the 10-17 daily, one from the growth
function and one as that day's forward question. So the **10-16 fourth level** decided it, the level
its author called *the last the artefacts can support*: when two items share a raising commit, item
numbers are assigned in raise order, so **item 20 goes first.** Nineteenth selection in twenty daily
runs made by the rule rather than by judgment.

## What the item asked, and the one false sentence in it

Item 20: *Four webfont families and 521,408 bytes on an ENGLISH article.* It names two reductions
and declares both out of reach — **subset to the corpus's glyph inventory** (needs `fonttools` +
`brotli`) and **drop a family** (a Designer judgment). The second is still a Designer judgment and
stays open.

The first is declined on a stated ground that is **false about the thing it names**. The row says
subsetting would break *"a byte-for-byte mirror of the response it replaced, which is the property
`qa_third_party_origins` and the whole 10-08 design rest on."* `qa_third_party_origins` asserts
exactly one thing: that no served page fetches automatically from an origin we do not own. It
contains no hash, no byte comparison, and no claim whatever about Google's response. The mirror is a
design choice recorded in `build_font_bundle.py`'s own header, for a better reason than the one
quoted — not collapsing the `unicode-range` carve — and **no gate holds it.** This is item 26's
question (*which check's stated reason for not asserting something has quietly become false?*)
pointed at a queue item's reason for not *acting*, and it is worth separating from the measurement
because a wrong reason survives longer than a wrong number: nobody re-reads it.

*(The subset stays declined, on the correct ground instead. A subset computed over today's 44 pieces
is right the day it is written and silently wrong the next time an article prints a glyph it does
not contain, and the failure mode is a fallback no reader reports. That is the 2026-06-07 rule
verbatim — generated artefacts that must mirror the article set are build-generated, never
hand-maintained — and it is a stronger objection than the one the item made.)*

## The finding

**A woff2 file in `dist` is not a byte anybody has received.** It is transferred only when the
layout engine must paint a glyph out of it, and whether that happens is a product of four things
that meet nowhere except at render time: the page's text, the cascade's font stacks, the
`unicode-range` carve, and the browser's own matching. Every one of this operation's thirty-eight
standing assertions reads a byte that **exists** — in `dist`, in `web/src/content`, in a workflow
file, in this repository's prose. **Not one of them reads a byte that is REQUESTED.**

The consequence is measured rather than argued. Two defects of this class were found **by hand**,
eight days apart, in the same queue lane:

- **2026-10-17** — `.site-footer__closing` set the Arabic strapline in Newsreader Italic, a
  Latin-only face. It rendered from the system serif and the browser fetched **146,872 bytes to
  paint none of it**: the single largest request on every Arabic page.
- **2026-10-25** — two `<em>` tags in the about paragraph slanted Arabic. `Amiri Italic` is a real
  slanted face, so unlike the strapline it *did* render: **131,100 bytes (111,720 + 19,380) to paint
  29 characters**, 3,852 bytes each.

Arabic typography has no italic convention — the same fact as *tracking is never applied to Arabic*
(2026-08-18 clause 4). **This stylesheet had already said so twice**, at `[dir="rtl"] .pullquote`
and again in `SiteFooter.astro` on 2026-10-17, the very day item 20 was raised. Both were written
per component. Neither reached the `<em>`. *A point fix reaches the instance it was sent to; only a
rule reaches the class* — #113's sentence, one week old, earned again in a different lane.

One rule in `global.css` (`[dir="rtl"] em, i, cite { font-style: normal }`), re-probed on the
rebuilt `dist` with the same instrument:

| page | before | after | delta |
|---|---|---|---|
| EN home | 778,376 | 647,276 | **−131,100 (−16.8%)** |
| AR home | 426,728 | 295,628 | **−131,100 (−30.7%)** |

**The Arabic home page lost 30.7% of its font payload to two lines of CSS.** The page was rendered
at 1280 × 2400 and looked at: upright throughout, shaped, joined, nothing else moved.

## The instrument — standing assertion 39, `qa_font_payload`

39 assertions, 24 `postbuild`, **36 of 39 gating**, all three derived by `qa_patch_queue`. It serves
`dist`, drives headless Chrome at six pages across both editions, logs every `*.woff2` the browser
requested, and reads the painted text back out of the layout engine. It parses the `@font-face`
blocks out of **the served bundle** rather than carrying a list, because the bundle is regenerated.

**Limb 1, asserted — no slanted Arabic.** No painted run containing an Arabic code point resolves to
a computed `font-style` other than `normal`. The boundary is exact and the artefact supplies it: a
code point is in an Arabic block or it is not. #113's and #114's method applied to a script.

**Limb 2, asserted — no dead fetch.** Every fetched file is justified by a painted code point inside
its own `unicode-range`, in a run whose stack names its family and whose style and weight its
`@font-face` accepts. Deliberately conservative, and the reason is in the tool's header: plain JS
returns the *declared* stack, not the resolved face, so the limb cannot produce a false red from
that direction and can miss a waste case.

**Measured and not asserted:** per-page totals, bytes-per-painted-character, fetches justified by
non-letters alone, and runs whose stack cannot paint their own script. A ceiling would be the wrong
gate today — the two reductions item 20 names are both out of this lane's reach, so a floor above
today's reality reds every build until work nobody here can do lands. That is `qa_bridge_coverage`'s
2.3% reasoning in a second costume.

## Proved both ways, and the two failures are the valuable half

Three controls green, and each injection was asserted to have changed the artefact before Chrome was
pointed at it (#35, and the 09-14 trap).

**Bite 1 — today's own defect, re-injected** into a copy of `dist`'s served CSS: red on *both*
limbs, exit 1, naming all four `<em>` runs across the two home pages. It also surfaced something the
fix's own arithmetic had hidden: of the 131,100 bytes, **19,380 were a pure dead fetch** —
`amiri-italic-400-latin.woff2`, pulled in by the slant and painting nothing at all.

**Bite 2 — the 2026-10-17 defect, restored exactly as it stood — DID NOT BITE.** Exit 0, control-green,
on the historical defect this limb was built for. The reason is the finding: the Arabic strapline
`صُنع رغمًا عن الظروف، لا بفضلها.` **ends in a full stop**, U+002E, which is inside Newsreader's Latin
`unicode-range`. So the 146,872 bytes were never a *dead* fetch. They were a fetch justified by **one
character that every Latin subset in the world contains.** Limb 2's unit is the file, and a file is
justified by its cheapest glyph.

**A bite that does not bite is the instrument telling you where its edge is**, which is the third
time in eight days this operation has been taught that (#114's first bite, #112's fifth, and now
this) — and this one is the sharpest, because the bite was aimed at a *real published defect* rather
than at an invented one. The measured limb that came out of it is now printed on every run: **five
fetches on the probed pages are justified by punctuation, digits or symbols alone, with not one
letter painted.**

## What the instrument found that nobody was looking for

**89 painted Arabic runs across six pages carry a font stack that names no bundled family covering
Arabic** — every Arabic date, kicker, section label, nav item and the Arabic footer rights line.
They are painted by whatever Arabic font the reader's system happens to have. The cause is a rule
whose own comment shows it never considered the case: `[dir="rtl"] .uppercase, .kicker, .mono {
font-family: var(--font-mono) }`, commented *"Mono / uppercase Latin labels stay Latin even on the
Arabic page."* The labels are not Latin. They are Arabic, set in a mono stack with no Arabic in it.

It is printed and not asserted, and handed to the Designer and the Web Developer as item 40, because
**the Arabic edition's chrome being set in a font we do not control is a typographic judgment, not a
byte count** — and because a floor there reds every build today.

## The general form

> **An assertion scoped to bytes that EXIST cannot see a cost paid in bytes that are REQUESTED.**
> Everything this operation enumerates is a product; a transfer is a negotiation between the product
> and a reader, and it happens after the last gate has run. The enumeration family has asked, six
> times, *what can this check not see?* — and six times the answer was a surface inside `dist`. This
> is the first time the answer is a quantity that **is not in `dist` at all**, and the 38 instruments
> that could not see it were not scoped too narrowly. They were scoped to the wrong noun.

## Carried forward

1. **Item 40**, raised today: the 89 Arabic runs with no bundled Arabic family in their stack.
2. **Item 20 stays open in its Designer half** — drop a family, and what replaces italic emphasis in
   Arabic now that the slant is gone. Both are face judgments and neither is this lane's.
3. **Newsreader italic, 146,872 bytes for 196 painted characters on an English article** — 28.2% of
   that page, legitimate typography, now with a number against it for the first time.
