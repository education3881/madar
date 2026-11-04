#!/usr/bin/env python3
"""Harness for item 29's three new limbs. Bite first, control either side.

#35 and its 2026-09-14 addendum: a bite that fails to change the artefact reads
exactly like a passing control, so EVERY injection is asserted to have changed
the file before the check is run on it. And 2026-11-03's harness lesson: capture
the subprocess's own returncode, never an `if`'s.
"""
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/runner/work/madar/madar")
TOOL = REPO / "agents" / "tools" / "qa_composition.py"
SCRATCH = Path("/tmp/madarwork/scratch")


def fresh():
    if SCRATCH.exists():
        shutil.rmtree(SCRATCH)
    (SCRATCH / "web").mkdir(parents=True)
    shutil.copytree(REPO / "web" / "dist", SCRATCH / "web" / "dist")
    shutil.copytree(REPO / "web" / "src", SCRATCH / "web" / "src",
                    ignore=shutil.ignore_patterns("content"))
    (SCRATCH / "web" / "src" / "content").mkdir(exist_ok=True)
    return SCRATCH


def run(root):
    p = subprocess.run([sys.executable, str(TOOL), str(root)],
                       capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def edit(path, before, after, count=1):
    """Apply one textual injection and PROVE it changed the file."""
    old = path.read_text(encoding="utf-8")
    new = old.replace(before, after, count)
    if new == old:
        raise SystemExit("INJECTION DID NOT APPLY to %s — the bite would have "
                         "read as a passing control. Aborting." % path)
    path.write_text(new, encoding="utf-8")
    return len(old), len(new)


results = []


def case(name, limb, mutate, expect):
    root = fresh()
    d = root / "web" / "dist"
    note = mutate(d)
    rc, out = run(root)
    ok = (rc == expect)
    tail = [l for l in out.splitlines()
            if "FAIL" in l or "REFUSED" in l or l.startswith("CLEAN")]
    results.append((name, limb, expect, rc, ok, note, tail[:3]))
    print("%-46s limb %s  expected %d got %d  %s"
          % (name, limb, expect, rc, "PASS" if ok else "*** HARNESS FAILURE ***"))
    for l in tail[:3]:
        print("      | %s" % l.strip())


# ---- control: untouched copy must be silent -------------------------------
case("CONTROL untouched dist", "-", lambda d: "no change", 0)

# ---- bite 1, limb 3: two pages describe one @id differently ---------------
def bite_ld(d):
    page = d / "about" / "index.html"
    sizes = edit(
        page, "</head>",
        '<script type="application/ld+json">'
        '{"@context":"https://schema.org","@id":'
        '"https://education3881.github.io/madar/#organization",'
        '"@type":"Organization","name":"Madar Digest"}</script></head>')
    return "about/ describes #organization with name 'Madar Digest' (%d -> %d bytes)" % sizes


case("BITE 1  one @id, two descriptions", "3", bite_ld, 1)

# ---- control 2: a bare REFERENCE to the same @id must stay silent ---------
def control_ref(d):
    page = d / "about" / "index.html"
    sizes = edit(
        page, "</head>",
        '<script type="application/ld+json">'
        '{"@context":"https://schema.org","@id":'
        '"https://education3881.github.io/madar/#organization"}</script></head>')
    return "about/ REFERENCES #organization and claims nothing (%d -> %d bytes)" % sizes


case("CONTROL a bare @id reference is not a claim", "3", control_ref, 0)

# ---- bite 2, limb 4: the two feeds share one item identity ----------------
def bite_feed(d):
    en = (d / "rss.xml").read_text(encoding="utf-8")
    first = en.split("<guid", 1)[1].split("</guid>", 1)[0]
    guid = first.split(">", 1)[1]
    ar = d / "ar" / "rss.xml"
    text = ar.read_text(encoding="utf-8")
    victim = text.split("<guid", 1)[1].split("</guid>", 1)[0].split(">", 1)[1]
    sizes = edit(ar, victim, guid)
    return "ar/rss.xml item 1 guid := the EN feed's item 1 guid (%d -> %d bytes)" % sizes


case("BITE 2  one guid in both feeds", "4", bite_feed, 1)

# ---- bite 3, limb 5: an alternate stops naming its namer back -------------
def bite_oneway(d):
    page = d / "ar" / "index.html"
    text = page.read_text(encoding="utf-8")
    tag = [l for l in text.split("<link") if 'hreflang="en"' in l][0]
    frag = "<link" + tag.split(">")[0] + ">"
    sizes = edit(page, frag, "")
    return "ar/ drops its hreflang=en alternate back to / (%d -> %d bytes)" % sizes


case("DELEGATED 3 one-way cluster: silent here", "5", bite_oneway, 0)

# ---- bite 4, limb 5: two pages claim one canonical -----------------------
def bite_canon(d):
    page = d / "about" / "index.html"
    sizes = edit(page,
                 'rel="canonical" href="https://education3881.github.io/madar/about/"',
                 'rel="canonical" href="https://education3881.github.io/madar/"')
    return "about/ claims the site root as its canonical (%d -> %d bytes)" % sizes


case("BITE 4  two pages, one canonical", "5", bite_canon, 1)

# ---- bite 5, limb 5: the error page names a preferred URL ----------------
def bite_404(d):
    page = d / "404.html"
    sizes = edit(page, "</head>",
                 '<link rel="canonical" '
                 'href="https://education3881.github.io/madar/"></head>')
    return "404.html declares the site root as its canonical (%d -> %d bytes)" % sizes


case("BITE 5  a canonical on the error page", "5", bite_404, 1)


# ---- bite 6, limb 5: the 404 clause ALONE, isolated from bite 4 -----------
# Bite 5 was caught TWICE (the error page named the site root, which / already
# claims), so it did not isolate the clause. #126's lesson on a kernel applies
# to a bite: a defect two limbs catch proves neither of them necessary.
def bite_404_isolated(d):
    page = d / "404.html"
    sizes = edit(page, "</head>",
                 '<link rel="canonical" '
                 'href="https://education3881.github.io/madar/404/"></head>')
    return "404.html claims /404/, which no other page claims (%d -> %d bytes)" % sizes


case("BITE 6  404 canonical, claimed by nothing else", "5", bite_404_isolated, 1)


# ---- bite 7, limb 5: an alternate names a URL this build does not serve ---
def bite_dangling(d):
    page = d / "index.html"
    sizes = edit(page,
                 'hreflang="ar" href="https://education3881.github.io/madar/ar/"',
                 'hreflang="ar" href="https://education3881.github.io/madar/arabic/"')
    return "/ names /arabic/ as its Arabic alternate (%d -> %d bytes)" % sizes


case("DELEGATED 7 dangling alternate: silent here", "5", bite_dangling, 0)


# ---- bite 8, limb 5: a real page loses its canonical ---------------------
def bite_nocanon(d):
    page = d / "articles" / "2026-05-26-bahrain-bqa-public-grades" / "index.html"
    text = page.read_text(encoding="utf-8")
    frag = "<link" + [l for l in text.split("<link")
                      if 'rel="canonical"' in l][0].split(">")[0] + ">"
    sizes = edit(page, frag, "")
    return "an article page drops its canonical (%d -> %d bytes)" % sizes


case("BITE 8  a page other than 404 with no canonical", "5", bite_nocanon, 1)


# ---- the delegation is PROVED, not assumed (#125): the sibling must bite ---
SIBLING = REPO / "agents" / "tools" / "qa_hreflang_clusters.py"


def sibling_case(name, mutate, expect):
    root = fresh()
    d = root / "web" / "dist"
    note = mutate(d)
    p = subprocess.run([sys.executable, str(SIBLING), str(root / "web" / "dist")],
                       capture_output=True, text=True)
    ok = p.returncode == expect
    results.append((name, "sib", expect, p.returncode, ok, note, []))
    print("%-46s sibling  expected %d got %d  %s"
          % (name, expect, p.returncode, "PASS" if ok else "*** HARNESS FAILURE ***"))
    for l in (p.stdout + p.stderr).splitlines():
        if "FAIL" in l or "CLEAN" in l or "one-way" in l.lower():
            print("      | %s" % l.strip()[:150])
            break


sibling_case("SIBLING control, untouched dist", lambda d: "no change", 0)
sibling_case("SIBLING bites the one-way cluster", bite_oneway, 1)
sibling_case("SIBLING bites the dangling alternate", bite_dangling, 1)

# ---- control 3: dist untouched again, after all of that ------------------
case("CONTROL untouched dist, second reading", "-", lambda d: "no change", 0)

print()
bad = [r for r in results if not r[4]]
print("%d case(s), %d harness failure(s)" % (len(results), len(bad)))
for name, limb, expect, rc, ok, note, tail in results:
    print("  %-46s limb %-2s %s   %s" % (name, limb, "ok " if ok else "BAD", note))
sys.exit(1 if bad else 0)
