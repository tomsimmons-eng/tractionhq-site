"""Generate raster brand assets (logo, favicons, Open Graph image) with headless Chrome."""
import os, re, subprocess, sys, tempfile, io
from pathlib import Path
from PIL import Image
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "static"
BRAND = Path(os.environ.get("BRAND_DIR", ROOT.parent / "brand/v2"))
final = BRAND / "final"
MARK = final / "mark-17-final.svg" if (final / "mark-17-final.svg").exists() else BRAND / "svg/mark-17.svg"
print("using mark:", MARK)
mark_svg = MARK.read_text()
mark_svg = re.sub(r"<\?xml[^>]*\?>|<!--.*?-->", "", mark_svg, flags=re.S).strip()
mark_svg = re.sub(r'<rect width="\d+" height="\d+" fill="#fff"/>', "", mark_svg)

def shot(html, w, h, out, transparent=True):
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "a.html"
        p.write_text(html)
        args = ["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                f"--window-size={w},{h}", f"--screenshot={out}", "--force-device-scale-factor=1"]
        if transparent:
            args.append("--default-background-color=00000000")
        args.append(p.as_uri())
        subprocess.run(args, check=True, capture_output=True)

def mark_png(size, out):
    html = f"""<html><body style="margin:0;background:transparent">
<div style="width:{size}px;height:{size}px">{mark_svg.replace('width="1000" height="1000"', f'width="{size}" height="{size}"')}</div></body></html>"""
    shot(html, size, size, out)

img = OUT / "assets/img"; img.mkdir(parents=True, exist_ok=True)
tmp = Path(tempfile.mkdtemp())
mark_png(1024, tmp / "mark1024.png")
big = Image.open(tmp / "mark1024.png").convert("RGBA")
for s in (64, 128, 256):
    big.resize((s, s), Image.LANCZOS).save(img / f"logo-seal-{s}.webp", "WEBP", quality=90, method=6)
big.resize((512, 512), Image.LANCZOS).save(OUT / "logo-512.png", optimize=True)
big.resize((512, 512), Image.LANCZOS).save(OUT / "icon-512.png", optimize=True)
big.resize((192, 192), Image.LANCZOS).save(OUT / "icon-192.png", optimize=True)

# Small-size favicon: simplified emblem (navy disc + white T + amber dots), no ring text
fav = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="31" fill="#13294B"/><circle cx="32" cy="32" r="26" fill="none" stroke="#FFFFFF" stroke-width="2"/><path d="M19 18h26v7h-9v22h-8V25h-9z" fill="#FFFFFF"/><circle cx="9.5" cy="32" r="2.2" fill="#F2A33A"/><circle cx="54.5" cy="32" r="2.2" fill="#F2A33A"/></svg>"""
(OUT / "favicon.svg").write_text(fav)
ims = [Image.open(io.BytesIO(cairosvg.svg2png(bytestring=fav.encode(), output_width=s, output_height=s))).convert("RGBA") for s in (16, 32, 48)]
ims[2].save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)], append_images=ims[:2])
# apple touch icon: full-bleed navy square w/ white T (iOS masks corners)
apple = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180"><rect width="180" height="180" fill="#13294B"/><circle cx="90" cy="90" r="70" fill="none" stroke="#FFFFFF" stroke-width="5"/><path d="M55 52h70v19H101v58H79V71H55z" fill="#FFFFFF"/><circle cx="34" cy="90" r="5" fill="#F2A33A"/><circle cx="146" cy="90" r="5" fill="#F2A33A"/></svg>"""
Image.open(io.BytesIO(cairosvg.svg2png(bytestring=apple.encode(), output_width=180, output_height=180))).convert("RGB").save(OUT / "apple-touch-icon.png", optimize=True)

# Open Graph image 1200x630
mark_inline = mark_svg.replace('width="1000" height="1000"', 'width="400" height="400"')
og = f"""<html><head><style>
body{{margin:0;width:1200px;height:630px;background:#13294B;font-family:'Source Sans 3',sans-serif;color:#fff;display:flex;align-items:center;overflow:hidden}}
.m{{margin-left:80px;flex:0 0 400px}} .t{{margin-left:64px;padding-right:60px}}
h1{{font-size:76px;font-weight:800;margin:0;line-height:1}} .tag{{font-size:44px;font-weight:600;color:#F2A33A;margin:22px 0 26px}}
p{{font-size:30px;margin:0;color:#EEF2F5;line-height:1.3}} .u{{margin-top:34px;font-size:28px;font-weight:700;letter-spacing:2px;color:#9fd6d4}}
.bar{{position:absolute;left:0;bottom:0;height:14px;width:1200px;background:#0C7574}}
</style></head><body><div class="m">{mark_inline}</div><div class="t"><h1>Traction Consulting</h1>
<div class="tag">Making AI work for you.</div><p>Hands-on AI and technology consulting for Charlotte-area small businesses.</p><div class="u">TRACTIONHQ.AI</div></div><div class="bar"></div></body></html>"""
shot(og, 1200, 630, tmp / "og.png", transparent=False)
Image.open(tmp / "og.png").convert("RGB").save(OUT / "assets/img/og-default.jpg", "JPEG", quality=88, optimize=True, progressive=True)
print("done", sorted(p.name for p in OUT.rglob("*") if p.is_file()))
