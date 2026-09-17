# Publish gate — 2026-09-17

**Run in writing before the commit, per the skill. This is a HELD-EDIT gate, not a
publication gate: no piece flips today and nothing new is served to a reader.**

## What is being committed that is editorial

Two held article files were edited — `web/src/content/articles/2026-09-14-africa-best-system-ruler.md`
and its Arabic twin — closing items 1, 2 and 4 of today's verification verdict. **Both
remain `approved: false`.** No other content file moved.

## The gate, item by item

| Gate | State |
|---|---|
| Editor's five-test pair verdict on file | ✅ `2026-09-15-ed05-best-system-pair-verdict.md` — PASS, banked |
| **Verifier's verdict on file** | ✅ `2026-09-17-africa-best-system-ruler-verification.md` — **FAIL-5, 3 closed in-run, 2 OPEN** |
| Arabic gate on file | ✅ `2026-09-14-africa-best-system-ruler-ar-gate.md` — PASS (+ addendum 09-15); **two register questions from 09-15 still owed before the wave flips** |
| Hero still on disk | ✅ `web/public/stills/2026-09-14-africa-best-system-ruler.svg` |
| Share card on disk | ✅ `web/public/og/2026-09-14-africa-best-system-ruler.png` |
| `npm run build` clean | ✅ exit 0, 120 pages, 3.9s; full build with all postbuild gates 18.5s |
| Standing assertions green | ✅ **15 of 15 run, exit 0, no silent passes** (incl. new assertion 17) |
| **Held-slug leak zero** | ✅ `qa_held_assets`: 4 held slugs, 8 assets withheld, **no held piece contributes bytes**; `qa_lastmod`: held files contribute **no date** |
| Flag state (#18) | ✅ `approved: false` in **both** files; **no stale `approved: true` duplicate anywhere in the tree** |
| Caps at compose | ✅ EN title 53/100, dek 162/200 · AR title 58/100, dek 145/200 (code points, tashkeel +1) |
| Numeral multiset EN↔AR | ✅ EN 109 / AR 102, **zero Arabic-only figures**; 7 English-only tokens, all grade labels |
| `related:` resolution | ✅ 3 slugs, all present, all held; `qa_body_links` 0 rail dead ends |

## The verdict on shipping

**DO NOT FLIP.** Two items from today's verification verdict are open and both are the
Editor's — item 3 (a crown on ruler two resting on no reading) **blocks the wave**, and
item 5 (a citation whose publisher no longer exists) is unresolved. The wave also still
owes three confirmation reads, the Arabic Editor's two register questions, the three
reciprocal `related:` edges, and one completed `qa_sources_alive --held-only` sweep.

## Non-editorial changes in the same commit, declared

`web/src/styles/global.css` and `web/public/valence/index.html` — one CSS rule each,
fixing a live typographic defect on the **published** corpus (ruling #55). This **does**
change served bytes on every page, and it is the only thing in this commit that a reader
will see. It was proved four ways, the full assertion set was re-run after it, and the
rendered output was looked at in both languages before staging.

`agents/tools/qa_arabic_shaping.py` + `web/package.json` — the new assertion and its gate.

— Manager · 2026-09-17
