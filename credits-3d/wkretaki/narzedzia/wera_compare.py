"""Compare each published Wera holder's socket with Wera catalogue data (www.wera.de 'Facts and figures', read 2026-11-04
by two independent readers that agreed on every value used here)."""
import json, re
refs = {r['file'][4:-4]: r for r in json.load(open('wera_sockets_ref.json'))}
pub = json.load(open('wera_sockets.json'))
# catalogue: model -> {size: (blade_d, handle_length)}
PH = {'0': (3.0, '81'), '1': (4.5, '98'), '2': (6.0, '105'), '3': (8.0, '112'), '4': (10.0, '112')}
CAT = {
 '350_ph': PH, '355_pz': PH,
 '335_flat': {'20': (2.5, '70'), '25': (2.5, '70'), '30': (3.0, '81'), '35': (3.5, '81'), '40': (4.0, '98'), '55': (5.5, '98'), '60': (6.0, '105')},
 '334_flat': {'50': (5.0, '98'), '60': (6.0, '105'), '65x150': (6.0, '105'), '65x200': (7.0, '105'), '70': (7.0, '105'), '80': (7.0, '112'), '100': (9.0, '112')},
 '367_tx': {'5': (3.5, '70'), '6': (3.5, '70'), '7': (3.5, '70'), '8': (3.5, '81'), '9': (4.0, '81'), '10': (4.0, '81'), '15': (4.0, '98'), '20': (4.5, '98'), '25': (5.0, '105'), '27': (5.5, '105'), '30': (6.0, '105'), '40': (7.0, '112')},
}
VDE_HL = {'160i_vde_flat': {'25': '81', '30': '81', '35': '81', '40': '98', '55': '98', '65': '105'}, '160iS_vde_flat': {'40': '98', '55': '98'},
          '162i_vde_ph': {'0': '81', '1': '98', '2': '105', '3': '112', '4': '112'}, '162iS_vde_ph': {'1': '98', '2': '105'},
          '165iS_vde_pz': {'1': '98', '2': '105'}, '165iS_vde_pzs': {'1': '98', '2': '105'},
          '167i_vde_tx': {'5': '81', '6': '81', '7': '81', '8': '81', '9': '81', '10': '81', '15': '98', '20': '98', '25': '105', '30': '105'}}
def handle_class(w):
    best = min(refs.items(), key=lambda kv: abs(kv[1]['handle_z9'] - w))
    return best[0], round(w - best[1]['handle_z9'], 2)
rows = []
for r in pub:
    f = r['file']; m = re.match(r'screwdriver_holder_wera_(\d+[a-zA-Z]*(?:_vde)?_[a-z]+)_([0-9x]+)(.*)\.stl', f)
    if not m: rows.append((f, 'not a Wera model file', r)); continue
    key, size, var = m.group(1), m.group(2), m.group(3)
    cls, dcls = handle_class(r['handle_z9'] or 0)
    exp = None; blade = None
    if key in CAT and size in CAT[key]: blade, exp = CAT[key][size]
    elif key in VDE_HL and size in VDE_HL[key]: exp = VDE_HL[key][size]
    st = []
    if exp and not cls.startswith(exp): st.append(f'handle socket {cls} but Wera handle length {exp}')
    if blade is not None and r['shaft_z-11'] is not None:
        gap = (r['shaft_z-11'] - blade) / 2
        if gap < 0.1: st.append(f'shaft hole {r["shaft_z-11"]} vs blade {blade} -> {gap:+.2f} mm/side')
    rows.append((f, '; '.join(st) if st else ('OK' if exp else 'no catalogue data'), dict(shaft=r['shaft_z-11'], ferrule=r['ferrule_z0'], handle_cls=cls, dcls=dcls, blade=blade, wera_handle=exp)))
json.dump(rows, open('wera_compare.json', 'w'), indent=0)
import collections
print(collections.Counter(x[1] if x[1] in ('OK', 'no catalogue data', 'not a Wera model file') else 'MISMATCH' for x in rows))
for x in rows:
    if x[1] not in ('OK', 'no catalogue data', 'not a Wera model file'): print(x[0], '|', x[1], '|', x[2])
