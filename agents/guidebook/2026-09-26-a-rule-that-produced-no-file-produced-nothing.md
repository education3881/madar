# Ruling #67 — a rule that names an assertion and produces no file has produced nothing

**Filed:** 2026-09-26 · **Daily run, QA lane** · **Section 1 row 62**
**Family:** assertion discipline (sixteenth member)
**Origin case:** the 2026-08-16 chrome-link sweep, re-tested 41 days later against the defect it was written to prevent.

---

## The statement

**The 2026-09-13 rule counted the assertions this operation owns and asked which of them were wired
into CI.** Twelve files, seven gating, five running only when a human remembered them — and wiring
three of the five found defects on first contact. It is a good rule and it has one blind spot, which
is the shape of every enumeration ruling in this register: **it can only ask about a file that
exists.**

**An assertion that was codified as a rule, executed once by hand, recorded as the action of record,
and never written to disk is invisible to it.** It is not in the count. It cannot drift out of the
count. No weekly review will ever print a ratio that notices it. The defect it exists to prevent is
exactly as free to ship as it was before the rule was written — and the rule's existence is what makes
nobody look.

**So: a rule that names an assertion has not delivered the assertion. The deliverable is the file.**
Where a rule prescribes a check, the same commit that codifies it either lands the tool or states in
the rule why there is no tool — and "we ran it by hand and it was clean" is a reading, not a check.

## The evidence

On **2026-08-16** the weekly review found the footer's RSS link had pointed at `/rss.xml` — off the
`/madar` base path, a hard 404 — in the footer of **every page, in both languages, since the first
publish on 2026-05-25. Eighty-three days and thirty-five QA passes.** The rule codified that day is
unambiguous:

> "the QA pass enumerates every `href`/`src` emitted by `Base.astro`, `SiteHeader.astro`,
> `SiteFooter.astro` and any layout-level component, and asserts each resolves in `dist`"

It was executed the next morning by hand — 98 unique targets across seven pages, zero unresolved — and
that reading was written into the 08-17 log as the rule running green on its first day. **It never
became a file.** Forty-one days later the defect was re-injected exactly as it shipped (`"/madar/rss.xml"`
→ `"/rss.xml"`, two occurrences on the English home, injection hash-verified), and the three assertions
that plausibly cover it were run:

```
qa_reachability      control=0  bite=0   BLIND
qa_body_links        control=0  bite=0   BLIND
qa_consumer_surface  control=0  bite=0   BLIND
```

**Nothing we own catches it.** And each silence is correct: `qa_reachability` asserts that every page is
*arrived at*, and a pointer at nothing produces no orphan because it is not an edge; `qa_body_links`
enumerates an **article's** promises; `qa_consumer_surface` reads the metadata surfaces. Three correct
scopes with a hole between them, and a rule sitting over the hole.

**The sibling case makes it a class rather than an incident.** The 2026-08-17 orphan sweep — *is every
served page pointed at?* — became `qa_reachability`, a real file, wired, proved both ways. The 08-16
chrome sweep — *does every pointer resolve?* — is its exact mirror and became prose. **Two halves of
one enumeration were codified one day apart and only one was built**, and the half that was built is
the half that did not already feel finished, because the chrome sweep had a clean hand-run to point at.
**A hand-run that comes back green is the most effective way to stop an assertion being written.**

## Action of record — and this time the phrase means a file

`agents/tools/qa_chrome_links.py`, **standing assertion 25**, landed the same run. Proved three ways
per #35, and the bite is the historical defect rather than a composed one (#66): control exit 0 on the
real 121-page build; bite 1 the restored footer link, exit 1, both occurrences named as off-base rather
than as missing; bite 2 a chrome stylesheet repointed at a hash the build does not emit, exit 1; bite 3
the 2026-08-16 silent-pass trap, run against a directory with no HTML, exit 2. Wired into `postbuild`
in `web/package.json` in the same commit, because this identity cannot write `.github/workflows/**`,
and declared to `qa_census` so its population reconciles against the corpus like every other
instrument. **25 assertions, 22 gating.**

It also prints the **chrome set by name** — the targets carried by ≥95% of served pages, `/madar/rss.xml`
among them. A report that says *0 unresolved of 4,755* does not tell its reader the footer was
enumerated, and the whole history of this defect is a report that did not say what it had read.

## Corollaries

1. **"Action of record" is a claim about an artefact.** If the record names no path, nothing was
   delivered. Write the path.
2. **A clean hand-run is evidence about one morning.** It is never evidence about the rule, and it is
   the strongest available argument for not writing the tool.
3. **Count what does not exist.** A weekly ratio over the files in `agents/tools/` cannot find this
   class. The only instrument that can is re-reading the rules for the checks they promised — which is
   what #66's probe does from the other end, by re-injecting the defect and watching nothing happen.
4. **Where a rule genuinely should not produce a file, say so in the rule** — the same discipline the
   2026-09-13 rule already imposes on an assertion kept out of CI.

---

**Origin:** the 2026-09-25 forward question, tested 2026-09-26. The probe was looking for checks that
fail to catch their own defects; it found a defect with no check at all, behind a rule that had been
green for 41 days.
