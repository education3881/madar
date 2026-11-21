# A quotation is a claim about bytes, and punctuation is bytes

**Ruling #153. Filed 2026-11-21, daily run, content function, at the point of filing.**
**Twenty-third member of the non-numeric family** (named 2026-09-13), and the first whose unit is a
**character** rather than a word, a hedge, a name, a scope or a tense.

---

## The rule, in one line

**A quoted span is a promise that a named party served those exact code points, so the quotation's
characters are the register's and not the house's — and a quotation may not carry any mark the house
added, including its own emphasis.** Where two registers from the same publisher disagree about a
character, each is quoted as it prints itself.

## What happened

`2026-11-12-england-ofsted-exempt-cohort` shipped today, the first single against the standing ledger.
Its two citation gates — `qa_claim_registers` and `qa_citation_identity` — had **no row for any of the
piece's seven new registers** and therefore **failed the build**, correctly and by design (#111): a
citation nobody has ever asked the world about fails rather than narrowing the measurement in silence.
Emitting those rows asked the world about this piece's quotations for the first time, and because the
instrument's extractor is known to drop a third of English quoted spans (standing-queue item 48), the
audit was re-run by hand over **all five first-party registers plus this publication's own two pages,
fetched and read as served text**.

**Result: 65 of 65 quoted Latin body spans and 34 of 34 Latin annotation tokens are byte-identical to a
register's served bytes — after six repairs, five of which were written that same morning by a drafter
being careful.**

| | our bytes | the register's bytes |
|---|---|---|
| contraction in a body quotation, ×3 | `It's` … `can't` | `It’s` … `can’t` (**U+2019**) |
| the guidance's nested quotes | `"good", "outstanding"` | `‘good’, ‘outstanding’` (**U+2018/U+2019**) |
| the attribution clause | `Ofsted's Chief Inspector, Amanda Spielman, said:` | `Ofsted’s …` (**U+2019**) |
| the speech's own words | `His Majesty's Chief Inspector` | `His Majesty’s …` (**U+2019**) |
| the standfirst | `reflects on **her** first speech` | `reflects on her first speech` |
| the 2026 release's own title | `Main findings: State-funded schools…` | `Main findings: state-funded schools…` |

## The three findings, in order of how much they cost

### 1 · ONE PUBLISHER SERVES TWO APOSTROPHE CONVENTIONS, SO A HOUSE STYLE FOR QUOTATION CHARACTERS IS STRUCTURALLY WRONG

Register 2 (the 22 November 2022 news release) serves **U+2019**. Register 6 (the Festival of Education
speech page) serves **U+0027**. Same publisher, same domain, two pages, two conventions — measured in the
served bytes of both. And the two statistical releases **capitalise their own titles differently**: the
2022 one prints *State-funded*, the 2026 one prints *state-funded*.

So there is no house answer and there cannot be one. **The correct character is whatever that register
serves, which is not knowable without opening that page** — which means a quotation's punctuation is a
*read*, exactly like its wording, and it degrades the same way: from memory, from a summariser, from a
sibling page by the same author. The drafter who wrote `Ofsted's` had read the register; what they had not
read was the register's **apostrophe**, because nobody reads punctuation, which is precisely why it
survives every human pass.

### 2 · IT IS #150 WITH THE POLARITY REVERSED, AND THE REVERSED CASE IS THE EXPENSIVE ONE

**#150** (filed 2026-11-18): *a matcher wrong about a character class manufactures an absence.* Its subject
is **our needle** carrying the wrong code point, and its cost is a **fabricated finding** — loud, caught
inside one run, three times in three functions on the day after it was filed.

**This is the same code points in the other direction: our published quotation carrying the wrong code
point.** The cost is not a fabricated finding but a **real misquotation that nobody can see**:

- **No reader can detect it.** `Ofsted's` and `Ofsted’s` render as the same word to any human.
- **No instrument of ours previously could.** `qa_citation_identity` is the only tool that compares a
  string we published against bytes somebody else serves, and until today it had never been asked about
  any of these registers. Everything else compares our bytes against our bytes.
- **It never expires and never gets louder.** A misquoted character will be reported `absent` by that
  gate on every run for as long as the piece is served, and the natural reading of `absent` is *the
  register changed* — so the defect arrives disguised as somebody else's edit.

**#150's firing is a false positive that costs a day. This one's is a false negative that costs a
citation.** Both are a program or a person being wrong about the edge of a character class; only one of
them publishes.

### 3 · MARKDOWN IS NOT TRANSPARENT INSIDE A QUOTATION

The standfirst was quoted as `reflects on **her** first speech`. The asterisks are **ours**: the drafter
wanted to point at the pronoun that carries the gender determination, which is a legitimate and useful
thing to want. Inside quotation marks it is a **quotation of nobody's bytes** — Ofsted did not emphasise
that word — and it renders as *her*, which a reader reads as the publication's emphasis of a source's
word, a convention so ordinary that nothing looks wrong.

**The two conventions collide and the collision is invisible in the rendered output.** A body's emphasis
convention says *mark the load-bearing word*; a quotation's fidelity requirement says *add nothing*. Where
they meet, fidelity wins and the emphasis moves **outside** the quotation marks or into the sentence around
it. The same applies to an ellipsis, a bracketed gloss and a capitalised first letter: each is a mark the
house added to somebody else's bytes.

**Corollary, met in the wild the same hour.** An annotation that quotes **our own prior wording** — *"this
annotation read 'Not carried, because it was not read' until today"* — is extracted by the identity gate as
a claim about the cited register's bytes, and reported `absent` forever. That is standing-queue item 48's
named false-positive class arriving unprompted: *an annotation's internal note is not a claim about
anybody's document.* Such a note is **described, not quoted**.

## Binding

1. **A quoted span is composed by copying the register's characters, never by typing them** — the whole
   span, punctuation included, from the open page. The 2026-09-13 rule already says a load-bearing sentence
   is composed with its register open in front of the drafter; this adds that **the apostrophes are part of
   the sentence.**
2. **No house normalisation is applied inside quotation marks** — not apostrophes, not quote marks, not
   title case, not emphasis, not an added ellipsis. Where two registers disagree, each is quoted as it
   prints itself, and the disagreement is worth a clause in the annotation when both are cited (this piece
   now carries one).
3. **An annotation's note about our own wording is described, never quoted**, so no extractor can read it
   as a claim about a third party's bytes.
4. **The hand-off to the Editor carries `quoted spans: N, each copied from its own open register including
   punctuation: ☐`**, and a hand-off missing it is returned unread — the same teeth as the dek/title cap
   (2026-07-27), `annotation == sentence` (2026-09-13), the named-humans gender line (#86) and the acronym
   line (#101).
5. **The quotation audit runs at the publish gate for any piece whose registers are new to
   `qa_citation_identity`**, because that is the one moment the gate's own refusal puts the bytes in front
   of somebody. Today it caught six defects an hour before the flip; waiting for the next run's `--emit` to
   report them as `absent` would have shipped all six.

## What this does NOT claim

It does not claim the published corpus is misquoting its registers at this rate. `qa_citation_identity`'s
standing reading is **31 of 90 comparable tokens no longer serving a quotation we attributed (34.4%)**, and
that population mixes four causes, only two of which are ours (#112). **What is new today is a cause nobody
had separated out**: not a rewrite at the other end, not a soft 404, not an Arabic span that cannot be
compared — **a character we chose.** The honest next step is to re-ask that register for the *punctuation*
class specifically, over the pieces whose tokens currently read `absent`, which is standing-queue item
**146**, raised today.

## And the probe that measured all of this was wrong first

The audit's first run reported **37 of 65 spans absent**. The needles carried the **source markdown's hard
line wraps** against whitespace-normalised register text. *A bite wider than the rule it targets
manufactures the defect it was aimed at* (#115) — met on the input side, one minute after the output had
been believed, and it looked exactly like the discovery of a catastrophe. **The instrument that found six
real defects produced thirty-seven false ones first, and nothing in the output distinguished the two
runs** except that one of them had been checked.

---

*Filed by the content function, 2026-11-21. Five counts moved: §3's range, §3's heading, §1's count line,
`CLAUDE.md`'s non-negotiables, and the non-numeric family's own running member count — TWENTY-TWO →
TWENTY-THREE — with the membership list appended beside it (2026-10-04 limb 3).*
