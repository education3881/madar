#!/usr/bin/env bash
# lastmod_tree_guard — proof harness. Ruling #35: an assertion is proved BOTH
# ways, and the bite is proved as carefully as the control (#74 — an injection
# that fails to change the artefact reads exactly like a passing control).
#
# Standing-queue item 8, taken 2026-10-15 at 7 days and four displacements.
#
# Every case runs on a CLONE under /tmp, never on the live tree: the subject of
# this guard is the working tree itself, so a harness that dirtied the real one
# would be injecting into the thing it is measuring.
#
# Bites first, control last — deliberately. A harness whose control runs first
# teaches you only that the tool can stay quiet.
#
#   usage: bash agents/tools/proofs/lastmod_tree_guard_proof.sh
set -u

REPO="$(git rev-parse --show-toplevel)"
WORK="$(mktemp -d /tmp/ltg-proof.XXXXXX)"
GUARD="agents/tools/lastmod_tree_guard.py"
ART="web/src/content/articles/2026-07-28-england-report-cards-first-term.md"
PASS=0; FAIL=0

fresh() {  # a clean clone, carrying the WORKING-TREE copies of the instruments
  local d="$WORK/$1"
  rm -rf "$d"
  git clone -q --no-hardlinks "$REPO" "$d" 2>/dev/null
  git -C "$d" config user.email p@example.com
  git -C "$d" config user.name "proof harness"
  # The instruments under test are not committed yet, and a clone carries only
  # committed state. Copy them in and commit, so each case starts from a tree
  # that is clean BY GIT and current BY CONTENT — otherwise every control would
  # pass for the wrong reason: a guard that is not there cannot refuse.
  cp "$REPO/$GUARD" "$d/$GUARD"
  cp "$REPO/agents/tools/qa_live_drift.py" "$d/agents/tools/qa_live_drift.py"
  cp "$REPO/agents/tools/qa_served_manifest.py" "$d/agents/tools/qa_served_manifest.py"
  git -C "$d" add -A >/dev/null
  git -C "$d" diff --cached --quiet || git -C "$d" commit -qm "proof: instruments under test"
  echo "$d"
}

# changed <dir> <path> — #74: assert the injection actually moved the artefact.
changed() {
  if git -C "$1" status --porcelain --untracked-files=all -- "$2" | grep -q .; then
    return 0
  fi
  echo "    HARNESS BROKEN: injection at $2 left the tree unchanged"
  return 1
}

run() {  # run <label> <expected-exit> <expected-substring> <dir>
  local label="$1" want="$2" needle="$3" dir="$4"
  local out code
  out="$(python3 -I "$dir/$GUARD" "$dir" 2>&1)"; code=$?
  if [[ "$code" == "$want" ]] && grep -qF "$needle" <<<"$out"; then
    echo "  PASS  $label  (exit $code)"
    PASS=$((PASS + 1))
  else
    echo "  FAIL  $label  (exit $code, wanted $want + '$needle')"
    sed 's/^/        /' <<<"$out" | head -8
    FAIL=$((FAIL + 1))
  fi
}

echo "== BITES (the guard must refuse: exit 4) =="

d=$(fresh b1); sed -i 's/<footer/<footer data-proof="1"/' "$d/web/src/components/SiteFooter.astro"
changed "$d" web/src/components/SiteFooter.astro && \
  run "1  dirty chrome component" 4 "chrome — dates every page that includes it" "$d"

d=$(fresh b2); printf '\nAn injected sentence.\n' >> "$d/$ART"
changed "$d" "$ART" && \
  run "2  dirty APPROVED article" 4 "approved content — dates its own page" "$d"

d=$(fresh b3); echo "export const x = 1;" > "$d/web/src/lib/injected-by-proof.mjs"
changed "$d" web/src/lib/injected-by-proof.mjs && \
  run "3  UNTRACKED file in a chrome glob" 4 "injected-by-proof.mjs" "$d"

d=$(fresh b4); rm "$d/$ART"
changed "$d" "$ART" && \
  run "4  DELETED approved article (approved in HEAD)" 4 "approved content" "$d"

d=$(fresh b5)
# A held draft, committed clean, then flipped to approved in the working tree
# only: the resolver may now read a date off it, so the axis is unsupportable.
sed 's/^approved: true$/approved: false/' "$d/$ART" > "$d/web/src/content/articles/zz-proof-held.md"
git -C "$d" add -A >/dev/null; git -C "$d" commit -qm "proof: a held draft"
sed -i 's/^approved: false$/approved: true/' "$d/web/src/content/articles/zz-proof-held.md"
changed "$d" web/src/content/articles/zz-proof-held.md && \
  run "5  held draft FLIPPED to approved in the tree" 4 "zz-proof-held" "$d"

d=$(fresh b6); sed -i 's/const CHROME_GLOBS/const CHROME_GLOBS_RENAMED/' \
  "$d/web/src/lib/sitemapLastmod.mjs"
changed "$d" web/src/lib/sitemapLastmod.mjs && \
  run "6  resolver's glob list UNPARSEABLE (cannot establish)" 4 "guards nothing" "$d"

d=$(fresh b7); rm "$d/web/src/lib/sitemapLastmod.mjs"
changed "$d" web/src/lib/sitemapLastmod.mjs && \
  run "7  resolver MISSING (cannot establish)" 4 "not found under" "$d"

# Built by EXPORT rather than by deleting a clone's .git: a clone's objects are
# read-only, `rm -rf` leaves a partial .git, and a partial .git refuses for a
# reason this case does not claim. An export is definitionally not a work tree.
d="$WORK/b8"; mkdir -p "$d"
git -C "$REPO" archive --format=tar HEAD | tar -x -C "$d"
cp "$REPO/$GUARD" "$d/$GUARD"
if [[ -e "$d/.git" ]]; then
  echo "    HARNESS BROKEN: .git survived, so this is not the case being proved"
  FAIL=$((FAIL + 1))
else
  run "8  not a git work tree (cannot establish)" 4 "Cannot-establish is refused" "$d"
fi

echo
echo "== CONTROLS (the guard must stay silent: exit 0) =="

d=$(fresh c1)
printf '\nA note.\n' >> "$d/agents/RUNBOOK.md"
sed -i 's/max-width: 100%/max-width: 99%/' "$d/web/src/styles/global.css" 2>/dev/null
echo "scratch" > "$d/content-drafts/zz-proof-scratch.md"
changed "$d" agents/RUNBOOK.md && \
  run "9  dirt OUTSIDE the resolver's read paths (incl. styles, excluded by design)" \
    0 "SUPPORTABLE" "$d"

d=$(fresh c2)
sed 's/^approved: true$/approved: false/' "$d/$ART" > "$d/web/src/content/articles/zz-proof-held.md"
git -C "$d" add -A >/dev/null; git -C "$d" commit -qm "proof: a held draft"
printf '\nStill held, still edited.\n' >> "$d/web/src/content/articles/zz-proof-held.md"
changed "$d" web/src/content/articles/zz-proof-held.md && \
  run "10 dirty HELD draft — excluded by the resolver's own semantics" \
    0 "dirty held draft(s) excluded by design" "$d"

d=$(fresh c3)
run "11 clean clone of the real tree" 0 "SUPPORTABLE" "$d"

echo
echo "-- $PASS passed, $FAIL failed --"
chmod -R u+w "$WORK" 2>/dev/null; rm -rf "$WORK"
[[ "$FAIL" == 0 ]]
