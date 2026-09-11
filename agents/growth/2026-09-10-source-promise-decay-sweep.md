# Growth — the source-promise decay sweep, first run

**Filed:** 2026-09-10 · Growth, with the Verifier · Tool: `agents/tools/qa_sources_alive.py` (new, **not** a deploy gate)

## The argument, before the numbers

Every check this operation owns asks whether a link is **rendered**. `qa_body_links` (#10) proves that every `sources[].url` an article declares is emitted as an anchor on its built page — and stops there. Nothing has ever asked whether the thing at the other end still answers.

That gap sits on top of the publication's only differentiator. Madār's argument for being worth returning to is that every figure stands on a named primary source the reader can open. When a source link rots, the piece does not degrade slightly — its central promise turns into a 404 **in front of the one reader who cared enough to click**. That reader is, by definition, the returning reader. This is a return-rate instrument, not a traffic one, and it is measured in promises kept, not visits.

It is also the check with the shortest shelf life we have. The Sudan re-verification (08-31) found **two of seven registers changed serving state in eighteen days**, with **zero figures going false**. Serving state drifts faster than facts, and always in the direction the reader experiences.

## First run — scope: the Edition 05 held pairs only

Deliberate scope. The three held pairs are exactly where a source problem is still **free** to fix: before the wave gate, before a URL is on the origin.

**28 distinct source URLs across Zambia, Sierra Leone and Sudan. Twenty answered. Eight did not.**

| Bucket | n | Reading |
|---|---|---|
| `ok` (200) | 20 | promise kept |
| `unreachable` | 4 | all four `parliament.gov.zm` — reachable at compose (08-23/08-25) |
| `walled` (403) | 3 | bot walls, not deaths — two are UNICEF pages this operation fetched successfully **today** through a different client |
| `error` (404) | **1** | **a genuinely dead source on a held piece** |

### The one that matters

```
HTTP 404  https://www.savethechildren.org.uk/blogs/2026/the-results-are-out-sierra-leone-education-innovation-challenge
cited by: 2026-08-28-sierra-leone-sleic-outcomes [en] + [ar]
```

The Save the Children blog — the *green provider* register, the one whose unnamed provider the 08-28 OPM read identified as Lot 3, Rising Academy. It served on 28 August. It 404s on 10 September, **thirteen days later, and thirteen days before the earliest plausible flip.** Had the wave shipped on schedule with nothing checking this, Sierra Leone would have gone live carrying a dead link to the source behind one of its most-quoted paragraphs — and no assertion we own would have said a word, because the anchor renders perfectly.

Routed to the Editor for the confirmation read: the figures it carried are all independently anchored in the OPM evaluation (read in full 08-28), so **nothing in the piece falls**. The decision is whether to supersede the URL with a first-party register or carry it as fetched-on-date (#41). Recommendation: supersede — a 404 in a `sources[]` list is worse than no entry, because it advertises the failure.

### The four Zambia parliament links

All four `parliament.gov.zm` URLs — two node pages, the Bill PDF, the ministerial statement PDF — failed at the transport layer, not with a status code. That is one host, not four sources, and could be an outage, a TLS change or a block. **Per #20 this is not yet rot**: it was probed twice (HEAD then GET) in one sitting, which is one sitting. It goes on the confirmation read's list to be probed again on a different day from a different client before any editorial move. If it holds, the Bill text is the piece's spine and needs a durable register.

### The three walls

`tandfonline.com` (the Brown et al. trial), and two `unicef.org` pages. The UNICEF pair is the instructive one: **this operation read both of them successfully today, in this same run, through a different client.** A 403 is a statement about who is asking, not about whether the source exists — which is why the tool buckets it separately and refuses to call it dead. Naming the disagreement rather than resolving it is #38's habit applied to reachability.

## What ships from this

1. **`qa_sources_alive.py` is a weekly sampled sweep, never a deploy gate.** The far side belongs to UNESCO, UNICEF, ministries and journals; a GPE outage at 09:00 must not stop us publishing. It exits non-zero only when the sweep itself is broken — including when it finds zero URLs to check (the 08-16 silent-pass trap).
2. **It runs on the held set before every wave gate**, and on a 60-URL sample of the live corpus weekly. The full corpus carries ~570 promises; sending all of them at institutional hosts on a schedule is rude and unnecessary.
3. **Buckets, not a pass/fail.** `ok` / `walled` / `unreachable` / `error` — because "we cannot see it" and "it is gone" are different facts and only one of them is an editorial problem.

## The honest traffic line

The site carries no third-party tracker by design, so this memo claims no visitor numbers and none exist. What it claims is a count of promises: **28 checked, 20 kept, 1 broken, 7 unresolved.** That is the only audience metric this operation can honestly produce, and it happens to be the one that predicts whether a reader comes back.

— Growth · 2026-09-10
