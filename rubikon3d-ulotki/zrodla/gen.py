"""Generate 3 single-sided A6 leaflets (105x148 trim + 3 mm bleed) as HTML."""
import re, pathlib

B = pathlib.Path(__file__).parent
A = B / "assets"

def qr(k):
    s = (A / f"qr-{k}.svg").read_text()
    n = re.search(r'width="(\d+)"', s).group(1)
    s = re.sub(r'width="\d+" height="\d+"', f'viewBox="0 0 {n} {n}" shape-rendering="crispEdges"', s, count=1)
    return s

ISO = """<svg class="iso" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="iso{id}" width="6.928mm" height="8mm" patternUnits="userSpaceOnUse" viewBox="0 0 6.928 8">
<g stroke="{c}" stroke-width="0.08" fill="none"><path d="M0 0V8M0 0L6.928 4M0 4L6.928 0M0 4L6.928 8M0 8L6.928 4"/></g></pattern></defs>
<rect width="100%" height="100%" fill="url(#iso{id})"/></svg>"""

CSS = (A / "fonts.css").read_text() + """
:root{--red:#E51636;--pink:#F9CDC6;--mid:#F39890;--ink:#1D1D1B;--wa:#40BB61}
@page{size:111mm 154mm;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:111mm;height:154mm;background:#fff}
body{font-family:'Space Grotesk',sans-serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.sheet{position:relative;width:111mm;height:154mm;overflow:hidden;background:#fff}
.iso{position:absolute;inset:0;width:100%;height:100%}
.mono{font-family:'Space Mono',monospace}
.abs{position:absolute}
.qr svg{display:block;width:100%;height:100%}
.contact{font-size:7.6pt;line-height:1.45}
.contact b{font-weight:700}
.lbl{font-family:'Space Mono',monospace;font-size:5.6pt;letter-spacing:.06em;text-transform:uppercase;opacity:.75}
"""

def page(body, extra=""):
    return f"<!doctype html><html lang=pl><head><meta charset=utf-8><style>{CSS}{extra}</style></head><body><div class=sheet>{body}</div></body></html>"

# ---------- A: insert do paczki (podziękowanie + kod rabatowy) ----------
A_CSS = """
.top{position:absolute;left:0;top:0;width:111mm;height:74mm;background:var(--red);overflow:hidden}
.logo{position:absolute;left:11mm;top:12mm;display:flex;align-items:center;gap:3.2mm}
.logo .c{height:15mm}.logo .w{height:10.5mm}
.thx{position:absolute;left:11mm;top:35mm;right:11mm;color:#fff}
.thx h1{font-size:25pt;line-height:1.02;font-weight:700;letter-spacing:-.01em}
.thx p{margin-top:3mm;font-size:9pt;line-height:1.35;color:#fff;opacity:.95}
.cpn{position:absolute;left:11mm;right:11mm;top:81mm;height:31mm;border:.45mm dashed var(--red);border-radius:2.5mm;display:flex;align-items:center;padding:0 5mm;gap:5mm}
.cpn .pct{font-size:36pt;font-weight:700;color:var(--red);line-height:1;letter-spacing:-.02em}
.cpn .t{font-size:8pt;line-height:1.35}
.cpn .code{display:inline-block;margin-top:1.6mm;font-family:'Space Mono',monospace;font-weight:700;font-size:12pt;letter-spacing:.12em;background:var(--red);color:#fff;padding:.8mm 2.4mm;border-radius:1mm}
.bot{position:absolute;left:11mm;right:11mm;top:118mm;display:flex;gap:4.5mm;align-items:stretch}
.bot .txt{height:24mm;display:flex;flex-direction:column;padding:.12mm 0 .46mm} /* korekta: ink glifów (ł, /) równo z krawędziami QR */
.bot .txt h2{text-box-trim:trim-start;text-box-edge:cap alphabetic}
.bot .txt .wa{margin:.9mm 0 0}
.bot .txt .contact{line-height:1.4;margin-top:auto;text-box-trim:trim-end;text-box-edge:cap alphabetic}
.cpn .fine{display:block;margin-top:1.5mm;font-size:5.8pt;color:#8a8a8a}
.bot .qr{width:24mm;height:24mm;flex:none}
.bot h2{font-size:11pt;font-weight:700;color:var(--red);line-height:1.15}
.bot .wa{font-size:7.4pt;color:var(--wa);font-weight:700;margin:1mm 0 1.4mm}
"""
A_BODY = f"""
<div class=top>{ISO.format(id='a', c='#ffffff33')}
 <div class=logo><img class=c src="assets/cube.svg"><img class=w src="assets/wordmark.svg"></div>
 <div class=thx><h1>Dziękujemy<br>za zamówienie!</h1>
 <p>Twoje zamówienie wydrukowaliśmy z dbałością o każdy detal. Mamy nadzieję, że długo posłuży.</p></div>
</div>
<div class=cpn><div class=pct>−10%</div>
 <div class=t><b>Na Twoje następne zamówienie od 50 zł.</b><br>Podaj kod przy zamówieniu:<br><span class=code>PACZKA10</span><span class=fine>Kod ważny do odwołania.</span></div></div>
<div class=bot><div class=qr>{qr('a')}</div>
 <div class=txt><h2>Masz pomysł?<br>Wydrukujemy to.</h2>
 <div class=wa>Zeskanuj i napisz na WhatsApp</div>
 <div class=contact><b>+48 609 692 311</b><br>rubikon3d.com · druk@rubikon3d.com<br>FB / IG: <b>Rubikon3D</b></div></div>
</div>
"""

# ---------- B: ogólna usługowa (3 kroki + co drukujemy) ----------
B_CSS = """
.top{position:absolute;left:0;top:0;width:111mm;height:40mm;background:var(--red);overflow:hidden}
.logo{position:absolute;left:0;right:0;top:11mm;display:flex;justify-content:center;align-items:center;gap:3.2mm}
.logo .c{height:17mm}.logo .w{height:12mm}
.hd{position:absolute;left:11mm;right:11mm;top:46mm}
.hd h1{font-size:21pt;line-height:1.05;font-weight:700;color:var(--red);letter-spacing:-.01em}
.hd p{margin-top:2mm;font-size:9pt;line-height:1.35}
.steps{position:absolute;left:11mm;right:11mm;top:75mm;display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}
.st .n{width:7mm;height:7mm;border-radius:50%;background:var(--red);color:#fff;font-family:'Space Mono',monospace;font-weight:700;font-size:9pt;display:flex;align-items:center;justify-content:center}
.st b{display:block;margin-top:1.8mm;font-size:8.6pt;line-height:1.15}
.st span{display:block;margin-top:.8mm;font-size:7pt;line-height:1.3;opacity:.8}
.tags{position:absolute;left:11mm;right:11mm;top:102mm;display:flex;flex-wrap:wrap;gap:1.4mm}
.tags i{font-style:normal;font-size:7.2pt;background:var(--pink);color:#8c0d21;padding:.9mm 2.2mm;border-radius:5mm;font-weight:500}
.bot{position:absolute;left:0;right:0;bottom:0;height:37mm;background:var(--ink);color:#fff;display:flex;gap:5mm;align-items:center;padding:0 11mm 2mm}
.bot .qr{width:25mm;height:25mm;flex:none;background:#fff;padding:2.2mm;border-radius:1.2mm}
.bot .wa{font-size:8pt;color:var(--wa);font-weight:700;margin-bottom:1.6mm}
.bot .en{margin-top:1.6mm;font-size:6.6pt;opacity:.7}
"""
B_BODY = f"""
<div class=top>{ISO.format(id='b', c='#ffffff33')}
 <div class=logo><img class=c src="assets/cube.svg"><img class=w src="assets/wordmark.svg"></div></div>
<div class=hd><h1>Masz pomysł?<br>Wydrukujemy to.</h1>
 <p>Projektujemy i drukujemy w 3D rzeczy, których nie kupisz w sklepie: na wymiar, w jednym egzemplarzu albo w serii.</p></div>
<div class=steps>
 <div class=st><div class=n>1</div><b>Wyślij zdjęcie lub wymiary</b><span>WhatsApp albo e-mail, wystarczy szkic.</span></div>
 <div class=st><div class=n>2</div><b>Dostajesz projekt i wycenę</b><span>Bez zobowiązań.</span></div>
 <div class=st><div class=n>3</div><b>Drukujemy i wysyłamy</b><span>Gotowe do użycia.</span></div>
</div>
<div class=tags><i>uchwyty i organizery</i><i>części zamienne</i><i>akcesoria do auta</i><i>prezenty z personalizacją</i><i>prototypy</i><i>do domu i warsztatu</i></div>
<div class=bot><div class=qr>{qr('b')}</div>
 <div><div class=wa>Zeskanuj i napisz na WhatsApp</div>
 <div class=contact><b>+48 609 692 311</b><br>druk@rubikon3d.com<br><b>rubikon3d.com</b> · FB / IG: Rubikon3D</div>
 <div class=en>We also speak English!</div></div>
</div>
"""

# ---------- C: "Zepsuło się? Nie wyrzucaj." (części zamienne, mocny haczyk) ----------
C_CSS = """
.bg{position:absolute;inset:0;background:var(--red)}
.big{position:absolute;right:-16mm;top:-10mm;height:78mm;opacity:.95;transform:rotate(0deg)}
.brand{position:absolute;left:11mm;top:11mm;height:9mm}
.hd{position:absolute;left:11mm;right:11mm;top:52mm;color:#fff}
.hd h1{font-size:30pt;line-height:.98;font-weight:700;letter-spacing:-.02em}
.hd p{margin-top:3.2mm;font-size:9.6pt;line-height:1.35;max-width:84mm}
.list{position:absolute;left:11mm;right:11mm;top:91mm;color:#fff;font-family:'Space Mono',monospace;font-size:7.2pt;letter-spacing:.08em;line-height:1.7}
.card{position:absolute;left:8mm;right:8mm;bottom:8mm;height:39mm;background:#fff;border-radius:2.5mm;display:flex;gap:4.5mm;align-items:center;padding:0 5mm}
.card .qr{width:27mm;height:27mm;flex:none}
.card h2{font-size:10.2pt;line-height:1.15;font-weight:700;color:var(--red)}
.card .wa{font-size:7.2pt;color:var(--wa);font-weight:700;margin:1.2mm 0 1.4mm}
"""
C_BODY = f"""
<div class=bg></div>{ISO.format(id='c', c='#ffffff2e')}
<img class=big src="assets/cube.svg">
<img class=brand src="assets/wordmark.svg">
<div class=hd><h1>Zepsuło się?<br>Nie wyrzucaj.</h1>
 <p>Brakującą albo pękniętą część zaprojektujemy na wymiar i wydrukujemy w 3D.</p></div>
<div class=list>KLIPS · POKRĘTŁO · ZAŚLEPKA · ZACZEP<br>UCHWYT · NÓŻKA · OBUDOWA · KOŁO ZĘBATE</div>
<div class=card><div class=qr>{qr('c')}</div>
 <div><h2>Wyślij zdjęcie<br>zepsutej części</h2>
 <div class=wa>Zeskanuj i napisz na WhatsApp</div>
 <div class=contact><b>+48 609 692 311</b><br>rubikon3d.com<br>FB / IG: <b>Rubikon3D</b></div></div>
</div>
"""

# ---------- B2: treść B w układzie A (czerwona góra, biały dół, bez czarnej stopki) ----------
B2_CSS = A_CSS + """
.top{height:70mm}
.thx{top:33mm}
.thx h1{font-size:24pt}
.steps{position:absolute;left:11mm;right:11mm;top:76.5mm;display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}
.st .n{width:6.4mm;height:6.4mm;border-radius:50%;background:var(--red);color:#fff;font-family:'Space Mono',monospace;font-weight:700;font-size:8.4pt;display:flex;align-items:center;justify-content:center}
.st b{display:block;margin-top:1.6mm;font-size:8.4pt;line-height:1.15}
.st span{display:block;margin-top:.7mm;font-size:6.9pt;line-height:1.3;opacity:.8}
.tags{position:absolute;left:11mm;right:11mm;top:100mm;display:flex;flex-wrap:wrap;gap:1.3mm}
.tags i{font-style:normal;font-size:7pt;background:var(--pink);color:#8c0d21;padding:.8mm 2.1mm;border-radius:5mm;font-weight:500}
.bot{top:117mm}
.bot .en{margin-top:1.2mm;font-size:6.4pt;opacity:.65}
"""
B2_BODY = f"""
<div class=top>{ISO.format(id='b2', c='#ffffff33')}
 <div class=logo><img class=c src="assets/cube.svg"><img class=w src="assets/wordmark.svg"></div>
 <div class=thx><h1>Masz pomysł?<br>Wydrukujemy to.</h1>
 <p>Projektujemy i drukujemy w 3D rzeczy, których nie kupisz w sklepie: na wymiar, w jednym egzemplarzu albo w serii.</p></div>
</div>
<div class=steps>
 <div class=st><div class=n>1</div><b>Wyślij zdjęcie lub wymiary</b><span>WhatsApp albo e-mail, wystarczy szkic.</span></div>
 <div class=st><div class=n>2</div><b>Dostajesz projekt i wycenę</b><span>Bez zobowiązań.</span></div>
 <div class=st><div class=n>3</div><b>Drukujemy i wysyłamy</b><span>Gotowe do użycia.</span></div>
</div>
<div class=tags><i>uchwyty i organizery</i><i>części zamienne</i><i>akcesoria do auta</i><i>prezenty z personalizacją</i><i>prototypy</i><i>do domu i warsztatu</i></div>
<div class=bot><div class=qr>{qr('b')}</div>
 <div><h2>Napisz, wycenimy<br>bez zobowiązań.</h2>
 <div class=wa>Zeskanuj i napisz na WhatsApp</div>
 <div class=contact><b>+48 609 692 311</b><br>rubikon3d.com · druk@rubikon3d.com<br>FB / IG: <b>Rubikon3D</b></div>
 <div class=en>We also speak English!</div></div>
</div>
"""

# ---------- D: uniwersalna w stylu C (szerszy zakres pomysłów) ----------
D_CSS = C_CSS + """
.big{top:-6mm;height:50mm;right:-5mm}
.hd{top:37mm}
.hd h1{font-size:26pt;line-height:1}
.hd p{margin-top:3mm;font-size:9.2pt}
.cats{position:absolute;left:11mm;right:11mm;top:79mm;color:#fff;display:grid;grid-template-columns:1fr 1fr;gap:2.6mm 4mm}
.cats div{border-top:.25mm solid #ffffff80;padding-top:1.3mm}
.cats b{display:block;font-family:'Space Mono',monospace;font-weight:700;font-size:6.6pt;letter-spacing:.12em}
.cats span{display:block;font-size:7.8pt;margin-top:.3mm}
.card{height:36mm}
.card .qr{width:26mm;height:26mm}
"""
D_BODY = f"""
<div class=bg></div>{ISO.format(id='d', c='#ffffff2e')}
<img class=big src="assets/cube.svg">
<img class=brand src="assets/wordmark.svg">
<div class=hd><h1>Zepsuło się?<br>Nie ma w sklepie?<br>Wydrukujemy to.</h1>
 <p>Pękniętą część dorobimy na wymiar. Twój pomysł zaprojektujemy od zera.</p></div>
<div class=cats>
 <div><b>NAPRAWA</b><span>klips, pokrętło, zaślepka</span></div>
 <div><b>WARSZTAT I NARZĘDZIA</b><span>uchwyt na wiertła, organizer na bity, adapter do odkurzacza</span></div>
 <div><b>PREZENTY</b><span>lampka ze zdjęciem, mapa 3D ulubionego miejsca, tabliczka</span></div>
 <div><b>FIRMY</b><span>prototyp, krótka seria</span></div>
</div>
<div class=card><div class=qr>{qr('d')}</div>
 <div><h2>Wyślij zdjęcie,<br>szkic albo wymiary</h2>
 <div class=wa>Zeskanuj i napisz na WhatsApp</div>
 <div class=contact><b>+48 609 692 311</b><br>rubikon3d.com<br>FB / IG: <b>Rubikon3D</b></div></div>
</div>
"""

A2_BODY = A_BODY.replace("<h1>Dziękujemy<br>za zamówienie!</h1>", "<h1>Bardzo dziękujemy<br>za zamówienie!</h1>")
A2_CSS = A_CSS + ".thx h1{font-size:23.5pt}"

# B, C, B2 odrzucone (zostają w kodzie tylko do wglądu)
for name, css, body in [("A-paczka", A_CSS, A_BODY), ("A-paczka-bardzo-dziekujemy", A2_CSS, A2_BODY), ("D-pomysly", D_CSS, D_BODY)]:
    (B / f"{name}.html").write_text(page(body, css))
print("ok")
