"""Static site builder for tractionhq.ai. Run: python tools/build.py  -> writes ./docs"""
import json, re, shutil, html, datetime
from pathlib import Path
import markdown as md

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs"
SITE = "https://tractionhq.ai"
NAME = "Traction Consulting"
EMAIL = "tom@tractionhq.ai"
TODAY = "2026-11-15"
MAILTO = "mailto:tom@tractionhq.ai?subject=Free%20consultation%20request"
OG = SITE + "/assets/img/og-default.jpg"

import sys; sys.path.insert(0, str(Path(__file__).parent))
from content import PAGES, POSTS, SERVICES, FAQ_ALL  # noqa

CSS = (Path(__file__).parent / "site.css").read_text()
CSS = re.sub(r"/\*.*?\*/", "", CSS, flags=re.S)
CSS = re.sub(r"\s+", " ", CSS).replace(" {", "{").replace("{ ", "{").replace("; ", ";").replace(" }", "}").replace(": ", ":").strip()

ORG_ID = SITE + "/#organization"
AREAS = ["Charlotte", "Waxhaw", "Matthews", "Ballantyne", "Huntersville", "Concord", "Mint Hill", "Indian Trail", "Monroe", "Cornelius", "Davidson", "Mooresville", "Gastonia"]
AREAS_SC = ["Fort Mill", "Rock Hill", "Tega Cay", "Indian Land"]

def org_graph():
    area = [{"@type": "City", "name": f"{a}, NC"} for a in AREAS] + [{"@type": "City", "name": f"{a}, SC"} for a in AREAS_SC] + [
        {"@type": "AdministrativeArea", "name": "Charlotte metropolitan area"}]
    return [
        {"@type": ["ProfessionalService", "Organization"], "@id": ORG_ID, "name": NAME, "legalName": "Traction Consulting, LLC",
         "url": SITE + "/", "logo": {"@type": "ImageObject", "url": SITE + "/logo-512.png", "width": 512, "height": 512},
         "image": OG, "email": EMAIL, "slogan": "Making AI work for you.",
         "description": "AI-focused business and technology consultancy for Charlotte-area small businesses. Forward deployed engineers embed with your team to map processes, build and integrate tools, and train employees.",
         "founder": {"@type": "Person", "name": "Tom Simmons"},
         "address": {"@type": "PostalAddress", "addressLocality": "Charlotte", "addressRegion": "NC", "addressCountry": "US"},
         "areaServed": area, "priceRange": "$$",
         "contactPoint": {"@type": "ContactPoint", "contactType": "sales", "email": EMAIL, "areaServed": "US", "availableLanguage": "English"},
         "knowsAbout": ["Artificial intelligence", "Large language models", "Generative engine optimization", "Search engine optimization",
                        "Google Business Profile", "Business process mapping", "Key performance indicators", "API integration",
                        "Custom software", "AI training", "Exit planning", "Lead generation"],
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
             {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "url": f"{SITE}/services/{s['slug']}/"}} for s in SERVICES]}},
        {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": NAME, "publisher": {"@id": ORG_ID}, "inLanguage": "en-US"},
    ]

def crumbs_ld(crumbs, url):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    for i, (n, h) in enumerate(crumbs, start=2):
        items.append({"@type": "ListItem", "position": i, "name": n, "item": SITE + h})
    return {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": items}

NAV = [("Services", "/services/"), ("How it works", "/how-it-works/"), ("Pricing", "/pricing/"), ("About", "/about/"), ("Blog", "/blog/"), ("FAQ", "/faq/")]

def header(path):
    links = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if path.startswith(h) else ""}>{n}</a></li>' for n, h in NAV)
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap hdr">
<a class="brand" href="/" aria-label="Traction Consulting home"><img src="/assets/img/logo-seal-128.webp" srcset="/assets/img/logo-seal-64.webp 64w, /assets/img/logo-seal-128.webp 128w, /assets/img/logo-seal-256.webp 256w" sizes="56px" width="56" height="56" alt="Traction Consulting seal logo"><span class="bt"><b>Traction</b> Consulting</span></a>
<button class="mbtn" type="button" aria-expanded="false" aria-controls="nav" onclick="var o=document.getElementById('nav').classList.toggle('open');this.setAttribute('aria-expanded',o)">Menu</button>
<nav aria-label="Main"><ul class="nav" id="nav">{links}<li><a class="btn btn-sm" href="/contact/">Free consultation</a></li></ul></nav>
</div></header>"""

def footer():
    svc = "".join(f'<li><a href="/services/{s["slug"]}/">{s["short"]}</a></li>' for s in SERVICES)
    return f"""<footer class="site-footer"><div class="wrap fgrid">
<div><p class="fbrand">Traction Consulting</p><p>Making AI work for you.</p><p>AI and technology consulting for small businesses in Charlotte, NC and the surrounding area.</p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div><p class="fh">Services</p><ul>{svc}</ul></div>
<div><p class="fh">Company</p><ul><li><a href="/how-it-works/">How it works</a></li><li><a href="/pricing/">Pricing</a></li><li><a href="/about/">About</a></li><li><a href="/charlotte-ai-consulting/">Charlotte service area</a></li><li><a href="/blog/">Blog</a></li><li><a href="/faq/">FAQ</a></li><li><a href="/contact/">Contact</a></li><li><a href="/privacy/">Privacy</a></li></ul></div>
</div><div class="wrap legal"><p>&copy; 2026 Traction Consulting, LLC. Serving the Charlotte metro area.</p></div></footer>"""

def breadcrumbs_html(crumbs):
    if not crumbs: return ""
    parts = ['<li><a href="/">Home</a></li>']
    for i, (n, h) in enumerate(crumbs):
        parts.append(f'<li><span aria-current="page">{n}</span></li>' if i == len(crumbs) - 1 else f'<li><a href="{h}">{n}</a></li>')
    return f'<nav class="crumbs wrap" aria-label="Breadcrumb"><ol>{"".join(parts)}</ol></nav>'

def esc(s): return html.escape(s, quote=True)

def page_html(p):
    path = p["path"]; url = SITE + path
    t, d = p["title"], p["description"]
    graph = org_graph()
    wp = {"@type": p.get("pagetype", "WebPage"), "@id": url + "#webpage", "url": url, "name": t, "description": d,
          "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": ORG_ID}, "inLanguage": "en-US",
          "primaryImageOfPage": {"@type": "ImageObject", "url": p.get("og", OG)}, "dateModified": TODAY}
    if p.get("crumbs"):
        graph.append(crumbs_ld(p["crumbs"], url)); wp["breadcrumb"] = {"@id": url + "#breadcrumb"}
    graph.append(wp)
    graph += p.get("ld", [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    ogtype = "article" if p.get("article") else "website"
    extra = ""
    if p.get("article"):
        extra = f'<meta property="article:published_time" content="{p["date"]}"><meta property="article:modified_time" content="{p["date"]}">'
    robots = "noindex, follow" if p.get("noindex") else "index, follow, max-image-preview:large, max-snippet:-1"
    canon = "" if p.get("nocanon") else f'<link rel="canonical" href="{url}">'
    return f"""<!doctype html>
<html lang="en-US"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t)}</title>
<meta name="description" content="{esc(d)}">
<meta name="robots" content="{robots}">
{canon}
<meta property="og:type" content="{ogtype}"><meta property="og:site_name" content="Traction Consulting"><meta property="og:locale" content="en_US">
<meta property="og:title" content="{esc(t)}"><meta property="og:description" content="{esc(d)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{p.get('og', OG)}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Traction Consulting: Making AI work for you.">{extra}
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(t)}"><meta name="twitter:description" content="{esc(d)}"><meta name="twitter:image" content="{p.get('og', OG)}">
<meta name="theme-color" content="#13294B">
<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/source-sans-3-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="alternate" type="application/rss+xml" title="Traction Consulting blog" href="/blog/feed.xml">
<style>{CSS}</style>
<script type="application/ld+json">{ld}</script>
</head><body>
{header(path)}
{breadcrumbs_html(p.get("crumbs"))}
<main id="main">
{p["body"]}
</main>
{footer()}
</body></html>
"""

def check(p):
    probs = []
    if not (50 <= len(p["title"]) <= 60): probs.append(f"title len {len(p['title'])}")
    if not (150 <= len(p["description"]) <= 160): probs.append(f"desc len {len(p['description'])}")
    h1 = len(re.findall(r"<h1[\s>]", p["body"]))
    if h1 != 1: probs.append(f"h1 count {h1}")
    levels = [int(x) for x in re.findall(r"<h([1-6])[\s>]", p["body"])]
    for a, b in zip(levels, levels[1:]):
        if b > a + 1: probs.append(f"heading skip h{a}->h{b}")
    for m in re.findall(r"<img[^>]*>", p["body"]):
        if "alt=" not in m: probs.append("img no alt")
    return probs

def html_to_md(s):
    s = re.sub(r"<script.*?</script>", "", s, flags=re.S)
    s = re.sub(r"<h([1-6])[^>]*>(.*?)</h\1>", lambda m: "\n" + "#" * int(m.group(1)) + " " + m.group(2) + "\n", s, flags=re.S)
    s = re.sub(r"<li[^>]*>", "\n- ", s)
    s = re.sub(r'<a [^>]*href="(/[^"]*)"[^>]*>(.*?)</a>', lambda m: f"[{m.group(2)}]({SITE}{m.group(1)})", s, flags=re.S)
    s = re.sub(r'<a [^>]*href="([^"]*)"[^>]*>(.*?)</a>', r"[\2](\1)", s, flags=re.S)
    s = re.sub(r"</?(strong|b)>", "**", s)
    s = re.sub(r"<(p|tr|div|section|table|br)[^>]*>", "\n", s)
    s = re.sub(r"<t[dh][^>]*>", " | ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    return s.strip()

def main():
    if OUT.exists(): shutil.rmtree(OUT)
    shutil.copytree(ROOT / "static", OUT)
    allp = PAGES + POSTS
    bad = {}
    titles, descs = {}, {}
    for p in allp:
        pr = check(p)
        if p["title"] in titles: pr.append("dup title")
        if p["description"] in descs: pr.append("dup desc")
        titles[p["title"]] = 1; descs[p["description"]] = 1
        if pr and not p.get("noindex"): bad[p["path"]] = pr
        dest = OUT / ("404.html" if p["path"] == "/404.html" else p["path"].lstrip("/") + "index.html")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page_html(p))
    # sitemap
    urls = "".join(f"<url><loc>{SITE}{p['path']}</loc><lastmod>{p.get('date', TODAY)}</lastmod></url>" for p in allp if not p.get("noindex"))
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    bots = ["*", "Googlebot", "Bingbot", "GPTBot", "OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "Perplexity-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "Google-Extended", "Applebot", "Applebot-Extended", "DuckDuckBot", "CCBot", "meta-externalagent", "Amazonbot", "MistralAI-User"]
    rb = "\n".join(f"User-agent: {b}\nAllow: /\n" for b in bots)
    (OUT / "robots.txt").write_text(f"# Traction Consulting: all public pages may be crawled, indexed and cited by search engines and AI assistants.\n{rb}\nSitemap: {SITE}/sitemap.xml\n")
    (OUT / "CNAME").write_text("tractionhq.ai\n")
    (OUT / ".nojekyll").write_text("")
    (OUT / "site.webmanifest").write_text(json.dumps({"name": NAME, "short_name": "Traction", "start_url": "/", "display": "standalone", "background_color": "#FFFFFF", "theme_color": "#13294B",
        "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=1))
    # RSS
    items = "".join(f"<item><title>{esc(p['h1'])}</title><link>{SITE}{p['path']}</link><guid>{SITE}{p['path']}</guid><pubDate>{datetime.datetime.strptime(p['date'],'%Y-%m-%d').strftime('%a, %d %b %Y 12:00:00 -0500')}</pubDate><description>{esc(p['description'])}</description></item>" for p in POSTS)
    (OUT / "blog/feed.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Traction Consulting blog</title><link>{SITE}/blog/</link><description>Practical AI for Charlotte small business owners.</description><language>en-us</language>{items}</channel></rss>\n')
    # llms.txt / llms-full.txt
    from content import LLMS_INTRO
    lines = [f"# {NAME}", "", "> " + LLMS_INTRO, ""]
    lines += ["## Key facts", "", "- Mission: Making AI work for you.", "- Service area: Charlotte, NC metro (including Waxhaw, Matthews, Ballantyne, Huntersville, Concord, Mint Hill, Indian Trail, Monroe, Fort Mill SC and Rock Hill SC). Service-area business; no public storefront.",
              "- Pricing: weekly, no contracts, pay as you go. Tier 1 (under $1M revenue, 1–10 employees): $1,250/week. Tier 2 ($1M–$3M revenue, up to 15 employees): custom quote.",
              "- The cost listed does not include subscriptions, token usage, and other expenses, which are kept to a minimum for the client's benefit.",
              "- Founder: Tom Simmons. Contact: tom@tractionhq.ai. First consultation is free.", ""]
    groups = [("Main pages", [p for p in PAGES if not p["path"].startswith("/services/") or p["path"] == "/services/"]), ("Services", [p for p in PAGES if p["path"].startswith("/services/") and p["path"] != "/services/"]), ("Blog articles", POSTS)]
    for g, ps in groups:
        lines += [f"## {g}", ""] + [f"- [{p['h1']}]({SITE}{p['path']}): {p['description']}" for p in ps if not p.get("noindex")] + [""]
    lines += ["## Optional", "", f"- [Full text of this site for language models]({SITE}/llms-full.txt)", f"- [Sitemap]({SITE}/sitemap.xml)", ""]
    (OUT / "llms.txt").write_text("\n".join(lines))
    full = [f"# {NAME}: full site text", "", "> " + LLMS_INTRO, ""]
    for p in allp:
        if p.get("noindex"): continue
        full += [f"---", "", f"URL: {SITE}{p['path']}", "", html_to_md(p["body"]), ""]
    (OUT / "llms-full.txt").write_text("\n".join(full))
    print(f"built {len(allp)} pages")
    for k, v in bad.items(): print("WARN", k, v)

if __name__ == "__main__":
    main()
