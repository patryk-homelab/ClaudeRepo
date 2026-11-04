"""Find round through-holes (screw holes) in a mesh by sections along x, y and z; report diameter profile
(countersink), hole axis, and compare with countersunk wood-screw heads and with the bit axis (wall check).
usage: screw_holes.py MESH '[bit axis]' OUT.json"""
import sys, json, math, numpy as np, trimesh
from shapely.geometry import Polygon
m = trimesh.load(sys.argv[1], force='mesh'); bit = np.array(json.loads(sys.argv[2]), float); bit /= np.linalg.norm(bit)
found = []
for ax in range(3):
    n = np.zeros(3); n[ax] = 1
    lo, hi = m.bounds[0][ax], m.bounds[1][ax]
    for off in np.arange(lo + 0.05, hi, 0.1):
        o = np.zeros(3); o[ax] = off
        sec = m.section(plane_origin=o, plane_normal=n)
        if sec is None: continue
        pl, T = sec.to_2D()
        for poly in pl.polygons_full:
            for ring in poly.interiors:
                p = Polygon(ring); A, P = p.area, p.length
                if P == 0: continue
                rnd = 4 * math.pi * A / P ** 2; d = 2 * math.sqrt(A / math.pi)
                if rnd > 0.97 and 3.0 < d < 14.0:
                    c2 = np.array(p.centroid.coords[0]); c3 = trimesh.transform_points([[c2[0], c2[1], 0]], T)[0]
                    found.append((ax, round(off, 3), c3, d))
groups = []
for ax, off, c3, d in found:
    for g in groups:
        if g['ax'] == ax and np.linalg.norm(np.delete(g['c'] - c3, ax)) < 0.4:
            g['prof'].append((off, d)); break
    else:
        groups.append(dict(ax=ax, c=c3, prof=[(off, d)]))
res = []
heads = {'3.5': {'DIN7997_dk': 6.5}, '4.0': {'DIN7997_dk': 7.5, 'manufacturer_dk': [7.0, 8.9]}, '4.5': {'DIN7997_dk': 8.3, 'manufacturer_dk': [7.6, 9.6]}}
for g in groups:
    if len(g['prof']) < 6: continue
    prof = sorted(g['prof']); offs = np.array([p[0] for p in prof]); ds = np.array([p[1] for p in prof])
    dmin = float(ds.min()); dmax = float(ds.max())
    n = np.zeros(3); n[g['ax']] = 1
    # countersink: the end where the diameter grows
    end = 'max' if ds[-1] > ds[0] + 0.3 else ('min' if ds[0] > ds[-1] + 0.3 else None)
    cyl = offs[np.abs(ds - dmin) < 0.08]
    csk_len = None; angle = None
    if end:
        grow = offs[ds > dmin + 0.15]; csk_len = float(np.ptp(grow) + 0.1) if len(grow) else None
        sel = ds > dmin + 0.15
        if sel.sum() >= 3:
            k = np.polyfit(offs[sel], ds[sel], 1)[0]; angle = round(2 * math.degrees(math.atan(abs(k) / 2)), 1)
    wall_n = n * (1 if end == 'max' else -1) if end else None   # countersink faces away from the wall
    rec = dict(axis='xyz'[g['ax']], centre=np.round(g['c'], 2).tolist(), length=round(float(np.ptp(offs)) + 0.1, 2), d_min=round(dmin, 2), d_max_at_face=round(dmax, 2),
               countersink_end=end, countersink_len=csk_len, countersink_angle_deg=angle)
    if wall_n is not None:
        rec['bit_axis_dot_wall_normal'] = round(float(bit @ wall_n), 3)
        rec['screw_fit'] = {k: dict(shank_clear_per_side=round((dmin - float(k)) / 2, 2), flush_DIN7997=v['DIN7997_dk'] <= dmax + 1e-6,
                                     flush_manufacturer_max=(v['manufacturer_dk'][1] <= dmax + 1e-6) if 'manufacturer_dk' in v else None) for k, v in heads.items()}
    res.append(rec)
json.dump(dict(file=sys.argv[1], bit_axis=bit.round(4).tolist(), holes=res), open(sys.argv[3], 'w'), indent=1)
print(json.dumps(res, indent=0)[:3000])
