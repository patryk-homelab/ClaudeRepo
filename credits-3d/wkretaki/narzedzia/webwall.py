# minimum material width in horizontal sections: distance between neighbouring holes and from holes to the outline
import sys, trimesh, numpy as np
from shapely.geometry import Polygon
from shapely.strtree import STRtree
m = trimesh.load(sys.argv[1]); m.apply_translation([0, 0, -m.bounds[0][2]])
for z in [0.1, 0.3, 1.0, 3.0, 7.0, 12.0, 14.5]:
    if z > m.bounds[1][2]: continue
    s = m.section(plane_origin=[0, 0, z], plane_normal=[0, 0, 1])
    loops = [Polygon(np.asarray(l)[:, :2]) for l in s.discrete]
    loops.sort(key=lambda p: -p.area); outer, holes = loops[0], [p for p in loops[1:] if p.area > 20]
    tree = STRtree(holes); dmin = 99
    for i, h in enumerate(holes):
        for j in tree.query(h.buffer(3.0)):
            if j != i: dmin = min(dmin, h.distance(holes[j]))
        dmin_o = min(h.exterior.distance(outer.exterior) for h in holes)
    print(f"z={z}: holes {len(holes)}, min web between holes {dmin:.3f} mm, min hole-to-outline {dmin_o:.3f} mm")
