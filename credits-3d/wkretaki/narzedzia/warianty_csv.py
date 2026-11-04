"""Variant table for P078 (one Wera/Holex holder per row): names, author test status, catalogue check, Bambu X2D grams/time.
usage: make_csv.py RESULTS.txt WERA_COMPARE.json OUT.csv"""
import sys, re, json, csv, collections
res, cmpf, out = sys.argv[1:4]
slices = {}
for l in open(res):
    m = re.match(r'w140_screwdriver_holder_(\S+)_snapfix rc=(\d+) result=\'([^\']*)\' support_features=(\d*).*?weight \[g\] : ([\d.]+).*?time ([\d.]+) h', l)
    if m: slices[m.group(1)] = dict(ok=m.group(3) == 'Success.', sup=int(m.group(4) or 0), g=float(m.group(5)), h=float(m.group(6)))
cmp = {x[0].replace('screwdriver_holder_', '').replace('.stl', ''): x[1] for x in json.load(open(cmpf))}
TESTED = {('160i','flat','2.5'),('160i','flat','3.0'),('247','flat','3.0'),('334','flat','6.5x150'),('335','flat','3.5'),('335','flat','4.0'),
 ('350','PH','1'),('350','PH','2'),('350','PH','3'),('355','PZ','1'),('355','PZ','2'),('355','PZ','3'),('367','TX','10'),('367','TX','15'),('367','TX','20'),
 ('367','TX','25'),('367','TX','30'),('391','nasadka','6'),('391','nasadka','7'),('391','nasadka','8'),('393S','',''),('812/1','',''),('917','PH','1'),('917','PH','2'),
 ('917','PH','3'),('918','PZ','1'),('918','PZ','2'),('918','PZ','3'),('932A','flat','7.0'),('932A','flat','5.5'),('932A','flat','10')}
UNTESTED = {('160iS','flat','4.0'),('160iS','flat','5.5'),('162iS','PH','1'),('162iS','PH','2'),('165iS','PZ','1'),('165iS','PZ','2'),('334','flat','5.0'),
 ('334','flat','6.0'),('334','flat','6.5x200'),('334','flat','7.0'),('334','flat','8.0'),('334','flat','10'),('335','flat','2.5'),('335','flat','3.0'),
 ('335','flat','5.5'),('335','flat','6.0'),('350','PH','0'),('350','PH','4'),('352','hex','1.5'),('352','hex','2'),('352','hex','2.5'),('352','hex','3'),
 ('352','hex','4'),('352','hex','5'),('352','hex','6'),('352','hex','8'),('352','hex','10'),('355','PZ','0'),('355','PZ','4'),('367','TX','5'),('367','TX','6'),
 ('367','TX','7'),('367','TX','8'),('367','TX','9'),('367','TX','27'),('367','TX','40'),('395','nasadka','5'),('395','nasadka','5.5'),('395','nasadka','6'),
 ('395','nasadka','7'),('395','nasadka','8'),('395','nasadka','10'),('395','nasadka','13'),('932A','flat','3.5'),('932A','flat','4.5'),('977','TX','20'),('977','TX','25')}
def num(s):  # Wera encodes mm x10 in file names: 25 -> 2.5, 100 -> 10, 130 -> 13
    return ('%g' % (int(s) / 10)) if s.isdigit() else s
def holex(s):  # Holex files use plain mm, except 45 -> 4.5 and 55 -> 5.5
    return {'45': '4.5', '55': '5.5'}.get(s, s)
rows = []
for stem in sorted(slices) + [s for s in cmp if s not in slices]:
    t = stem.split('_'); prod = 'Holex' if t[0] == 'holex' else 'Wera'
    hole = next((x.replace('mm', ' mm') for x in t if re.fullmatch(r'\d\dmm', x)), ''); v2 = 'v2' in t
    t = [x for x in t if not re.fullmatch(r'\d\dmm', x) and x != 'v2']
    series, typ, size, name = '', '', '', ''
    if prod == 'Holex':
        series, typ, size = '62 2200', 'nasadka', holex(t[-1]); name = f'Holex 62 2200 nasadka {size} mm'
    else:
        series = t[1]; rest = t[2:]
        if rest and rest[0] == 'vde': rest = rest[1:]
        if not rest: typ, size = '', ''
        elif rest[0] in ('ph', 'pz', 'pzs', 'tx'): typ, size = rest[0].upper().replace('PZS', 'PZ/S'), rest[1]
        elif rest[0] == 'flat':
            s = rest[1]; typ = 'flat'
            if 'x' in s: a, b = s.split('x'); size = num(a) + 'x' + b
            else: size = num(s)
        elif rest[0] == 'hex': typ, size = 'hex', num(rest[1])
        elif rest[0] == 'nut': typ, size = 'nasadka', num(rest[1])
        elif rest[0] == 'square': typ, size = 'square', '#' + rest[1]
        else: typ, size = '', '_'.join(rest)
        if series in ('811', '812') and size == '1': series, typ, size = series + '/1', '', ''
        if series == '816': typ, size = '', 'RA'
        if series == '1427': typ, size = 'szydło', ''
        if series == '1428': typ, size = 'rozwiertak', ''
        lab = {'flat': 'płaski', 'hex': 'imbus', 'nasadka': 'nasadka', 'square': 'kwadrat'}.get(typ, typ)
        unit = ' mm' if typ in ('flat', 'hex', 'nasadka') else ''
        vde = ' VDE' if 'vde' in stem else ''
        sep = '' if typ in ('PH', 'PZ', 'PZ/S', 'TX') else ' '
        name = f'Wera {series}{vde} {lab}{sep}{size}{unit}'.replace('  ', ' ').strip()
    key = (series, {'PZ/S': 'PZ'}.get(typ, typ), size.replace('#', ''))
    if prod == 'Wera' and key[0] in ('393S',): key = ('393S', '', '')
    if prod == 'Wera' and key[0] in ('812/1',): key = ('812/1', '', '')
    k2 = key
    norm = lambda k: (k[0], k[1], ('%g' % float(k[2])) if k[2].replace('.', '', 1).isdigit() else k[2])
    TESTEDN = {norm(x) for x in TESTED}; UNTESTEDN = {norm(x) for x in UNTESTED}
    tested = norm(key) in TESTEDN
    untested = norm(key) in UNTESTEDN
    status = 'przetestowany przez autora' if tested and not hole and not ('PZ/S' in typ) else ('nieprzetestowany (wymiary z katalogu Wera)' if untested and not hole else 'nie ma na liście autora')
    if hole: status = 'wariant: otwór rękojeści ' + hole + ' (nie ma na liście autora)'
    code = {'flat': 'FL', 'hex': 'HEX', 'nasadka': 'NUT', 'square': 'SQ', 'szydło': 'AWL', 'rozwiertak': 'REAMER', 'PZ/S': 'PZS'}.get(typ, typ)
    sku = 'P078-' + ('HOLEX-' if prod == 'Holex' else series.upper().replace('/', '-') + '-') + (code + size.replace('#', '')).upper().replace(' ', '') \
          + ('-' + hole.split()[0] if hole else '') + ('-V2' if v2 else '')
    sku = sku.rstrip('-')
    sl = slices.get(stem, {})
    rows.append(dict(sku=sku, nazwa=name + (' (otwór ' + hole + ')' if hole else ''), producent=prod, seria=series, typ=typ, rozmiar=size, wersja_pliku='v2' if v2 else '',
        status_autora=status, katalog_wera={'OK': 'zgodny', 'no catalogue data': 'brak danych w katalogu', 'not a Wera model file': 'nie dotyczy'}.get(cmp.get(stem), ''),
        na_start='tak' if status.startswith('przetestowany') else 'nie (na zamówienie)', filament_g=sl.get('g', ''), czas_h=sl.get('h', ''),
        podpory_fragmenty=sl.get('sup', ''), plik_projektu=f'screwdriver_holder_{stem}_snapfix_X2D_PETG.3mf'))
names = collections.Counter(r['nazwa'] for r in rows)
for r in rows: r['duplikat'] = 'tak – wybrać jeden przed wystawieniem' if names[r['nazwa']] > 1 else ''
with open(out, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter=';'); w.writeheader(); w.writerows(rows)
print('rows', len(rows), 'sliced', sum(1 for r in rows if r['filament_g'] != ''), 'na_start', sum(r['na_start'] == 'tak' for r in rows),
      'dupl', sum(1 for r in rows if r['duplikat']), collections.Counter(r['status_autora'].split(' (')[0] for r in rows))
