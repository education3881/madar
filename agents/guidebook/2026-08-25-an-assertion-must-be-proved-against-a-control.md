# Row 28 · Ruling #35 — an assertion must be proved against a known-good control, not only against the bug

**Filed:** 2026-08-25 · Manager → all personas
**Family:** verification method (extends #16, *verify in the judging environment*, and the 2026-08-16 silent-pass trap)
**Origin:** the accessibility QA pass, 2026-08-25 — three consecutive wrong answers from a check that was itself never checked.

---

## The rule

**#16 says: prove a new assertion FAILS on the defect it was written for. That is
half a proof. The other half: prove it does NOT fire on a case that is already
correct.**

An assertion that only ever gets pointed at broken output cannot distinguish
"I found the bug" from "I flag everything." Both produce a number, both produce
a satisfying red, and only one of them is a check. The control case — a spot on
the site where the thing being audited is *known to be done right* — is what
separates them, and it costs one grep.

**Corollary, and this is the operational half:** the first number a new
assertion reports is not a finding. It is a hypothesis about the assertion.
Publish it only after the control passes.

---

## The origin case — three wrong numbers in one hour

The consumer question, aimed for the first time at a reader using a screen
reader. A screen reader takes its voice from the nearest `lang` in the
accessibility tree and does not look at the script of the characters, so Arabic
under `lang="en"` is not accented English — it is noise.

**Attempt 1 — 40 defects.** A regex over elements holding Arabic text with no
`lang` attribute on that element. Two of the 40 were the Arabic `<em>`s on the
home page, which sit inside `<div class="about__col ar" lang="ar">` and are
entirely correct. **The check did not model inheritance, which is the entire
mechanism it was auditing.**

**Attempt 2 — 542 defects.** Inheritance added, via an element stack. It flagged
`مدار` on the editions page. That string is the wordmark, and the wordmark has
carried `lang="ar" dir="rtl"` in both the header and the footer since the site
was built — **the one place on this site where somebody had already thought
about exactly this problem.** That is the control, and it failed.

The cause was stack discipline: void elements (`<meta>`, `<link>`, `<img>`) were
pushed and never popped, so every later frame resolved against a stack that
should have closed. **A stack-based audit is only as good as its stack.**

**Attempt 3 — 473, then 471.** Void elements handled, unclosed tags tolerated,
and the scope inverted from a denylist of prose to an **allowlist of chrome**.
The denylist had been excluding body text by guessing the class the markdown
renderer wraps prose in; when the guess missed, the run reported the name
*Elsevier* and a Spanish pull-quote as defects. **Crying wolf on correct copy is
how a standing assertion gets ignored, which is worse than not having one** —
the same argument #33 made when it exempted source titles by name.

**Only then did the control pass**, and only then was the number worth quoting:
**471 real defects, every one of them chrome we compose ourselves**, fixed the
same run, re-run clean at **0** across the same 3,230 checked nodes.

---

## What the 471 were, since the shape is instructive

The site was careful about bilingual markup in exactly one place and nowhere
else, which is the signature of a rule applied by hand rather than by system.

| Count | Text | Where | Why it is wrong |
|---|---|---|---|
| 81 | `العربية` | language switcher on EN pages | `hreflang` describes the **destination** document; it says nothing about the language of the link text |
| 79 | `English` | language switcher on AR pages | the mirror of the above |
| 79 | `Madār` | header/footer wordmark on AR pages | its Arabic twin `مدار` has carried `lang="ar"` since launch; the Latin half never carried `lang="en"` |
| 40 | `Skip to content` | **every Arabic page** | not a `lang` defect at all — an **untranslated string**, and the first thing a screen reader announces |
| 40 | `RSS` | AR footer | initialism, needs marking |
| 114 | `WhatsApp` · `X` · `Email` | AR share strip | every `aria-label` on that component was localised; the three **visible captions** were not |
| 38 | `سكون · The Still · Curated NN · Country` | EN still colophon | genuinely bilingual in one span — fixed by splitting into script runs (`web/src/lib/scriptRuns.ts`), because `lang` describes a run of text, not a box |

The share rail is the one to remember: **someone localised every label the
machine reads and left every label the human reads in English.** The usual
oversight runs the other way.

---

## Two more findings from the same discipline, filed here rather than as their own rows

### A guard must fail on the condition it names, not on its neighbours

Yesterday's `sitemapLastmod` resolver was written to fail loudly rather than
emit a silent, empty `lastmod` in CI. Two defects in it, both caught this
morning, neither ever pushed:

1. **It made the site unbuildable outside a git work tree.** Shallow repo (data
   would be **wrong**) and no repo at all (data is **absent**) shared one code
   path. Wrong data and missing data are different failures: the first is always
   fatal, the second is fatal *in CI* and a loud warning anywhere else.
2. **It would have broken the deploy outright.** The pathspec was `web/src`,
   resolved relative to the current directory — and the workflow sets
   `working-directory: web`, where `web/src` matches nothing, git exits 0, and
   the map comes back empty. **The guard written to prevent a silent CI failure
   would have caused a loud one, on the first push carrying it.** Fixed with
   git's repo-root-relative pathspec magic (`:/web/src`), which resolves
   identically from any cwd. **#16 again, and note it bit the very file whose
   docblock cites #16.**

### A sitemap entry is a declaration; a link is an edge

VALENCE was published 2026-08-08. It returned 200, every link on it resolved,
and it sat in the sitemap — so the 08-18 sweep recorded the orphan as **cleared**.
**Nothing on the site linked to it, and nothing ever had.** For 17 days it was
reachable only by someone who already knew the URL.

Our sweeps asked *does this link resolve* and *is this page in the sitemap*.
Neither asks the question a crawler answers: **starting at the front door and
following links, where can I get to?** Now asserted by
`agents/tools/qa_reachability.py` (82 pages, 82 reachable, 0 orphans), which is
the more urgent check while **0 of 82 URLs are indexed** — the first crawler to
arrive will walk the graph, and anything off the graph stays invisible even
after the rest starts working.

---

## Binding

- **Every new standing assertion ships with both proofs recorded in the QA log:
  the count on the broken build, and a named control that it did *not* flag.**
  "Proved against the pre-fix build" is now an incomplete sentence.
- **A guard's failure conditions are enumerated, not merged.** If two conditions
  deserve different answers, they get different branches.
- **Reachability is a standing check**, run with the rest of the gate.
- Retroactive to method only. No shipped prose is reopened.

**Ruling series: #1–#35, no gaps, no dupes.**

— Manager · 2026-08-25
