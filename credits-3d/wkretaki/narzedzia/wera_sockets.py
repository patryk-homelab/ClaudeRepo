"""Measure the socket of every published holder (native coords: y = depth from the back, z = up; STL y = -native z)."""
import sys, json, re, numpy as np, trimesh
from shapely.geometry import Polygon, LineString
def width_at(m, zn, y_line=25.0):
    s = m.section(plane_origin=[0, -zn, 0], plane_normal=[0, 1, 0])
    if s is None: return None
    best = None
    for l in s.discrete:
        p = np.asarray(l); q = Polygon(np.c_[p[:, 0], p[:, 2]]).buffer(0)
        if q.area < 1: continue
        # holes are interiors of the outer polygon OR separate loops; collect all loops as rings and find the gap on the line
        best = q if best is None or q.area > best.area else best
    if best is None: return None
    rings = [best] + [Polygon(r) for r in getattr(best, 'interiors', [])]
    L = LineString([(-30, y_line), (30, y_line)])
    I = best.intersection(L)
    segs = [I] if I.geom_type == 'LineString' else list(getattr(I, 'geoms', []))
    xs = sorted([tuple(sorted((g.coords[0][0], g.coords[-1][0]))) for g in segs if g.length > 0])
    gaps = [(xs[i][1], xs[i + 1][0]) for i in range(len(xs) - 1)]
    g = [b - a for a, b in gaps if a < 0 < b]
    return round(g[0], 2) if g else (0.0 if any(a <= 0 <= b for a, b in xs) else None)
out = []
for f in sys.argv[1:]:
    m = trimesh.load(f, force="mesh")
    rec = dict(file=f.split('/')[-1], width_x=round(float(m.extents[0]), 1))
    for name, zn in [("shaft_z-11", -11.0), ("ferrule_z0", 0.0), ("handle_z7", 7.0), ("handle_z9", 9.0)]:
        rec[name] = width_at(m, zn)
    out.append(rec)
json.dump(out, open(sys.argv[0].replace('.py', '.json'), 'w'), indent=0)
for r in out[:8]: print(r)
