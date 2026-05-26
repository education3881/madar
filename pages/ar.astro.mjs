import { o as createComponent, s as renderComponent, w as renderTemplate, r as maybeRenderHead, e as Fragment, B as unescapeHTML, m as addAttribute } from '../chunks/astro/server_DbByELL0.mjs';
import 'piccolore';
import { $ as $$Base } from '../chunks/Base_Bh3GLTX8.mjs';
import { g as getCollection } from '../chunks/_astro_content_CGwa19GH.mjs';
import { existsSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';
/* empty css                                 */
export { renderers } from '../renderers.mjs';

const $$Index = createComponent(async ($$result, $$props, $$slots) => {
  const arPieces = await getCollection("articles-ar", ({ data }) => data.approved !== false);
  const enPieces = await getCollection("articles", ({ data }) => data.approved !== false);
  const sortedAr = arPieces.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
  const sortedEn = enPieces.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
  const dateFormatterAr = new Intl.DateTimeFormat("ar-EG", {
    year: "numeric",
    month: "long",
    day: "numeric"
  });
  const __filename = fileURLToPath(import.meta.url);
  const __dirname = dirname(__filename);
  const wordmarkPath = resolve(__dirname, "../../../public/wordmark/madar-wordmark.svg");
  let wordmarkSvg = null;
  if (existsSync(wordmarkPath)) {
    try {
      wordmarkSvg = readFileSync(wordmarkPath, "utf-8").replace(/^<\?xml[^?]*\?>\s*/, "").replace(/<!--[\s\S]*?-->/g, "");
    } catch {
      wordmarkSvg = null;
    }
  }
  const jordan = sortedEn.find((p) => p.id === "2026-05-25-jordan-double-shift");
  const jordanExcerpts = jordan ? [
    { ar: "\u062A\u0622\u0643\u0644 \u0627\u0644\u0645\u0628\u0627\u0646\u064A", en: "building fatigue" },
    { ar: "\u062F\u0648\u0627\u0645 \u0627\u0644\u062A\u0631\u062A\u064A\u0628 \u0627\u0644\u0645\u0624\u0642\u062A", en: "the permanence of the temporary arrangement" }
  ] : [];
  return renderTemplate`${renderComponent($$result, "Base", $$Base, { "title": "\u0645\u062F\u0627\u0631 \u2014 \u0627\u0644\u062A\u0639\u0644\u064A\u0645\u060C \u0628\u062A\u0623\u0646\u064D\u0651\u060C \u0628\u0644\u063A\u062A\u064A\u0646", "lang": "ar", "noHeader": true, "data-astro-cid-7ksm7tax": true }, { "default": async ($$result2) => renderTemplate`${maybeRenderHead()}<div class="top-bar" data-astro-cid-7ksm7tax> <div class="top-bar__inner container" data-astro-cid-7ksm7tax> <div class="top-bar__left" data-astro-cid-7ksm7tax> <span lang="ar" dir="rtl" data-astro-cid-7ksm7tax>العدد ٠١ · مايو ٢٠٢٦ · مدار</span> </div> <div class="top-bar__right" data-astro-cid-7ksm7tax> <span class="top-bar__lang" data-astro-cid-7ksm7tax> <a href="/" lang="en" data-astro-cid-7ksm7tax>EN</a> <span aria-hidden="true" data-astro-cid-7ksm7tax>·</span> <a href="/ar/" class="is-active" lang="ar" dir="rtl" data-astro-cid-7ksm7tax>عربي</a> </span> </div> </div> </div> <header class="masthead" data-astro-cid-7ksm7tax> <div class="masthead__inner container" data-astro-cid-7ksm7tax> <a href="/ar/" class="masthead__mark" aria-label="مدار — الرئيسية" data-astro-cid-7ksm7tax> ${wordmarkSvg ? renderTemplate`${renderComponent($$result2, "Fragment", Fragment, {}, { "default": async ($$result3) => renderTemplate`${unescapeHTML(wordmarkSvg)}` })}` : renderTemplate`<span class="masthead__fallback" lang="ar" dir="rtl" data-astro-cid-7ksm7tax>مدار</span>`} </a> <div class="masthead__rule" aria-hidden="true" data-astro-cid-7ksm7tax></div> <p class="masthead__tagline" lang="ar" dir="rtl" data-astro-cid-7ksm7tax>
التعليم، بتأنٍّ، بلغتين
</p> </div> </header> <section class="section container" data-astro-cid-7ksm7tax> <div class="section__head" data-astro-cid-7ksm7tax> <span class="section__kicker" lang="ar" dir="rtl" data-astro-cid-7ksm7tax>الأحدث</span> <span class="section__meta" data-astro-cid-7ksm7tax>Issue 01 · 2026 · 05 · 25</span> </div> ${sortedAr.length === 0 && renderTemplate`<div class="placeholder" data-astro-cid-7ksm7tax> <p lang="ar" dir="rtl" class="placeholder__lead" data-astro-cid-7ksm7tax>
لم يصدر بعد عددٌ عربيٌّ مكتمل. حتى ذلك الحين، يمكنك قراءة المقالات الإنجليزية على
<a href="/" data-astro-cid-7ksm7tax>الصفحة الإنجليزية</a>.
</p> <p lang="ar" dir="rtl" class="muted" data-astro-cid-7ksm7tax>
القطعةُ الثانيةُ في العدد الأول — عن نظام الدوامَين في المدارس الأردنية — تحملُ مقاطعَ
          عربيةً مقتبسةً من مذكّرة الوزارة، وقد جُمعت هنا للقارئ العربيّ ريثما تكتمل النسخةُ الكاملة.
</p> </div>`} ${sortedAr.length > 0 && renderTemplate`<ul class="piece-list" data-astro-cid-7ksm7tax> ${sortedAr.map((piece) => renderTemplate`<li class="piece" data-astro-cid-7ksm7tax> <a${addAttribute(`/ar/articles/${piece.id}/`, "href")} class="piece__link" data-astro-cid-7ksm7tax> <span class="piece__meta" data-astro-cid-7ksm7tax> <span class="piece__country" lang="ar" dir="rtl" data-astro-cid-7ksm7tax>${piece.data.country}</span> <span class="piece__date" data-astro-cid-7ksm7tax>${dateFormatterAr.format(piece.data.date)}</span> </span> <h2 class="piece__title" lang="ar" dir="rtl" data-astro-cid-7ksm7tax>${piece.data.title}</h2> ${piece.data.dek && renderTemplate`<p class="piece__dek" lang="ar" dir="rtl" data-astro-cid-7ksm7tax>${piece.data.dek}</p>`} </a> </li>`)} </ul>`} </section> ${jordanExcerpts.length > 0 && renderTemplate`<section class="excerpts container" data-astro-cid-7ksm7tax> <div class="excerpts__head" data-astro-cid-7ksm7tax> <p class="kicker" data-astro-cid-7ksm7tax>From the issue</p> <p class="excerpts__lead" lang="ar" dir="rtl" data-astro-cid-7ksm7tax>
مقاطعُ عربيّةٌ مقتبسةٌ من القطعة الأردنية في العدد الأول — لقراءة النصّ كاملاً
<a${addAttribute(`/articles/${jordan.id}/`, "href")} data-astro-cid-7ksm7tax>اقرأ المقالة بالإنجليزية</a>.
</p> </div> <ul class="excerpts__list" data-astro-cid-7ksm7tax> ${jordanExcerpts.map((ex) => renderTemplate`<li class="excerpt" data-astro-cid-7ksm7tax> <p class="excerpt__ar" lang="ar" dir="rtl" data-astro-cid-7ksm7tax>${ex.ar}</p> <p class="excerpt__en" data-astro-cid-7ksm7tax>— ${ex.en}</p> </li>`)} </ul> </section>`}<section class="about container" data-astro-cid-7ksm7tax> <div class="about__head" data-astro-cid-7ksm7tax> <p class="about__label" lang="ar" dir="rtl" data-astro-cid-7ksm7tax>عن مدار</p> </div> <div class="about__body" lang="ar" dir="rtl" data-astro-cid-7ksm7tax> <p data-astro-cid-7ksm7tax>
«مدار» مجلّةٌ تحريريّةٌ بطيئةُ الإيقاع تَتناولُ التعليمَ في مرحلتَيِ الطفولةِ
        المبكّرةِ والتعليمِ العامّ، تَصدرُ بالعربيّةِ والإنجليزيّة. ننشرُ نوعَين من
        المواد: <em data-astro-cid-7ksm7tax>تقاريرَ ميدانيّة</em> نَكتبُها بأنفسنا، و<em data-astro-cid-7ksm7tax>قراءاتٍ مختاَرة</em>
لمصدرٍ واحدٍ يَستحقّ الإصغاء. أداةُ بحثٍ، لا مجلّةً.
</p> <p data-astro-cid-7ksm7tax>
نكتبُ من مدارٍ واحدٍ بلغتَين، ولكلٍّ منهما وزنُها الخاصّ.
</p> </div> </section> ` })} `;
}, "/sessions/keen-lucid-shannon/mnt/Educational Website/web/src/pages/ar/index.astro", void 0);

const $$file = "/sessions/keen-lucid-shannon/mnt/Educational Website/web/src/pages/ar/index.astro";
const $$url = "/ar";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Index,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
