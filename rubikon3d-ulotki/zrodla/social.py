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
.hd{position:absolute;left:84px;right:84px;top:286px}
.hd h1{font-size:104px;white-space:nowrap;line-height:.98;font-weight:700;letter-spacing:-.025em}
.hd p{margin-top:28px;font-size:32px;line-height:1.3}
.cats{position:absolute;left:84px;right:84px;top:650px;display:grid;grid-template-columns:1fr 1fr;gap:26px 48px}
.cats div{border-top:2px solid #ffffff80;padding-top:14px}
.cats span{display:block;font-family:'Space Mono',monospace;font-weight:700;font-size:20px;letter-spacing:.12em}
.cats b{display:block;margin-top:6px;font-size:29px;font-weight:400}
.ct{position:absolute;left:84px;right:84px;bottom:84px;border-top:2px solid #ffffffd9;padding-top:30px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:28px}
.ct span{display:block;white-space:nowrap;font-family:'Space Mono',monospace;font-size:18px;opacity:.85}
.ct b{display:block;margin-top:10px;font-size:40px;font-weight:700;letter-spacing:-.005em}
"""

HTML = f"""<!doctype html><html lang=pl><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=sheet>
{GRID}
<div class=logo><img class=c src="assets/cube.svg"><img class=w src="assets/wordmark.svg"></div>
<div class=hd><h1>Masz pomysł?<br>Wydrukujemy to.</h1>
<p>Na wymiar, od jednej sztuki.<br>Wyślij zdjęcie lub wymiary, wycenimy bez zobowiązań.</p></div>
<div class=cats>
 <div><span>NAPRAWA</span><b>klips, pokrętło, zaślepka</b></div>
 <div><span>WARSZTAT I NARZĘDZIA</span><b>uchwyty, organizery, adaptery</b></div>
 <div><span>FIRMY</span><b>prototypy, krótkie serie</b></div>
 <div><span>PREZENTY</span><b>lampka ze zdjęciem, mapa 3D</b></div>
</div>
<div class=ct>
 <div><span>FB / INSTAGRAM</span><b>Rubikon3D</b></div>
 <div><span>TEL. / WHATSAPP</span><b>609 692 311</b></div>
 <div><span>STRONA INTERNETOWA</span><b>rubikon3d.com</b></div>
</div>
</div></body></html>"""

html = B / "social-fb.html"
html.write_text(HTML)
js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();
const p=await b.newPage({{viewport:{{width:1080,height:1080}},deviceScaleFactor:2}});
await p.goto('file://{html}');await p.evaluate(()=>document.fonts.ready);await p.evaluate(()=>{{for(const d of document.querySelectorAll('.ct>div')){{const l=d.querySelector('span'),v=d.querySelector('b');const w=e=>{{const r=document.createRange();r.selectNodeContents(e);return r.getBoundingClientRect().width}};l.style.letterSpacing='0px';const n=[...l.textContent].length;const ls=(w(v)-w(l))/(n-1);l.style.letterSpacing=ls+'px';l.style.marginRight=(-ls)+'px';l.dataset.fit=ls.toFixed(2)}}}});console.log(await p.evaluate(()=>[...document.querySelectorAll('.ct>div')].map(d=>{{const w=e=>{{const r=document.createRange();r.selectNodeContents(e);return r.getBoundingClientRect().width}};return d.querySelector('span').textContent+' ls='+d.querySelector('span').dataset.fit+' label='+(w(d.querySelector('span'))+parseFloat(d.querySelector('span').style.marginRight)).toFixed(1)+' value='+w(d.querySelector('b')).toFixed(1)}}).join(' | ')));
await p.screenshot({{path:'{OUT}/Rubikon3D-grafika-FB-1080.png'}});await b.close()}})()"""
subprocess.run(["node", "-e", js], check=True, cwd=B)
html.unlink()
print("ok")
