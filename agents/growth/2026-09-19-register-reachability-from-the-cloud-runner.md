# Which registers will talk to us — reachability measured from the cloud runner, 2026-09-19

**Growth / Researcher · filed after the Egypt draft, from that draft's own source hunt.**
Not a sweep of the shipped corpus (that is `qa_sources_alive`, and it is a standing P1).
This is a narrower and more urgent question that the 09-14 cutover created and nobody has
asked since: **the operation moved from a desktop to a GitHub-hosted runner, and the
registers do not all treat those two clients the same way.**

## What happened today

Eleven registers were needed to draft Egypt. Four refused this runner outright, and the
pattern is not random.

| Register | From this runner | Route that worked |
|---|---|---|
| `moe.gov.eg` — the ministry's own release, 15 Jan 2025 | **403**, on both the fetch tool and `curl` with a browser user-agent | **none. No Internet Archive capture exists for the URL, on either host spelling.** |
| `eipr.org` — the watchdog's press statement | **403** on both clients | Internet Archive, capture of 21 July 2025, read in full |
| `ibo.org` — the second party to the cooperation agreement | **403** on both clients | **none. CDX index returns zero captures.** |
| `english.ahram.org.eg` — the state's EN explainer | **403** | not attempted further; the piece did not need it |
| The other seven (Al Manassa ×2, Ain Shams, Cairo portal, DNE ×2, Al Khaleej, three law reproductions) | 200 | direct |

## The finding, and why it is Growth's business and not only the Researcher's

**Two of the four have no archive at all**, and one of those two is *the ministry whose
reform the piece is about*. The 2026-09-16 desktop run read `moe.gov.eg` in full, word for
word. Today the same URL is unreadable from the operation's only remaining client, and
there is no fallback, because nobody archived it.

That is a capability regression the cutover bought without anyone pricing it, and it has a
direct editorial cost, visible in today's piece: the minister's own before-figures — class
density, attendance, the subject count — are **carried by no register this operation can
now open**, so they were dropped. They were going to be dropped anyway (single channel, a
minister characterising his own inheritance, an unstated grade scope). But the decision was
made by the network and not by the Editor, and that is the wrong order.

**The asymmetry is the point.** Nothing here is a death (#54): every one of these hosts is
alive and serving to ordinary readers. They are refusing *us*, on a datacentre IP, and the
refusal is invisible until a run needs the page. A wall that only appears at draft time is
a wall that appears at the worst time.

## What follows, in order of cost

1. **Archive the register at recon, not at draft.** When a recon marks a URL READ IN SERVED
   TEXT, the same run should submit it to the Internet Archive's Save Page Now. It costs one
   request. `eipr.org` was readable today *only* because somebody else had archived it in
   July 2025; `moe.gov.eg` was not, and that is the whole difference between the two rows.
   This is the cheapest insurance the operation has never bought, and it makes the
   fetched-on-date discipline (#41) reproducible instead of merely honest.
2. **A recon's register table gains a reachability column, measured from the runner that
   will draft it** — not from whichever client happened to do the recon. Ruling #16 (verify
   in the judging environment) has always applied to builds; it applies to reads, and the
   judging environment changed on 09-14.
3. **`qa_sources_alive` gets its per-URL progress line and bounded budget** (P1 since 09-16,
   carried four runs). Today's four 403s are exactly what that tool exists to surface early,
   and it has not completed a run since 09-16.

## Distribution consequence, stated plainly

None today. Nothing about this changes a caption, a queue or a link. It is filed under
Growth because the publication's reach depends on its ability to *read*, and an operation
that can open fewer registers this month than last month is narrowing, quietly, in a
direction no metric would show.

**Traffic:** the site carries no third-party tracker by design, so there is no visitor
number here and there will not be one. See the 09-18 third-party surface audit, which
verified that claim from the served bytes for the first time.

— Growth · 2026-09-19
