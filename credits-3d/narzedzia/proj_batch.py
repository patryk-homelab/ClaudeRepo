"""For every Bambu project *_X2D_PETG.3mf under a folder: is the stored mesh closed, how many bodies, faces vs the source mesh
(source = same name without _X2D_PETG, searched in the same folder, ../oryginal and ../../oryginal; .3mf or .stl)."""
import sys, os, glob, zipfile, re, json, numpy as np, trimesh
from concurrent.futures import ProcessPoolExecutor
def load_proj(p):
    z = zipfile.ZipFile(p); parts = []; nf = 0
    for n in z.namelist():
        if not n.endswith('.model'): continue
        x = z.read(n).decode()
        for obj in re.findall(r'<mesh>(.*?)</mesh>', x, re.S):
            v = re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', obj); t = re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', obj)
            parts.append(trimesh.Trimesh(np.array(v, float), np.array(t, int), process=True)); nf += len(t)
    return (trimesh.util.concatenate(parts) if len(parts) > 1 else parts[0]), nf
def find_src(p):
    base = os.path.basename(p).replace('_X2D_PETG.3mf', ''); d = os.path.dirname(p)
    for dd in (d, os.path.join(d, '..', 'oryginal'), os.path.join(d, '..', '..', 'oryginal'), os.path.join(d, '..')):
        for ext in ('.3mf', '.stl'):
            q = os.path.join(dd, base + ext)
            if os.path.exists(q): return q
    return None
def check(p):
    m, nf = load_proj(p); s = find_src(p); sf = None; sdeg = None; sv = None
    if s:
        sm = trimesh.load(s, force='mesh'); sf = len(sm.faces); sdeg = int((sm.area_faces < 1e-12).sum()); sv = round(sm.volume, 2)
    return dict(project=os.path.relpath(p, sys.argv[1]), faces=nf, watertight=bool(m.is_watertight), bodies=int(m.body_count), vol=round(m.volume, 2),
                source=os.path.relpath(s, sys.argv[1]) if s else None, source_faces=sf, source_degenerate=sdeg, source_vol=sv)
if __name__ == '__main__':
    files = sorted(glob.glob(os.path.join(sys.argv[1], '**', '*_X2D_PETG.3mf'), recursive=True))
    with ProcessPoolExecutor(4) as ex: res = list(ex.map(check, files))
    json.dump(res, open(sys.argv[2], 'w'), indent=1)
    bad = [r for r in res if not r['watertight'] or (r['source_faces'] and r['faces'] != r['source_faces'])]
    print('projects', len(res), 'not closed or faces changed:', len(bad))
    for r in bad: print('  ', r)
