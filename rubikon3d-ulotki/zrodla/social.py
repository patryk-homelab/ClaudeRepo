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
:root{--red:#E51636}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px}
body{font-family:'Space Grotesk',sans-serif;-webkit-font-smoothing:antialiased}
.sheet{position:relative;width:1080px;height:1080px;overflow:hidden;background:var(--red);color:#fff}
.iso{position:absolute;inset:0;width:100%;height:100%}
.logo{position:absolute;left:84px;top:96px;display:flex;align-items:center;gap:28px}
.logo .c{height:132px}.logo .w{height:92px}
.hd{position:absolute;left:84px;right:84px;top:418px}
.hd h1{font-size:104px;white-space:nowrap;line-height:.98;font-weight:700;letter-spacing:-.025em}
.hd p{margin-top:40px;font-family:'Space Mono',monospace;font-size:24px;letter-spacing:.14em;opacity:.92}
.ct{position:absolute;left:84px;right:84px;bottom:96px;border-top:2px solid #ffffff99;padding-top:34px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:28px}
.ct span{display:block;font-family:'Space Mono',monospace;font-size:20px;letter-spacing:.12em;opacity:.8}
.ct b{display:block;margin-top:10px;font-size:40px;font-weight:700;letter-spacing:-.005em}
"""

HTML = f"""<!doctype html><html lang=pl><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=sheet>
{GRID}
<div class=logo><img class=c src="assets/cube.svg"><img class=w src="assets/wordmark.svg"></div>
<div class=hd><h1>Masz pomysł?<br>Wydrukujemy to.</h1>
<p>NA WYMIAR · CZĘŚCI ZAMIENNE · PREZENTY</p></div>
<div class=ct>
 <div><span>FACEBOOK / INSTAGRAM</span><b>Rubikon3D</b></div>
 <div><span>TEL. / WHATSAPP</span><b>609 692 311</b></div>
 <div><span>STRONA</span><b>rubikon3d.com</b></div>
</div>
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
