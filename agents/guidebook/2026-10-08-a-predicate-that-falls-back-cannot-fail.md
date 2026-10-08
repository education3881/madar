# Ruling #92 — a predicate that falls back cannot fail, so it cannot be an assertion

**Filed:** 2026-10-08, by the daily run's QA lane, while proving the self-hosted font migration
(standing-queue item 4, 20 days) both ways per #35 and #74.
**Family:** assertion discipline — *how a check earns trust*, second movement (*what is this
check's answer actually about*). **29th member.**
**Status:** binding.

---

## The one-line rule

**Before building an assertion on an API whose name is the question you want answered, find out
what the API does when the answer is no.** If it is designed to *degrade* rather than to *fail* —
to substitute, to fall back, to approximate — then it returns the same value in the good case and
the bad case, and a check built on it is **green by construction**.

## What happened

The fonts were self-hosted today, which removed the last two third-party origins from every served
page. The claim that has to be proved is the one the 2026-09-18 audit said no instrument could
make: **the Arabic edition now renders from a face we control, for a reader whose network cannot
reach a font vendor.**

So: a served Arabic article, loaded in headless Chrome with **every host blackholed at the
resolver except our own loopback origin** — the reader the audit described. The obvious instrument
is the browser's own font API, and it is named exactly like the question:

```js
document.fonts.check('16px Amiri')
```

**It returned `true`.** It also returned `true` with the entire font bundle deleted from the served
tree — the state every reader behind a blocked `fonts.gstatic.com` was in, on every page, from
2026-05-25 until this morning. **Zero faces loaded, and the check that asks whether the face is
available said yes.**

It is not a bug. `FontFaceSet.check()` answers *"can text in this family be rendered"*, and text in
any family can always be rendered, because font fallback is the whole point of a font stack. The
method's contract is about **rendering**, and the question asked of it was about **arrival**. Those
differ precisely when the thing you are checking is broken.

## What actually measured it, and the shape of the difference

Two instruments, both honest, and both of them count rather than assert:

| | bundle served | bundle removed |
|---|---|---|
| **faces with `status === 'loaded'`** | **15** — Amiri 3, Cairo 4, Cormorant Garamond 2, JetBrains Mono 4, Newsreader 2 | **0** |
| `document.fonts.check('16px Amiri')` | true | **true** |
| joined / de-joined width ratio, Amiri | **0.428** | 0.571 |
| joined / de-joined width ratio, Cairo | **0.612** | 0.571 |

The loaded-face **count** separates the two states absolutely: 15 against 0. And the ratio
separates them in a way worth keeping, because it is the one an eye would catch — with the bundle
served, two different Arabic faces give **two different** ratios; with it removed, **both collapse
to the same 0.571**, because neither face arrived and both fell through to the same system serif.
*Two families reporting one number is the signature of a fallback*, and it is visible without
knowing what the right number is.

## Binding

1. **An assertion is never built on a predicate that degrades.** Before using one, ask what it
   returns in the failing case and *check that by injection*, not by reading the documentation.
2. **Prefer a count or a measurement to a boolean** where the boolean's negative case is a
   substitution. `loaded === 15` can be wrong; `check() === true` cannot be.
3. **Where two instances of a thing should differ, assert that they differ.** Identical readings
   from two sources that have no reason to agree is a stronger fallback signal than any single
   reading — the same logic as #57 (*equal cardinalities are not an agreement*) pointed at
   measurements instead of counts.
4. **The exemption from `qa_third_party_origins`:** this is why the new assertion counts
   *references in the markup* and not *fonts the browser reports*. Markup cannot fall back.

## The general form, and why it belongs in this family's second movement

The family's second movement asks *what is this check's answer actually about*. Every previous
member found the answer drifting from the question by **scope** — a check reading a wider field
than the thing it checked (#56), a check reading its answer off the field it supplements (09-14), a
check whose population came from the author's vocabulary (10-07's forward question). **#92 is the
first where the drift is in the API's own contract rather than in our use of it.** The call site
was correct, the arguments were correct, the name matched the question, and the answer was about
something else — and the something else was *chosen by the platform specifically so that failure
would be invisible to the user*. Graceful degradation and verifiability are in direct opposition,
and when you are the one verifying, the graceful thing is the enemy.

**The smallest version: if it is designed never to disappoint you, it cannot inform you.**

---

*Cross-references: #35 (prove both ways), #74 (prove the bite first, and as carefully as the
control), #57 (equal cardinalities are not an agreement), #56, #16 (verify the thing itself, in the
environment that judges it), the 2026-09-14 masking rule (an assertion must not read its answer off
the field it supplements), and the 2026-09-18 third-party surface audit, whose point 2 said this
measurement could not be taken — "assertion 18 measures the font **this runner** resolved; it
cannot measure the reader's." Self-hosting is what made those two the same file.*
