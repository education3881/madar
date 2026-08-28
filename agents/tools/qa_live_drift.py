#!/usr/bin/env python3
"""
qa_live_drift — standing assertion: what the ORIGIN serves is what we built.

WHY (Manager, 2026-08-27 — the 08-26 forward question, answered)
----------------------------------------------------------------
Every check this operation owns reads `dist`: the output of one build, on one
machine, at one moment. Nothing had ever compared what we BUILT to what is
actually being SERVED. The evidence that this is a real blind spot is not
hypothetical — it is the operation's own history, three times over:

- 2026-07-02→07-07: the deploy was dead for four days while every local check
  stayed green. The build was fine; the origin was stale (rulings #16/#17).
- 2026-08-26: the live site had been serving the 08-23 build for three days
  and NO assertion reported it. It was noticed only because state verification
  is a human habit at the top of the run, not a check.
- 2026-08-27 (today): the gap reached four days — a commit stranded outside
  origin plus a full uncommitted day, and still nothing mechanical said so.

Ruling #36 says a claim must be DERIVED from the thing it describes. The claim
"the site is current" describes the live origin, not our disk. So this check
fetches the origin and diffs it against local `dist` on three axes:

1. sitemap URL set        — pages added or removed but not yet served
2. sitemap <lastmod> map  — pages whose content date drifted
3. sampled page heads     — title / canonical / og:image / twitter:card on the
                            two front doors and one article per language, so a
                            metadata fix that never deployed is caught even
                            when the URL set and lastmod agree

DRIFT IS A FINDING, NOT ALWAYS A FAULT. On the morning of a staged-but-unpushed
day, drift is EXPECTED — the check's job is to make the gap loud and countable
(N URLs differ, M lastmods behind, K days since origin moved) instead of a
thing a human happens to notice. After a push deploys, the check must go CLEAN.
A clean read is the only mechanical statement this operation has ever had that
the reader is seeing the work.

Proved both ways before being trusted, per ruling #35:
- CONTROL (must be silent): live origin vs a build of origin/main (5e16db2) —
  0 URL drift, 0 lastmod drift, 4/4 sampled heads identical.
- BITE (must fire): live origin vs today's working-tree build — lastmod drift
  on the pages touched since 08-23 and head drift on the front doors (the
  brand card shipped to `dist` on 08-26 and never reached the origin).

Exit codes: 0 origin matches dist · 1 drift (named, counted) · 2 could not
fetch the origin (a FAILURE to check, per the 08-16 silent-pass trap — an
unreachable origin is never reported as "no drift").

Usage: python3 agents/tools/qa_live_drift.py [dist_dir] [--live https://...]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import requests
except ImportError:  # pragma: no cover
    print("FAIL(2): python-requests unavailable — the origin cannot be read, "
          "and an unread origin is not a clean origin.")
    sys.exit(2)

LIVE = "https://education3881.github.io/madar"
TIMEOUT = 20

# Head fields whose drift we care about on sampled pages. Deliberately the
# consumer-facing metadata: what a crawler or a share card reads first.
HEAD_FIELDS = {
    "title": re.compile(r"<title>(.*?)</title>", re.S),
    "canonical": re.compile(r'rel="canonical" href="([^"]*)"'),
    "og:image": re.compile(r'property="og:image" content="([^"]*)"'),
    "twitter:card": re.compile(r'name="twitter:card" content="([^"]*)"'),
}

# Sampled URLs, dist-relative. Front doors in both languages plus one article
# per language — enough to catch head-level drift without fetching all 82.
SAMPLES = [
    "index.html",
    "ar/index.html",
    "articles/2026-07-28-england-report-cards-first-term/index.html",
    "ar/articles/2026-07-28-england-report-cards-first-term/index.html",
]


def sitemap_map(xml: str) -> dict[str, str]:
    """URL -> lastmod ('' if absent)."""
    out: dict[str, str] = {}
    for m in re.finditer(r"<url>(.*?)</url>", xml, re.S):
        block = m.group(1)
        loc = re.search(r"<loc>(.*?)</loc>", block)
        mod = re.search(r"<lastmod>(.*?)</lastmod>", block)
        if loc:
            out[loc.group(1).strip()] = mod.group(1).strip() if mod else ""
    return out


def head_sig(html: str) -> dict[str, str]:
    head = html.split("</head>", 1)[0]
    return {k: (rx.search(head).group(1).strip() if rx.search(head) else "ABSENT")
            for k, rx in HEAD_FIELDS.items()}


def fetch(url: str) -> str | None:
    try:
        r = requests.get(url, timeout=TIMEOUT)
        return r.text if r.status_code == 200 else None
    except requests.RequestException:
        return None


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--live")]
    live = LIVE
    for i, a in enumerate(sys.argv):
        if a == "--live" and i + 1 < len(sys.argv):
            live = sys.argv[i + 1].rstrip("/")
    dist = Path(args[0] if args else "web/dist")
    if not dist.is_dir():
        print(f"FAIL(2): dist not found at {dist} — nothing to compare is not a pass.")
        return 2

    live_xml = fetch(f"{live}/sitemap-0.xml")
    if live_xml is None:
        print(f"FAIL(2): could not fetch {live}/sitemap-0.xml — an unreachable "
              "origin is a failure to check, never 'no drift'.")
        return 2
    local_xml_path = dist / "sitemap-0.xml"
    if not local_xml_path.exists():
        print("FAIL(2): no sitemap-0.xml in dist.")
        return 2

    live_map = sitemap_map(live_xml)
    local_map = sitemap_map(local_xml_path.read_text())

    drift = 0
    only_local = sorted(set(local_map) - set(live_map))
    only_live = sorted(set(live_map) - set(local_map))
    if only_local:
        drift += len(only_local)
        print(f"DRIFT: {len(only_local)} URL(s) built but not served:")
        for u in only_local[:10]:
            print(f"  + {u}")
    if only_live:
        drift += len(only_live)
        print(f"DRIFT: {len(only_live)} URL(s) served but no longer built:")
        for u in only_live[:10]:
            print(f"  - {u}")

    mod_drift = [u for u in sorted(set(live_map) & set(local_map))
                 if live_map[u] != local_map[u]]
    if mod_drift:
        drift += len(mod_drift)
        print(f"DRIFT: {len(mod_drift)} page(s) whose <lastmod> differs "
              "(origin serves an older state of an existing page):")
        for u in mod_drift[:10]:
            print(f"  ~ {u}  origin={live_map[u] or '—'}  local={local_map[u] or '—'}")
        if len(mod_drift) > 10:
            print(f"  … and {len(mod_drift) - 10} more")

    for rel in SAMPLES:
        local_page = dist / rel
        if not local_page.exists():
            print(f"DRIFT: sampled page missing locally: {rel}")
            drift += 1
            continue
        url = f"{live}/{rel.removesuffix('index.html').rstrip('/')}/".replace(f"{live}//", f"{live}/")
        live_html = fetch(url)
        if live_html is None:
            print(f"DRIFT: sampled page not served (non-200): {url}")
            drift += 1
            continue
        ls, ds = head_sig(live_html), head_sig(local_page.read_text())
        for k in HEAD_FIELDS:
            if ls[k] != ds[k]:
                print(f"DRIFT: {rel} head field '{k}': origin={ls[k]!r} local={ds[k]!r}")
                drift += 1

    if drift:
        print(f"\nDRIFT({drift}): the origin is not serving what we built. If a "
              "push is staged, this is the count of what the reader is waiting "
              "on; if nothing is staged, the deploy pipeline is the suspect.")
        return 1
    print(f"CLEAN — origin matches dist: {len(local_map)} URLs, "
          f"{len(mod_drift)} lastmod drift, {len(SAMPLES)} sampled heads identical.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
