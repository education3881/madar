# Staged workflow patch — the `verify` job's feed-validator step is a coin flip

**Filed:** 2026-09-24 · **Owner:** any hand holding `workflow` scope · **Issue:** #7
**Blocks:** a green deploy. The 2026-09-23 deploy is RED on this step and the
publication was never at fault.

---

## Why this file exists rather than the edit

`.github/workflows/**` is not writable by the autonomous run's identity. Re-probed
today on a scratch branch, and the refusal is verbatim what 09-14 and 09-20 recorded:

```
! [remote rejected] scratch/workflow-write-probe -> scratch/workflow-write-probe
  (refusing to allow a GitHub App to create or update workflow
   `.github/workflows/astro-pages.yml` without `workflows` permission)
```

Per the 2026-09-14 rule, the repair is written where the operation *can* write it,
and named. This is the **second** staged workflow repair (issue #7 carries the first).
What is new, and what changes the priority of issue #7: the first repair was an
*improvement* that could wait. This one repairs a gate that **is currently failing at
random**, which means every future run's state verification has to decide whether a red
deploy is real. That is the cost of leaving it.

## The defect

The step at `.github/workflows/astro-pages.yml:250` reads the ETag with one request and
revalidates with a second. The two requests land on independently chosen Fastly edges.
GitHub Pages unpacks each deploy onto more than one origin replica, and nginx mints
`ETag: "<hex-mtime>-<hex-size>"`, so the 09-23 artefact has **two permanent validators
per URL**, differing only in the mtime limb:

```
rss.xml      "6ab3a42c-7344"   "6ab3a42d-7344"
ar/rss.xml   "6ab3a42c-920e"   "6ab3a42d-920e"
                     ^ one second apart      ^ identical size
```

When the second request reaches the other replica, that edge has never seen the ETag it
was handed and a 200 is the only correct answer it can give. The step reads that as
"validator not honored" and fails the deploy. **It is a coin flip on every deploy, on
either feed** — green on 09-21 and 09-22 by luck. The two mtimes were still being served
23 hours later, so this is not propagation settling; it is permanent.

## The fix, in one sentence

Do what a polling reader actually does: **hold one connection, and revalidate on it.**
A TCP connection terminates at one edge, which holds one validator. Measured on the live
origin 2026-09-24 — 3 trials, 2 distinct validators across them, **304 every time**; and
16/16 with the replacement check at `agents/tools/qa_feed_validators.py`.

This is strictly *stronger* than the step it replaces: every revalidation must be honored,
not merely one of them. Ruling #63.

## The replacement step — paste over lines 250–266

```yaml
      - name: Feed cache validators work for a polling reader
        run: python3 agents/tools/qa_feed_validators.py --attempts 6
```

The reasoning, the measurements and the both-ways proof live in that tool's header, which
is the right home for them — the inline shell had none and could not have carried them.

## Also owed in the same edit — the non-gating list

`agents/tools/qa_feed_validators.py` reads the ORIGIN, so when it is *not* in the verify
job it does not gate, and the 2026-09-13 rule requires the reason be stated where the
others are listed. Once this patch lands it **does** gate (from `verify`, like the byte
compare), and the ratio returns to **22 of 24**. Until then it is **21 of 24**, and the
third ungated assertion's reason belongs beside `qa_live_drift`'s and
`qa_sources_alive`'s:

```
# qa_feed_validators — reads the ORIGIN, so it cannot run in the build job;
# it is the verify job's own step above (see agents/tools/patches/).
```

## Verification after applying

```bash
python3 agents/tools/qa_feed_validators.py --attempts 8   # expect exit 0
```

Then re-run `astro-pages.yml` and confirm `verify` is green.
