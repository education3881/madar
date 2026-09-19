# Ruling #57 — equal counts are not an agreement

**Filed:** 2026-09-19 · **Status:** binding · **Section 1, row 52**
**Earned on:** three instruments printing the number **120** about three different sets of
120 pages, on a healthy build, with every arithmetic identity between them true.

---

## The rule

**A count is a claim about a set. Two different sets of the same size are
indistinguishable from their counts alone — so the equality of two cardinalities is not
evidence that two instruments agree about anything. Where two checks' populations must
stand in a relation, the relation is asserted BY NAME — element for element, with every
difference declared and every declared difference required to exist — and never by
arithmetic.**

Stated as the failure it prevents: a page can be dropped from the sitemap and a different
page added to it in the same commit, and every number this operation prints will be
unchanged.

---

## How it was found

The forward question had been carried unanswered for three runs (09-16, 09-17, 09-18):
*nothing compares the assertions' counts to one another — eight numbers, already emitted
by eight instruments, that must agree within known offsets and have never been read
together.* Asked deliberately today, per the 08-23 rule, it failed on first contact —
and **not in the direction the question anticipated.**

The arithmetic was fine. Every identity held: 121 served pages against 120 sitemap URLs,
differing by one; 62 English and 59 Arabic summing to 121; 59 clusters doubled plus two
no-alternate pages exhausting the sitemap's 120; 76 approved article pages being twice
the 38 approved slugs. Nothing to report.

Underneath it:

| instrument | prints | the set it means |
|---|---|---|
| `qa_lastmod` | **120** | the sitemap's `<loc>` set = served − {404} |
| `qa_jsonld` | **120** | `dist/**/index.html` = served − {404} |
| `qa_consumer_surface` | **120** | every `*.html` except VALENCE = served − {valence} |

Each exclusion is deliberate, stated in its own file, and **correct**. There is no defect
in any of the three. The defect is that the QA log has been printing them in one grid, on
one line, as one number — and no reader of that grid, including the next run and
including the weekly review, could tell that the first two columns and the third disagree
about which pages exist.

This is the 2026-08-17 orphan lesson arriving from the opposite side. There, a difference
of exactly one (82 pages against 81 sitemap URLs) stood for nine days because **nothing
compared the counts**. Here the counts compare perfectly and **the sets do not**. Equal
cardinalities are not an agreement; they are the absence of one particular disagreement.

---

## Corollaries

**1. A count carries the name of its set, or it is a number and not a count.**
Found on the census's first run: `qa_dist_input` printed `120 built page(s)` for a `dist`
containing **121** built pages, because it enumerated `index.html` and the branded 404 is
not one. Harmless to the freshness test it exists for, and wrong in the log, which is
where the number is actually consumed. Corrected in the same commit.

**2. An exemption is asserted in BOTH directions.**
`served − sitemap` must equal the declared not-routed set exactly: anything undeclared in
that difference is a defect, **and** anything declared that the build does not serve is
also a defect. An exemption list nobody checks is where defects hide (`qa_reachability`'s
own rule, now applied to the census's own list).

**3. An invariant that has held for every case so far is still an assumption — do not
divide by it.** The census derived "held slugs" as `len(held files) // 2`, because every
piece in this corpus has always had an Arabic twin. It bit on the first build where that
was false: today's Egypt draft is English-only until its Arabic is composed, so nine held
files are **five** held slugs and the halving said four. `qa_held_assets` was right and
the new instrument was wrong. **Dividing by an invariant is how an assumption gets welded
into an instrument**, where it is no longer visible as one.

**4. A meta-instrument reads the number the instrument PRINTS, not the number it
computes.** The printed line is the artefact a human, a QA log and the next run consume.
A tool that computes correctly and prints a mislabelled number is a real defect class,
and only a reader of stdout catches it — corollary 1 is the proof that this is not a
theoretical distinction.

**5. An assertion's answer must not depend on who called it.**
Two of the eleven siblings (`qa_body_links`, `qa_held_assets`) resolve the content
collection as the relative path `web/src/content`, so from `web/` — which is exactly where
`postbuild` runs — they look for `web/web/src/content` and exit 2 and 1. Latent for weeks
only because the workflow has always invoked them from the repository root. The census was
the first caller to invoke them from anywhere else and found it immediately. The fix is
for the caller to **name** the environment it judges in rather than inherit one: #16 (verify
in the judging environment) turned around and pointed at the caller.

---

## Family placement

The enumeration family, one turn further in. Its questions so far:

- *What can this check not see?* (08-16 → 09-06)
- *Is its bite real?* (#35, 09-14)
- *Which artefact did it read?* (#52)
- *At which layer?* (#55)
- *Which question did it actually answer?* (#56)
- **Which set did it count?** (this)

Nearest sibling is **#56**, filed yesterday, and the two are the same shape seen from
either end. #56 says an instrument that cannot name the *question it answered* looks like
it answered yours. #57 says an instrument that cannot name the *set it counted* looks like
it agrees with its neighbour. Both failures are invisible precisely because the output is
well formed.

Also kin to **#51** (*a claim inherits the scope of its register*) with the register being
one of our own tools: a number inherits the scope of the enumeration that produced it, and
reporting it beside a number of different scope narrows neither and misleads about both.

---

## Binding on the operation

1. **Standing assertion 19, `qa_census.py`**, landed and gated today. It derives every
   population independently from `dist` and the content collection, asserts the set
   relations by name, and compares each instrument's printed number against the population
   that instrument declares it means. Proved both ways per #35 — control clean on the real
   build; bites on an orphan page, on a `<loc>` swapped for another (every cardinality
   unchanged), on a printed number altered without a behaviour change, and on a pattern
   that matches nothing.
2. **The QA log stops printing a grid of bare numbers.** Where counts are reported side by
   side, each carries the name of its set, or the census's own summary line is quoted
   instead of a hand-assembled table.
3. **A new assertion states its population in its own output**, in words, not only its
   size — so the next instrument that must agree with it has something to agree with.

---

## The limit, stated because it is real

The census compares populations the operation can derive from its own artefacts. It cannot
tell whether a population is the *right* population — that is each instrument's own job,
proved separately. And it reads stdout, so it is coupled to the wording of eleven other
files: a sibling that rephrases its report breaks the census loudly, by design, because a
number it cannot find is a failure rather than a pass. That cost is the price of checking
the printed artefact rather than a private return value, and it is paid deliberately.
