"""Compare the snap/rail interface profile of every published holder STL with the v3 reference (native coords)."""
import sys, glob, json, numpy as np, trimesh
from shapely.geometry import Polygon, box
REF = sys.argv[1]; files = sys.argv[2:]
def native_profile(path, is_native=False):
    m = trimesh.load(path, force="mesh")
    s = m.section(plane_origin=[0, 0, 0], plane_normal=[1, 0, 0])
    polys = []
    for l in s.discrete:
        l = np.asarray(l)
        yz = np.c_[l[:, 1], l[:, 2]] if is_native else np.c_[l[:, 2], -l[:, 1]]   # STL -> native: y_n = z_s, z_n = -y_s
        polys.append(Polygon(yz).buffer(0))
    polys.sort(key=lambda p: -p.area); P = polys[0]
    for q in polys[1:]: P = P.symmetric_difference(q)
    return P, m.extents
ref, _ = native_profile(REF, True)
win = box(0, -16, 12.5, 11)          # back interface region: both hooks, the cavity and the foot
refw = ref.intersection(win)
out = []
for f in files:
    try:
        P, ext = native_profile(f)
        d = P.intersection(win).symmetric_difference(refw).area
        out.append((f.split('/')[-1], round(d, 3), [round(e, 1) for e in ext]))
    except Exception as e:
        out.append((f.split('/')[-1], None, repr(e)[:80]))
json.dump(out, open('/tmp/claude-0/-home-user-ClaudeRepo/3bd185f0-9323-594a-8376-ea53d0d67cdd/scratchpad/wk/out/wera_snap_check.json', 'w'))
import collections
print(collections.Counter('match' if (o[1] is not None and o[1] < 0.5) else ('error' if o[1] is None else 'differs') for o in out))
for o in sorted(out, key=lambda o: -(o[1] or 99))[:25]: print(o)
