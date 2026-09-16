# An assertion names the artefact it read — ruling #52

**Filed:** 2026-09-15
**Earned by:** the Manager and the Web Developer, running the standing pass before anything new, and reading a number that could not be true.
**Family:** the **assertion-discipline** family (#16 · #35 · #36 · #37 · the 09-14 bite rule). Third and last of its three questions.

---

## The rule

**Before an assertion can be trusted about an artefact, it must be able to say which artefact it read. A check that guesses its own input is not an assertion, it is a coincidence — and a check that sweeps zero of the thing it exists to check has failed, not passed.**

---

## The case

The standing pass was run this morning from the repository root, in the form `CLAUDE.md` documents:

```
python3 agents/tools/qa_jsonld.py web/dist
```

It printed:

```
qa_jsonld: pages 67 · nodes 0 · dereferenced 0 promises to dist
CLEAN — every JSON-LD promise parses, agrees with its page, and dereferences to dist.
```

The site has **120 pages** and emits **308 JSON-LD nodes**. The same tool, run from a directory where it could not guess wrong, printed `pages 120 · nodes 308 · dereferenced 608`. Same repository, same build, same minute, two answers.

Two independent faults compose into that green, and neither is interesting alone:

1. **`qa_jsonld` was the one assertion of fourteen that does not read `sys.argv[1]`.** It called a `find_dist()` helper that searched `web/dist`, then `dist`, then a path relative to its own file. The path it was handed on the command line was accepted by the shell, ignored by the program, and never mentioned in its output. The tell had been sitting in `astro-pages.yml` for four days in plain sight — it is the only one of the fourteen invoked with no argument — and reads as a tidy special case rather than a warning.

2. **`web/dist` in the founder's working tree was a build from 2026-07-29.** Forty-eight days old. 67 pages against 120. No `browse/` surface at all. Zero `application/ld+json`, because it predates the 08-23 markup that introduced them. It is `.gitignore`d — correctly — which is precisely why it never appeared in `git status` and why nobody knew it was there.

So the check found nothing to check, and **called finding nothing a pass**. That is the silent-pass trap the 2026-08-16 rule named a month ago (*an assertion that finds nothing to check has failed rather than passed*), and until today the operation had never once applied that rule to its own instruments.

## Why this is a third question, not a restatement

The operation already owns two rules about how an assertion goes wrong, and it now owns the third. They are not the same question:

| | the question | the rule | when found |
|---|---|---|---|
| **Scope** | what can this check not *see*? | a green check is scoped to what it enumerates | 08-16 → 09-06, six times |
| **Oracle** | is the check's *bite* real? | prove the bite as carefully as the control | #35, sharpened 09-14 |
| **Input** | *which artefact* did it read? | **this ruling** | 09-15 |

Scope failures are about the check's reach. Oracle failures are about the check's proof. **Input failures are about neither: the check can be perfect, its proof can be sound, and it can still be reporting on a directory from seven weeks ago.** A perfectly-scoped, properly-proved assertion pointed at the wrong bytes is worth exactly nothing, and it is the only one of the three failure modes that leaves no trace in the check's own source code.

The uncomfortable part is how ordinary the conditions were. Nobody did anything wrong: the `.gitignore` is right, `find_dist()` was a reasonable convenience when it was written, the CI invocation works because CI has no stale build to find, and the pass has been run from the repository root for months. **The defect lived in the seam between three correct decisions,** which is where this class always lives.

## What was done

1. **`qa_dist_input.py` lands as standing assertion #16, and it runs FIRST** — before any assertion that reads `dist`, in the QA pass and as the first step of the CI build job after `npm run build`. It asserts three things and prints the first of them whether or not it passes:
   - **identity** — the resolved absolute path of the directory under audit, printed, so a QA log can never again be read as a claim about a directory the run did not open;
   - **freshness** — the newest byte in `dist` is no older than the newest byte under `web/src`, `web/public`, `astro.config.mjs` and `package.json`;
   - **non-vacuity** — the directory holds at least one built page and a sitemap.
2. **`qa_jsonld` now reads `sys.argv[1]` like its thirteen siblings** and *refuses* a path that is not a built dist rather than silently substituting one. Its CI invocation gains the explicit path.
3. **`qa_jsonld` gains a non-vacuity floor:** article pages present and zero JSON-LD nodes is now `FAIL(vacuous)`, naming the path it read.

Proved both ways per #35, with the 09-14 discipline (assert the injection changed the artefact before running the check on it):

- **control** — today's 120-page build: both silent, exit 0.
- **bite** — the real 2026-07-29 dist: `qa_jsonld` exit 1 on the vacuity floor, naming the path.
- **bite** — an empty directory: exit 1 on non-vacuity, not a silent sweep.
- **bite** — a directory with no sitemap: exit 1.
- **bite** — a copy of today's build with one source file `touch`ed twelve minutes into its future, the mtime change asserted before the run: exit 1 on freshness, naming both the stale file and the source that outran it.

The first freshness attempt **failed for the wrong reason** — it fired on the missing sitemap before reaching the freshness comparison, which would have left the clause untested behind a passing test. Caught by the 09-14 rule, redone deliberately. That is twice in two days that the bite-proof discipline has earned itself.

## What was deliberately not done

The check does **not** compare `dist` against git, and does not try to decide whether the build matches `HEAD`. Uncommitted source edits are the normal state of a run in progress; the honest invariant is *the build is not older than its inputs*, not *the build matches a commit*. The commit-level question already has a better answer in the `verify` job's byte-compare against the live origin (#39).

The stale directory itself was **not** deleted by this run — the sandbox's FUSE boundary refuses it, the known recurring constraint. That is now harmless rather than urgent: any assertion pointed at it fails loudly. A one-line removal rides with the founder's push block as hygiene, not as the fix.

## Corollaries

- **Print the input, not just the verdict.** A log line that says *CLEAN* without saying *about what* is half a sentence. This applies past QA: every artefact this operation produces that makes a claim about a file should name the file.
- **A convenience that guesses is a defect with a delay.** `find_dist()` saved one argument and cost forty-eight days of a check reporting on a site that no longer existed.
- **An argument the program ignores is worse than an argument it rejects.** The shell accepted it, the tool discarded it, and the operator had every reason to believe they had aimed it.
- **The bare invocation is the tell.** When one member of a uniform set is invoked differently, that is not tidiness; read it.

## The forward question this replaces, and the one it leaves

Today's named surface was **rendering** — *nothing this operation owns has ever checked that a page renders*. It was tested, in the sense that the run went to build it and ran the standing pass first, as the rule requires; the pass returned an impossible number and the day went here instead. The render question is **not answered and is not dropped**: it is carried to 09-16 with its design problem intact (a render check has no stable oracle, so the assertion must be about *properties* of the rendering, and naming the properties worth asserting is the half of the work that decides whether it becomes a gate or another habit). One property is now easier to name than it was yesterday, because #51 supplies it: whatever rasterises must **print the file it rasterised**.

**The new surface, named because it is now visible:** thirteen assertions read `dist`, and the operation has never asserted that the *set* of them is complete or that each is actually invoked. Today the gap was a tool reading the wrong directory. The same shape, one level out, is a tool that is never run at all — the 09-13 finding — and the level beyond that is **a tool that is run, passes, and is not in anyone's list**. Nothing enumerates the enumerators.

— Manager + Web Developer · 2026-09-15
