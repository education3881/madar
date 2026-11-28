# Publish gate — `2026-11-27-saudi-pisa-2025-two-clocks-disagree` · cell 8 · 2026-11-28

**Edition 06's SIXTH piece, which is the founder directive's floor reached, eight days before the
edition's window closes.**

## First: the hold of 2026-11-27 is LIFTED, and its premise is why

Yesterday's run held this piece at cell 8 on purpose and wrote the reasoning into the ledger so today's
run would not re-decide it. **The reasoning is quoted here and then measured, because that is the only
honest way to lift it:**

> today's floor is already met by the UAE ship, Ed06 stands at 5 of 6 with nine days of window, and **the
> only other row in flight is Uzbekistan at cell 4 — five cells from the flag, with the Verifier
> structurally a run behind the pair verdict, so no run tomorrow could ship it.** Flipping Saudi today
> would meet a floor that is already met and break tomorrow's.

**Every clause of that is now false, and three of them were falsified by the content run that wrote it,
within the same run.** Uzbekistan did not stay at cell 4: the same run took it to cells 5 and 7, and this
run closed its cell 6. Uruguay did not stay at cell 1: the same run took it to cell 7, and this run closed
its cell 6 too. **Both other rows are at 7 of 8.** So the guarantee the hold was buying — a piece one cell
from the flag for tomorrow — is now bought twice over, and holding a third would be hoarding it.

**This is not a re-decision; it is the recorded decision applied to the state it names.** The ledger rule
is that a run does not re-take a recorded judgment, and the judgment recorded was conditional on a board
that moved three hours after it was written. The plan's own default governs the rest: **each piece ships
the day its own gate closes**, and this gate closed this morning.

**And the day is covered three deep after this flip**: Uzbekistan for 2026-11-29, Uruguay for 2026-11-30,
in an order the corpus fixes rather than the Manager choosing — each of their `related:` rails names a
slug that must already be approved.

## A. The eight cells

| Cell | Artefact | Date |
|---|---|---|
| 1 Editor's brief | `content-drafts/briefs/2026-11-27-saudi-pisa-2025-two-clocks-disagree-brief.md` | 2026-11-27 |
| 2 EN draft | `content-drafts/drafts/2026-11-27-saudi-pisa-2025-two-clocks-disagree.md` | 2026-11-27 |
| 3 Editor's five-test verdict | `content-drafts/verdicts/2026-11-27-saudi-pisa-2025-two-clocks-disagree.md` — **PASS** | 2026-11-27 |
| 4 AR composition | `content-drafts/drafts/2026-11-27-saudi-pisa-2025-two-clocks-disagree-ar.md` | 2026-11-27 |
| 5 Arabic Editor's gate | `content-drafts/verdicts/ar/2026-11-27-saudi-pisa-2025-two-clocks-disagree-arabic-gate.md` — **APPROVED** | 2026-11-27 |
| 6 Verifier | `content-drafts/verdicts/2026-11-28-saudi-pisa-2025-two-clocks-disagree-verification.md` — **VERIFIED**, two corrections applied in-run | 2026-11-28 |
| 7 Still + og card | `web/public/stills/` and `web/public/og/` | 2026-11-27 |
| 8 The flag | **this document** | 2026-11-28 |

## B. The five standing checks

1. **Editor and Arabic verdicts on file** — yes, both, with the Verifier's between them.
2. **Hero still and share card on disk** — yes, and now *served* rather than withheld.
3. **`astro build` clean with the flags already flipped** — run **before** this commit was written, which
   is the binding rule the UAE flip earned yesterday, *because the gates that matter at cell 8 cannot see
   cell 7.* It earned its keep immediately: see §D.
4. **Assertions green** — 40 of 43, including the twelve build-job gates run locally out of the workflow
   file.
5. **Held-slug leak** — the invariant inverts at a flip (the 2026-08-09 rule). Asserted both ways:
   `qa_pair_frontmatter` reads **54 pairs, 52 approved, 2 held** (was 51/3), and `qa_held_assets` is CLEAN
   on the two that remain — so the flipped piece contributes bytes and the two still held contribute none.

## C. The rail step, and the displacement question is ANSWERED BY DECLINING IT

The 2026-11-27 amendment is binding: at cell 8 the forward edges are derived from the piece's **own final
`related:`**, not from cell 1's list. Four slugs, so four reciprocal edges were owed. **Three were written,
in both collections — six file edits — and the fourth was DECLINED:**

| Older piece | Rails before | After | Note |
|---|---|---|---|
| `2026-11-26-qatar-pisa-2025-two-of-three` | 5 | **6** | at the convention's cap |
| `2026-11-27-thailand-pisa-2025-fourth-list` | 4 | **5** | under |
| `2026-11-26-jordan-pisa-2025-counts-from-2022` | 5 | **6** | at the convention's cap |
| `2026-11-26-pisa-2025-three-lists-of-risers` | **6** | **6** | **DECLINED — no edge written** |

**Why declined rather than granted or displaced.** The edition's opener reached six rails on yesterday's
UAE flip, and that gate handed the question forward in writing with a reason this run accepts: *answering
it inside a flip commit would be a rail policy invented at the one moment nobody can review it.* There are
three defensible answers — give the hub a seventh because a hub's degree is a function of its edition's
size and not of a reader's patience; displace its oldest edge; or leave it — and **choosing between them
is a policy, not a gate step.** The weekly review runs **tomorrow, 2026-11-29**, which is the shortest
possible wait for the right desk.

**What the decline costs, stated rather than hidden:** a reader on the edition's opener has no link to
this piece. The reverse edge exists — this piece points at the opener — so the pair is connected in one
direction, and the opener is reachable from both home pages and both editions pages anyway. **The cost is
one inbound path on one piece for one day.** Recorded because an omission nobody writes down is how a
convention becomes a silent rule.

## D. What the flip-time build found — THREE gates, not yesterday's two, and the class is now measured

The build ran three times before it exited 0, and each failure was the same structural fact arriving
through a different instrument. **Yesterday's UAE flip red two gates; this one red three, and the third
was the expensive one.**

| Order | Gate | What it said | Cleared by |
|---|---|---|---|
| 1 | `qa_claim_registers --check` | **3 cited registers with no archive row** — the two self-citations to the Qatar pair and `etec.gov.sa/en/home` | the network `--emit` half, which is what it is for. Now **384 cited registers with a dated observation**, `archived 308 · live-only 53 · walled-no-snapshot 10 · ours-git-archived 10 · cited-as-archive 2 · GONE 1` |
| 2 | `qa_citation_identity --check` | **2 registers supplying a quoted identity token with no row** — the same two self-citations | its own `--emit` |
| 3 | `qa_annotation_figures` | **26 annotation quantities** neither printed in a body nor carrying a provenance | **thirteen rows written BY HAND**, as #114 requires, each naming where the figure was read from. The tool never seeds its own register |

**All three are blind to a held piece by construction, so a flip is the first moment any of them is asked
anything about it.** That is the 2026-08-09 inversion rule reached from the far side, now with a number
on it: *an assertion scoped to a corpus state must be re-derived when the state changes* — and these three
did not change scope, **they acquired a subject.** The 2026-11-27 rule *build once with the flags already
flipped before writing the flip commit* was followed and earned its keep three times over in one
afternoon.

**And the thirteen hand-written rows say something about the class worth recording.** Not one of them is a
figure about education. They are **two capture-timestamp minute fields (16, 51), one HTTP status (403),
three byte counts of archive objects (2,426,000 · 2,544,478 · 1,614,913), one table label the tokeniser
read as a decimal (2.3), three comma-split fragments of OECD table rows, and three ruling numbers (86 ·
134 · 161)**. The provenance apparatus ruling #161 requires — timestamp, object, hash — is itself made of
digits, so **the more rigorously a piece documents where its figures came from, the more work it hands to
the gate that checks figures.** That is not an argument against either; it is the reason this cell costs
what it costs, and it was 40 quantities yesterday and 26 today.

## E. What ships

**"Saudi Arabia's reading, up five and down eighteen"** · `2026-11-27-saudi-pisa-2025-two-clocks-disagree`
· EN dek 195/200, AR dek 167/200, `edition: 6` · the two clocks disagreeing in sign on reading alone, with
the chapter's fourteen tables parsed and the count upheld against a text sweep that returned thirteen.
Verification reproduced **the full-report hash for the fourth independent time** and 27 of 27 spans
verbatim in two independent captures each after its two repairs.

**Served and verified in this run, in `dist`, before the commit:** EN page 66,314 bytes, AR page 77,887
bytes, still 3,405 bytes, og card 1,598 bytes, **both URLs in the sitemap** with reciprocal hreflang, and
**three entries in each feed**. `qa_held_assets` now reads **2 held slugs, 52 approved**.

**Edition 06: 6 of 6. The floor, met on 2026-11-28, with eight days of window left and two pieces one cell
from the flag.** Today therefore served **two** pieces — the UAE piece this run unblocked, and this one.
