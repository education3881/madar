import { n as createAstro, o as createComponent, r as maybeRenderHead, m as addAttribute, w as renderTemplate, s as renderComponent, B as unescapeHTML, e as Fragment, t as renderHead, v as renderSlot } from './astro/server_DbByELL0.mjs';
import 'piccolore';
/* empty css                         */
import { existsSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';
import 'clsx';

const $$Astro$2 = createAstro("https://example.github.io");
const $$SiteHeader = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro$2, $$props, $$slots);
  Astro2.self = $$SiteHeader;
  const { lang = "en", variant = "home" } = Astro2.props;
  const __filename = fileURLToPath(import.meta.url);
  const __dirname = dirname(__filename);
  const wordmarkPath = resolve(__dirname, "../../../design-assets/wordmark/madar-wordmark.svg");
  let wordmarkSvg = null;
  if (existsSync(wordmarkPath)) {
    try {
      wordmarkSvg = readFileSync(wordmarkPath, "utf-8");
      wordmarkSvg = wordmarkSvg.replace(/^<\?xml[^?]*\?>\s*/, "");
    } catch {
      wordmarkSvg = null;
    }
  }
  const homeHref = lang === "ar" ? "/ar/" : "/";
  const otherLangHref = lang === "ar" ? "/" : "/ar/";
  const otherLangLabel = lang === "ar" ? "English" : "\u0627\u0644\u0639\u0631\u0628\u064A\u0629";
  const nav = {
    en: { latest: "Latest", about: "About", newsletter: "Newsletter" },
    ar: { latest: "\u0627\u0644\u0623\u062D\u062F\u062B", about: "\u0639\u0646 \u0627\u0644\u0645\u0646\u0634\u0648\u0631", newsletter: "\u0627\u0644\u0646\u0634\u0631\u0629" }
  }[lang];
  const aboutHref = lang === "ar" ? "/ar/about/" : "/about/";
  return renderTemplate`${maybeRenderHead()}<header${addAttribute(`site-header site-header--${variant}`, "class")}${addAttribute(lang, "data-lang")} data-astro-cid-ctg3m53h> <div class="container site-header__inner" data-astro-cid-ctg3m53h> ${variant === "article" && renderTemplate`<a${addAttribute(homeHref, "href")} class="site-header__back"${addAttribute(lang === "ar" ? "\u0627\u0644\u0639\u0648\u062F\u0629" : "Back to home", "aria-label")} data-astro-cid-ctg3m53h> <span aria-hidden="true" data-astro-cid-ctg3m53h>${lang === "ar" ? "\u2190" : "\u2190"}</span> <span class="uppercase" data-astro-cid-ctg3m53h>${lang === "ar" ? "\u0627\u0644\u0639\u0648\u062F\u0629" : "Index"}</span> </a>`} <a${addAttribute(homeHref, "href")} class="site-header__mark" aria-label="Madār — home" data-astro-cid-ctg3m53h> ${wordmarkSvg ? renderTemplate`${renderComponent($$result, "Fragment", Fragment, {}, { "default": ($$result2) => renderTemplate`${unescapeHTML(wordmarkSvg)}` })}` : renderTemplate`${renderComponent($$result, "Fragment", Fragment, {}, { "default": ($$result2) => renderTemplate`<span class="mark-latin" data-astro-cid-ctg3m53h>Madār</span> <span class="mark-divider" aria-hidden="true" data-astro-cid-ctg3m53h>·</span> <span class="mark-arabic" lang="ar" dir="rtl" data-astro-cid-ctg3m53h>مدار</span> ` })}`} </a> ${variant === "home" && renderTemplate`<nav class="site-nav"${addAttribute(lang === "ar" ? "\u062A\u0646\u0642\u0651\u0644" : "Navigation", "aria-label")} data-astro-cid-ctg3m53h> <a${addAttribute(homeHref, "href")} class="uppercase" data-astro-cid-ctg3m53h>${nav.latest}</a> <a${addAttribute(aboutHref, "href")} class="uppercase" data-astro-cid-ctg3m53h>${nav.about}</a> <span class="site-nav__sep" aria-hidden="true" data-astro-cid-ctg3m53h>·</span> <a${addAttribute(otherLangHref, "href")} class="uppercase"${addAttribute(lang === "ar" ? "en" : "ar", "hreflang")} data-astro-cid-ctg3m53h>${otherLangLabel}</a> </nav>`} ${variant === "article" && renderTemplate`<nav class="site-nav site-nav--article"${addAttribute(lang === "ar" ? "\u062A\u0646\u0642\u0651\u0644" : "Navigation", "aria-label")} data-astro-cid-ctg3m53h> <a${addAttribute(otherLangHref, "href")} class="uppercase"${addAttribute(lang === "ar" ? "en" : "ar", "hreflang")} data-astro-cid-ctg3m53h>${otherLangLabel}</a> </nav>`} </div> ${variant === "home" && renderTemplate`<div class="site-header__rule" aria-hidden="true" data-astro-cid-ctg3m53h> <span class="site-header__rule-bar" data-astro-cid-ctg3m53h></span> </div>`} </header> `;
}, "/sessions/keen-lucid-shannon/mnt/Educational Website/web/src/components/SiteHeader.astro", void 0);

const $$Astro$1 = createAstro("https://example.github.io");
const $$SiteFooter = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro$1, $$props, $$slots);
  Astro2.self = $$SiteFooter;
  const { lang = "en" } = Astro2.props;
  const year = (/* @__PURE__ */ new Date()).getFullYear();
  const copy = {
    en: {
      issue: "Issue 01 \xB7 2026",
      rights: `\xA9 ${year} Mad\u0101r \u2014 an editorial publication, independently operated.`,
      closing: "Made in spite of, not because of.",
      rss: "RSS",
      contact: "Contact",
      aboutLabel: "About",
      aboutHref: "/about/",
      homeHref: "/",
      otherLangHref: "/ar/",
      otherLangLabel: "\u0627\u0644\u0639\u0631\u0628\u064A\u0629"
    },
    ar: {
      issue: "\u0627\u0644\u0639\u062F\u062F \u0660\u0661 \xB7 \u0662\u0660\u0662\u0666",
      rights: `\xA9 ${year} \u0645\u062F\u0627\u0631 \u2014 \u0645\u0646\u0634\u0648\u0631 \u062A\u062D\u0631\u064A\u0631\u064A \u0645\u0633\u062A\u0642\u0644.`,
      closing: "\u0635\u064F\u0646\u0639 \u0631\u063A\u0645\u064B\u0627 \u0639\u0646 \u0627\u0644\u0638\u0631\u0648\u0641\u060C \u0644\u0627 \u0628\u0641\u0636\u0644\u0647\u0627.",
      rss: "RSS",
      contact: "\u0627\u062A\u0635\u0644",
      aboutLabel: "\u0639\u0646 \u0627\u0644\u0645\u0646\u0634\u0648\u0631",
      aboutHref: "/ar/about/",
      homeHref: "/ar/",
      otherLangHref: "/",
      otherLangLabel: "English"
    }
  }[lang];
  return renderTemplate`${maybeRenderHead()}<footer class="site-footer" data-astro-cid-gcn2mc3v> <div class="container site-footer__inner" data-astro-cid-gcn2mc3v> <div class="site-footer__cell site-footer__cell--issue" data-astro-cid-gcn2mc3v> <p class="kicker" data-astro-cid-gcn2mc3v>${copy.issue}</p> <p class="site-footer__closing" data-astro-cid-gcn2mc3v>${copy.closing}</p> </div> <div class="site-footer__cell site-footer__cell--mark" data-astro-cid-gcn2mc3v> <a${addAttribute(copy.homeHref, "href")} class="site-footer__mark" aria-label="Madār — home" data-astro-cid-gcn2mc3v> <span class="mark-latin" data-astro-cid-gcn2mc3v>Madār</span> <span aria-hidden="true" class="mark-divider" data-astro-cid-gcn2mc3v>·</span> <span class="mark-arabic" lang="ar" dir="rtl" data-astro-cid-gcn2mc3v>مدار</span> </a> <p class="site-footer__rights mono sage" data-astro-cid-gcn2mc3v>${copy.rights}</p> </div> <div class="site-footer__cell site-footer__cell--nav" data-astro-cid-gcn2mc3v> <ul class="site-footer__links" data-astro-cid-gcn2mc3v> <li data-astro-cid-gcn2mc3v><a${addAttribute(copy.aboutHref, "href")} class="uppercase" data-astro-cid-gcn2mc3v>${copy.aboutLabel}</a></li> <li data-astro-cid-gcn2mc3v><a${addAttribute(copy.otherLangHref, "href")} class="uppercase"${addAttribute(lang === "ar" ? "en" : "ar", "hreflang")} data-astro-cid-gcn2mc3v>${copy.otherLangLabel}</a></li> <li data-astro-cid-gcn2mc3v><a href="/rss.xml" class="uppercase" data-astro-cid-gcn2mc3v>${copy.rss}</a></li> </ul> </div> </div> </footer> `;
}, "/sessions/keen-lucid-shannon/mnt/Educational Website/web/src/components/SiteFooter.astro", void 0);

const $$Astro = createAstro("https://example.github.io");
const $$Base = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$Base;
  const {
    title,
    description = "An editorial publication on education, from underrepresented geographies.",
    lang = "en",
    ogImage,
    noHeader = false
  } = Astro2.props;
  const dir = lang === "ar" ? "rtl" : "ltr";
  const canonicalURL = new URL(Astro2.url.pathname, Astro2.site);
  return renderTemplate`<html${addAttribute(lang, "lang")}${addAttribute(dir, "dir")}> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="generator"${addAttribute(Astro2.generator, "content")}><title>${title}</title><meta name="description"${addAttribute(description, "content")}><link rel="canonical"${addAttribute(canonicalURL.href, "href")}><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=JetBrains+Mono:wght@400;500&family=Amiri:ital,wght@0,400;0,700;1,400&family=Cairo:wght@400;500;600;700&display=swap" rel="stylesheet"><meta property="og:type" content="article"><meta property="og:title"${addAttribute(title, "content")}><meta property="og:description"${addAttribute(description, "content")}><meta property="og:url"${addAttribute(canonicalURL.href, "content")}>${ogImage && renderTemplate`<meta property="og:image"${addAttribute(ogImage, "content")}>`}<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title"${addAttribute(title, "content")}><meta name="twitter:description"${addAttribute(description, "content")}>${ogImage && renderTemplate`<meta name="twitter:image"${addAttribute(ogImage, "content")}>`}<meta name="robots" content="index, follow"><meta name="color-scheme" content="light">${renderHead()}</head> <body> <a class="skip-link" href="#main">Skip to content</a> ${!noHeader && renderTemplate`${renderComponent($$result, "SiteHeader", $$SiteHeader, { "lang": lang })}`} <main id="main"> ${renderSlot($$result, $$slots["default"])} </main> ${renderComponent($$result, "SiteFooter", $$SiteFooter, { "lang": lang })} </body></html>`;
}, "/sessions/keen-lucid-shannon/mnt/Educational Website/web/src/layouts/Base.astro", void 0);

export { $$Base as $, $$SiteHeader as a };
