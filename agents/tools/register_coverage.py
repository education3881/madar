#!/usr/bin/env python3
"""register_coverage.py — is a reachability measurement green because the defects live in
the documents the instrument cannot open?

Standing-queue item 34, raised 2026-10-22 as the daily's forward question, taken at the head
on 2026-11-06 at 15 days. The row's own words:

    `qa_citation_identity` could compare only 90 of 218 quotation-bearing registers; the 80 it
    declined are 34 walled, 13 PDFs, 20 script-mismatched, 6 dead. EVERY STATE DOCUMENT IN THIS
    CORPUS IS A PDF - every yearbook, every decree, every performance report - and a PDF is the
    class this instrument reports as *unreadable* rather than *checked*. So 34.4% is a rate over
    the registers that happen to be open HTML, which is systematically the journalism and
    systematically not the primary sources this publication's whole method rests on.
    ... report coverage PER CLASS instead of one rate over the union.

WHY THIS IS NOT AN ASSERTION, AND THE REASON IS THE ROW'S OWN.
  The row asks for a measurement and names it as one: *report coverage per class*. There is no
  floor here that could gate. A floor above today's per-class coverage reds every build until
  somebody else's PDF becomes readable, which is #93's reasoning exactly, and the one limb that
  looks assertable - *every row is classifiable* - is vacuous by construction, because an
  unclassifiable row simply lands in the UNKNOWN bucket and the bucket is honest. So this file
  carries no `qa_` prefix: the assertion count globs `qa_*.py` and this is a measurement, like
  `run_envelope.py`, `build_job_gates.py` and `lastmod_tree_guard.py` before it.
  Per #125, a decline names what covers it instead: nothing does, and that is the finding.

WHAT IT READS. Only the two registers already on disk, both written by gated instruments:
  agents/stats/claim-registers.json   (qa_claim_registers --emit, #111)
  agents/stats/citation-identity.json (qa_citation_identity --emit, #112)
It makes no network request. It is deterministic and offline, and can be re-run by any later run
to falsify every number it prints.

THE PARTY RULE IS POSITIVE-ONLY, AND THAT IS DELIBERATE.
  A host suffix can positively identify an OFFICIAL publisher (a state, an intergovernmental
  body, a university, our own origin). Nothing in a hostname can positively identify journalism.
  So the partition this tool prints is OFFICIAL against NOT-IDENTIFIED-AS-OFFICIAL, and it never
  calls the complement `journalism` - the row's hypothesis says the comparable population is
  *systematically the journalism*, and a classifier that assumed the complement was journalism
  would be assuming the thing it was built to test. Every rule is enumerated in the output so
  a reader can disagree with it by looking.
"""
import json
import os
import sys
import collections
from urllib.parse import urlparse

# --- the party rule, enumerated so it can be argued with -------------------------------------
GOV_SUFFIXES = (
    '.gov', '.mil', '.int',
    '.gov.uk', '.gov.br', '.gov.in', '.gov.tr', '.gov.ua', '.gov.pl', '.gov.om', '.gov.eg',
    '.gov.sl', '.gov.zm', '.gov.sg', '.gov.ph', '.gov.bh', '.gov.sa', '.gov.ae', '.gov.jo',
    '.gov.ng', '.gov.gh', '.gov.ke', '.gov.pk', '.gov.bd', '.gov.lk', '.gov.my', '.gov.au',
    '.gov.za', '.gov.il', '.gov.qa', '.gov.kw', '.gov.lb', '.gov.ye', '.gov.sd', '.gov.ma',
    '.gov.it', '.gov.gr', '.gov.pt', '.gov.es', '.gov.ie', '.gov.cy', '.gov.mt', '.gov.hk',
    '.govt.nz', '.go.id', '.go.jp', '.go.ke', '.go.tz', '.go.ug', '.go.kr', '.go.th', '.go.cr',
    '.gob.mx', '.gob.cl', '.gob.pe', '.gob.ar', '.gob.es', '.gob.ec', '.gob.bo', '.gob.do',
    '.gouv.fr', '.gouv.sn', '.gouv.ci', '.gouv.bj', '.gouv.ml', '.gouv.ht', '.gouv.qc.ca',
    '.admin.ch', '.europa.eu', '.gv.at', '.bund.de', '.overheid.nl', '.rijksoverheid.nl',
)
EDU_SUFFIXES = ('.edu', '.ac.uk', '.edu.au', '.edu.uy', '.edu.sg', '.ac.jp', '.ac.nz',
                '.ac.za', '.edu.br', '.edu.mx', '.ac.ir', '.ac.in', '.edu.tr', '.edu.sa')
IGO_HOSTS = (
    'worldbank.org', 'unesco.org', 'unicef.org', 'unhcr.org', 'unrwa.org', 'un.org',
    'oecd.org', 'oecd-ilibrary.org', 'iea.nl', 'uis.unesco.org', 'undp.org', 'wfp.org',
    'who.int', 'ilo.org', 'iom.int', 'confemen.org', 'adb.org', 'afdb.org', 'ebrd.com',
    'eurydice.eacea.ec.europa.eu', 'cedefop.europa.eu',
)
OWN_HOSTS = ('education3881.github.io',)


def party(url):
    """OFFICIAL | OURS | OTHER | UNKNOWN. Positive identification only."""
    h = (urlparse(url).hostname or '').lower()
    if not h:
        return 'UNKNOWN'
    if h in OWN_HOSTS or any(h.endswith('.' + o) or h == o for o in OWN_HOSTS):
        return 'OURS'
    if any(h == s.lstrip('.') or h.endswith(s) for s in GOV_SUFFIXES):
        return 'OFFICIAL'
    if any(h == s.lstrip('.') or h.endswith(s) for s in EDU_SUFFIXES):
        return 'OFFICIAL'
    if any(h == g or h.endswith('.' + g) for g in IGO_HOSTS):
        return 'OFFICIAL'
    return 'OTHER'


def fmt_from(url, ctype):
    """PDF | HTML | OTHER | UNFETCHED. ctype wins; the URL is the fallback."""
    c = (ctype or '').split(';')[0].strip().lower()
    if c == 'application/pdf':
        return 'PDF'
    if c in ('text/html', 'application/xhtml+xml'):
        return 'HTML'
    if c:
        return 'OTHER'
    u = url.lower().split('?')[0]
    if u.endswith('.pdf'):
        return 'PDF'
    if u.endswith(('.csv', '.xlsx', '.xls', '.doc', '.docx', '.zip')):
        return 'OTHER'
    return 'UNFETCHED'


def pct(n, d):
    return '--' if not d else '%.1f%%' % (100.0 * n / d)


def table(rows, header):
    w = [max(len(str(r[i])) for r in [header] + rows) for i in range(len(header))]
    out = ['  ' + '  '.join(str(header[i]).ljust(w[i]) for i in range(len(header)))]
    out.append('  ' + '  '.join('-' * w[i] for i in range(len(header))))
    for r in rows:
        out.append('  ' + '  '.join(str(r[i]).ljust(w[i]) for i in range(len(header))))
    return '\n'.join(out)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    cr_p = os.path.join(root, 'agents/stats/claim-registers.json')
    ci_p = os.path.join(root, 'agents/stats/citation-identity.json')
    for p in (cr_p, ci_p):
        if not os.path.exists(p):
            print('REFUSED register_coverage — missing %s' % p)
            return 4

    cr = json.load(open(cr_p, encoding='utf-8'))
    ci = json.load(open(ci_p, encoding='utf-8'))
    crr, cir = cr['registers'], ci['registers']

    # citation-identity carries ctype; claim-registers does not. Join on url so the archival
    # half can be classified by the format the OTHER instrument observed.
    #
    # AND THE LABEL MATTERS. A claim-registers row whose URL is not in citation-identity at all
    # has no observed format because NOBODY ASKED - citation-identity only covers the
    # quotation-bearing registers. Calling that `UNFETCHED` would report our own scope as a
    # failed fetch, which is the 2026-09-14 trap (an assertion reading its answer off the field
    # it supplements) in a column header. The two states are kept apart.
    ctype_by_url = {r['url']: r.get('ctype') for r in cir}
    asked = set(ctype_by_url)

    print('register_coverage — coverage PER CLASS, not one rate over the union')
    print('  standing-queue item 34, raised 2026-10-22, taken at the head 2026-11-06')
    print('  claim-registers.json observed %s, %d rows' % (cr.get('observed'), len(crr)))
    print('  citation-identity.json observed %s, %d rows' % (ci.get('observed'), len(cir)))
    print('  PRINTED AND NOT ASSERTED. The reason is in this file\'s header and it is the row\'s own:')
    print('  the ask is a measurement, and a floor above today\'s per-class coverage would red')
    print('  every build until somebody else\'s PDF became readable (#93).')
    print()

    # ---------------- 1 · the archival half, per class --------------------------------------
    print('1 · ARCHIVAL COVERAGE (qa_claim_registers, #111) BY CLASS')
    print('    `archived` means an archive holds a snapshot. The published rate is one number')
    print('    over the union; these are the classes inside it.')
    print()
    for key, label in (('fmt', 'format'), ('party', 'publisher')):
        buckets = collections.defaultdict(lambda: collections.Counter())
        for r in crr:
            if key == 'fmt':
                if r['url'] not in asked:
                    k = 'NOT-ASKED'
                else:
                    k = fmt_from(r['url'], ctype_by_url.get(r['url']))
            else:
                k = party(r['url'])
            buckets[k][r.get('state')] += 1
            buckets[k]['n'] += 1
        rows = []
        for k in sorted(buckets, key=lambda x: -buckets[x]['n']):
            b = buckets[k]
            n = b['n']
            arch = b['archived'] + b['cited-as-archive']
            rows.append([k, n, arch, pct(arch, n), b['live-only'],
                         b['walled-no-snapshot'], b['GONE']])
        tot = sum(b['n'] for b in buckets.values())
        ta = sum(b['archived'] + b['cited-as-archive'] for b in buckets.values())
        rows.append(['ALL', tot, ta, pct(ta, tot),
                     sum(b['live-only'] for b in buckets.values()),
                     sum(b['walled-no-snapshot'] for b in buckets.values()),
                     sum(b['GONE'] for b in buckets.values())])
        print('  by %s:' % label)
        print(table(rows, ['class', 'rows', 'archived', 'rate', 'live-only', 'walled', 'gone']))
        print()

    # ---------------- 2 · the identity half, per class --------------------------------------
    print('2 · QUOTATION-IDENTITY COVERAGE (qa_citation_identity, #112) BY CLASS')
    print('    comparable = the register has at least one token we could actually compare')
    print('    (verdict `found` or `absent`). declined = every token came back')
    print('    `script-mismatch`, or the fetch failed. failing = at least one `absent`.')
    print()

    def classify_reg(r):
        verds = [t.get('verdict') for t in (r.get('tokens') or [])]
        comparable = any(v in ('found', 'absent') for v in verds)
        failing = any(v == 'absent' for v in verds)
        return comparable, failing, len(verds)

    for key, label in (('fmt', 'format'), ('party', 'publisher')):
        buckets = collections.defaultdict(lambda: collections.Counter())
        for r in cir:
            k = (fmt_from(r['url'], r.get('ctype')) if key == 'fmt' else party(r['url']))
            comparable, failing, ntok = classify_reg(r)
            b = buckets[k]
            b['n'] += 1
            b['tokens'] += ntok
            if comparable:
                b['comparable'] += 1
                if failing:
                    b['failing'] += 1
            if r.get('note'):
                b['fetch_failed'] += 1
        rows = []
        for k in sorted(buckets, key=lambda x: -buckets[x]['n']):
            b = buckets[k]
            rows.append([k, b['n'], b['tokens'], b['comparable'], pct(b['comparable'], b['n']),
                         b['failing'], pct(b['failing'], b['comparable']), b['fetch_failed']])
        t = collections.Counter()
        for b in buckets.values():
            t.update(b)
        rows.append(['ALL', t['n'], t['tokens'], t['comparable'], pct(t['comparable'], t['n']),
                     t['failing'], pct(t['failing'], t['comparable']), t['fetch_failed']])
        print('  by %s:' % label)
        print(table(rows, ['class', 'regs', 'tokens', 'comparable', 'cov', 'failing',
                           'fail-rate', 'fetch-fail']))
        print()

    # ---------------- 3 · the row's own hypothesis, tested ----------------------------------
    print('3 · THE ROW\'S HYPOTHESIS, TESTED RATHER THAN REPEATED')
    print('    The row says the comparable population is "systematically the journalism and')
    print('    systematically not the primary sources this publication\'s whole method rests on."')
    print()
    off_n = off_c = oth_n = oth_c = 0
    for r in cir:
        p = party(r['url'])
        comparable, _, _ = classify_reg(r)
        if p in ('OFFICIAL', 'OURS'):
            off_n += 1
            off_c += 1 if comparable else 0
        else:
            oth_n += 1
            oth_c += 1 if comparable else 0
    print('    OFFICIAL/OURS .... %3d registers, %3d comparable (%s)' % (off_n, off_c, pct(off_c, off_n)))
    print('    OTHER ............ %3d registers, %3d comparable (%s)' % (oth_n, oth_c, pct(oth_c, oth_n)))
    share = pct(oth_c, off_c + oth_c)
    print('    So %s of everything the identity instrument can actually compare sits on a host'
          % share)
    print('    this rule cannot identify as official.')
    print()

    # ---------------- 4 · the finer partition this morning forced ---------------------------
    print('4 · THE PARTITION IS NOT FINE ENOUGH, AND A LIVE CASE SAYS SO (2026-11-06, content)')
    print('    This morning the content function read both language editions of ONE first-party')
    print('    PDF series. The 24-25 Arabic report carries 17 /ToUnicode CMaps and extracts to')
    print('    63,344 characters; the English edition we CITE carries 80 cmap glyphs against the')
    print('    Arabic edition\'s 207 and drops whole words and figures; and the AY 2025-2026')
    print('    report on the same index carries ZERO /ToUnicode CMaps and extracts to 3,565')
    print('    characters of unanchored numerals over 39 pages.')
    print('    Three documents, one publisher, one series, one format - and `PDF` holds all three.')
    print('    So the honest next unit is not the format but WHETHER THE TEXT LAYER IS PRESENT,')
    print('    which no register on disk records and which costs one fetch per PDF to learn.')
    pdfs = [r for r in cir if fmt_from(r['url'], r.get('ctype')) == 'PDF']
    pdf_off = sum(1 for r in pdfs if party(r['url']) in ('OFFICIAL', 'OURS'))
    print('    Population that question would have to ask: %d PDF registers in citation-identity,'
          % len(pdfs))
    print('    %d of them on a host this rule calls official.' % pdf_off)
    print()
    print('  the party rule, so it can be disagreed with by looking: %d gov suffixes, %d edu'
          % (len(GOV_SUFFIXES), len(EDU_SUFFIXES)))
    print('  suffixes, %d intergovernmental hosts, %d of our own. Positive identification only:'
          % (len(IGO_HOSTS), len(OWN_HOSTS)))
    print('  nothing in a hostname identifies journalism, so OTHER means not-identified-as-official')
    print('  and never means journalism.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
