#!/usr/bin/env python3
"""
Madār content statistics.

Scans the EN and AR content collections, parses frontmatter, and emits:
  - a JSON snapshot (stdout with --json)
  - an HTML stats panel in the site's look-and-feel (default), ready to inject
    into the daily brief
  - appends a dated snapshot line to /agents/stats/history.jsonl (with --log)

Usage:
  python3 agents/tools/madar_stats.py            # prints HTML panel
  python3 agents/tools/madar_stats.py --json     # prints JSON snapshot
  python3 agents/tools/madar_stats.py --log      # also append to history.jsonl

No third-party dependencies required (uses a minimal frontmatter parser);
PyYAML is used if available for robustness.
"""
import os, re, json, sys, glob, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EN_DIR = os.path.join(ROOT, "web", "src", "content", "articles")
AR_DIR = os.path.join(ROOT, "web", "src", "content", "articles-ar")
HIST = os.path.join(ROOT, "agents", "stats", "history.jsonl")

try:
    import yaml  # type: ignore
    HAVE_YAML = True
except Exception:
    HAVE_YAML = False


def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}
    block = m.group(1)
    if HAVE_YAML:
        try:
            data = yaml.safe_load(block) or {}
            return data if isinstance(data, dict) else {}
        except Exception:
            pass
    # minimal fallback: top-level scalars + inline [a, b] lists
    data = {}
    for line in block.splitlines():
        mm = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if not mm:
            continue
        key, val = mm.group(1), mm.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            data[key] = [v.strip().strip('"\'') for v in val[1:-1].split(",") if v.strip()]
        elif val:
            data[key] = val.strip('"\'')
    return data


def load(dir_path):
    out = []
    for f in sorted(glob.glob(os.path.join(dir_path, "*.md"))):
        with open(f, encoding="utf-8") as fh:
            fm = parse_frontmatter(fh.read())
        fm["_file"] = os.path.basename(f)
        out.append(fm)
    return out


def themes_of(fm):
    t = fm.get("themes")
    if isinstance(t, list):
        return [str(x).strip() for x in t]
    if isinstance(t, str):
        return [x.strip() for x in t.strip("[]").split(",") if x.strip()]
    return []


def tally(items, key):
    counts = {}
    for it in items:
        v = it.get(key)
        if v:
            counts[str(v)] = counts.get(str(v), 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))


def build_snapshot():
    en, ar = load(EN_DIR), load(AR_DIR)
    en_approved = [a for a in en if str(a.get("approved")).lower() == "true"]
    ar_approved = [a for a in ar if str(a.get("approved")).lower() == "true"]
    theme_counts = {}
    for a in en:
        for th in themes_of(a):
            theme_counts[th] = theme_counts.get(th, 0) + 1
    dates = sorted([str(a.get("date")) for a in en if a.get("date")])
    # pieces per ISO week
    weeks = {}
    for d in dates:
        try:
            iso = datetime.date.fromisoformat(d).isocalendar()
            wk = f"{iso[0]}-W{iso[1]:02d}"
            weeks[wk] = weeks.get(wk, 0) + 1
        except Exception:
            pass
    snap = {
        "as_of": datetime.date.today().isoformat(),
        "articles": {
            "en_total": len(en),
            "ar_total": len(ar),
            "en_approved": len(en_approved),
            "ar_approved": len(ar_approved),
            "ar_parity_pct": round(100 * len(ar) / len(en)) if en else 0,
        },
        "by_region": tally(en, "region"),
        "by_country": tally(en, "country"),
        "by_type": tally(en, "type"),
        "by_theme": dict(sorted(theme_counts.items(), key=lambda kv: (-kv[1], kv[0]))),
        "cadence": {
            "first_piece": dates[0] if dates else None,
            "latest_piece": dates[-1] if dates else None,
            "pieces_per_week": dict(sorted(weeks.items())),
        },
        # Traffic is intentionally not auto-collected: the site carries no
        # third-party tracker (privacy posture). These fields are filled by hand
        # in the weekly review once the channels are live.
        "traffic": {
            "site_analytics": "not tracked (no third-party tracker, by design)",
            "substack": "pending launch (opens / return rate / country once live)",
            "attributable_shares": "manual search; record in weekly review",
        },
    }
    return snap


def fmt_pairs(d, n=None):
    items = list(d.items())[: n] if n else list(d.items())
    return " · ".join(f"{k} {v}" for k, v in items)


PANEL_CSS = """
<!-- Panel CSS (add once to the brief's <style> if not present):
.stats { border-top: 1px solid var(--color-ink); padding-block: 2rem; margin-bottom: 1rem; }
.stats h3 { font-family: var(--font-mono); font-size: 10.5px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--color-sage); margin-bottom: 1rem; }
.stats__grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin-bottom: 1.25rem; }
@media (max-width: 640px){ .stats__grid { grid-template-columns: repeat(2,1fr); } }
.stat { border-inline-start: 2px solid var(--color-orange); padding-inline-start: 0.75rem; }
.stat__n { display:block; font-family: var(--font-display); font-size: 2rem; line-height:1; color: var(--color-ink); }
.stat__l { display:block; font-family: var(--font-mono); font-size: 10px; letter-spacing:0.08em; text-transform:uppercase; color: var(--color-sage); margin-top:0.3rem; }
.stats__rows { font-size: 0.95rem; line-height: 1.9; }
.stats__k { font-family: var(--font-mono); font-size: 10px; letter-spacing:0.1em; text-transform:uppercase; color: var(--color-orange); margin-inline-end: 0.5rem; }
-->"""


def html_panel(s):
    a = s["articles"]
    region = fmt_pairs(s["by_region"])
    top_themes = fmt_pairs(s["by_theme"], 5)
    cad = s["cadence"]
    wk = cad["pieces_per_week"]
    wk_str = " · ".join(f"{k.split('-W')[1]} -> {v}" for k, v in wk.items())
    panel = (
        '<div class="stats">\n'
        f'  <h3>Statistics &middot; as of {s["as_of"]}</h3>\n'
        '  <div class="stats__grid">\n'
        f'    <div class="stat"><span class="stat__n">{a["en_total"]}</span><span class="stat__l">English pieces</span></div>\n'
        f'    <div class="stat"><span class="stat__n">{a["ar_total"]}</span><span class="stat__l">Arabic pieces</span></div>\n'
        f'    <div class="stat"><span class="stat__n">{a["ar_parity_pct"]}%</span><span class="stat__l">AR/EN parity</span></div>\n'
        f'    <div class="stat"><span class="stat__n">{len(s["by_country"])}</span><span class="stat__l">Countries covered</span></div>\n'
        '  </div>\n'
        '  <div class="stats__rows">\n'
        f'    <div><span class="stats__k">By region</span> {region}</div>\n'
        f'    <div><span class="stats__k">Top themes</span> {top_themes}</div>\n'
        f'    <div><span class="stats__k">Pieces per ISO week</span> {wk_str}</div>\n'
        f'    <div><span class="stats__k">Cadence</span> first {cad["first_piece"]} &middot; latest {cad["latest_piece"]}</div>\n'
        '    <div><span class="stats__k">Traffic</span> site: no tracker, by design &middot; Substack: pending launch &middot; shares: manual (weekly)</div>\n'
        '  </div>\n'
        '</div>'
    )
    return panel + "\n" + PANEL_CSS


def main():
    snap = build_snapshot()
    if "--log" in sys.argv:
        os.makedirs(os.path.dirname(HIST), exist_ok=True)
        with open(HIST, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(snap, ensure_ascii=False) + "\n")
    if "--json" in sys.argv:
        print(json.dumps(snap, ensure_ascii=False, indent=2))
    else:
        print(html_panel(snap))


if __name__ == "__main__":
    main()
