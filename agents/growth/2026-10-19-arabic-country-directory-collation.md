# Growth — the Arabic country directory now sorts in Arabic

**2026-10-19 · closes standing-queue item 23 (raised 2026-10-18 by the growth function) ·
[WD] with the Arabic Editor on the convention**

## The defect, as a reader met it

The hub's country directory shipped on 2026-10-18 and gave **38 countries a linked, indexable
name in both languages at the cost of zero new pages.** On the Arabic hub it read:

> أستراليا، البحرين، بنغلاديش …

which is **Australia, Bahrain, Bangladesh** — the English collation key, rendered in Arabic
script. It is not alphabetical in any sense an Arabic reader has. Found by rendering the page and
looking at it, not by reading markup (#16), and queued rather than fixed on the spot, because the
worst version of this is changing it quietly.

## The decision, and it is a convention rather than a bug fix

The sort now runs on **the name the reader sees**, folded four ways. Three of the foldings are
mechanical; the fourth is an editorial convention and is the reason this was queued:

1. **NFD, combining marks dropped** — removes tashkeel (`عُمان`, `الفلبّين`) and folds `أ إ آ` onto
   `ا`, because the hamzated alifs canonically decompose.
2. **`ى` → `ي`** and 3. **`ة` → `ه`** — the two orthographic pairs an Arabic index treats as one
   letter. NFD does not reach either.
4. **The definite article `ال` is dropped from the front of the name**, so `المغرب` files under
   `م`. This is the convention of Arabic reference indexes and atlases, and **the corpus says why
   it matters rather than leaving it to taste: 17 of the directory's names begin with `ال`.**
   Filing on the article would put roughly a third of the list under a single letter. That is a
   pile, not an index.

After the foldings the comparison is plain code-point order, which for the Arabic block **is** the
hijāʾī order — so there is no ICU, no locale and no environment in the answer (#59), and
`qa_stable_order.py` can predict it in Python in the same four operations.

## What the two editions now do, and why that is not a regression

**The two editions diverge by design.** `qa_stable_order` asserted one derivation on both sides;
it now expects **two orders**, and it reads the Arabic names out of `web/src/lib/i18n-geo.ts`
rather than restating them — a copy of fifty-two names in a second file is #57 waiting to happen.
The parse is guarded: **a map that comes back under 40 names refuses the check**, because the
fallback behaviour is to order every Arabic name on its English key, which would read as a pass.

*A single derivation is a virtue only where both sides are answering the same question, and
alphabetical order is a question about an alphabet.*

## Proved both ways (#35)

* **Control** — `npm run build` exit **0**, all eighteen postbuild gates green, 135 pages.
* **Bite** — the Arabic page reverted to the English order, rebuilt: exit **1**, and the message
  names the position and both slugs — *country directory diverges at position 2: serves
  2026-05-26-bahrain-bqa-public-grades, canonical is 2026-05-31-indonesia-permen-13-coding-ai*.
* **Inverse bite, taken by accident and worth recording:** the first build after the page changed
  but before the check learned the second order failed in the opposite direction, at the same
  position. The assertion was wrong about the page and said so.
* **English order unchanged** — `Australia, Bahrain, Bangladesh, Benin, Brazil, Chad, Chile,
  Ghana …`, verified in the built EN page, so the fix is additive.
* **Looked at** — the Arabic hub rendered in headless Chrome at 1280 and read: `ا` group, then
  `ب` (البحرين، البرازيل، بنغلاديش، بنين، بولندا), `ت`, `ج`, `ر`, `ز`, `س` (سنغافورة before
  السنغال before سوريا), `ع` (العراق before عُمان), `غ`, `ف` (الفلبّين، فلسطين، فيتنام), `ق`,
  `ك` (كوريا الجنوبية، الكويت، كينيا), `ل`, `م` (المغرب، المملكة المتحدة، موريشيوس). Correct
  throughout. *The probe served `dist` at the server root, so the `/madar/`-prefixed stylesheets
  404'd and the capture is unstyled: what this render verifies is the **order and the
  right-to-left direction**, not the styling, which is covered by the four render gates that ran
  green in the same build.*

## Why this is a growth action and not a tidy-up

Arabic is this publication's distribution advantage, not its translation cost (CHARTER). The
directory is the only surface on the site that names 38 countries we have written about exactly
once each, and on the Arabic side it was sorted by a key the reader cannot see. **No traffic
figure is claimed or estimated: the site carries no third-party tracker by design.** What is
claimed is narrower and checkable without anybody's permission — 38 Arabic country names are now
findable by the letter an Arabic reader would look under, and the build fails if that stops being
true.
