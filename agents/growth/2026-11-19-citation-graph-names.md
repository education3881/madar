# Growth — the citation graph stopped telling machines a false title

**2026-11-19 · standing-queue item 87, raised 2026-11-08, closed today at 11 days.**

## What was wrong

Every article page emits a JSON-LD `Article` node carrying a `citation` array — the bibliography, machine
readable, and the highest-leverage on-page lever this publication controls while the domain question is
still open. Each entry was built as `{ '@type': 'CreativeWork', name: s.title, url: s.url }`.

**`s.title` is not a title.** It is our whole annotation about the document: why we opened it, what we
read in it, when, in what state, and what we declined to carry. Measured today across both editions:
**714 source entries, median 274 characters, mean 441, longest 3,237, and 663 of them — 92.9% — over the
110 characters at which a consumer stops showing a title.**

So a machine was being told that an Ofsted press release is **titled** with our commentary on why we
opened it. **This is the 2026-08-18 share-card defect one surface over and strictly worse:** a promise
that resolves, renders, and *says the wrong thing* cannot 404, so nothing in this operation could have
noticed. `qa_jsonld` passed on it every day, correctly — every reference parsed, agreed with its page and
dereferenced. It was never asked whether a field meant what its name says.

## Why the obvious repair was refused, twice

Item 87 proposed cutting at the first ` (` and **measured its own refusal**: the cut improves 503 entries
and **damages 163 — 23.2%** — because a parenthesis is as often part of a name as the start of a gloss
(*Free Quality School Education (FQSE)*).

Re-measured this morning with a narrower rule — cut only when the tail opens an annotation clause — and
it got **worse**: 55 cuts taken, 621 declined, and the resulting median name still 244 characters. A
better guess is still a guess.

## The fix is structural, and schema.org already draws the line

`name` is a NAME. `description` is prose about the thing. The annotation belongs in the second.

- **`description` carries the full annotation on all 714 nodes** — the property where long text is
  legitimate, and nothing is lost: everything a machine was told before, it is still told.
- **`name` is emitted only where a document name can be EVIDENCED**, and the evidence is a boundary the
  **artefact supplies** rather than one the builder guesses (#113): a span the drafter marked with
  quotes or emphasis, in the annotation's opening window.
- **Where no name can be evidenced, no `name` is emitted at all.** Telling a consumer nothing about a
  title is strictly better than telling it something false — which is the whole finding, applied to our
  own repair.

### Measured before and after, from the served bytes

| | before | after |
|---|---|---|
| citation nodes served | 714 | 714 |
| nodes carrying `url` | 714 | 714 |
| nodes carrying `description` | 0 | **714** |
| nodes carrying `name` | 714 | **122 (17.1%)** |
| name length, median | 274 | **58** |
| name length, max | 3,237 | **105** |
| **names over 110 characters** | **663** | **ZERO** |

`qa_jsonld` CLEAN at 138 pages after the change; full build exit 0.

## Two measurements that decided the design, recorded because both were close calls

**The window was measured, not chosen.** A marked span is genuinely ambiguous between the register's
*title* and a *quotation from it* — #112 found **529 quoted tokens over 218 registers** inside these same
annotations, so in the corpus as a whole quotations are the majority of marked spans. What separates them
is **position**: a title sits immediately after the publisher, a quotation sits later in the gloss. The
first marked span within the opening N characters yields **191 names at N=400, 163 at 200, 120 at 120,
75 at 90**. Hand-sampling twelve at N=120 returned **twelve genuine document titles**; the same sample at
N=400 contained *"are not matters for this court"* — a courtroom quotation about to be served as a
register's name. **N=120 is taken: precision over recall**, because a false title is the defect this
change exists to remove and a missing one is merely a silence.

**And the first version of the matcher sprang today's own ruling.** It read a **possessive apostrophe** as
a closing quote and produced names like *"s founding figure On the gender attributed to the named
founding figure: this register refer…"* — a span running from one possessive to the next. U+2019 is the
same code point in *the release's own words* as in *'Results of Government Schools Reviews'*; the
difference is **positional**, not in the character. Fixed by requiring an opening mark to follow the
start, a space or a bracket, and a closing mark to precede the end, a space or punctuation — never a
letter. **That is the third firing of ruling #150's family inside one run**, in three different
functions, and it is the day's ruling.

## What is left, and it is editorial rather than structural

**592 of 714 entries carry no evidenced name**, and the reason is that their annotation never marked one
— `Teaching Service Commission of Sierra Leone — Teacher Management Policy` names a document perfectly
well in prose and marks nothing. **No builder can supply that boundary and none should try**; what can
supply it is the drafter, by marking the register's own title the way 122 entries already do. Raised as
standing-queue item **134** for the Editor rather than fixed here, because it is a change to how
annotations are written and that is not the growth function's to decide.

## Traffic honesty

No visitor number appears here and none is estimated. The site carries **no third-party tracker, no
analytics and no automatic third-party request by design**, so this operation cannot say whether any
consumer reads this graph. What it can say is what it serves, counted from its own bytes: **714 citation
nodes, 714 descriptions, 714 URLs, 122 names and not one of them over the length at which a title stops
being shown.** That is a claim about our output, which we own, and not a forecast about a search engine,
which we do not.
