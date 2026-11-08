# Growth, 2026-11-08 — we publish a machine-readable citation graph, and not one node names a document

**The bet's property:** the outcome is readable without anybody's permission, because the subject is
our own built HTML. No traffic figure appears below, and none exists — the site carries no third-party
tracker by design.

## What was looked for, and why it was the wrong question

The lever this run went looking for was the obvious one: *does this publication's distinguishing asset —
**704 source citations over 353 named primary registers** — reach a machine at all?* The answer is yes
and has been for some time. Every one of the **88 article pages** emits a JSON-LD `Article` node, and
every one of those 88 carries a **`citation`** array. **704 `CreativeWork` nodes**, 352 English and 352
Arabic, each with `@type`, `name` and `url`. Nothing to fix.

**So the question moved one step in, to what the nodes SAY, and there the answer is bad.**

## The finding

**`citation[].name` is not the cited document's name. It is our whole annotation about the document.**

| Measure | Value |
|---|---|
| citation nodes served | **704** (EN 352 · AR 352) |
| median `name` length | **262 characters** |
| mean / longest | 414 / **3,237** characters |
| over 110 characters — the practical ceiling at which a consumer stops showing a title | **653 of 704 — 92.8%** |
| shortest | 40 |

A consumer handed `name` is handed a sentence like

> *"Ministry of Education, Singapore — press release, 13 July 2016: 'Changes to PSLE Scoring and
> Secondary One Posting' (the design filed in writing: stated aim #1 'reduce fine differentiation of
> students'; 29 possible PSLE Scores against more than 200 T-score Aggregates)"*

where the document's name is six words of it and the remaining four-fifths is **our editorial note on
why we opened it.** The note is the best thing about this publication's sourcing and it is the wrong
value for that key: `name` means *the name of the thing*, and a consumer that believes us is told this
press release is titled with our commentary. **The richest citation graph in the operation is
unusable as a citation graph**, and this is the 2026-08-18 defect's shape one surface over — not a
promise that resolves and renders nowhere, but a promise that resolves, renders, and **says the wrong
thing** — which is worse, because it cannot 404 and nothing can notice.

## The fix was specified, attempted on paper, and REFUSED — which is the actual output

The cheap fix is a one-line template change: cut `name` at the first ` (` and keep the remainder as
`description`. It was measured before it was written, and **it damages 163 of 704 nodes — 23.2%**:

> *"The Straits Times (Tang Yi Qing), 9 January 2025, republished on STOMP — the final batch of 24
> schools adopting Full Subject-Based Banding (…)"*

truncates to **"The Straits Times"**, because the first parenthesis in that annotation is a byline, not
a gloss. 503 nodes would improve, 163 would be destroyed, 38 have no parenthesis to cut. **A heuristic
that is right 71% of the time on a served field is not a fix; it is a different defect with better
press.** This operation has paid for that lesson once already, in the `hr.rule` fabricated defect of
2026-11-01: *a bite wider than the rule it targets manufactures the defect it was aimed at.* So nothing
shipped today, deliberately, and the measurement is the deliverable.

## What the right fix is, and the boundary that makes it cheap

**The artefact already supplies an exact boundary on most of the population.** `qa_citation_identity`
exists because **416 of 704 source entries quote their registers verbatim inside quotation marks**; read
the same way here, **452 of the 704 citation nodes — 64.2% — carry a quoted document title.** A quoted
string is not a guess about where a name ends: it is a boundary the annotation's own author wrote, which
is **#113's method** (an acronym states its own word count) and **#114's** (a digit is an exact
boundary) applied a third time, to a title.

So the work partitions, and the partition is the point:

1. **452 nodes (64.2%)** — the quoted span is the document's name. `name` = the quote, `description` =
   the rest. Mechanical, and checkable against the register's own bytes, because
   `qa_citation_identity` already fetches exactly these strings and reports **100 registers confirmed**
   as of today.
2. **252 nodes (35.8%)** — no quoted title. These need an editorial field, not a parser. A `sources[]`
   entry grows one optional key and the 252 are filled over time; until a key is present, `name` stays
   as it is, because a wrong short name is worse than a long right one.

**Why this is growth and not tidying:** a serious reader and a search engine reward the same thing here,
and it is the one thing this publication has that the field does not — every piece standing on named
primary registers read in served text. We publish that graph already. We publish it in a form that names
no document. Fixing bucket 1 alone puts **452 correctly-titled citations of 353 distinct primary
registers** into machine-readable form on 88 pages, in two languages, with no new content and no new
source.

**Raised as standing-queue item 87**, with bucket 1 separable from bucket 2 so the first can land
without waiting for the second. Not shipped today because the cost is a schema field plus a template
change plus a gate, and this run had minutes rather than hours — stated plainly rather than attempted
badly.

## The honest limit of this note

`name` being wrong is **measured**; a consumer *acting* on `name` is **not observed**, by us or by
anybody — which is standing-queue item 83 exactly, named two days ago: *of the artefacts handed to a
machine we do not own, how many has anybody ever observed in the consumer's own rendering?* A JSON-LD
citation array is the fourth handover point on that list and nobody here has ever seen one rendered.
The 92.8% is a fact about our bytes. The consequence is an inference, and is written as one.
