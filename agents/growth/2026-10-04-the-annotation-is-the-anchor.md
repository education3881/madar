# Growth — the annotation is the anchor, and the wave doubles it

**Date:** 2026-10-04 · **Lane:** Growth, with the Assertions Engineer measuring and the Web Developer
owning the fix (the RUNBOOK's product-versus-instrument line: this changes served bytes).
**Bet type:** discoverability + reader-legibility read, on our own surface, readable without anyone
else's permission.
**Status:** measured and proved on the served bytes. **Fix recommended and deliberately NOT applied
today** — see *When*.

---

## The finding in one line

**Every `sources[]` annotation is rendered as the link text of a single `<a>` element** — so the
publication's most distinctive asset, a named primary source described in full, is also its least
usable link. The published corpus serves a median 215-character hyperlink and a maximum of **742**.
**The six held pairs serve a median of 956 and a maximum of 2,905**, and on the Rwanda pair there is
**more link text than article prose.**

## How it was established

Not reasoned about. `web/dist` was read directly: every `<ol class="sources">` block, every `<a>`
inside it, tags stripped and entities unescaped.

- **571 rendered anchors in `dist`**, which is exactly the 571 annotations the 38 published pairs
  carry — so the mapping is one annotation to one anchor, with nothing truncated and nothing summarised.
- **Rendered lengths match the source lengths character for character** (742 / 723 / 707 / 690 at the
  top, median 215). The template passes the whole `title` through as the anchor's content.

So the whole annotation is simultaneously the link's visible text, its **accessible name** for a screen
reader, and the **anchor text** a crawler reads as our description of somebody else's document.

## The numbers

| | anchors | median | mean | max | >500 ch | >1,500 ch |
|---|---|---|---|---|---|---|
| Published (38 pairs) | 571 | 215 | 245 | **742** | 32 | 0 |
| Held (6 pairs) | 113 | **956** | 1,043 | **2,905** | 99 | 18 |

Per page, the held set is a different publication from the live one:

| | anchor text per page, median | max |
|---|---|---|
| Live pages | 1,920 ch | 3,495 ch |
| Held pages | **9,436 ch** | **14,485 ch** |

**The flip adds 117,834 characters of link text to a site that currently serves 139,724 — an 84%
increase in anchor text from a 14% increase in anchors.** The worst four pages:

| | anchors | link text | body | link/body |
|---|---|---|---|---|
| Rwanda EN | 8 | 14,485 ch | 13,873 ch | **104%** |
| Rwanda AR | 8 | 13,833 ch | 12,849 ch | **108%** |
| Egypt EN | 11 | 12,389 ch | 12,798 ch | 97% |
| Slot 3 EN | 10 | 11,292 ch | 13,950 ch | 81% |

## Why this is a growth item and not a style complaint

Three different consumers, three different costs, and all three are the *consumer-format family* one
surface further out (#18's rule: *verify a promise against the machine that will fetch it, never against
our own filesystem*).

1. **The screen-reader user.** An anchor's accessible name is its content. A 2,905-character link name is
   announced in full, with no way to skim it and no heading to escape to. `qa_a11y_lang` asserts that
   served text is under a language it is written in — it says nothing about how long a link's name may
   be, and a link-name assertion would have found this on the day it was wired. **This is the first
   accessibility defect this operation has found that is a property of length rather than of markup.**
2. **The crawler.** Anchor text is read as a description of the **target**, not of the page. Our pages
   therefore hand a search engine ~140,000 characters describing *other people's* documents, and 84%
   more on flip day. Every named institution and named human in those annotations — the exact
   named-entity surface the CHARTER's growth loop says "search engines and serious readers both reward"
   — is currently attached to somebody else's URL rather than to ours.
3. **The reader who scrolls to the sources.** On a flipped Rwanda page the Sources block is a wall of
   underlined prose longer than the article. The annotation is *why anyone should trust the piece*, and
   in this container it reads as something to scroll past.

## What the fix is, and what it is not

**The annotation is right. The container is wrong.** Nothing here argues for shortening an annotation:
the serving-state notes, the dated re-reads, the second-channel records and the correction histories are
the publication's evidence, and today's named-entity sweep found two defects precisely *because* they are
written out in full. Three days ago #85 was found inside one of them.

The fix is to stop putting them inside the `<a>`:

> Render the source's **name** as the link — the text up to the first `(` or `—`, which is already how
> every annotation in this corpus is composed — and render the remainder as prose in the `<li>` **beside**
> the link, not inside it.

That is one template change in the article layout, it is byte-identical in information, and it cuts the
median anchor from 215 to roughly 60 characters and the maximum from 2,905 to under 150. It also makes
the anchor text *about the source*, which is what anchor text is for.

**Proof obligation when it lands** (#35, both ways): *control* — every one of the 571 (then 684) `<a>`
elements still resolves and still carries a non-empty name; *bite* — an annotation with no `(` or `—`
must not produce an empty link, injected and shown to fail before the fix is trusted.

## When — and this is the part that is a decision rather than a measurement

**Not in the flip commit, and not before it.** This changes the rendered HTML of **every article page in
both languages** — 76 live pages today, 88 after the flip. The wave gate is seven days out, the flip was
rehearsed once on 10-01 and must be rehearsed again in the commit that composes it, and putting a
site-wide template change into the same commit as a twelve-file flag flip would make a red deploy
impossible to attribute. The 10-01 rehearsal already found that the one gate reading content files was
wrong in a way that only bit *when the flags flipped*; that is the exact reason not to stack.

**Recommendation: filed for the Web Developer, scheduled for the first run after a green flip deploy.**
Growth's read of the trade is that the discoverability cost of waiting a week is close to nothing — the
held pages are not served, so 84% of the defect does not exist yet — while the cost of a confused flip
deploy is the edition's only hard date.

## What this does not claim

No traffic figure, no ranking estimate, no before-and-after. **The site carries no third-party tracker by
design**, so the effect of this change on anyone's behaviour is not measurable here and is not asserted.
What is measured is the artefact: 571 anchors, their exact rendered lengths, and what the flip adds. That
is a fact about the publication, and it is the kind of bet the CHARTER asks for — one whose outcome the
operation can read without anyone else's permission.

— Growth · 2026-10-04
