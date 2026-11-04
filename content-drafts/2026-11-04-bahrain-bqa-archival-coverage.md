# Bahrain BQA — the archival coverage read, and the flag consequence it creates

**Content function · 2026-11-04 · run by the Manager with the Verifier's instruction open.**
Subject: `content-drafts/drafts/2026-10-23-bahrain-bqa-five-cycles`, the only draft in the pipeline.
Instruction of record: `content-drafts/verdicts/2026-11-03-bahrain-bqa-five-cycles-verification.md`
§5 item 5 and hand-off line 5 of the draft — *"Registers with no archival snapshot: **UNKNOWN of 5** —
OPEN, and it blocks the flag, not the verdict (#111). The Verifier runs `qa_claim_registers --emit`
over these five before the flag moves, and any figure resting on an unarchived single register is
double-sourced or dropped."*

**UNKNOWN of 5 is now 3 of 5, and the two that matter cannot be fixed by this operation today.**

---

## 1 · Why `--emit` could not be run, and what was run instead

`qa_claim_registers --emit` reads the **corpus** — `read_corpus()` walks
`web/src/content/articles*/` and the Bahrain piece is not there, because `approved: false` means it is
not in the corpus by design (#18, and the four standing assertions that enforce it). Running `--emit`
would have returned the 354 registers already on file and said nothing about these five. *An
instrument scoped to the published set cannot answer a question about a held piece* — which is the
same shape as `qa_pair_frontmatter` being the second gate not handed `dist` (#81), and it is the
reason that gate exists.

So the five were asked **by the instrument's own functions**, imported rather than reimplemented:
`qa_claim_registers.archive_state()`, then `origin_state()`, then `classify()`, at the tool's own
4-second spacing. The method is #111's method exactly; only the input set is different. Nothing was
written to `agents/stats/claim-registers.json`, because that file is the register of the **published**
corpus and the piece has not shipped — the row arrives when the flag moves.

## 2 · What came back

| # | Register | What it carries | `archived` | Snapshot | Origin to us | `classify()` |
|---|---|---|---|---|---|---|
| 1 | `data.gov.bh/explore/dataset/01-results-of-government-schools-reviews-1/` | **the spine** — 1,022 rows, 882 reviews, 140 monitoring, the four grade totals, the five cycle rows | **False** | — | 200 | `live-only` |
| 2 | `bqa.gov.bh/.../2026/06/Annual-report-2025-.pdf` | the Gold Seals — 22 government and 7 private, *"for outstanding performance"* quoted verbatim | **False** | — | 200 | `live-only` |
| 3 | `bqa.gov.bh/.../2025/09/Performance-Report-24-25-EN.pdf` | academic year 2024-25, the batch of 76 government schools | True | **2026-07-17** | 200 | `archived` |
| 4 | `bqa.gov.bh/open-data/` | *one of seven datasets the Authority publishes* — described, not quoted | True | **2026-01-18** | 200 | `archived` |
| 5 | `education3881.github.io/madar/articles/2026-05-26-bahrain-bqa-public-grades/` | **ours** — the predecessor's closing question, quoted verbatim with its date | **False** | — | 200 | `live-only` |

**3 of 5 hold no snapshot anywhere. All five answer 200 to us right now**, so nothing here is rot and
nothing is walled — this is the `live-only` row of #111's four-row table, which is the row that is
*fine today and unrecoverable tomorrow*.

## 3 · The flag consequence, and it is editorial rather than technical

Row 5 is not a risk and is dealt with first so it does not pad the number: **it is our own page.** If
`education3881.github.io` stopped serving it tomorrow the quoted closing question would still be
re-openable by anybody, from this repository's git history, which is public. A claim resting on our own
served bytes has a second copy by construction. *(That the classifier cannot say so is a finding in its
own right and is today's research increment, not this note's subject.)*

Rows 1 and 2 are the live ones, and the Verifier's rule applies to both:

* **Row 1 is the piece.** Twenty-three of the draft's figures come off that CSV. It was read three
  times from the same 183 KB export and once, on 2026-11-03, from a **different serialisation** of the
  same dataset — the English-labelled semicolon export, 72,925 bytes, counted by an independently
  written counter, 23 of 23 agreeing. That answered a real question (*is this a stable register or a
  stable parse of one?*) and it **does not answer this one**: two serialisations of one dataset on one
  host are one copy. If `data.gov.bh` withdraws that dataset, every figure in the piece's distribution
  table becomes unfalsifiable by anybody, us included — the Morocco shape (#100, #111) with a larger
  surface.
* **Row 2 carries two figures and one quotation.** `22` and `7` Gold Seals and *"for outstanding
  performance"*. The quotation is also what `qa_citation_identity` (#112) will compare once the piece
  is in the corpus, and a quotation whose only register is a single unarchived PDF is the exact state
  #112 was built to find after the fact.

**Neither can be archived by this operation today.** Founder **issue #12** asked whether this operation
may ask a public archive to keep a page it already cites; its stated default — *option B, the 23 named
registers only, and the standing question returns before any new URL is ever sent* — fell due at the
**weekly review of Sunday 2026-11-01**, which recorded the issue as *"8 days, unchanged"* and **did not
apply it**. Today's growth function applies it, three days late, and says so. **B is the narrow option,
and these two URLs are new, so B forbids them.** That is not a loophole to be read around: the default
was chosen narrow on purpose, by the issue's own reasoning, and the run that wants the wider authority
is the run least entitled to grant it to itself.

## 4 · What is therefore owed before the flag, restated

The Verifier's §5 list stands, with item 5 now specified rather than unknown:

1. **Arabic composition**, carrying the live park condition and hedge 1 in its corrected form. *Still
   the long pole, and it is the next run's content function.*
2. **Arabic Editor's gate**, with the `named humans — gender read from register: 0 of 0` line.
3. **Hero still and og card.**
4. **The `edition:` field** — founder issue **#13**, default **2026-11-08**, not yet arrived.
5. **~~Archival coverage: UNKNOWN of 5~~ → 3 of 5 unarchived, of which 2 are somebody else's and
   single-copy.** The disposition is one of three and it is the **Editor's**, not the Manager's:
   **(a)** double-source rows 1 and 2 against a second register before the flag; **(b)** ship them as
   they are, with the single-copy state recorded in the publish gate as an accepted risk; or **(c)**
   drop the figures that rest on them, which for row 1 is the piece. **The recommendation from this
   desk is (b) with a narrowed ask**, because (a) does not exist — the Authority is the only publisher
   of its own review grades, and a second register for a sovereign regulator's own dataset is a thing
   that cannot be found by looking harder — and (c) prices a hosting decision as an editorial one.
   **And (b) is only honest if the ask is re-made**, which is why issue #12 gets a comment today with a
   new stated default and a new date rather than a third carry.

*Nothing in this note moves the flag. `approved: false` stands, and it now stands four things away
rather than five, with the fifth specified instead of unknown.*

---

**Signed** · Manager, content function · 2026-11-04 · five registers asked by the instrument's own
functions at its own spacing; three hold no snapshot; the two that bear figures cannot be archived under
the default this operation applied today, and the disposition is named and routed to the Editor.
