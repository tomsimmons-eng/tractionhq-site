# tractionhq.ai

Source for the Traction Consulting website, https://tractionhq.ai.

- `tools/content.py` – page content and structured data
- `posts/*.md` – blog articles (Markdown with front matter)
- `tools/site.css` – styles (inlined at build time)
- `tools/build.py` – builds the static site into `docs/` (sitemap, robots.txt, llms.txt, llms-full.txt, RSS)
- `tools/make_assets.py` – generates logo rasters, favicons and the Open Graph image
- `static/` – fonts, icons and images copied into `docs/`

Build: `pip install markdown && python tools/build.py`. GitHub Pages serves the `docs/` folder on `main`.
