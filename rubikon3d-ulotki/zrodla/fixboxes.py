"""Set exact 111x154 mm MediaBox/BleedBox and 105x148 mm TrimBox on print PDFs, then verify QR in previews."""
import sys, pypdf
MM = 72 / 25.4
for f in sys.argv[1:]:
    r = pypdf.PdfReader(f); w = pypdf.PdfWriter(); pg = r.pages[0]; H = float(pg.mediabox.top)
    y0 = H - 154 * MM
    pg.mediabox = pypdf.generic.RectangleObject([0, y0, 111 * MM, H]); pg.cropbox = pg.mediabox; pg.bleedbox = pg.mediabox
    pg.trimbox = pypdf.generic.RectangleObject([3 * MM, y0 + 3 * MM, 108 * MM, H - 3 * MM])
    w.add_page(pg); w.write(f)
