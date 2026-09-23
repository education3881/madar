# Growth — the distribution perimeter, swept for the first time

**2026-09-23 · Growth action of record.** Not a new experiment: an audit of everything this
operation has ever written *about* its own pieces for an audience, run with an instrument built
this morning and now gating the deploy.

## Why today

Yesterday's read found the struck *120-year* figure still alive in the wave packet's Egypt
caption, one day after the piece had been corrected in two languages — **ruling #50 committed a
second time inside the document #50 was filed on.** The QA log closed with the question that
follows from it: *does every figure in `social-drafts/**` appear in the shipped text of the piece
it names?*

The reason nobody could answer was structural, and it is worth restating because it is the whole
argument for what was built: **a distribution packet has no `sources[]`, so the Verifier's trace
cannot reach it; it is never built, so the standing assertions miss it; it is not rendered HTML,
so the 08-23 artefact-perimeter rule misses it too. Three perimeters, and every caption this
publication has ever written falls outside all three** — while being the only text we write that
is read by people who have not read the piece.

## What was swept

Every `.md` under `social-drafts/`. Four files carry per-piece captions and were bound to their
pieces with explicit markers (`<!-- piece: slug -->`, `<!-- caption:en -->` / `<!-- caption:ar -->`):
the **Ed05 wave packet** (5 entries, held) and the **Vietnam**, **Brazil** and **Kenya** packets
(3 live pieces, captions staged 2026-06-16 → 2026-07-04). **8 entries · 19 captions · 39
figures**, each checked against the title, dek, date, edition and body of the piece in that
caption's own language.

## What came back

**One real defect, on a live piece, 90 days old.** The Brazil packet's captions — English and
Arabic — advertised the federal Saeb result as **49%** where the piece ships **49.3%**, and the
short caption paired that rounded number with the **2025** indicator figure where the piece pairs
**2023 with 2023**. The advertised gap was 17 points; the piece's gap is seven. Rulings **#21**
and **#24** committed in the distribution copy of the piece written to explain them. Corrected in
both languages, from the piece's own sentence; the full record is appended to that packet.

**Three more instances of the same figure, one line outside the caption fences, invisible to the
check** — including the packet's own *"strongest distribution line, stated plainly"*, which exists
to be used verbatim. Found by reading the file the assertion had just marked clean, and corrected
by hand. **This is the assertion's scope limit and it is printed rather than discovered later:
the fence is the perimeter.**

**Two false positives, both the instrument's fault, both fixed before the gate was wired.** The
check reported `02` missing from three pieces, for captions reading *"New in Edition 02"* — a true
statement about each body and a false one about each piece, whose `edition` field says so. The
population now includes the rendered scalar frontmatter (`date`, `edition`) and an all-digit token
is compared against its leading-zero-stripped form. *The first number a new assertion reports is a
hypothesis about the assertion* (#35), and it was wrong twice out of five on first contact.

**The wave packet came back clean** — which is the correct result and not a null one: it was
re-read by hand yesterday, so a green here is a control on the instrument as much as on the copy.

## What this does not reach, said plainly

* **A figure spelled in words.** The Arabic captions carry more of these than the English, so the
  check is weaker on the Arabic side by construction. «ثمانية عشر مليون دولار» is a figure to a
  reader and nothing to this.
* **A claim with no number in it.** The 09-14 Sudan defect — *games that teach Arabic and maths* —
  would pass today exactly as it passed then.
* **Whether any of this was ever posted.** Growth does not post and the repository holds no record
  of what went out. It can say the Brazil captions were staged as ready on 2026-06-25 and were
  wrong for 90 days. It cannot say whether anyone read them. **That asymmetry is the argument for
  a gate rather than a posture note** — we cannot audit the outbox, so we audit the drafts, every
  build.

## The growth reading, which is the point of doing this

The operation's stated moat is that a reader can check us. **Every claim we have ever made outside
`dist` has been outside every instrument that makes that true**, and the one sweep run today found
a rounded decimal and a crossed vintage in the advertising copy for a piece about rounded decimals
and crossed vintages. Distribution is not a lower-stakes register than the piece; it is the same
publication in a shorter sentence, read by more people, with none of the annotations that let a
reader catch us.

**No traffic figure appears in this note. The site carries no third-party tracker by design and
none is estimated.** The outcome this action is measured on is readable without anyone's
permission: from today, a caption that misquotes its own piece fails the build.

**Owed:** the corrected Brazil Arabic caption is composed, not gated. With the wave packet's five,
the Arabic Editor now gates **six captions**.

— Growth · 2026-09-23
