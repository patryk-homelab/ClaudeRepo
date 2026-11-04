"""Find magnet pockets (rectangles ~60x10 and round ~6 mm) by horizontal sections every 0.1 mm.
Reports, per pocket, the inner size range over its height, its z range (depth) and whether it is open at the top or bottom.
usage: magnet_pockets.py MESH OUT.json"""
import sys, json, math, numpy as np, trimesh
from shapely.geometry import Polygon
m = trimesh.load(sys.argv[1], force='mesh')
if isinstance(m, trimesh.Scene): m = m.dump(concatenate=True)
z0, z1 = m.bounds[0][2], m.bounds[1][2]
rec = []
for z in np.arange(z0 + 0.05, z1, 0.1):
    sec = m.section(plane_origin=[0, 0, z], plane_normal=[0, 0, 1])
    if sec is None: continue
    pl, T = sec.to_2D()
    for poly in pl.polygons_full:
        for ring in poly.interiors:
            p = Polygon(ring); A = p.area
            if A < 15: continue
            r = p.minimum_rotated_rectangle; xs, ys = r.exterior.coords.xy
            e = sorted([math.dist((xs[0], ys[0]), (xs[1], ys[1])), math.dist((xs[1], ys[1]), (xs[2], ys[2]))])
            rnd = 4 * math.pi * A / p.length ** 2
            c = np.array(p.centroid.coords[0]); c3 = trimesh.transform_points([[c[0], c[1], 0]], T)[0]
            kind = 'round' if rnd > 0.97 else ('rect' if A / (e[0] * e[1]) > 0.97 else 'other')
            if kind == 'other': continue
            rec.append(dict(z=round(z, 2), kind=kind, c=c3[:2], w=e[0], l=e[1], d=2 * math.sqrt(A / math.pi)))
groups = []
for r in rec:
    for g in groups:
        if g['kind'] == r['kind'] and np.linalg.norm(g['c'] - r['c']) < 0.6 and abs(np.median(g['l']) - r['l']) < 3:
            g['z'].append(r['z']); g['w'].append(r['w']); g['l'].append(r['l']); g['d'].append(r['d']); break
    else:
        groups.append(dict(kind=r['kind'], c=r['c'], z=[r['z']], w=[r['w']], l=[r['l']], d=[r['d']]))
out = []
for g in groups:
    if len(g['z']) < 3: continue
    big = (g['kind'] == 'rect' and 40 < np.median(g['l']) < 80) or (g['kind'] == 'round' and 4 < np.median(g['d']) < 14)
    if not big: continue
    out.append(dict(kind=g['kind'], centre=np.round(g['c'], 1).tolist(), z_from=min(g['z']), z_to=max(g['z']), height=round(max(g['z']) - min(g['z']) + 0.1, 2),
                    width=[round(min(g['w']), 2), round(max(g['w']), 2)], length=[round(min(g['l']), 2), round(max(g['l']), 2)],
                    diameter=[round(min(g['d']), 2), round(max(g['d']), 2)] if g['kind'] == 'round' else None, part_z=[round(z0, 2), round(z1, 2)]))
json.dump(dict(file=sys.argv[1], pockets=out), open(sys.argv[2], 'w'), indent=1)
print(sys.argv[1].split('/')[-1], 'bbox', np.round(m.extents, 2).tolist())
for o in out: print('  ', o)
