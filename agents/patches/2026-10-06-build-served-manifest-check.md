# Staged workflow patch — the served-bytes manifest's CHECK half has no gated home

**Filed:** 2026-10-06 · **Owner:** any hand holding `workflow` scope · **Issue:** #7
**Blocks:** nothing red. It blocks the only direction of the `<lastmod>` contract that
no gate in this operation can currently observe.

---

## Why this file exists rather than the edit

`.github/workflows/**` is not writable by the autonomous run's identity — the refusal is
recorded verbatim in this directory's README and in the 09-14 rule, clause 4. The repair is
therefore written where the operation *can* write it, and named in the day's brief. This is
the **fourth** staged workflow item; issue #7 carries the credential question for all of them.

## What landed today without a patch, and what did not

`qa_served_manifest.py` emits a per-URL manifest of the served bytes into `dist`, and that
half **is** gated — it is the last entry in `web/package.json`'s `postbuild`, and `qa_census`
asserts its routed-page count against the sitemap's own `<loc>` set, so a manifest that
quietly stops describing some pages fails the build instead of narrowing in silence. The
published artefact is the memory; that part needs no workflow write.

The half with no home is `--check`: fetch the manifest the origin is **currently** serving
and compare this build against it, so that a page whose rendered content changed without its
`<lastmod>` moving fails loudly.

## Why the `verify` job is the wrong home, which is the part worth reading

The obvious home is wrong, and it is wrong for a structural reason rather than a
configuration one. `verify` downloads the exact artifact `deploy-pages` published and
byte-compares it against the origin. By the time it runs, **origin == artifact by
construction**, so a manifest comparison there compares the manifest against itself. It
would pass forever. That is a check in the wrong home — which is standing-queue item 1's
entire subject, and it would have been filed as a fifth gating assertion with no way to fail.

The question is *across* deploys. The only moment it can be asked is in the **build job,
after `npm run build`, while the origin still serves the previous deploy** — before this
build replaces it.

## The step

Add to `.github/workflows/astro-pages.yml`, in the `build` job, immediately after
`- run: npm run build` and before the `qa_dist_input` step:

```yaml
      # The output-bounded half of the <lastmod> contract (2026-10-06, ruling #89,
      # standing-queue item 2 — raised 2026-09-06, named twelve times). Every other
      # instrument derives "did this page change" from SOURCE PROVENANCE: git history
      # over CONTENT_DIRS and CHROME_GLOBS. The truth lives in the served bytes.
      # qa_lastmod bounds dates from ABOVE (no date newer than its ceiling). This
      # bounds the other direction: a page whose rendered content changed and whose
      # date says it did not. Measured, not argued — one character in
      # design-assets/wordmark/madar-wordmark.svg, which three build-time readers
      # inline into every page and which is in NEITHER CHROME_GLOBS nor the
      # resolver's git pathspec, changes what 117 served pages say and moves zero
      # dates.
      #
      # It runs HERE and not in `verify`: verify compares the artifact it just
      # published against the origin, so origin == artifact by construction and the
      # manifest would be compared against itself — a check in the wrong home,
      # passing forever. Here, the origin still serves the PREVIOUS deploy, which is
      # the only baseline that makes the question answerable.
      #
      # Exit 3 (no baseline yet at the origin) is tolerated deliberately: the first
      # deploy carrying the tool seeds the baseline and has nothing to compare
      # against. Exit 1 (silent content change) and exit 2 (failure to check) both
      # red the build. `|| [ $? -eq 3 ]` is the whole of that tolerance and it
      # disappears on its own after one deploy.
      - name: every page whose rendered content changed says so in its date
        working-directory: .
        run: |
          python3 agents/tools/qa_served_manifest.py web/dist --check --budget 300 \
            || [ $? -eq 3 ]
```

## Why it is not simply gated from `postbuild` like its emit half

Two reasons, and the second is the load-bearing one.

- It reads the **origin**. A briefly unreachable github.io must not red a deploy, and must
  never be downgraded to a pass either — which is what exit 2 is for. The workflow already
  takes exactly this stance on `qa_live_drift`, and says so where the others are listed.
- **Its counts are a function of deploy latency, not of the commit.** On a staged-but-
  undeployed morning the origin's manifest is older than `HEAD`, so the comparison spans
  several commits and the presentation-only and unbacked-date counts describe the *gap*
  rather than the *change*. That is exactly right for a daily measurement and wrong for a
  gate. Inside the `build` job of a deploy run, the gap is one deploy by construction, which
  is the only condition under which those counts mean what they say.

Both halves of that argument are in the tool's own header, at the point a reader meets the
code, per the 09-13 rule's clause 2.

## Until it lands

The check is **hand-run in every daily run** and its three counts are recorded in the QA
log. That is the 09-13 defect by name — *a hand-run assertion is a habit, not a gate* — and
it is carried here deliberately, with a staged patch rather than a promise, because the
alternative is a check with no home at all. **If this patch is still here at a weekly review,
the right question is not "re-run it by hand again" but "why does issue #7 still have no
answer".**

## This file carries no numeric claim about the gate register

Deliberately, per ruling #75. The register lives in three real homes — `agents/tools/`,
this workflow's build steps, and `web/package.json`'s `postbuild` — and is derived by
`python3 agents/tools/qa_patch_queue.py .`. A count copied into a fourth file, least of all
into a file this identity cannot then correct, is the defect that rule exists to stop. The
figures quoted above (117 pages, zero dates) are measurements of a probe, not claims about
the register, and `qa_patch_queue` reads this file on every build.
