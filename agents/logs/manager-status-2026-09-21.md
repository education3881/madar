# Manager status — 2026-09-21 (Monday, Asia/Dubai)

**State at open:** tree clean, `HEAD == origin/main == 0e7c1e9`, live origin serving it. No dark
day. The 09-20 deploy that Sunday's review predicted would go red **went green**, so the entire
weekly review is served and nothing is waiting.

## Shipped

- **Edition 05 row 5 is a pair.** `2026-09-19-egypt-baccalaureate-published-first` composed in
  Arabic and gated the same run — Arabic Editor **PASS**, held. Title 38/100, dek 149/200, measured
  at compose. **Numeral multiset 39/39, zero one-sided figures either way** — the edition's first
  pair clean in both directions.
- **One finding from the crossing, and it changed the English.** The EN draft's *"the 120-year-old
  examination"* is struck in both languages, with no number replacing it. Nothing we read says 120;
  the nearest served registers give 1887 (139 years) and are press, not documents. Fifth
  consecutive non-numeric finding in this edition; second found by a language crossing.
- **Ruling #59** — *a comparator with no locale asks the machine* — filed, with the register range,
  the §3 heading and its own Section 1 row reconciled in the same commit (the 09-20 rule). §3 now
  reads 1→59, verified no gaps, no duplicates.
- **Two repairs and two assertion extensions**, each proved control and bite: the browse index's
  tie-break no longer asks the environment (build output byte-identical, which is the control), and
  nine Arabic pages stop printing their dates in Western digits after seven days (not identical —
  it is a repair). Assertion 20 now covers 38 browse pages; `qa_ar_language` now covers 116 listing
  dates and bit on the real defect.
- **Growth:** the browse surface after the wave flip, computed before the flip. One new page per
  language, nothing lost, no URL changed, EN and AR identical.

## Held, and why

- **The whole Edition 05 wave.** Five slugs, ten files, still `approved: false`. Row 5 now owes the
  Editor's five-test pair verdict and then the Verifier's. Rows 1–4 still owe their confirmation
  reads and the two clock items the weekly review found.
- **Nothing was flipped and nothing was rushed toward the 10-11 gate target.** Twenty days left,
  and the order of sacrifice stated on 09-13 is unchanged: the date gives, the verdicts do not.

## Queued

1. **Editor's five-test pair verdict on row 5** — the next lane, and the only thing standing
   between Egypt and the verification queue.
2. **Verifier's verdict on row 5**, the run after.
3. **Rwanda re-verification** — row 6, unclaimed for eight days, released to any run on Sunday.
4. **Tomorrow's forward question, tested before anything new:** every date here is a bare
   `YYYY-MM-DD` parsed as midnight UTC on a UTC runner for a Dubai publication. Does any surface
   disagree with the file about which day a piece was published?
5. **Two patches still unappliable by this identity** (`.github/workflows/**`): the feed-check
   retry, and the gate-register comment.

## Not done, and named

- `qa_sources_alive --sample 0` did not run to completion; a 14-URL sample of the held set did, all
  200. Sixth day this P1 is carried. It is still the last step before the flip commit and still the
  only unbounded one.
- The output-bounded `lastmod` manifest is **owed for the fifth time**. Today gave it a second
  witness: `qa_live_drift` reported the origin clean at a moment when nine pages in `dist`
  differed from it by design.

Corpus unchanged at **38 EN / 38 AR**. No approved flips. **Fifty-fifth consecutive day without a
published piece** — and the held set's Arabic side is complete for the first time.
