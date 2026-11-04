# sections perpendicular to pocket axis, measured as depth below the top face (max projection)
import sys, json, trimesh, numpy as np, collections
path = sys.argv[1]; ax = np.array(json.loads(sys.argv[2]), float); ax /= np.linalg.norm(ax)
depths = json.loads(sys.argv[3])
m = trimesh.load(path, force="mesh")
top = (m.vertices @ ax).max()
print("top face projection", round(top, 3), "axis tilt from Z deg", round(np.degrees(np.arccos(ax[2])), 2))
def width(p):
    ws = [np.ptp(p @ [np.cos(a), np.sin(a)]) for a in np.radians(np.arange(0, 180, 0.25))]
    return min(ws), max(ws)
for d in depths:
    sec = m.section(plane_origin=ax * (top - d), plane_normal=ax)
    if sec is None: print(d, "none"); continue
    pl = sec.to_2D()[0] if hasattr(sec, "to_2D") else sec.to_planar()[0]
    sizes = collections.Counter(); corners = collections.Counter(); nv = collections.Counter()
    for poly in pl.polygons_full:
        for r in poly.interiors:
            p = np.asarray(r.coords)[:-1]; a, b = width(p)
            sizes[round(a, 2)] += 1; corners[round(b, 2)] += 1; nv[len(p)] += 1
    print(f"depth {d}: holes {sum(sizes.values())} flats {dict(sizes)} corners {dict(corners)} nverts {dict(nv)}")
