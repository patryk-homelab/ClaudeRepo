# horizontal shelf with vertical through-holes: z-levels, hole sizes, centres, back wall position
import sys, json, math, trimesh, numpy as np, collections
from shapely.geometry import Polygon
m = trimesh.load(sys.argv[1], force="mesh"); out = sys.argv[2]
zs = collections.Counter(np.round(m.vertices[:, 2], 2)); print("z levels (count>20):", sorted(k for k, v in zs.items() if v > 20)[:20])
def holes_at(z):
    s = m.section(plane_origin=[0, 0, z], plane_normal=[0, 0, 1]); res = []
    if s is None: return res, None
    loops = [np.asarray(l)[:-1, :2] for l in s.discrete]
    polys = sorted([Polygon(l) for l in loops], key=lambda p: -p.area)
    outer = polys[0]
    for p in polys[1:]:
        if p.area < 5 or p.area > 2000: continue
        c = np.array(p.centroid.coords[0]); pts = np.asarray(p.exterior.coords)
        ws = [np.ptp(pts @ [math.cos(a), math.sin(a)]) for a in np.radians(np.arange(0, 180, 0.5))]
        res.append(dict(c=c.round(3).tolist(), flats=round(min(ws), 3), corners=round(max(ws), 3), area=round(p.area, 2), n=len(pts) - 1))
    return res, outer
info = {}
for z in [float(a) for a in sys.argv[3:]]:
    h, outer = holes_at(z)
    if not h: print(z, "no holes"); continue
    fl = collections.Counter(x["flats"] for x in h); co = collections.Counter(x["corners"] for x in h)
    print(f"z={z}: holes {len(h)} flats {dict(fl)} corners {dict(co)} outer bounds {np.round(outer.bounds,2).tolist()}")
    info[z] = dict(holes=h, outer_bounds=list(outer.bounds), outer_wkt=outer.wkt)
json.dump(info, open(out, "w"))
