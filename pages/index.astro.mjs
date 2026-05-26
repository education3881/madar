import { o as createComponent, s as renderComponent, w as renderTemplate, r as maybeRenderHead, m as addAttribute, e as Fragment } from '../chunks/astro/server_DbByELL0.mjs';
import 'piccolore';
import { $ as $$Base } from '../chunks/Base_Bh3GLTX8.mjs';
import { g as getCollection } from '../chunks/_astro_content_CGwa19GH.mjs';
/* empty css                                 */
export { renderers } from '../renderers.mjs';

const $$Index = createComponent(async ($$result, $$props, $$slots) => {
  const all = await getCollection("articles", ({ data }) => data.approved !== false);
  const sorted = all.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
  const LEAD_SLUG = "2026-05-25-bo-teacher-chalk";
  const lead = sorted.find((p) => p.id === LEAD_SLUG) ?? sorted[0];
  const secondary = sorted.filter((p) => p && p.id !== lead?.id);
  const dateFormatter = new Intl.DateTimeFormat("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric"
  });
  const placeholder = sorted.length === 0;
  function hasProvisionalSources(p) {
    return p.data.sources.some((s) => /PLACEHOLDER SOURCE/i.test(s.title));
  }
  const fieldLabel = {
    curated: "Curated",
    short: "Field Note",
    essay: "Essay"
  };
  function kickerFor(piece, i) {
    const num = String(i + 1).padStart(2, "0");
    const label = fieldLabel[piece.data.type] ?? "Piece";
    const register = piece.data.type === "curated" ? "Curated" : "Editorial";
    return `${label} ${num} \xB7 ${register}`;
  }
  return renderTemplate`${renderComponent($$result, "Base", $$Base, { "title": "Mad\u0101r \xB7 \u0645\u062F\u0627\u0631 \u2014 Issue 01", "lang": "en", "noHeader": true, "data-astro-cid-j7pv25f6": true }, { "default": async ($$result2) => renderTemplate`${maybeRenderHead()}<div class="top-bar" data-astro-cid-j7pv25f6> <div class="top-bar__inner container" data-astro-cid-j7pv25f6> <div class="top-bar__left" data-astro-cid-j7pv25f6>
Issue 01 · May 2026 <span lang="ar" dir="rtl" data-astro-cid-j7pv25f6>· مدار</span> </div> <div class="top-bar__right" data-astro-cid-j7pv25f6> <span class="top-bar__meta" data-astro-cid-j7pv25f6>A research instrument</span> <span class="top-bar__lang" data-astro-cid-j7pv25f6> <a href="/" class="is-active" lang="en" data-astro-cid-j7pv25f6>EN</a> <span aria-hidden="true" data-astro-cid-j7pv25f6>·</span> <a href="/ar/" lang="ar" dir="rtl" data-astro-cid-j7pv25f6>عربي</a> </span> </div> </div> </div> <header class="masthead" data-astro-cid-j7pv25f6> <div class="masthead__inner container" data-astro-cid-j7pv25f6> <a href="/" class="masthead__mark" aria-label="Madār — home" data-astro-cid-j7pv25f6> <img src="/wordmark/madar-wordmark.svg" alt="Madār مدار" class="masthead__wordmark" data-astro-cid-j7pv25f6> </a> <div class="masthead__rule" aria-hidden="true" data-astro-cid-j7pv25f6></div> <p class="masthead__tagline" data-astro-cid-j7pv25f6>
Education, written slowly, in two languages
<span class="masthead__tagline-ar" lang="ar" dir="rtl" data-astro-cid-j7pv25f6>التعليم، بتأنٍّ، بلغتين</span> </p> </div> </header> <p class="wordmark-note container" data-astro-cid-j7pv25f6>[ Placeholder wordmark v0.2 — path-outlined, font-independent · to be replaced by commissioned mark ]</p> <section class="section container" data-astro-cid-j7pv25f6> <div class="section__head" data-astro-cid-j7pv25f6> <div class="section__head-left" data-astro-cid-j7pv25f6> <span class="section__kicker" data-astro-cid-j7pv25f6>This week</span> <span class="section__kicker-ar" lang="ar" dir="rtl" data-astro-cid-j7pv25f6>هذا الأسبوع</span> </div> <div class="section__meta" data-astro-cid-j7pv25f6>
Issue 01 · 2026 · 05 · 25 · ${sorted.length} piece${sorted.length === 1 ? "" : "s"} </div> </div> ${placeholder && renderTemplate`<div class="placeholder" data-astro-cid-j7pv25f6> <p class="uppercase muted" data-astro-cid-j7pv25f6>Pre-launch</p> <h2 data-astro-cid-j7pv25f6>The publication has not yet published its first piece.</h2> <p class="muted measure" data-astro-cid-j7pv25f6>
When the Editor's seed pieces are approved by the founder, they appear here.
          Until then, this page is a deliberate blank — a reminder that nothing ships
          before it passes the quality bar.
</p> </div>`} ${!placeholder && lead && (() => {
    const draft = hasProvisionalSources(lead);
    const kicker = kickerFor(lead, 0);
    const thumb = lead.data.hero?.src ?? `/stills/${lead.id}.svg`;
    const alt = lead.data.hero?.alt ?? lead.data.title;
    return renderTemplate`<article class="lead" data-astro-cid-j7pv25f6> <a${addAttribute(`/articles/${lead.id}/`, "href")} class="lead__thumb"${addAttribute(`Read this issue's lead \u2014 ${lead.data.title}`, "aria-label")} data-astro-cid-j7pv25f6> <img${addAttribute(thumb, "src")}${addAttribute(alt, "alt")} width="800" height="500" loading="eager" decoding="async" data-astro-cid-j7pv25f6> </a> <div class="lead__body" data-astro-cid-j7pv25f6> <span class="lead__label" data-astro-cid-j7pv25f6>Read this issue's lead</span> <div class="lead__meta" data-astro-cid-j7pv25f6> <span class="lead__type" data-astro-cid-j7pv25f6>${kicker}</span> <span class="lead__country" data-astro-cid-j7pv25f6>${lead.data.country}</span> </div> <h2 class="lead__title" data-astro-cid-j7pv25f6> <a${addAttribute(`/articles/${lead.id}/`, "href")} data-astro-cid-j7pv25f6>${lead.data.title}</a> </h2> ${lead.data.dek && renderTemplate`<p class="lead__dek" data-astro-cid-j7pv25f6>${lead.data.dek}</p>`} <div class="lead__byline" data-astro-cid-j7pv25f6>
By The Editors · ${dateFormatter.format(lead.data.date)} ${draft && renderTemplate`${renderComponent($$result2, "Fragment", Fragment, { "data-astro-cid-j7pv25f6": true }, { "default": async ($$result3) => renderTemplate`${" \xB7 "}<span class="pill" data-astro-cid-j7pv25f6>Draft — pending source verification</span> ` })}`} </div> <a class="lead__read"${addAttribute(`/articles/${lead.id}/`, "href")} data-astro-cid-j7pv25f6>Read the lead piece →</a> </div> </article>`;
  })()} ${!placeholder && secondary.length > 0 && renderTemplate`<section class="also" data-astro-cid-j7pv25f6> <div class="also__head" data-astro-cid-j7pv25f6> <div data-astro-cid-j7pv25f6> <span class="also__label" data-astro-cid-j7pv25f6>Also this issue</span> <span class="also__label-ar" lang="ar" dir="rtl" data-astro-cid-j7pv25f6>من هذا العدد أيضاً</span> </div> <div class="also__meta" data-astro-cid-j7pv25f6> ${secondary.length} piece${secondary.length === 1 ? "" : "s"} · Issue 01
</div> </div> <div class="also__grid" data-astro-cid-j7pv25f6> ${secondary.map((piece, i) => {
    const draft = hasProvisionalSources(piece);
    const kicker = kickerFor(piece, i + 1);
    const thumb = piece.data.hero?.src ?? `/stills/${piece.id}.svg`;
    const alt = piece.data.hero?.alt ?? piece.data.title;
    return renderTemplate`<article class="secondary" data-astro-cid-j7pv25f6> <a${addAttribute(`/articles/${piece.id}/`, "href")} class="secondary__thumb"${addAttribute(`Also this issue \u2014 ${piece.data.title}`, "aria-label")} data-astro-cid-j7pv25f6> <img${addAttribute(thumb, "src")}${addAttribute(alt, "alt")} width="360" height="240" loading="lazy" decoding="async" data-astro-cid-j7pv25f6> </a> <div class="secondary__body" data-astro-cid-j7pv25f6> <div class="secondary__meta" data-astro-cid-j7pv25f6> <span class="secondary__type" data-astro-cid-j7pv25f6>${kicker}</span> <span class="secondary__country" data-astro-cid-j7pv25f6>${piece.data.country}</span> </div> <h3 class="secondary__title" data-astro-cid-j7pv25f6> <a${addAttribute(`/articles/${piece.id}/`, "href")} data-astro-cid-j7pv25f6>${piece.data.title}</a> </h3> ${piece.data.dek && renderTemplate`<p class="secondary__dek" data-astro-cid-j7pv25f6>${piece.data.dek}</p>`} <div class="secondary__byline" data-astro-cid-j7pv25f6>
By The Editors · ${dateFormatter.format(piece.data.date)} ${draft && renderTemplate`${renderComponent($$result2, "Fragment", Fragment, { "data-astro-cid-j7pv25f6": true }, { "default": async ($$result3) => renderTemplate`${" \xB7 "}<span class="pill" data-astro-cid-j7pv25f6>Draft — pending source verification</span> ` })}`} </div> </div> </article>`;
  })} </div> </section>`} </section> <div class="macron-divider" aria-hidden="true" data-astro-cid-j7pv25f6> <span class="macron-divider__rule" data-astro-cid-j7pv25f6></span> </div> <section class="about container" data-astro-cid-j7pv25f6> <div class="about__head" data-astro-cid-j7pv25f6> <p class="about__label" data-astro-cid-j7pv25f6>About</p> <p class="about__label-ar" lang="ar" dir="rtl" data-astro-cid-j7pv25f6>عن مدار</p> </div> <div class="about__body" data-astro-cid-j7pv25f6> <div class="about__col en" data-astro-cid-j7pv25f6> <p data-astro-cid-j7pv25f6>
Madār is a slow-cadence editorial publication on early childhood and
          K-12 education, written in English and Arabic. We publish two kinds of
          pieces: <em data-astro-cid-j7pv25f6>field notes</em> we report ourselves, and <em data-astro-cid-j7pv25f6>curated
          readings</em> of one carefully-chosen source worth listening to. Two
          to three pieces an issue. One issue a month. A research instrument,
          not a magazine.
</p> <p data-astro-cid-j7pv25f6> <a href="/about/" class="about__more" data-astro-cid-j7pv25f6>Read the About page →</a> </p> </div> <div class="about__col ar" lang="ar" dir="rtl" data-astro-cid-j7pv25f6> <p data-astro-cid-j7pv25f6>
«مدار» مجلّةٌ تحريريّةٌ بطيئةُ الإيقاع تَتناولُ التعليمَ في مرحلتَيِ
          الطفولةِ المبكّرةِ والتعليمِ العامّ، تَصدرُ بالعربيّةِ والإنجليزيّة.
          نَنشرُ نوعَين من المواد: <em data-astro-cid-j7pv25f6>تقاريرَ ميدانيّة</em> نَكتبُها بأنفسنا،
          و<em data-astro-cid-j7pv25f6>قراءاتٍ مختاَرة</em> لمصدرٍ واحدٍ يَستحقّ الإصغاء. قطعتان أو ثلاث
          في كلّ عدد. عددٌ واحدٌ كلّ شهر. أداةُ بحثٍ، لا مجلّةً.
</p> <p data-astro-cid-j7pv25f6> <a href="/ar/" class="about__more" data-astro-cid-j7pv25f6>اقرأ صفحةَ «عن مدار» ←</a> </p> </div> </div> </section> ` })} `;
}, "/sessions/keen-lucid-shannon/mnt/Educational Website/web/src/pages/index.astro", void 0);

const $$file = "/sessions/keen-lucid-shannon/mnt/Educational Website/web/src/pages/index.astro";
const $$url = "";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Index,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
