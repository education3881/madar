# Ruling #73 — a control character is not an embedding: a metadata lever is verified at the layer that consumes it, never from the spec's vocabulary

**Filed:** 2026-09-28, QA lane, testing the named forward surface (the feed's Arabic direction, owed 40
days) and building standing assertion 26, `qa_feed_direction`.
**Family:** assertion discipline / which register speaks for the owner.

## The claim that stood in our own source for 36 days

`web/src/lib/feed.ts`, added 2026-08-23, said this in a comment — not as a plan, as a mechanism:

> `<title>` is PLAIN TEXT by spec. No markup, so no `dir` attribute. ... **The only available lever is
> to prefix the value with U+200F, which sets the paragraph base direction to RTL.**

It does not. **U+200F RLM is a strong directional *character*.** It satisfies the **first-strong
heuristic** — which is what `dir="auto"` consults, and what an HTML paragraph consults when its base
direction is not otherwise determined — and it has **no effect whatsoever** on a paragraph whose base
direction is already determined. Which is precisely the reader case that comment describes: a subscriber's
reader drops our title into its own document, whose direction is the reader's UI language.

Measured in headless Chrome inside a host explicitly `dir="ltr"`, the same Arabic string with and
without the RLM prefix laid out **identically, to the pixel** — first character at x=258, trailing full
stop at x=269 in both. The lever that changes the embedding level is an **isolate**, U+2066 LRI or
U+2067 RLI closed by U+2069 PDI, and it was never tried. Measured, it works: the trailing stop moves
from x=269 to x=8, the left edge, where an Arabic paragraph puts it.

Every Arabic item title and category in the feed has carried that inert prefix since the feeds shipped.
Two other classes fell out of the same measurement: the channel's own `title` and `description` were
passed through **neither** direction helper from the day the feeds shipped — the first Arabic a
subscriber ever sees, carrying nothing — and the English feed's fields carry no direction either, so an
English dek ending in a full stop puts that stop on the wrong side in an Arabic-language reader by the
identical mechanism. **43 fields of 232.**

## The ruling

> **A metadata lever is verified at the layer that consumes it.** A claim about what a control
> character, an attribute or a header *does* is a claim about a machine we do not own, and reading the
> specification's description of the character is not the same act as rendering it. The 08-23 comment
> was written from the spec's vocabulary — RLM *is* described as setting direction, in the narrow
> context of the first-strong heuristic — and the sentence that vocabulary produced was false about the
> case the comment itself was about.

And the corollary that makes it checkable:

> **An assertion must not read the lever; it must read the effect.** A check that had found `‏` at
> the head of every Arabic title would have reported the feed correct for 36 more days. The oracle that
> works asks the reader's question instead: *render the field twice, once in an LTR host and once in an
> RTL host, and compare the visual order of its own characters.* A field that carries its own direction
> renders identically in both. A field that inherits differs. No attribute is read anywhere in the
> check.

## Why the oracle is invariance and not "is it RTL"

Asserting *this Arabic field resolves RTL* is the wrong assertion twice over. It is unmeasurable for a
plain-text field (there is no element to compute style on that we control), and it is **wrong** for the
common case: a field that is one unbroken Arabic run with no punctuation, digits or Latin at its edges
lays out right-to-left in an LTR host too, because bidi handles the run itself. 37 of our 38 Arabic
titles are that field, and they need no direction metadata. Only the *paragraph-level* placement of
neutrals and opposite-direction runs depends on the base direction — so the property to assert is
**independence from the host**, which is exactly what a subscriber's reader varies and we do not.

Same shape as assertion 18 (`qa_arabic_joining`): compare the artefact against **itself** under a known
transformation, so the control is a construction rather than a defect that must be arranged to exist.

## Proved seven ways (#35, #66)

Control (after the fix): exit 0, 232 fields, 16,953 character positions. Bite, on the live defect
before the fix: exit 1, 43 fields named, in four distinct classes. Five injections into the *fixed*
artefact, each hash-proved to have landed, each firing exit 1 and naming the field injected — including
one that replaced the isolates with the U+200F this file used until today and **still fired**, which is
the ruling asserted as a check rather than as prose.

## Cross-references

- **#55** — the layer question. This is it applied to a promise made in a format, not in CSS.
- **RUNBOOK 2026-08-18** — a resolving asset is not a usable asset; *a promise in the metadata is a
  promise to a machine we do not own — verify it against that machine's accepted formats.* This ruling
  extends "formats" to "behaviours", which is the harder half: a format can be checked against a list, a
  behaviour has to be rendered.
- **#70** — a check's bucket set is an enumeration too. Sibling: there, the check could not report a
  distinction; here, the check would have read the wrong field entirely.
- **#67** — the deliverable is the file. The 08-23 work produced a file and half of it was right; the
  wrapper on `<description>` was the real instrument all along and the measurement says so.
