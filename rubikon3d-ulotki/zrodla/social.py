"""Square 1080x1080 graphic for Facebook group replies (style of leaflet D). Renders PNG via Playwright."""
import re, pathlib, subprocess, sys

B = pathlib.Path(__file__).parent
A = B / "assets"
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else B

def qr(k):
    s = (A / f"qr-{k}.svg").read_text()
    n = re.search(r'width="(\d+)"', s).group(1)
    return re.sub(r'width="\d+" height="\d+"', f'viewBox="0 0 {n} {n}" shape-rendering="crispEdges"', s, count=1)

# same isometric grid as print leaflets, scaled to px (cell ~43 px, line ~2.6 px)
S = 6.2
GRID = f"""<svg class="iso" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="g" width="{13.856*S:.2f}" height="{8*S:.2f}" patternUnits="userSpaceOnUse" viewBox="0 0 13.856 8">
<g stroke="#E92F4C" stroke-width="{2.2/S:.3f}" fill="none"><path d="M0 -1V9M6.928 -1V9M13.856 -1V9M0 0L13.856 8M0 8L13.856 0M-6.928 4L6.928 12M-6.928 4L6.928 -4M6.928 -4L20.784 4M6.928 12L20.784 4"/></g></pattern></defs>
<rect width="100%" height="100%" fill="url(#g)"/></svg>"""

CSS = (A / "fonts.css").read_text() + """
:root{--red:#E51636;--ink:#1D1D1B;--wa:#2FA552}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px}
body{font-family:'Space Grotesk',sans-serif;-webkit-font-smoothing:antialiased}
.sheet{position:relative;width:1080px;height:1080px;overflow:hidden;background:var(--red);color:#fff}
.iso{position:absolute;inset:0;width:100%;height:100%}
.cube{position:absolute;right:-30px;top:-40px;height:400px}
.brand{position:absolute;left:72px;top:78px;height:92px}
.hd{position:absolute;left:72px;right:72px;top:285px}
.hd h1{font-size:104px;line-height:.98;font-weight:700;letter-spacing:-.02em}
.hd p{margin-top:24px;font-size:34px;line-height:1.3}
.tags{position:absolute;left:72px;right:72px;top:688px;display:flex;flex-wrap:wrap;gap:14px}
.tags i{font-style:normal;background:var(--red);font-family:'Space Mono',monospace;font-weight:700;font-size:25px;letter-spacing:.1em;border:2px solid #ffffffb3;border-radius:40px;padding:8px 20px}
.card{position:absolute;left:48px;right:48px;bottom:48px;height:270px;background:#fff;color:var(--ink);border-radius:24px;display:flex;align-items:center;gap:40px;padding:0 44px}
.card .txt{flex:1;min-width:0}
.card .wa{font-size:30px;font-weight:700;color:var(--wa)}
.card .tel{font-size:70px;font-weight:700;letter-spacing:-.01em;line-height:1.05;margin:6px 0 12px;color:var(--red)}
.card .more{font-size:28px;line-height:1.35}
.card .more b{font-weight:700}
.card .qr{width:190px;height:190px;flex:none}
.card .qr svg{display:block;width:100%;height:100%}
"""

HTML = f"""<!doctype html><html lang=pl><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=sheet>
{GRID}
<img class=cube src="assets/cube.svg">
<img class=brand src="assets/wordmark.svg">
<div class=hd><h1>Wydrukujemy<br>to w 3D.</h1>
<p>Na wymiar, od jednej sztuki.<br>Wyślij zdjęcie lub wymiary. Wycena bez zobowiązań.</p></div>
<div class=tags><i>NAPRAWA</i><i>WARSZTAT</i><i>FIRMY</i><i>PREZENTY</i></div>
<div class=card><div class=txt><div class=wa>Napisz na WhatsApp</div><div class=tel>+48 609 692 311</div>
<div class=more>rubikon3d.com · FB / IG: <b>Rubikon3D</b></div></div>
<div class=qr>{qr('fb')}</div></div>
</div></body></html>"""

html = B / "social-fb.html"
html.write_text(HTML)
js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();
const p=await b.newPage({{viewport:{{width:1080,height:1080}},deviceScaleFactor:2}});
await p.goto('file://{html}');await p.evaluate(()=>document.fonts.ready);
await p.screenshot({{path:'{OUT}/Rubikon3D-grafika-FB-1080.png'}});await b.close()}})()"""
subprocess.run(["node", "-e", js], check=True, cwd=B)
html.unlink()
print("ok")
