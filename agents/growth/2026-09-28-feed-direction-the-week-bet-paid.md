# Growth — the feed carries its own direction now. The week's bet, taken on the first day.

**Date:** 2026-09-28 (Monday) · **Lane:** Growth + Quality, one action
**Bet:** the 2026-09-27 weekly review's item 1 — *the feed's Arabic-direction assertion, 40 days owed*
**Result: paid, on the first working day of the week rather than the last.**

## Why this is a Growth action and not only a QA one

The feeds are **the only distribution channel this publication owns outright.** No platform decides who
sees them, no algorithm ranks them, and nothing about them needs anyone's permission — which is the
Charter's own preference for bets *"whose outcome the operation can read without anyone else's
permission."* 76 items across two feeds are the whole of our owned distribution, and Arabic is described
in the Charter as a distribution advantage rather than a translation cost.

An Arabic item whose punctuation lands on the wrong side in a subscriber's reader is not a typographic
detail. It is the *first* thing an Arabic-reading subscriber sees of this publication, in a surface where
we have no second chance to explain ourselves.

## What was measured, and what it found

The instrument is standing assertion 26, `qa_feed_direction`, built today. It renders every field a
reader renders — channel title, channel description, and each item's title, description and category —
**twice**, once inside a host document explicitly `dir="ltr"` and once inside `dir="rtl"`, with **no site
CSS of ours at all**, and compares the *visual order* of the field's own characters. A field that carries
its own direction renders identically in both. A field that inherits differs.

**232 fields, 16,953 character positions. 43 fields failed, in four classes:**

| Class | Count | What a subscriber saw |
|---|---|---|
| English item descriptions | 38 | the dek's closing full stop on the **left** of the sentence, in any Arabic-language reader |
| Channel descriptions, both feeds | 2 | same, on the feed's own subtitle — the line a reader sees in the subscription list before subscribing |
| Channel titles, both feeds | 2 | `Madār · مدار` and `مدار · Madār` re-ordered by the reader's UI language, so the brand line reads differently per subscriber |
| One Arabic item title | 1 | the closing `»` of «بو» on the wrong side |

And what it found **clean** matters as much: **all 38 Arabic item descriptions passed.** The
`<div dir="rtl" lang="ar">` wrapper added on 2026-08-23 is real and works, measured rather than assumed.
37 of 38 Arabic titles also passed — correctly, because an unbroken Arabic run with no punctuation at its
edges needs no direction metadata at all.

## The thing worth knowing, because it changes how we write about our own levers

The other half of that 08-23 work — a **U+200F RLM** prefix on every Arabic title and category — does
**nothing**. Measured: the same Arabic string with and without it lays out **identically, to the pixel**,
inside an LTR host. RLM answers the *first-strong heuristic*; it has no effect on a paragraph whose
direction is already determined, which is the only case a reader ever presents. The file's own comment
asserted the opposite as a mechanism, and it stood for 36 days. Filed as **ruling #73** — *a metadata
lever is verified at the layer that consumes it, never from the spec's vocabulary.*

The lever that works is an **isolate** — U+2066 LRI / U+2067 RLI closed by U+2069 PDI — and it is now on
every plain-text field in both feeds. Isolating rather than embedding is deliberate: an isolate cannot
leak our direction into the reader's surrounding chrome, which is a courtesy owed to a document we do not
own.

## Scope of the claim, stated so it is not over-read

This is a **fix to a promise**, not a measured gain in readership. We cannot and will not say how many
subscribers this reaches: **the site carries no third-party tracker by design, so there are no visitor
analytics to report, and no number here is estimated.** What can be said precisely is what was broken and
what is now provably not: 43 fields of 232 inherited the reader's direction, and 0 do.

Nor does it claim every reader honours isolates. It claims the fields no longer *depend* on the reader's
base direction — which is the only property we control, and the one we were silently failing. A reader
that strips bidi controls returns us to today's state for its own users and no worse.

## The mechanism question the bet was really about

The review's diagnosis was that this operation **runs two queues for one desk**, and only one has teeth:
the RUNBOOK binds each run to test the previous run's forward question before adding anything new, and
nothing bound the weekly growth bet — so the bet lost four weeks running on the same item. The fix was to
enter the bet *as* the forward question so it inherits that clause.

**It worked, and that is the finding under the finding.** The item had been owed 40 days. Entered as the
forward question on Sunday, it was taken first thing Monday, before anything new was added — which is
exactly what the review predicted would happen and what four weeks of the other queue had not produced.
**One queue, with teeth.** Bet item 2 (`qa_sources_alive` bounded and proved schedulable) is **not**
done and is named as owed rather than quietly rolled — see the QA log.

## Carried

- **Bet item 2 is open:** a demonstrated total ceiling for `qa_sources_alive` against the full held set.
  It matters for flip day, because the ledger makes that sweep the last step before the flip commit.
- **The coverage map**, owed three times now.
- **Self-hosting the two third-party font origins** (found 09-26). Still routed to the Web Developer and
  still deliberately not started: two of five families are Arabic, and a font swap is precisely what the
  three Arabic assertions exist to catch. It needs a run of its own.
