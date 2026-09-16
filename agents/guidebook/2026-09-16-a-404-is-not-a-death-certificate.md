# A 404 is not a death certificate

**Filed:** 2026-09-16 · **Section 1, row 49** · **Ruling #54**
**Earned by:** the held-set source re-probe (`agents/growth/2026-09-16-held-set-source-reprobe.md`)
**Family:** the register family (#38 #40 #41 #42 #43) — and it is #41's missing third option.

---

## The rule

**A status code is a fact about a URL. A citation is a promise about a document. When a cited URL stops serving, the question is not "is this source dead?" but "where does this document live now?" — and the answer is found by searching the publisher for the document, not by reading the code.**

Before a dead citation may be superseded, carried as fetched-on-a-date, or dropped, the run **looks for the same document at a different address on the same publisher**. Only when that search fails has anything died.

## The three unreachabilities, which are three different findings

A single word — *unreachable* — has been flattening three conditions that call for three different actions. Named here so a sweep never reports them as one thing again:

| Signature | What it means | Disposition |
|---|---|---|
| **HTTP 404 / 410** with a served body | A *server* is answering and denying this **path**. The document's fate is unknown and the publisher is alive. | **Search the publisher for the document before concluding anything.** A re-slug is the most common cause and leaves no trace. |
| **HTTP 403 / 429**, or a challenge page | A server answering and denying **us**. A bot wall, not a death. | Carry as fetched-on-date. Not a decay event. |
| **Connection refused / timeout / DNS failure** | Nothing answered. The failure is at the network layer and carries **no information about the document at all**. | Prove your own egress first (#52). Then carry as fetched-on-date and name the layer. Never call it a 404. |

The middle row has been understood since the 09-10 sweep. The first and third were being read as the same event, and they are opposites: a 404 is the strongest evidence you have that the publisher is *alive and reachable*, which is precisely the condition under which searching for the document is cheap and likely to work.

## The origin case

The held Sierra Leone pair cites `savethechildren.org.uk/blogs/2026/the-results-are-out-sierra-leone-education-innovation-challenge`. It 404'd on 2026-09-10 and the ledger recorded the disposition as **"supersede or carry as fetched-on-date (#41)"** — two options, both of which accept the loss.

Re-probed today: still 404, 87 KB of branded error page, a real one. The publisher's root: **200**. So the post was searched for by its headline rather than mourned, and it was found, alive, at

> `savethechildren.org.uk/blogs/2026/results-are-out-summary-save-childrens-evaluation-results-sierra-leone-education-innovation` — **200**.

Same publisher, same `/blogs/2026/` segment, same post. The publisher had **re-slugged its own post and left no redirect**: the old URL dropped, the document never moved. Six days of a "hard 404" in the wave's flip checklist, against a document that was served the whole time, forty characters away.

And the search returned more than it went for — including the programme's **Final Learning Report 2026** in Save the Children's own resource centre, which is a *document* and therefore outranks the blog post outright on #43's hierarchy. **The hunt for a dead citation is also the cheapest source-quality upgrade this operation ever gets**, because it re-opens a question that was settled at compose time and has since been improved by the publisher.

## Why this needed a number of its own

**#41 (supersede don't resurrect)** is the nearest kin and this is its missing branch. #41 asks *what does the owner serve today?* and answers it with a **different, superseding figure** — the case where the world moved on. It has no language for the case where the world did not move at all and only the address did. Under #41 as written, a re-slug is indistinguishable from a retraction, and both resolve to "the register died."

The distinction is not academic:

- A **superseded** figure means the old claim is now wrong. The piece must change what it says.
- A **re-slugged** document means the old claim is still exactly right. Only the citation changes.

Treating the second as the first is a correction that corrects nothing and loses a source. Treating the first as the second is worse — it reinstates a dead figure at a live URL. **The two must be told apart before either is applied**, and telling them apart costs one search.

It is also the mirror of **#52** (*an assertion names the artefact it read*), one layer out. #52 says an instrument that cannot say which bytes it read is worthless. This says the same of a *citation*: a URL is the instrument, the document is the artefact, and a run that reports on the URL while claiming to report on the document has made #52's error with a link checker instead of a Python file.

## Corollaries

1. **The publisher's root is the first probe after a 404.** If the root is alive, the document probably is. If the root is dead too, the failure is a different kind and belongs in row 3 of the table above.
2. **Search by the headline, never by the slug.** The slug is the thing that changed. A title, an author and a date survive a CMS migration; a URL is the one part of a citation the publisher feels free to rewrite.
3. **A re-slug is not a correction and must not be recorded as one.** The prose is untouched; only the `sources[]` URL moves. A verdict that logs it as a content fix will send a later reader hunting for a change that never happened (#50's blast radius, pointed backwards).
4. **A dead-link hunt is a source-quality review.** Whatever replaces the link is re-ranked on #43's hierarchy against what is now available, not merely swapped in at the same tier. A blog post that dies into a published report should be allowed to.
5. **Our own link checker inherits this.** `qa_sources_alive.py` reports status codes and is right to — it is a *link* checker and it should not be taught to guess about documents. The interpretation layer is a human reading its output against this table, and the memo that does it is the artefact, not the tool's exit code. **Do not fix this by making the tool cleverer**; a tool that searches for replacements would start proposing them, and a proposed citation is a figure composed from a pattern (#41's second corollary).
6. **Conversely: prove the egress before reading any silence as a fact about the world** (#52). Today's re-probe ran four control fetches first, and one of them — a 403 from `unicef.org` — is the cleanest possible proof that "no content" and "no answer" are different events, because it is a server going to the trouble of refusing.

## Binding

- The Verifier's confirmation-read checklist gains a row: **for every non-200 source, which of the three signatures, and — if 404 — was the publisher searched for the document?** A 404 disposed of without a search is an open item, exactly like an untraced figure.
- `agents/growth/*-source-*-sweep.md` memos report the **signature**, not just the word *unreachable*.
- The Edition 05 flip checklist's Sierra Leone row is updated in the same commit as this ruling: the hard 404 is **closed**, with the live URL on file and the Final Learning Report routed to the Verifier as a candidate upgrade.

**Series: #1–#54, no gaps, no duplicates.**
