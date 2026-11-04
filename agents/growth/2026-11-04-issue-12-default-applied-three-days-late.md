# Growth — issue #12's stated default applied, three days late, and the ruler it broke on the way

**2026-11-04 · growth function · the action is an audience action in the only sense that matters for this
publication: it protects the re-openability of what we have already published.**

## What was done, and that it was owed

Founder **issue #12** — *may this operation ask a public archive to keep a copy of a public page we
already cite?* — carried a stated default: **if nobody replies by the weekly review of Sunday
2026-11-01, option B is applied** — the **23 named** registers submitted at five per run, the backlog
closed, and the standing question returning before any new URL is ever sent.

**Nobody replied, and the review did not apply it.** The 2026-11-01 weekly review listed the issue in
its founder-decision table as *"8 days · unchanged"* and moved on. That is the one failure mode the
operating instruction names in its own words: *a default is not a mandate; if a deadline passes in
silence, apply the default and say in the brief that you applied it, so a decision made by silence is
visible as one.* Carried as unchanged, a lapsed default becomes a third kind of thing — neither
answered nor applied — and that is worse than either, because the question stops being open without
anybody deciding it.

**Applied today, three days late. Said here and in brief 120.**

## The set, derived rather than remembered

B authorises **the 23 named**, and "named" had to mean something checkable. The issue was opened
2026-10-24; the register as it stood in that commit
(`fff32d8:agents/stats/claim-registers.json`, 342 rows) holds **exactly 23 rows in state
`live-only`** — archived nowhere, answering us at 200. That is the set, reconstructed from the artefact
rather than from the issue's prose, and the count agrees to the row.

**Two of the twenty-three are excluded, and the reason became today's ruling.** They are
`web.archive.org/web/…` URLs — pages we cite *through* a snapshot because the owner's copy had already
gone. Submitting a snapshot to Save Page Now is asking the archive to keep its own bytes. They scored
`live-only` because the availability API, asked *is there a snapshot of this URL*, correctly says no:
there is no snapshot of a snapshot. **So the two rows in the whole register that are archived by
construction sat in the state the claim-level join prices as single-copy risk** — the second instance of
ruling **#127**, found while assembling this batch, and the one that restates a published figure. #111
is quoted for *40 of 342 exist in exactly one copy*; the correct figure was **38**.

Twenty-one submittable, **five submitted**, in sorted order so the batch is reproducible and the next
run knows where to resume.

## What the archive did

| # | Register | Save Page Now | Verified |
|---|---|---|---|
| 1 | `almanassa.com/en/news/26936` | **200** | snapshot `20261104123338` serves 200; availability API now `archived: True · 2026-11-04` |
| 2 | `en.baochinhphu.vn/viet-nam-to-exempt-tuition-…` | `URLError` | not created |
| 3 | `files.eric.ed.gov/fulltext/ED673992.pdf` | `URLError` | not created |
| 4 | `github.com/Fab-Inc/FabMatch_SLE` | **200** | snapshot `20261104123841` serves 200; availability API now `archived: True · 2026-11-04` |
| 5 | `github.com/fergal-turner/2025_SCUK_SLEIC_Results` | `URLError` | not created |

**Two of five created, three declined, and the three are an observation about the archive and about us
rather than about those documents** — the same reading #111 insisted on when its first emit got 100
answers and then 242 consecutive 429s. They go back in the queue at the head of the next batch; nothing
is recorded as attempted-and-failed in the register, because a failed submission changes nothing about
the document's state.

**The two are verified twice**, deliberately, and neither verification is the submission's own receipt:
the snapshot URL the archive named in its `Content-Location` serves 200 to a plain `HEAD`, **and** the
availability API — the instrument this operation already uses to ask the question — now answers
`archived: True`. The register rows carry `caused_by_us: true`, which is the distinction issue #12's
option A asked for in writing: *records each one it caused as distinct from each one it found.*

**Register state after: `archived 291 · live-only 45 · walled-no-snapshot 14 · cited-as-archive 2 ·
GONE 1`**, over 353 cited registers. This morning it read `archived 289 · live-only 49 ·
walled-no-snapshot 14 · GONE 1`. Of the four-row move, **two rows are a real gain** (we caused two
documents to exist in two places) and **two rows are a ruler correction** (they always existed twice and
the ruler could not say so). *Those two halves must not be reported as one number, which is the whole
of #127.*

## What is NOT claimed, and the honest state of the bet

* **No traffic figure.** The site carries no third-party tracker by design. This action has no audience
  metric attached to it and inventing one would be the thing the CHARTER forbids.
* **The outcome is readable without anyone's permission**, which is why it qualifies as a bet under the
  CHARTER's own test: the availability API answers us, and `qa_claim_registers --emit` re-reads it on a
  schedule the operation controls.
* **19 of the 23 remain**, and at five a run with today's hit rate that is several runs. The backlog is
  not closed and saying it is would be the 2026-09-27 staged-patch defect in a growth note.

## And the ask is re-made, because B is now blocking a piece

Issue #12 gets a comment today rather than a fourth carry. The reason is concrete and arrived this
morning from the content function: **the Bahrain BQA draft's two figure-bearing registers are
single-copy and unarchived** — the `data.gov.bh` dataset carrying 23 of the piece's figures, and the
Annual Report 2025 PDF carrying the Gold Seals and a verbatim quotation. Both are new URLs. **B forbids
them by design**, and B was chosen narrow on purpose by the issue's own reasoning: *the run that already
overstepped should not inherit a standing authority as the consequence of having overstepped.* That
reasoning is still right, which is exactly why the run that wants the wider authority may not grant it
to itself — so it is asked, with a new stated default and a new date, and the piece ships or holds on
the Editor's disposition rather than on this.
