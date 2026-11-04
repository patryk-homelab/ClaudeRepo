import sys, numpy as np, trimesh, math
from shapely.geometry import Polygon, box
from shapely.affinity import translate
h = trimesh.load(sys.argv[1]); r = trimesh.load(sys.argv[2])
def prof(m, x, plane='x'):
    s = m.section(plane_origin=[x, 0, 0], plane_normal=[1, 0, 0])
    polys = [Polygon(np.asarray(l)[:, 1:3]) for l in s.discrete]
    polys.sort(key=lambda p: -p.area); P = polys[0]
    for q in polys[1:]: P = P.difference(q)
    return P
H = prof(h, float(sys.argv[3]) if len(sys.argv) > 3 else 0.0)
R0 = prof(r, 10.0)  # rail coords: (y_r, z_r)
# map rail -> holder: y_h = 5 - z_r ; z_h = y_r - 3  (rail back z=4.5 at holder back y=0.5, rail centre at cutout centre z=-3)
Rc = np.asarray(R0.exterior.coords)
A = float(sys.argv[4]) if len(sys.argv) > 4 else 4.55
R = Polygon(np.c_[A - Rc[:, 1], Rc[:, 0] - 3.0])
print("holder back-region outline (y<10):")
pts = np.asarray(H.exterior.coords); print([tuple(p) for p in np.round(pts[pts[:, 0] < 10], 2)][:40])
print("assembled overlap area mm2:", round(H.intersection(R).area, 4))
# insertion: rail moves from behind (y shift -6) to seated (0) in 0.05 steps; record overlap and its z extent (deflection proxy)
worst = (0, None)
for dy in np.arange(-6.0, 0.0001, 0.05):
    Rs = translate(R, xoff=dy)
    ov = H.intersection(Rs)
    if ov.area > 1e-4:
        parts = [ov] if ov.geom_type == 'Polygon' else list(ov.geoms)
        for p in parts:
            zmin, zmax = p.bounds[1], p.bounds[3]
            pen = zmax - zmin
            side = 'top' if (zmin + zmax) / 2 > -3 else 'bottom'
            if pen > worst[0]: worst = (pen, (round(dy, 2), side, round(p.area, 3), [round(v, 2) for v in p.bounds]))
print("max z-penetration during insertion (needed lip deflection, both sides together if symmetric):", round(worst[0], 3), worst[1])
