import { n as createAstro, o as createComponent, s as renderComponent, w as renderTemplate, r as maybeRenderHead, e as Fragment, m as addAttribute } from '../../chunks/astro/server_DbByELL0.mjs';
import 'piccolore';
import { $ as $$Base, a as $$SiteHeader } from '../../chunks/Base_Bh3GLTX8.mjs';
import { r as renderEntry, g as getCollection } from '../../chunks/_astro_content_CGwa19GH.mjs';
/* empty css                                     */
export { renderers } from '../../renderers.mjs';

const $$Astro = createAstro("https://example.github.io");
async function getStaticPaths() {
  const all = await getCollection("articles", ({ data }) => data.approved !== false);
  return all.map((piece) => ({
    params: { slug: piece.id },
    props: { piece }
  }));
}
const $$ = createComponent(async ($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$;
  const { piece } = Astro2.props;
  const { Content } = await renderEntry(piece);
  const dateFormatter = new Intl.DateTimeFormat("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric"
  });
  const sourcesAreProvisional = piece.data.sources.some(
    (s) => /PLACEHOLDER SOURCE/i.test(s.title)
  );
  const stillSrc = piece.data.hero?.src ?? `/stills/${piece.id}.svg`;
  const stillAlt = piece.data.hero?.alt ?? "";
  const stillCaption = piece.data.hero?.caption ?? `\u0633\u0643\u0648\u0646 \xB7 The Still`;
  const fieldLabel = {
    curated: "Curated",
    short: "Field Note",
    essay: "Essay"
  }[piece.data.type] ?? "Piece";
  return renderTemplate`${renderComponent($$result, "Base", $$Base, { "title": `${piece.data.title} \u2014 Mad\u0101r`, "description": piece.data.dek, "lang": "en", "ogImage": piece.data.hero?.src, "noHeader": true, "data-astro-cid-c7vabzjd": true }, { "default": async ($$result2) => renderTemplate` ${renderComponent($$result2, "SiteHeader", $$SiteHeader, { "lang": "en", "variant": "article", "data-astro-cid-c7vabzjd": true })} ${maybeRenderHead()}<article class="article container" data-astro-cid-c7vabzjd>  <header class="title-block" data-astro-cid-c7vabzjd> <div class="title-block__meta" data-astro-cid-c7vabzjd> <p class="kicker" data-astro-cid-c7vabzjd> ${fieldLabel} · ${piece.data.type === "curated" ? "Curated" : "Editorial"} </p> <p class="kicker-meta" data-astro-cid-c7vabzjd> <span data-astro-cid-c7vabzjd>By The Editors</span><br data-astro-cid-c7vabzjd> <span data-astro-cid-c7vabzjd>${dateFormatter.format(piece.data.date)}</span><br data-astro-cid-c7vabzjd> <span data-astro-cid-c7vabzjd>${piece.data.country} · ${piece.data.region}</span><br data-astro-cid-c7vabzjd> <span data-astro-cid-c7vabzjd>${piece.data.themes.slice(0, 2).join(" \xB7 ")}</span> </p> ${sourcesAreProvisional && renderTemplate`<p class="title-block__draft" data-astro-cid-c7vabzjd> <span class="pill" data-astro-cid-c7vabzjd>Draft — pending source verification</span> </p>`} </div> <div class="title-block__title" data-astro-cid-c7vabzjd> <h1 class="title" data-astro-cid-c7vabzjd>${piece.data.title}</h1> ${piece.data.dek && renderTemplate`<p class="dek" data-astro-cid-c7vabzjd>${piece.data.dek}</p>`} </div> </header>  <div class="body-grid" data-astro-cid-c7vabzjd> <aside class="body-left" aria-hidden="true" data-astro-cid-c7vabzjd></aside> <div class="body-main body-main--dropcap" data-astro-cid-c7vabzjd> ${renderComponent($$result2, "Content", Content, { "data-astro-cid-c7vabzjd": true })} </div> <aside class="body-right marginalia" data-astro-cid-c7vabzjd> <h4 data-astro-cid-c7vabzjd>Field reference</h4> <p data-astro-cid-c7vabzjd>${piece.data.country} · ${piece.data.region}</p> <p data-astro-cid-c7vabzjd>Level · ${piece.data.level}</p> <p data-astro-cid-c7vabzjd>Themes · ${piece.data.themes.join(", ")}</p> ${piece.data.contains_composites && renderTemplate`${renderComponent($$result2, "Fragment", Fragment, { "data-astro-cid-c7vabzjd": true }, { "default": async ($$result3) => renderTemplate` <h4 data-astro-cid-c7vabzjd>Composite figures</h4> <p data-astro-cid-c7vabzjd>This piece uses a composite character marked with † on first appearance. See the footnote above the sources list.</p> ` })}`} ${sourcesAreProvisional && renderTemplate`${renderComponent($$result2, "Fragment", Fragment, { "data-astro-cid-c7vabzjd": true }, { "default": async ($$result3) => renderTemplate` <h4 data-astro-cid-c7vabzjd>Editorial status</h4> <p data-astro-cid-c7vabzjd>One or more sources are placeholder citations. The Editor will replace these with verified ministry-document titles, dates, and URLs in the QA window.</p> ` })}`} </aside> </div>  <figure class="still"${addAttribute(stillAlt, "aria-label")} data-astro-cid-c7vabzjd> <div class="still__field" data-astro-cid-c7vabzjd> <img${addAttribute(stillSrc, "src")}${addAttribute(stillAlt, "alt")} loading="lazy" decoding="async" data-astro-cid-c7vabzjd> </div> <figcaption class="still__colophon" data-astro-cid-c7vabzjd> <span data-astro-cid-c7vabzjd><span class="still__num" data-astro-cid-c7vabzjd>${stillCaption}</span></span> <span data-astro-cid-c7vabzjd>Made in-house for Madār · 2026</span> </figcaption> </figure>  <footer class="article__footer" data-astro-cid-c7vabzjd> <div class="body-grid" data-astro-cid-c7vabzjd> <aside class="body-left" aria-hidden="true" data-astro-cid-c7vabzjd></aside> <div class="body-main" data-astro-cid-c7vabzjd> <h2 class="subhead" data-astro-cid-c7vabzjd>Sources</h2> <ol class="sources" data-astro-cid-c7vabzjd> ${piece.data.sources.map((s) => renderTemplate`<li data-astro-cid-c7vabzjd> ${/^https?:\/\/example\.com\//.test(s.url) ? renderTemplate`<span class="sources__title" data-astro-cid-c7vabzjd>${s.title}</span>` : renderTemplate`<a${addAttribute(s.url, "href")} rel="noopener noreferrer" data-astro-cid-c7vabzjd>${s.title}</a>`} </li>`)} </ol> ${sourcesAreProvisional && renderTemplate`<p class="sources__note muted small" data-astro-cid-c7vabzjd>
Placeholder URLs marked above will be replaced with the verified primary-source URL in the Editor's next QA pass.
</p>`} </div> <aside class="body-right" aria-hidden="true" data-astro-cid-c7vabzjd></aside> </div> </footer> </article> ` })} `;
}, "/sessions/keen-lucid-shannon/mnt/Educational Website/web/src/pages/articles/[...slug].astro", void 0);

const $$file = "/sessions/keen-lucid-shannon/mnt/Educational Website/web/src/pages/articles/[...slug].astro";
const $$url = "/articles/[...slug]";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$,
  file: $$file,
  getStaticPaths,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
