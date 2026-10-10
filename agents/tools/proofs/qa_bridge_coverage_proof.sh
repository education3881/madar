#!/usr/bin/env bash
# Proof harness for qa_bridge_coverage.py (standing assertion 32, ruling #93).
#
# BITE FIRST (#74), on copies in /tmp so a failed experiment cannot leave a
# mutation in the tree. Every injection is CHECKED FOR HAVING CHANGED THE FILE
# before the assertion is run on it (2026-09-14: "a bite that fails to change the
# artefact is a failed experiment, not a passing control") — and yesterday's
# sharper version of the same lesson (2026-10-08 guard 3): an injection that does
# not REACH the condition it tests is not a proof of that condition.
#
# Nothing here hardcodes a count. Every expected value is derived from the tree,
# because the 10-07 harness went stale inside an hour on its own hardcoded 89.
set -u

ROOT="${1:-$(cd "$(dirname "$0")/../../.." && pwd)}"
TOOL="$ROOT/agents/tools/qa_bridge_coverage.py"
WF_REL=".github/workflows/astro-pages.yml"
WORK="$(mktemp -d /tmp/bridgeproof.XXXXXX)"
pass=0; fail=0

cleanup() { rm -rf "$WORK"; }
trap cleanup EXIT

say() { printf '\n%s\n' "=== $* ==="; }

# A scratch repo root: the real dist (read-only use) + a mutable workflow copy.
scratch() {
  local d="$WORK/$1"; rm -rf "$d"; mkdir -p "$d/.github/workflows" "$d/web"
  cp "$ROOT/$WF_REL" "$d/$WF_REL"
  ln -s "$ROOT/web/dist" "$d/web/dist"
  echo "$d"
}

# changed <before> <after> — refuse to judge an injection that did nothing.
changed() {
  if cmp -s "$1" "$2"; then
    echo "  INJECTION DID NOT CHANGE THE FILE — not a proof, a failed experiment"
    return 1
  fi
  return 0
}

run() { python3 "$TOOL" "$1" >"$WORK/out" 2>&1; echo $?; }

expect() { # expect <label> <wanted-exit> <actual-exit> [grep-pattern]
  local label="$1" want="$2" got="$3" pat="${4:-}"
  if [ "$got" = "$want" ] && { [ -z "$pat" ] || grep -q "$pat" "$WORK/out"; }; then
    echo "  PASS  $label (exit $got)"; pass=$((pass+1))
  else
    echo "  FAIL  $label — wanted exit $want${pat:+ matching '$pat'}, got $got"
    sed 's/^/        /' "$WORK/out" | tail -12
    fail=$((fail+1))
  fi
}

say "BITE 1 — the lopsided bridge: drop ar/index.html from the verify sample"
d=$(scratch b1); cp "$ROOT/$WF_REL" "$WORK/orig"
sed -i 's|for f in index.html ar/index.html rss.xml|for f in index.html rss.xml|' "$d/$WF_REL"
changed "$WORK/orig" "$d/$WF_REL" && expect "Arabic page unspanned" 1 "$(run "$d")" "does not span an Arabic page"

# BITE 2 is also the proof of the tool's own first defect, found by this harness.
# `ar/rss.xml` is named TWICE in the verify job: once in the byte-compare loop and
# once in the feed-cache-validator loop, which only `curl -I`s for an ETag. The
# first parser was scoped to the whole job, so dropping the file from the compare
# loop left it credited by the cache loop and this bite read CLEAN. It now bites,
# which is the discrimination the fix exists to make — and on the real tree both
# parsers print 6, because the two lists overlap exactly on the feeds. The right
# number for the wrong reason (2026-09-14, the input-side scoping question).
say "BITE 2 — drop ar/rss.xml from the COMPARE loop while the cache loop still names it"
d=$(scratch b2)
sed -i 's|rss.xml ar/rss.xml sitemap-index.xml|rss.xml sitemap-index.xml|' "$d/$WF_REL"
changed "$WORK/orig" "$d/$WF_REL" && expect "Arabic feed unspanned" 1 "$(run "$d")" "does not span the Arabic feed"

say "BITE 3 — limb 1: the sample names a file the build does not produce"
d=$(scratch b3)
sed -i 's|for f in index.html|for f in feed-legacy.xml index.html|' "$d/$WF_REL"
changed "$WORK/orig" "$d/$WF_REL" && expect "missing bridge member" 1 "$(run "$d")" "bridge member not in dist: feed-legacy.xml"

say "BITE 4 — limb 2b: an .html member the sitemap does not claim (404.html is real)"
d=$(scratch b4)
sed -i 's|for f in index.html|for f in 404.html index.html|' "$d/$WF_REL"
changed "$WORK/orig" "$d/$WF_REL" && expect "unclaimed html member" 1 "$(run "$d")" "is not in the sitemap's <loc> set"

say "BITE 5 — the probe itself drifts off the tree"
d=$(scratch b5)
sed -i 's|dist/sitemap-0.xml|dist/sitemap-7.xml|g' "$d/$WF_REL"
changed "$WORK/orig" "$d/$WF_REL" && expect "probe member missing" 1 "$(run "$d")" "bridge member not in dist: sitemap-7.xml"

say "CONTROL NEGATIVE 1 — a cmp in the BUILD job is not a bridge to the origin"
# Scope check: only the verify job's comparisons count. If this leaked, the tool
# would report a wider bridge than exists — a FALSE PASS, the wrong direction.
d=$(scratch c1)
python3 - "$d/$WF_REL" <<'PY'
import re,sys
p=sys.argv[1]; t=open(p).read()
t=t.replace("      - name: robots.txt advertises the sitemap the build derives",
            "      - name: injected local compare, build job\n        run: cmp -s a dist/global.css\n      - name: robots.txt advertises the sitemap the build derives",1)
open(p,"w").write(t)
PY
changed "$WORK/orig" "$d/$WF_REL" && {
  got=$(run "$d")
  if [ "$got" = "0" ] && grep -q "ASSERTED) \.*  *6 " "$WORK/out"; then
    echo "  PASS  build-job cmp ignored, bridge still 6 (exit 0)"; pass=$((pass+1))
  else
    echo "  FAIL  build-job cmp leaked into the bridge count, or exit != 0 (got $got)"
    grep "ASSERTED" "$WORK/out" | sed 's/^/        /'; fail=$((fail+1))
  fi
}

say "CONTROL NEGATIVE 2 — reverting every injection restores CLEAN"
d=$(scratch c2)
expect "untouched workflow is clean" 0 "$(run "$d")" "CLEAN qa_bridge_coverage"

say "GUARD 1 — no workflow at all: exit 3, never a clean zero-width bridge"
d=$(scratch g1); rm -f "$d/$WF_REL"
expect "missing workflow -> 3" 3 "$(run "$d")" "FAILURE TO CHECK"

say "GUARD 2 — no built artefact: exit 3"
d=$(scratch g2); rm -f "$d/web/dist"
expect "missing dist -> 3" 3 "$(run "$d")" "FAILURE TO CHECK"

say "GUARD 3 — a verify job with no recognised comparison: exit 3, NOT clean"
# Reaches the condition: the job block still exists, so the parser finds it and
# then finds nothing in it. Checked below by asserting the message, not the code
# alone (2026-10-08: a guard whose injection never reaches its condition is not
# a proved guard).
d=$(scratch g3)
python3 - "$d/$WF_REL" <<'PY'
import re,sys
p=sys.argv[1]; t=open(p).read()
i=t.index("\n  verify:")
head,tail=t[:i],t[i:]
tail=re.sub(r"cmp\s+-s","true -s",tail)
open(p,"w").write(head+tail)
PY
changed "$WORK/orig" "$d/$WF_REL" && expect "no comparisons -> 3" 3 "$(run "$d")" "bridge that cannot be found"

say "GUARD 4 — the verify job is gone entirely: exit 3 with its own message"
d=$(scratch g4)
python3 - "$d/$WF_REL" <<'PY'
import sys
p=sys.argv[1]; t=open(p).read()
open(p,"w").write(t[:t.index("\n  verify:")]+"\n")
PY
changed "$WORK/orig" "$d/$WF_REL" && expect "no verify job -> 3" 3 "$(run "$d")" "no .verify:. job"

say "GUARD 5 — dist with no sitemap: exit 3"
d="$WORK/g5"; rm -rf "$d"; mkdir -p "$d/.github/workflows" "$d/web/dist"
cp "$ROOT/$WF_REL" "$d/$WF_REL"
cp "$ROOT/web/dist/index.html" "$d/web/dist/" 2>/dev/null || true
expect "no sitemap -> 3" 3 "$(run "$d")" "FAILURE TO CHECK"

say "USAGE — no argument: exit 2"
python3 "$TOOL" >"$WORK/out" 2>&1; expect "usage -> 2" 2 "$?" "usage:"

printf '\n===============================================\n'
printf 'qa_bridge_coverage proof: %d passed, %d failed\n' "$pass" "$fail"
printf '===============================================\n'
[ "$fail" -eq 0 ]
