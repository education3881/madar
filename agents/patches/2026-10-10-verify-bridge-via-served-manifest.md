# Staged workflow patch — the dist-to-origin bridge is six files wide and the wide instrument is already published

**Filed:** 2026-10-10 · **Owner:** any hand holding `workflow` scope · **Issue:** #7
**Blocks:** nothing red. It blocks the only thing that promotes 29 gating assertions'
conclusions from `dist` to the publication a reader is actually served.

---

## Why this file exists rather than the edit

`.github/workflows/**` is not writable by the autonomous run's identity — the refusal is
recorded verbatim in this directory's README and in the 09-14 rule, clause 4. The repair is
therefore written where the operation *can* write it, and named in the day's brief. This is
the **fifth** staged workflow item; issue #7 carries the credential question for all of them.

## The finding, measured on 2026-10-10 and now printed on every build

Standing-queue item 1 asked: *of the assertions that gate the deploy, which are wired
somewhere that cannot observe the thing they assert?* Enumerated: **none of them.** All 29
gating assertions read `web/dist` or the repository root, and both exist in the `build` job
where all 29 run. Not one is blind to its own subject.

**The wrong home belongs to the bridge, not to an assertion.** Every one of those 29
assertions concludes something about `dist`. A reader is served the origin. The only thing
that carries a conclusion from `dist` to the origin is this job's byte-compare, and it
compares:

| | |
|---|---|
| `sitemap-0.xml` | the retry probe |
| `index.html`, `ar/index.html` | two of 120 served pages |
| `rss.xml`, `ar/rss.xml` | both feeds |
| `sitemap-index.xml` | |

**Six files. The origin serves 120 pages and 137 assets.** Coverage is **6/257 = 2.3%**, and
of the 137 assets the four confirmed are the two feeds and the two sitemaps — so everything a
**page loads** is confirmed **zero** times: 46 stills, 40 share cards, **34 woff2 fonts**, two
stylesheets, one script.

The fonts are why this is urgent rather than merely true. They landed 2026-10-08 — the largest
single addition to the served surface in this publication's history, 40 files — and the 10-08
log named the exposure in writing: *"if it goes wrong the failure is silent, because the new
assertion asserts where we do not point and never what arrives."* On 2026-10-10 one `woff2` was
confirmed at the origin as `font/woff2` **by hand**. By hand is the 2026-09-13 defect: a green
that costs a human's attention is paid for out of the runs that have least of it.

## Why this is cheap, which is the part worth reading

**The wide instrument already exists, is already gated, and is already published.**
`qa_served_manifest --emit` runs in `postbuild` and writes a per-URL fingerprint of every
served page and asset into `dist`; `served-manifest.json` is live at the origin (confirmed
2026-10-10: `200`, 67,737 bytes, **256 entries**). A 257-file bridge therefore costs **one
`curl` and one comparison**, not 257 of them.

## The step

Add to `.github/workflows/astro-pages.yml`, in the `verify` job, immediately after the
existing `Origin serves this build, byte-for-byte` step:

```yaml
      # The byte-compare above samples six files. This compares the manifest the
      # origin now serves against the one in the artifact we just published — 256
      # entries, every page and every asset, for one request. Safe in THIS job and
      # only in this job: the manifest is a property OF the artifact, so comparing
      # it here is not the self-comparison that keeps --check out of verify (see
      # 2026-10-06-build-served-manifest-check.md). That one asks a cross-deploy
      # question; this one asks whether the deploy that just happened arrived whole.
      - name: The published manifest describes the artifact we published
        run: |
          BASE="https://education3881.github.io/madar"
          curl -fsSL "$BASE/served-manifest.json" -o live-manifest.json
          python3 - <<'PY'
          import json, sys
          live = json.load(open("live-manifest.json", encoding="utf-8"))
          ours = json.load(open("dist/served-manifest.json", encoding="utf-8"))
          bad = 0
          for section in ("pages", "assets"):
              l, o = live.get(section, {}), ours.get(section, {})
              for k in sorted(set(l) | set(o)):
                  if k not in l:
                      print(f"::error::{section} {k} is in the artifact we published and not at the origin")
                      bad += 1
                  elif k not in o:
                      print(f"::error::{section} {k} is at the origin and not in the artifact we published")
                      bad += 1
                  elif l[k] != o[k]:
                      print(f"::error::{section} {k} differs: origin {l[k]} vs artifact {o[k]}")
                      bad += 1
              print(f"{section}: {len(o)} entries compared")
          if not ours.get("pages"):
              print("::error::the artifact's manifest describes no pages — nothing was compared")
              sys.exit(3)
          sys.exit(1 if bad else 0)
          PY
```

**It needs nothing that does not already exist.** The step is self-contained: two JSON files
and a dict comparison, no tool path and therefore no `actions/checkout` in the `verify` job,
which currently downloads the artifact only. It exits **3** rather than 0 if the artifact's
manifest describes no pages, so an empty manifest is a failure to check and not a clean
comparison of nothing (#16's silent-pass trap).

## What this patch deliberately does NOT do

It does not raise an assertion floor on the coverage ratio. `qa_bridge_coverage` **measures**
the ratio and asserts only what is reachable from here: that every bridge member exists in
`dist`, that every `.html` member is a page the sitemap claims, and that the bridge spans
**both editions and both feeds** — because a bridge that silently lost its Arabic half would
byte-compare the English half and pass forever while half the publication crossed unverified.
A floor above today's measured reality would red every build until this patch lands, which is
`qa_feed_validators`' position turned into a self-inflicted outage.

## Re-read at every weekly review

Per the 2026-09-27 rule, every open patch is re-read against current state each week and
refreshed or withdrawn. **This file carries no count that is not derived at read time** — the
six-file bridge and the 2.3% are printed by `qa_bridge_coverage` on every build, so the
authority is the tool, not this prose. Run it rather than trusting this paragraph:

```bash
python3 agents/tools/qa_bridge_coverage.py .
```
