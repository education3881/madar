# Ruling #26 — A number you can *see* but cannot *quote* is not a citable figure

**Filed:** 2026-07-27 · **Origin:** the Netherlands doorstroomtoets Verifier pass (verdict `content-drafts/verdicts/2026-07-27-netherlands-doorstroomtoets-verification.md`). **Family:** sourcing method; the sibling of ruling #20 (*a 404 is an observation, not a verdict*).

## The situation
Trace-list item 1 asked the Verifier to either **bank** the exact 2026 revision-rate figure (recon flagged ~22.5% as unconfirmed) or **keep the qualitative form**. The exact number lives only in the PO-Raad *themarapportage* — `sectorrapportage.poraad.nl/p/Doorstroomtoets` — which is a **client-side (JavaScript) dashboard**: the fetch **redirect-cancelled**, and even had it resolved, the figure renders in-browser and is not present as quotable text in any served primary. The PO-Raad *news* primary confirmed the **direction** verbatim ("scholen stellen sindsdien veel vaker adviezen bij") but carried **no exact percentage**.

## The distinction (why this is not just #20)
Ruling #20 covers a source that is **walled or absent** — you cannot reach it, so you record the reach attempt as an observation and do not treat the gap as a finding. This case is one step further in: the source is **authoritative and reachable in principle, the number is real**, but it exists only as a **rendered value in a dashboard**, not as citable text. The temptation #20 does not address is the specific one here: *"I know the number is ~22.5%, I can practically see it — surely I can just state it."* No. **If you cannot quote it from a served text primary, it is not yet a citable figure**, however confident you are it exists.

## The rule
1. **A figure is citable only if it can be quoted, verbatim, from a served text primary** (HTML body, PDF text layer, a data file). A value that appears only inside a JS-rendered chart/dashboard is **not citable** until it is also published as text (release note, table, PDF) — treat the dashboard as an *observation that the number exists*, never as the citation.
2. **When the exact figure is un-quotable, keep the qualitative form and state the denominator** — as the Netherlands draft did ("about one in ten → around a quarter … share of all advices revised"). The direction is citable from the news primary; the precise level is not; the sentence carries exactly what is quotable and no more.
3. **Do not let recon confidence become draft precision.** Recon's "~22.5% (unconfirmed)" is a lead to chase, not a number to print. If the chase ends at a dashboard, the number stays out.

## The transferable test
Before any figure ships, ask: *can I paste the exact string I am citing out of a served text primary?* If the honest answer is "no — it's in a chart / behind rendering / I'm inferring it," the figure is not ready; downgrade to the qualitative claim the text primary does support. This closes the last gap between "the number is true" and "the number is cited," which is the gap Madār's whole sourcing posture exists to hold.

## Cross-refs
- Extends **#20** (a 404 is an observation, not a verdict) — walled source → this: rendered-but-unquotable source.
- Serves **figure-integrity axis 7 (Condition)** and the drafter≠verifier split: the Verifier is the last check that a printed number is *quotable*, not merely *believed*.
- INDEX: add to Section 2 (method rulings).
