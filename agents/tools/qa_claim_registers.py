#!/usr/bin/env python3
"""
qa_claim_registers — can the evidence under a published CLAIM still be opened,
and by whom?

WHY THIS EXISTS (standing-queue item 15, raised 2026-10-14, taken 2026-10-21
after six displacements and seven days at the head of the board)
------------------------------------------------------------------------------
Every instrument this operation owns that touches an outbound promise counts
URLs. `qa_body_links` proves each `sources[].url` is rendered. `qa_sources_alive`
asks whether the far side answers, and buckets what came back — alive, dead,
walled, timeout, bad certificate. `qa_reachability` asks the same of our own
pages. Item 15 asked the question none of them has a row for:

    which of our published CLAIMS can no longer be re-verified by anybody,
    including us?

A URL's health is not a claim's health, and the arithmetic does not carry in
either direction. The 2026-10-14 sweep reported *5 dead, 6 walled, 1 bad
certificate, 53 fine* out of 60 sampled from 342 distinct URLs. That report
cannot be converted into a number of unfalsifiable sentences: one dead URL
strands every figure whose only support it was, and strands nothing at all
where a second register carries the same figure. The one instance the
operation has ever found — Morocco's one-in-six refusal ratio, whose
denominator left the public record when the ministry withdrew two list PDFs
that no archive had snapshotted — was found by accident, because a *different*
citation on the same piece happened to 404 (#100).

WHAT IS ACTUALLY NEW HERE, AND IT IS ONE AXIS
---------------------------------------------
"Openable **today, by us**" is what `qa_sources_alive` measures. Item 15 asks
"by **anybody**", and those are different questions with different answers:

  * openable by us              — the register is live and we can read it
  * walled to us, open to others — 403 to this runner, fine in a browser (#70)
  * dead at origin, archived    — gone from its owner, still in the public
                                  record, re-verifiable by anyone who looks
  * dead at origin, no snapshot — **gone**, and every claim resting on it alone
                                  is now unfalsifiable, permanently

Only the last row is a claim-level defect, and nothing we own has ever queried
the axis that distinguishes it: **whether a snapshot exists**. That is one API
call per URL against a host that exists to answer it.

THE TWO HALVES, AND WHY ONLY ONE OF THEM GATES — the #89 design, reused
-----------------------------------------------------------------------
This is `qa_served_manifest`'s shape on a different subject, and the split is
load-bearing rather than tidy.

  `--emit` (NOT gated, network).  Reads the corpus, queries the archive for
  every distinct register, probes the origin ourselves for the ones with no
  snapshot, and writes a dated row per register into
  `agents/stats/claim-registers.json`. It must never gate a build: the far side
  belongs to ministries, UNESCO and journals, and an outage at archive.org at
  09:00 must not stop this publication deploying — the same reason
  `qa_sources_alive` is one of the three assertions that do not gate, written
  in `astro-pages.yml` where the others are listed.

  `--check` (GATED from postbuild, offline, deterministic).  Asserts that the
  register **covers the corpus**: every distinct `sources[].url` carried by an
  approved piece in either edition has a row. It makes no network call and
  knows nothing about the world. What it buys is the thing #89 bought: if the
  emit ever silently stops describing some registers, or a piece ships a
  citation nobody has ever asked an archive about, the build fails instead of
  the coverage narrowing in silence.

So the gate asserts our own bookkeeping and the measurement asserts nothing.
That is the honest division, and the reason it is the only one available is
worth stating plainly: **a claim's re-verifiability is a property of the world,
not of this repository and not of the served bytes.** Thirty-four assertions
read bytes we produce. This one cannot, so its network half is a register and
not a gate.

WHAT THE STATIC HALF ALSO PRINTS, AND DELIBERATELY DOES NOT ASSERT
------------------------------------------------------------------
The claim→register map, measured 2026-10-21 over 88 approved pieces: **1,896
distinct body numerals, of which 406 (21.4%) appear in no annotation of their
own piece.** That is a candidate list and not a defect list, and it is printed
with that label for the same reason item 17's name detector was abandoned as a
detector: a figure's boundary is not a textual property (#85). A body writes
*thirty-six facilitators* where its register prints `36`; it writes a year the
annotation never repeats; it recomputes a share the annotation states as a
count. Asserting on this number would fail on correct articles and be switched
off inside a week (#35). It is reported so the distribution is visible and so
the pieces at the top of it can be read by a human.

Exit codes: 0 clean · 1 defect · 2 cannot measure (emit only, network down).
"""
from __future__ import annotations

import collections
import datetime
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

REGISTER = pathlib.Path("agents/stats/claim-registers.json")
EDITIONS = (("articles", "en"), ("articles-ar", "ar"))
NUMERAL = re.compile(r"(?<![\w.,/-])(\d[\d,]*(?:\.\d+)?)(?![\w,]*[\w])")
AVAIL = "https://archive.org/wayback/available?url="
UA = "Madar-QA/1.0 (+https://education3881.github.io/madar/)"


def _split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    rest = text[4:]
    i = rest.find("\n---")
    if i < 0:
        return "", text
    return rest[:i], rest[i + 4 :]


def _normalise(token: str) -> str:
    t = token.replace(",", "")
    return t[:-2] if t.endswith(".0") else t


def read_corpus(root: pathlib.Path) -> list[dict]:
    """Every approved piece, with its registers and its body numerals."""
    pieces = []
    for folder, lang in EDITIONS:
        base = root / "web" / "src" / "content" / folder
        for path in sorted(base.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            front, body = _split_frontmatter(text)
            if "approved: true" not in front:
                continue
            titles = re.findall(r'^\s*-\s+title:\s*"(.*)"\s*$', front, re.M)
            urls = re.findall(r'^\s*url:\s*"(.*)"\s*$', front, re.M)
            annotated = {_normalise(n) for n in NUMERAL.findall(" ¶ ".join(titles))}
            # which registers carry each figure: the claim->register edge, and the
            # only reason a claim-level statement is possible at all. Pairing by
            # position is sound because `title` and `url` alternate inside one list
            # item; a piece where the two lists differ in length is reported, never
            # silently zipped short.
            carriers: dict[str, set[str]] = collections.defaultdict(set)
            if len(titles) == len(urls):
                for title, url in zip(titles, urls):
                    for n in {_normalise(x) for x in NUMERAL.findall(title)}:
                        carriers[n].add(url)
            pieces.append(
                {
                    "slug": path.stem,
                    "lang": lang,
                    "urls": urls,
                    "shape_ok": len(titles) == len(urls),
                    "body_numerals": {_normalise(n) for n in NUMERAL.findall(body)},
                    "annotated_numerals": annotated,
                    "carriers": dict(carriers),
                }
            )
    return pieces


def fan_in(pieces: list[dict]) -> dict[str, list[str]]:
    """url -> the pieces that lean on it, which is the claim side of the join."""
    fan: dict[str, list[str]] = collections.defaultdict(list)
    for piece in pieces:
        for url in dict.fromkeys(piece["urls"]):
            fan[url].append(f"{piece['slug']}:{piece['lang']}")
    return dict(fan)


# ---------------------------------------------------------------- the world


def _get(url: str, timeout: float = 20.0, method: str = "GET"):
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method=method)
    return urllib.request.urlopen(req, timeout=timeout)


def archive_state(url: str) -> dict:
    """Does a snapshot exist, and when was it taken? One call, one host."""
    try:
        with _get(AVAIL + urllib.parse.quote(url, safe=""), timeout=25.0) as r:
            payload = json.loads(r.read().decode("utf-8", "replace"))
    except Exception as exc:  # the archive is allowed to be down
        return {"archived": None, "archive_note": f"{type(exc).__name__}"}
    snap = (payload.get("archived_snapshots") or {}).get("closest") or {}
    if not snap.get("available"):
        return {"archived": False, "archive_note": "no snapshot"}
    stamp = snap.get("timestamp", "")
    return {
        "archived": True,
        "snapshot": f"{stamp[:4]}-{stamp[4:6]}-{stamp[6:8]}" if len(stamp) >= 8 else stamp,
        "archive_note": str(snap.get("status", "")),
    }


def origin_state(url: str) -> dict:
    """What WE receive. #20: never declare rot on one read — HEAD then GET."""
    for method in ("HEAD", "GET"):
        try:
            with _get(url, timeout=25.0, method=method) as r:
                return {"origin": r.status, "origin_note": method}
        except urllib.error.HTTPError as exc:
            if method == "GET":
                return {"origin": exc.code, "origin_note": "GET"}
        except Exception as exc:
            if method == "GET":
                return {"origin": None, "origin_note": type(exc).__name__}
    return {"origin": None, "origin_note": "unreached"}


def classify(row: dict) -> str:
    """The four rows of the table in this file's header."""
    archived, origin = row.get("archived"), row.get("origin")
    if archived is None:
        return "archive-unknown"
    if archived:
        return "archived"
    if origin is None:
        return "GONE-OR-UNREADABLE"
    if origin == 200:
        return "live-only"
    if origin in (401, 403, 429):
        return "walled-no-snapshot"
    return "GONE"


def emit(root: pathlib.Path, budget: int, spacing: float, stale_days: int) -> int:
    """Incremental and PACED, and the pacing is measured rather than chosen.

    The first run of this tool asked the archive about all 342 registers with
    six workers. It got 100 answers and then **242 consecutive HTTP 429s** —
    the availability endpoint rate-limits a burst of that size, and a row
    reading `archive-unknown` because we were throttled is not an observation
    about the world, it is an observation about us. So the emit carries a
    request budget and a spacing, re-asks only the rows that have no answer or
    a stale one, and tops the register up across runs. The gate below asserts
    that the register covers the corpus, which is what keeps a paced
    measurement from quietly becoming an abandoned one.
    """
    pieces = read_corpus(root)
    fan = fan_in(pieces)
    if not fan:
        print("FAIL qa_claim_registers — no registers found to ask about (silent-pass trap)")
        return 1
    today = datetime.date.today().isoformat()
    cutoff = (datetime.date.today() - datetime.timedelta(days=stale_days)).isoformat()

    path = root / REGISTER
    rows: dict[str, dict] = {}
    if path.exists():
        rows = {r["url"]: r for r in json.loads(path.read_text(encoding="utf-8")).get("registers", [])}

    def owed(url: str) -> bool:
        row = rows.get(url)
        if row is None or row.get("archived") is None:
            return True
        return str(row.get("observed", "")) < cutoff

    queue = [u for u in sorted(fan) if owed(u)][:budget]
    print(f"qa_claim_registers --emit · {len(fan)} cited registers · {len(rows)} rows on file · "
          f"{sum(1 for u in fan if owed(u))} owed an answer · asking {len(queue)} this run "
          f"(budget {budget}, {spacing}s apart)")

    asked = throttled = 0
    for url in queue:
        row = {"url": url, "pieces": fan[url], "observed": today}
        row.update(archive_state(url))
        if row.get("archived") is False:
            row.update(origin_state(url))
        row["state"] = classify(row)
        if row["state"] == "archive-unknown":
            throttled += 1
            # keep whatever the register already knew; an outage overwrites nothing
            rows.setdefault(url, row)
        else:
            rows[url] = row
        asked += 1
        if asked < len(queue):
            time.sleep(spacing)

    for url in fan:  # a row always exists, even if all it records is that we asked
        rows.setdefault(url, {"url": url, "pieces": fan[url], "observed": today,
                              "archived": None, "archive_note": "not yet asked",
                              "state": "archive-unknown"})
    for url, row in rows.items():  # the claim side moves with the corpus
        if url in fan:
            row["pieces"] = fan[url]

    if asked and throttled == asked:
        print(f"CANNOT MEASURE qa_claim_registers — archive returned nothing usable for all "
              f"{asked} registers asked; register left as it was")
        return 2

    out = root / REGISTER
    out.parent.mkdir(parents=True, exist_ok=True)
    ordered = [rows[u] for u in sorted(rows)]
    out.write_text(
        json.dumps({"observed": today, "registers": ordered}, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    rows_l = ordered
    buckets = collections.Counter(r["state"] for r in rows_l)
    print(f"  asked {asked}, throttled {throttled}; {len(rows_l)} rows now on file "
          f"across {len(pieces)} approved pieces")
    for state, n in buckets.most_common():
        print(f"  {state:<22} {n:>4}")
    stranded = [r for r in rows_l if r["state"].startswith("GONE")]
    if stranded:
        print("\n  registers with NO snapshot that we cannot read either — every claim")
        print("  resting on one of these alone is now unfalsifiable:")
        for r in stranded:
            print(f"    {r['origin']} · {r['url'][:96]}")
            print(f"        leaned on by {', '.join(r['pieces'])}")
    print(f"\n  written to {REGISTER}")
    return 0


# ---------------------------------------------------------------- the gate


def check(root: pathlib.Path) -> int:
    pieces = read_corpus(root)
    fan = fan_in(pieces)
    if not fan:
        print("FAIL qa_claim_registers — zero registers found in approved content (silent-pass trap)")
        return 1
    path = root / REGISTER
    if not path.exists():
        print(f"FAIL qa_claim_registers — no register at {REGISTER}; run --emit")
        return 1
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = {r["url"]: r for r in data.get("registers", [])}
    required = {"url", "pieces", "observed", "state"}

    missing = sorted(set(fan) - set(rows))
    malformed = sorted(u for u, r in rows.items() if not required <= set(r))
    orphans = sorted(set(rows) - set(fan))

    unpaired = [p["slug"] + ":" + p["lang"] for p in pieces if not p["shape_ok"]]
    print(f"qa_claim_registers --check · {len(fan)} distinct registers in {len(pieces)} approved pieces")
    if unpaired:
        print(f"  NOTE: {len(unpaired)} piece(s) whose title and url lines do not pair one-to-one, so")
        print(f"    no claim-level statement is made about them: {', '.join(unpaired[:6])}")
    print(f"  register observed {data.get('observed')} · {len(rows)} rows")
    print(f"  orphan rows (cited once, no longer cited) {len(orphans)} — kept on purpose, a withdrawn")
    print("    citation's observation is history and deleting it would lose the only record of it")

    unanchored = sum(len(p["body_numerals"] - p["annotated_numerals"]) for p in pieces)
    total = sum(len(p["body_numerals"]) for p in pieces)
    share = (100.0 * unanchored / total) if total else 0.0
    print(f"  CANDIDATE LIST, NOT ASSERTED: {unanchored} of {total} distinct body numerals "
          f"({share:.1f}%) appear in no")
    print("    annotation of their own piece. A boundary is not a textual property (#85); this is")
    print("    printed for a human to read, never failed on.")

    # ---- the claim-level join, which is item 15's actual question -----------
    # Offline: it reads the register's last observation, never the world. A
    # figure is AT RISK when every register that carries it is one nobody can
    # open — walled to us and snapshotted by no archive. This number is printed
    # and not asserted, because its input is a dated reading of somebody else's
    # server and a gate must never depend on one (the reason `qa_sources_alive`
    # does not gate, written in `astro-pages.yml`).
    at_risk_states = {"walled-no-snapshot", "GONE", "GONE-OR-UNREADABLE"}
    anchored = 0
    at_risk: collections.Counter = collections.Counter()
    for piece in pieces:
        for numeral in piece["body_numerals"]:
            carriers = piece["carriers"].get(numeral)
            if not carriers:
                continue
            anchored += 1
            states = {rows.get(u, {}).get("state") for u in carriers}
            if states and states <= at_risk_states:
                at_risk[f"{piece['slug']}:{piece['lang']}"] += 1
    print(f"  CLAIM-LEVEL JOIN: {anchored} body figures are anchored in a named register; "
          f"{sum(at_risk.values())} of them")
    print("    rest ONLY on registers that no archive holds and that we cannot read:")
    for key, n in at_risk.most_common():
        print(f"      {n:>3}  {key}")
    if not at_risk:
        print("      none")

    if missing or malformed:
        if missing:
            print(f"\nFAIL qa_claim_registers — {len(missing)} cited register(s) have no row:")
            for u in missing[:12]:
                print(f"  {u[:110]}")
                print(f"      cited by {', '.join(fan[u])}")
            if len(missing) > 12:
                print(f"  … and {len(missing) - 12} more")
        if malformed:
            print(f"FAIL qa_claim_registers — {len(malformed)} row(s) missing required fields")
            for u in malformed[:6]:
                print(f"  {u[:110]}")
        print("Run: python3 agents/tools/qa_claim_registers.py . --emit")
        return 1

    buckets = collections.Counter(rows[u].get("state") for u in fan)
    print("  state of the cited registers as last observed: " +
          " · ".join(f"{k} {v}" for k, v in buckets.most_common()))
    print(f"CLEAN qa_claim_registers — every one of {len(fan)} cited registers has a dated observation")
    return 0


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    root = pathlib.Path(args[0]).resolve() if args else pathlib.Path.cwd()
    if not (root / "web" / "src" / "content").is_dir():
        print(f"FAIL qa_claim_registers — {root} is not the repository root")
        return 1
    budget, spacing, stale = 40, 4.0, 30
    for a in argv[1:]:
        if a.startswith("--budget="):
            budget = int(a.split("=", 1)[1])
        elif a.startswith("--spacing="):
            spacing = float(a.split("=", 1)[1])
        elif a.startswith("--stale-days="):
            stale = int(a.split("=", 1)[1])
    if "--emit" in argv:
        return emit(root, budget, spacing, stale)
    return check(root)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
