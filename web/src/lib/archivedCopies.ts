/**
 * archivedCopies — a second route to a citation the reader can still open.
 *
 * Growth, 2026-10-21, under ruling #111. This publication's whole argument for
 * being worth returning to is that every figure stands on a named primary
 * source the reader can open. Today's measurement put a number on how fragile
 * that is: of 342 cited registers, 205 have been asked and **40 of those hold
 * no snapshot anywhere**, twelve of them refusing us as well. The other side of
 * the same measurement is the asset: **165 registers ARE snapshotted**, and the
 * reader was never told.
 *
 * So where `agents/stats/claim-registers.json` records a snapshot, the source
 * list offers it beside the live link. A ministry PDF that 404s next year stops
 * taking a figure with it, and the reader who follows a source — the reader who
 * was going to come back — keeps the route.
 *
 * DESIGN NOTES, because two of these are load-bearing:
 *  - The live register is always FIRST and always the link on the title. The
 *    archive is an offer, never a substitute: a cached copy is evidence about
 *    what a page said, and the owner's own URL is what the piece cites.
 *  - This emits an `<a href>` to an origin we do not own, which
 *    `qa_third_party_origins` counts and prints and deliberately does not
 *    assert — the classification is *by who initiates the fetch*, and a reader
 *    clicking a link is not this page fetching anything. Nothing is loaded
 *    automatically; no image, no script, no font.
 *  - The register may be absent (a fresh clone that has not run `--emit`) and
 *    the build must not care. Missing register == no archive offers.
 */
import { readFileSync } from 'node:fs';

type Row = { url: string; archived?: boolean | null; snapshot?: string; state?: string };

const PATHS = ['../agents/stats/claim-registers.json', 'agents/stats/claim-registers.json'];

function load(): Map<string, string> {
  for (const p of PATHS) {
    try {
      const data = JSON.parse(readFileSync(p, 'utf-8')) as { registers?: Row[] };
      const out = new Map<string, string>();
      for (const row of data.registers ?? []) {
        if (row.archived === true && row.snapshot && /^\d{4}-\d{2}-\d{2}$/.test(row.snapshot)) {
          out.set(row.url, row.snapshot);
        }
      }
      return out;
    } catch {
      /* try the next path */
    }
  }
  return new Map();
}

const SNAPSHOTS = load();

/** The date of the archived copy, or null if no archive is known to hold one. */
export function snapshotDate(url: string): string | null {
  return SNAPSHOTS.get(url) ?? null;
}

/** A link to the snapshot nearest the date we observed. */
export function snapshotUrl(url: string): string | null {
  const date = SNAPSHOTS.get(url);
  if (!date) return null;
  return `https://web.archive.org/web/${date.replace(/-/g, '')}/${url}`;
}

/** How many of a piece's registers we can offer a second route to. */
export function archivedCount(urls: string[]): number {
  return urls.filter((u) => SNAPSHOTS.has(u)).length;
}
