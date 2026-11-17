# Ruling #148 — a cost is a DEFECT only where an equivalent exists; otherwise it is a PRICE, and which one it is is decided mechanically

**Filed 2026-11-17** by the quality function, closing standing-queue items **116** (the board's only
DEFECT, 2 days) and **119** (OPEN, raised the day before) **together**, because the board had already
said in writing that the two were one question a glyph apart.
**Family:** assertion discipline — **SIXTY → SIXTY-ONE.**

---

## What the two rows asked, and why neither could be answered as asked

Item 116: the English home page spends **86,608 bytes** on a Newsreader `latin-ext` file that paints
**one** character, and JetBrains Mono spends **11,624** more on the same letter — **98,232 bytes for
`ā`** — *and whether body prose at 18px may take a decomposed macron is an Editor and Designer call.*
Item 119: one `ɔ` costs **10,532 bytes** on an Arabic article page, *and it is the same judgment one
glyph over.*

Both rows routed the question to taste, and both routed it to the same desk. A week would have been
spent on two conversations about typography. **The question is not a matter of taste and the rows could
not see that, because each measured a cost and neither asked what the alternative was.**

## The rule

> **A byte cost is a DEFECT when an equivalent exists that the artefact can already serve, and a PRICE
> when it does not. Establish which, mechanically, before anybody is asked for an opinion.**

For this corpus the mechanism is three lines, and both operands are ours:

```python
LATIN = <the `latin` unicode-range, read off web/public/fonts/madar-fonts.css>
nfd = unicodedata.normalize('NFD', ch)
defect = len(nfd) > 1 and all(ord(c) in LATIN for c in nfd)
```

It works because of a fact about our own bundle that nobody had read: **every family's `latin` cut
lists `U+0304`, `U+0308` and `U+0329` inside its own `unicode-range`**, beside `U+0000-00FF`; and
`latin-ext` is declared **before** `latin`, so where both claim a code point **the later rule wins** and
the glyph is painted out of a file the page already holds. The cheaper equivalent is not a trick; it is
a capability the stylesheet has always advertised.

| char | | verdict |
|---|---|---|
| `ā` U+0101 | → U+0061 U+0304, both in `latin` | **DEFECT** |
| `Ā` U+0100 | → U+0041 U+0304, both in `latin` | **DEFECT** |
| `ɔ` U+0254 | atomic | **PRICE** |
| `ʿ` U+02BF | atomic | **PRICE** |
| `ṣ` U+1E63 | → U+0073 U+0323, and U+0323 is **not** in `latin` | **PRICE** |
| `ḥ` U+1E25 | → U+0068 U+0323, same | **PRICE** |

**Item 116 is a defect. Item 119 is a price.** Not because one glyph matters more, but because one has
an equivalent and the other does not.

## What each verdict then obliged

**The defect was repaired and the equivalence proved before any byte moved** (#35, and #147 clause 2 on
aiming the probe at what the assertion reads). Three rulers in the faces and at the sizes that actually
pay, the **smallest measured first** because a combining mark is likeliest to break there and the
2026-11-15 precedent covered only a 22px display wordmark:

| face · size | advance width Δ | differing pixels at 8× |
|---|---|---|
| Newsreader 400 · 17.5px (the row said 18px; 17.5 is what the computed style says) | 0.000 px | **0 of 282,240** |
| JetBrains Mono 400 · 10.5px | 0.000 px | **0 of 101,808** |
| Cormorant Garamond 500 · 22px | 0.000 px | **0 of 446,688** |

then the ruler that cannot be mis-aimed: the whole Editions page, 1200×2600, before and after —
**0 differing pixels of 3,120,000** against 2,292,572 ink pixels. Measured saving across the six probe
pages, cache cleared: **−284,492 bytes**.

**The price was judged, paid, and written down with its number.** `ɔ` is a phoneme of the Krio phrase
the piece quotes; `Lan fo lan` would misspell a named language's orthography, which is a content
decision wearing performance clothes. There is nothing to subtract, so there is nothing an instrument
could have settled — and the row is closed as **judged**, not carried another week.

## The three things worth carrying

**1 · A row that frames a cost as a judgment has usually not looked for the equivalent.** Both rows were
written by careful runs and both skipped the same step. Asking *what else could paint this* is cheaper
than asking *is this worth it*, and it is the question that decides whether the second question exists.

**2 · The boundary is #116's DEFECT/OPEN boundary, sharpened on the other axis.** #116 drew the line at
*are these bytes wrong NOW*. This draws it at *is there a right version of these bytes that costs less*.
A price can be large, permanent, and not a defect; the corpus now carries **193,772 bytes of `latin-ext`
on one article page**, every byte of it correct.

**3 · And the rows' own numbers were the small ones, in the same direction, twice.** Item 116 named
98,232 bytes on the home page; the **Editions** page paid **140,900**, and the **AR editions page is the
only Arabic page that paid at all** — both because the inlined covers put the Latin wordmark at 40px in
the display face. Item 119 named 10,532 on an Arabic page; the **English** edition of that same piece
pays **95,540** for the same glyph in italic, 9× more, because the row measured one edition. Neither
undercount was careless: `qa_font_payload` probes **six fixed pages**, and the worst page in the corpus
is not one of them (standing-queue item 123). **A cost measured on the page where it was noticed is a
sample of one, and the page where a cost is noticed is not the page where it is largest.**

## Where it sits

Beside **#115** (the first assertion whose subject is a quantity not in `dist` at all) and **#145**
(a constraint about a script may not be enforced about a page), and it completes a short arc those two
started: #115 learned to *see* a font fetch, #145 learned to *scope* a font rule, #148 decides *whether a
fetch is a fault*. Against **#93** it is the complement rather than an exception: #93 says do not gate a
measurement whose floor would red every build; #148 says a measurement that cannot be gated can still be
adjudicated, if you ask what the alternative is instead of what the number is.
