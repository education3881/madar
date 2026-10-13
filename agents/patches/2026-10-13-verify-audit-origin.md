# Staged workflow patch — the published oracle has no auditor in the one job that can be one

**Filed:** 2026-10-13 · **Owner:** any hand holding `workflow` scope · **Issue:** #7
**Blocks:** nothing red. It blocks the only check that can tell us whether `served-manifest.json`
describes the bytes the origin is actually serving — the file every later answer rebases on.

---

## Why this file exists rather than the edit

`.github/workflows/**` is not writable by the autonomous run's identity; the refusal is recorded in
this directory's README and in the 09-14 rule, clause 4. This is the **fifth** staged workflow item
and issue #7 carries the credential question for all of them. This file states **no count** —
`qa_patch_queue` derives the register from its three real homes, so nothing here can go stale (#75).

## What landed today without a patch

`qa_served_manifest.py --audit-origin` (standing-queue item 7, raised 2026-10-06, four
displacements, reached the head today by the three-displacement clause with nothing to weigh).

It fetches the manifest the **origin** publishes and checks every claim in it against **the origin's
own bytes** — `pages`, `unrouted` and `assets`, each re-fetched and re-hashed by the same code that
wrote the claim. Proved eleven ways with the bite first, on loopback copies of `dist`. First live
run: **256 of 256 claims clean**, which is the first time the whole file has ever been checked
against the thing it is a description of. The hand-run of 2026-10-12 covered 120 of 216 entries;
today's manifest claims 256, of which **136 — every font, still, share card, stylesheet and script a
page loads — had never been verified by anything.**

## Why `verify` is the RIGHT home here, and the build job is the wrong one

This is the exact mirror of the 2026-10-06 patch, and the pair is worth reading together.

`--check` asks *did a page change between deploys?* — so `verify` is the **wrong** home, because
there origin == artifact by construction and the manifest would be compared against itself.

`--audit-origin` asks *does the published manifest describe the published bytes?* — and
"origin == artifact" is precisely the identity being asserted. The only moment it can be asked about
**this** run's artefact is **after `deploy-pages`, in the `verify` job.**

At `postbuild` time the origin still holds the previous deploy, so a failure there would be a
statement about a tree this build is already replacing: it would red the wrong run.

## The step

Add to `.github/workflows/astro-pages.yml`, in the `verify` job, after the existing byte-compare:

```yaml
      # The oracle's auditor (2026-10-13, standing-queue item 7). The verify job
      # byte-compares six files of ~284. served-manifest.json fingerprints all of
      # them and is published beside them, so auditing it against the origin turns
      # a 2.1% bridge into a full one for the cost of one fetch per entry.
      #
      # It runs HERE and not in the build job for the reason that is the mirror of
      # the --check patch: --check asks a question ACROSS deploys, so origin ==
      # artifact makes verify the wrong home; --audit-origin asks whether the
      # published manifest describes the published bytes, and origin == artifact is
      # the identity it exists to assert.
      #
      # Exit 3 (no manifest at the origin yet) is tolerated: the first deploy
      # carrying the tool publishes the file and there is nothing to audit before
      # it. Exit 1 (the oracle disagrees with the bytes) and exit 2 (an entry could
      # not be read twice) both red the deploy.
      - name: the published manifest describes the published bytes
        working-directory: .
        run: |
          python3 agents/tools/qa_served_manifest.py web/dist --audit-origin --budget 600 \
            || [ $? -eq 3 ]
```

## What it costs and what it must not become

One HTTPS GET per claimed entry, sequential, under a wall-clock ceiling (#88). On today's corpus
that is 256 reads in well under the budget. **Entries that fail are re-probed once before being
called unserved, and the recovery count is printed** — the first live run flagged one page that
`curl` then served 200 three times in a row, so a single probe is not a measurement (#91), and an
auditor that reds a deploy on one dropped socket is an auditor somebody switches off within a week.

It must not grow into a second `verify`: it asserts that the *oracle* is true, not that the deploy
landed. The byte-compare answers the second question and stays.
