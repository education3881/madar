# QA log — 2026-09-15

**Build:** route-around (`/tmp` working copy with the repo's own `.git` beside it, so the
`lastmod` resolver runs against real git history per ruling #16). `CI=true`,
session-unique vite cache. **Exit 0 · 120 pages · 3.81s.**
**Held-asset hook:** withheld 8 assets for 4 held pieces — a held piece contributes no bytes.
**Dist under audit:** `/tmp/madar-build-2/web/dist` — and for the first time, that sentence is
asserted rather than assumed. See §1.

---

## 1. The forward question was asked, and the answer came from underneath it

The 09-14 log named **rendering** as the surface for today: *nothing this operation owns has
ever checked that a page renders.* Per the 08-23 rule the run tested it before adding anything
new — which begins with running the standing pass, and the standing pass returned a number that
could not be true:

```
qa_jsonld: pages 67 · nodes 0 · dereferenced 0 promises to dist
CLEAN — every JSON-LD promise parses, agrees with its page, and dereferences to dist.
```

The site has **120 pages** and emits **308 JSON-LD nodes**. Two faults compose into that green:

1. **`qa_jsonld` was the one assertion of fourteen that ignores `sys.argv[1]`.** It called
   `find_dist()`, which searched `web/dist`, then `dist`, then a path relative to its own file.
   The path handed to it was accepted by the shell and discarded by the program. The tell has
   been in `astro-pages.yml` since 09-11 — it is the only one of the set invoked with no
   argument — and reads as tidiness rather than warning.
2. **`web/dist` in the working tree was a build from 2026-07-29.** 48 days old. 67 pages. No
   `browse/`. Zero `application/ld+json`, because it predates the 08-23 markup. `.gitignore`d,
   correctly, which is exactly why it never appeared in `git status`.

So the check found nothing to check and **called finding nothing a pass** — the silent-pass trap
the 08-16 rule named, applied for the first time to our own instruments.

**Reproduced deliberately before fixing anything:** same tool, same repository, same build,
same minute, two answers — `pages 67 · nodes 0` from the repo root, `pages 120 · nodes 308`
from a directory where it could not guess wrong.

### Filed as ruling #52 — *an assertion names the artefact it read*

Third question in the assertion-discipline family, and genuinely a third:

| | question | rule | found |
|---|---|---|---|
| scope | what can it not *see*? | a green check is scoped to what it enumerates | 08-16 → 09-06 |
| oracle | is the *bite* real? | prove the bite as carefully as the control | #35, 09-14 |
| **input** | **which artefact did it read?** | **#51** | **today** |

A perfectly-scoped, properly-proved assertion pointed at the wrong bytes is worth nothing, and
it is the only one of the three that leaves no trace in the check's own source.

### Fixed, and gated

- **`qa_dist_input.py` lands as standing assertion #16** and runs **first** — in the pass and as
  the first step of the CI build job after `npm run build`. Three clauses: **identity** (prints
  the resolved absolute path, pass or fail), **freshness** (the newest byte in `dist` is no older
  than the newest byte under `web/src`, `web/public`, `astro.config.mjs`, `package.json`),
  **non-vacuity** (at least one built page and a sitemap).
- **`qa_jsonld` reads `sys.argv[1]`** like its thirteen siblings and *refuses* a path that is not
  a built dist rather than substituting one. Its CI invocation gains the explicit path.
- **`qa_jsonld` gains a non-vacuity floor:** article pages present and zero nodes is now
  `FAIL(vacuous)`, naming the path it read.

**Proved both ways (#35), with the 09-14 discipline — the injection asserted to have changed the
artefact before the check ran on it:**

| | case | expected | result |
|---|---|---|---|
| control | today's 120-page build, both tools | silent | **exit 0** ✓ |
| bite | the real 2026-07-29 dist → `qa_jsonld` | vacuity | **exit 1**, names the path ✓ |
| bite | empty directory → `qa_jsonld` | refuse | **exit 1** ✓ |
| bite | empty directory → `qa_dist_input` | non-vacuity | **exit 1** ✓ |
| bite | directory with no sitemap | not a build | **exit 1** ✓ |
| bite | today's build, one source file `touch`ed 12 min into its future (mtime change asserted first) | freshness | **exit 1**, names stale file and the source that outran it ✓ |

The first freshness attempt **fired for the wrong reason** — it hit the missing-sitemap clause
before reaching the freshness comparison, which would have left that clause untested behind a
passing test. Caught by the 09-14 rule and redone deliberately. Second day running that the
bite-proof discipline has paid for itself.

**Not done:** the stale directory itself could not be deleted — the sandbox FUSE boundary
refused it, the known recurring constraint. That is now hygiene rather than urgency, because any
assertion pointed at it fails loudly; a one-line `rm -rf web/dist` rides with the push block.

---

## 2. Standing pass — 14 of 14 clean, against a dist proved to be today's

| # | assertion | result |
|---|---|---|
| 14 | `qa_dist_input` **(new)** | PASS — path printed; 120 pages; newest built 09:14:43 ≥ newest source 09:13:31 |
| 1 | `qa_robots` | PASS — 1 Sitemap line, derived, target exists, 0 Disallow |
| 2 | `qa_hreflang_clusters` | PASS — 120 sitemap URLs / 121 pages / 59 clusters / 2 named no-alternate |
| 3 | `qa_body_links` | PASS — every rail and sources promise rendered; twin rails equal; no dead ends |
| 4 | `qa_lastmod` | PASS — 120 URLs, 120 lastmod, newest ≤ ceiling; no held date leaks |
| 5 | `qa_held_assets` | PASS — 4 held slugs contribute no bytes; 76 approved control assets all served |
| 6 | `qa_reachability` | PASS — 0 orphans; `/404.html` exempt by named allowlist |
| 7 | `qa_jsonld` | PASS — **120 pages · 308 nodes · 608 promises · 306 in-document @id** |
| 8 | `qa_a11y_lang` | PASS — 121 pages, 5,027 text nodes, 0 defects |
| 9 | `qa_ar_language` | PASS — 59 Arabic pages, 328 chrome fields, 0 Latin controlled vocabulary |
| 10 | `qa_consumer_surface` | PASS — og:locale/type/site_name, raster og:image, sitemap lastmod, print block |
| 11 | `qa_geo_fields` | PASS — 84 pieces (42 EN / 42 AR); 2 declare `countries`; both held, correctly skipped |
| 12 | `qa_css_tokens` | PASS — every custom property defined, fallback'd, or runtime-set |
| 13 | `qa_live_drift` *(non-gating by design)* | **CLEAN — origin matches dist: 120 URLs, 0 lastmod drift, 4 sampled heads identical** |

`qa_live_drift` is the one that answers the state question: **the live origin is current with
`cc44be9`.** The founder's 09-14 push deployed (run #79, 52s), and the 09-14 cloud-run work —
the browse surface and the `--color-accent` fix — is served. Independently confirmed by fetching
`/browse/topic/ai-readiness/` from the origin: 6 pieces listed, rails resolving, canonical and
hreflang correct.

**Note on the count, since the log should carry it:** 13 assertions gate the deploy (12 as build
steps in `astro-pages.yml`, 1 — `qa_css_tokens` — as `postbuild` in `web/package.json`, because
the cloud identity is refused write access to `.github/workflows/**`). `qa_live_drift` and
`qa_sources_alive` stay out for stated reasons carried in the workflow file. **13 of 15.**

---

## 3. A parser fragility found on the way past, recorded not fixed

The Growth audit's first pass reported **37** approved English pieces where every other
instrument says **38**. Chased rather than rounded. Cause: the audit script split frontmatter on
the literal string `---`, and `2026-07-07-netherlands-doorstroomtoets.md` carries a source URL
containing `…schooljaar-2025---2026-vastgesteld`. The split truncated the frontmatter at
character 3,185 and the file's `approved: true` fell outside it.

**No content defect and no site defect** — Astro parses YAML properly and the piece is live and
correct. Recorded because it is #51's own shape one level down: *a tool that silently reads
something other than what it was pointed at.* Binding note for any future analysis script:
frontmatter ends at the first `---` **on a line of its own**, never at the first occurrence of
the string. The audit was re-run with a line-anchored parser and every figure in the Growth memo
comes from that run.

---

## 4. Publish gate — run in writing

| gate | state |
|---|---|
| Editor verdict on file | ✓ `verdicts/2026-09-15-africa-best-system-ruler-pair.md` — FAIL-1, fixed in-run, **BANKED** |
| Arabic gate | ✓ 09-14, PASS (two register questions routed to the Arabic Editor in today's verdict §4) |
| Verifier verdict | **✗ — owed. Scheduled for the next run.** The flip cannot happen without it (#18) |
| hero still + og card on disk | ✓ both, both correctly withheld from dist |
| `astro build` clean | ✓ exit 0, 120 pages |
| AR full pass | ✓ parity 38/38; `qa_ar_language` clean |
| **Ships editorially?** | **NO.** Corpus unchanged at 38 EN / 38 AR, 35 countries, **no approved flips.** |

All four Edition 05 pairs remain held and **mutually rail-bound** — they flip atomically, and the
three reciprocal `related:` edges into row 4 must be added in the same commit as the flip or
`qa_body_links` fails the build on a dead end.

---

## 5. Forward question (required per the 08-23 ruling) — for the 2026-09-16 run

**The render question is carried, not dropped.** It was asked today in the order the rule
requires and the standing pass answered with something underneath it. It keeps its design
problem intact: *a render check has no stable oracle* — a screenshot diff fails on every
legitimate edit, so the assertion must be about **properties** of the rendering, and naming the
properties worth asserting is the half of the work that decides whether it becomes a gate or
another habit. Today adds one property to the list for free: whatever rasterises must **print the
file it rasterised** (#51).

**The new surface, named because today made it visible: nothing enumerates the enumerators.**

The operation owns fifteen assertion scripts. Today one of them was reading a directory from
seven weeks ago and saying CLEAN. On 09-13 five of twelve were found not to run at all. On 09-11
one had existed for thirteen days without ever being wired. Three findings, three months, one
shape: **the set of checks is itself an artefact nobody checks.** There is no list that is known
to be complete, nothing asserts that every file in `agents/tools/qa_*.py` is invoked somewhere,
and nothing asserts that a check named in the QA log actually ran. The candidate is small and
mechanical — derive the tool list from the directory (never hand-maintain it, per 2026-06-07),
assert every tool is either a CI step, a `postbuild` step, or carries a stated reason for being
out, and have the pass emit a manifest of *tool → exit code → dist path read* that the log quotes
rather than the run summarising. The open question, and the reason this is a question: **a
manifest is a claim too, and the thing that writes it is inside the system it describes.**

— Manager + Web Developer · 2026-09-15
