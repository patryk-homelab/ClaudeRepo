"""Practical capacity of a shelf holder: how many screwdrivers with handle diameter D can hang at once.
A hole is usable if the handle circle (D/2 + 0.5 mm) clears everything that rises above the shelf top and the wall plane.
Then a greedy pick (rows from the front) keeps handle centres >= D + 1 mm apart."""
import sys, json, math, numpy as np, trimesh
from shapely.geometry import Point
from shapely.ops import unary_union
from shapely.geometry import Polygon
stl, holes_json, ztop, ywall = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
min_flats = float(sys.argv[5]) if len(sys.argv) > 5 else 0
m = trimesh.load(stl, force='mesh')
info = json.load(open(holes_json)); d = info[sorted(info, key=float)[len(info) // 2]]
H = [h for h in d['holes'] if h['flats'] >= min_flats]
C = np.array([h['c'] for h in H])
s = m.section(plane_origin=[0, 0, ztop + 3], plane_normal=[0, 0, 1])
obst = unary_union([Polygon(np.asarray(l)[:, :2]).buffer(0) for l in s.discrete]) if s is not None else None
res = {}
for D in [23, 27, 30, 36, 41]:
    ok = []
    for c in C:
        circ = Point(c).buffer(D / 2 + 0.5)
        if c[1] + D / 2 + 0.5 > ywall: continue
        if obst is not None and circ.intersects(obst): continue
        ok.append(c)
    ok = sorted(ok, key=lambda c: (c[1], c[0]))  # front rows first
    pick = []
    for c in ok:
        if all(np.hypot(*(c - p)) >= D + 1 for p in pick): pick.append(c)
    res[D] = dict(usable_holes=len(ok), at_once=len(pick))
print(json.dumps(dict(holes=len(C), obstacles_above_shelf_area=round(obst.area, 1) if obst else 0, capacity=res)))
