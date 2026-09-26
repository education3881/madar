# Ruling #66 — inject the defect that shipped, not the bite you wrote

**Filed:** 2026-09-26 · **Daily run, QA lane** · **Section 1 row 61**
**Family:** assertion discipline (fifteenth member)
**Origin case:** the 2026-09-25 forward question, tested first, on six of the operation's own historical defects.

---

## The statement

**Ruling #35 requires a control and a bite. It does not say who may write the bite, and until today
the answer was always the same person: the run that wrote the assertion.** That run composes the
injection out of the defect it is already holding in mind — which makes the bite the strongest
possible test of *the defect we imagined*, and no test at all of *the defect class*.

**The probe, and it is cheap because the material is free:** the defects this operation has already
found and fixed are on the record with their shapes intact. **Re-inject each one into today's
artefact, exactly as it shipped, and ask whether the assertion that now exists for it still fires.**
Not the bite that was written for it — the thing that was actually served.

Two outcomes are useful and the second is the one worth the ruling. A check that fires has been
proved against an adversary it did not choose. A check that stays silent has just told you that the
defect it was written for can ship again.

## The evidence

Six real defects, each restored into a scratch copy of the 121-page build or of `social-drafts/`,
each injection **proved to have changed the artefact before the check ran on it** (the 2026-09-14
trap: a bite that does not change the file reads exactly like a passing control), each artefact
restored and the restoration verified by hash.

| | The defect, as it shipped | Stood | Assertion | Verdict |
|---|---|---|---|---|
| H1 | the Brazil caption rounded **49.3** to **49** | 90 days | `qa_packet_figures` | **CAUGHT** |
| H2 | the Issue 01 subject counted *"ten years"* Sierra Leone has not had | 115 days | `qa_packet_figures` | **BLIND** |
| H3 | `og:image` served as an SVG | 83 days | `qa_consumer_surface` | **CAUGHT** |
| H4 | the footer RSS link pointed at `/rss.xml`, off the base path | 83 days | *(three tried)* | **BLIND** |
| H5 | *Skip to content* in English on an Arabic page | 93 days | `qa_a11y_lang` | **CAUGHT** |
| H6 | a JSON-LD breadcrumb `item` pointing at a page not in `dist` | 19 days | `qa_jsonld` | **CAUGHT** |

**Four of six caught. Two blind, and they are blind for different reasons, which is why one probe was
worth more than six bites.**

**H2 is a bounded blindness and is fine.** `qa_packet_figures` reads numerals; *ten* is a word. The
check is correctly scoped and the gap belongs to the non-numeric family, where it already lives.
Recorded rather than fixed, because widening a numeral check to read number-words would make it worse
at the thing it is good at.

**H4 is a hole.** `qa_reachability`, `qa_body_links` and `qa_consumer_surface` were all run against it
and all three returned exit 0. The footer 404 that stood for 83 days across 35 QA passes, and that
earned a codified RUNBOOK rule on 2026-08-16, is catchable by nothing this operation owns. Each tool's
silence is correct in isolation — reachability asserts that pages are *arrived at* and a pointer at
nothing is simply not an edge; `qa_body_links` enumerates what an *article* promises; consumer-surface
reads metadata. **The defect falls in the gap between three correct scopes**, which is the one place a
composed bite will never look, because a composed bite is written by someone already looking at one
tool. Closed the same day as **standing assertion 25** (`qa_chrome_links`) and filed as **ruling #67**.

## Corollaries

1. **A composed bite proves the check against its author.** A historical bite proves it against the
   publication. Both are needed and only the second is adversarial.
2. **The probe is a regression suite the operation already paid for.** Every ruling with a defect
   behind it is a test case, and the test case is free — it is written down in the log that found it.
3. **A blind result is a finding, not a failure of the probe.** Two of six here, one bounded and one a
   hole, and the day's assertion came out of the hole.
4. **Prove the bite as carefully as the control** — unchanged from 2026-09-14, and it bound today:
   every injection above was hash-checked before and after, because the cheapest way to get a green
   from this probe is an injection that never landed.
5. **Run it against the defect's own artefact class.** Three of these six live in `dist`, two in
   `social-drafts/`, one in both. A probe that only re-injects into `dist` re-tests only the checks
   that read `dist` — and this operation's newest assertions do not.

## What it does not license

It does not retire #35. A control and a bite still gate every new assertion at the moment it is
written; the author's bite is what proves the check works at all. This ruling adds a **second, later
pass** whose material is history rather than imagination, and whose value is precisely that nobody
chose it.

And it says nothing about a defect this operation has **not** yet found. Four of six caught is a
statement about our own record, not about our coverage. The probe cannot generate a defect class; it
can only stop us from believing we are protected against the ones we have already paid for.

---

**Origin:** 2026-09-25 QA log, §5 — *"every bite this operation has ever run was composed by the run
that wrote the assertion, against the defect that run was already thinking about."* Tested 2026-09-26
before anything new was added, per the 2026-08-23 rule.
