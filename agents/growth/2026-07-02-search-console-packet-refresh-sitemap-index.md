# Growth — Search Console packet refreshed for the generated sitemap (2026-07-02)

**From:** Growth · **Posture:** privacy-clean, discoverability only, no tracker.

## What changed today and why Growth cares

Quality landed the `@astrojs/sitemap` integration this run: the sitemap is now **build-generated** (`sitemap-index.xml` → `sitemap-0.xml`, 41 URLs, EN↔AR hreflang pairs emitted automatically), and `robots.txt` now advertises `sitemap-index.xml`. The bilingual discoverability surface — our single largest structural growth asset (Arabic is a distribution advantage) — no longer depends on a hand-patched file that drifted seven times.

## The refreshed one-action packet (supersedes the submission URL in `2026-06-07-search-console-sitemap-submission-packet.md`)

The 06-07 packet remains correct in every step **except the sitemap URL**. When the submission action fires, submit:

- ~~`https://education3881.github.io/madar/sitemap.xml`~~ → **`https://education3881.github.io/madar/sitemap-index.xml`**

(The legacy `/sitemap.xml` URL still resolves — it is now a stub index delegating to `sitemap-0.xml` — so nothing that bookmarked it breaks; but the index is the canonical submission target.)

## Standing sequence (unchanged, decision-gated, not time-gated)

Per the 2026-06-12 domain memo and the URL-binding ruling: **the domain decision fires before Search Console binds to a URL.** This packet is send-ready for whichever URL wins. Submitting under the github.io URL before the domain call would create the exact double-migration the ruling warns about — so the packet waits on that one founder decision, and says so honestly rather than counting a submission we haven't made.

## Grid note (after the six dark days)

The opening grid's last reconciled schedule (06-24) has lapsed — 06-26→07-01 produced no posts. The Mon/Wed/Fri cadence restarts w/c **2026-07-06**; the queue is already stocked (Korea, Egypt, Philippines, Oman, Brazil packets all shipped and unposted). No new asset needed today; the bottleneck is the posting action, not the material — flagged for the weekly's growth-bet slot.
