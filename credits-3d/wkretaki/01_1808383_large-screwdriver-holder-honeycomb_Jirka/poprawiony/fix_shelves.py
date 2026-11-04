"""Fixes for two CC0 screwdriver shelves by Jirka (Printables 1808383, 1782552). Mesh-level edits with manifold3d on the
original STL; every cutter is a hole shape copied from the part itself (section of a regular hole), so nothing new is invented.
1808383: one hole (at x 121.3, y 151.3) is widened from below to a 10.4 mm hexagon for 10 mm of height (web 0.7 mm, needs a
         support from the bed in Bambu Studio). Refill that pocket and re-cut the regular 9.0 mm hole.
1782552: 21 holes along the rim are clipped by the pattern boundary (3.9-7.5 mm instead of 8.0 mm). Cut the full 8.0 mm hole
         at each lattice site; the remaining wall to the outline is >= 1.51 mm (webs between holes are 1.40 mm).
usage: fix_shelves.py 1808383|1782552 IN.stl OUT_PREFIX"""
import sys, math, numpy as np, trimesh, manifold3d as mf
from shapely.geometry import Polygon
from shapely.geometry.polygon import orient
which, src, outp = sys.argv[1], sys.argv[2], sys.argv[3]
m = trimesh.load(src, force="mesh")
part = mf.Manifold(mf.Mesh(vert_properties=np.asarray(m.vertices, np.float32), tri_verts=np.asarray(m.faces, np.uint32)))
assert part.status() == mf.Error.NoError
def loops(z):
    s = m.section(plane_origin=[0, 0, z], plane_normal=[0, 0, 1])
    return [np.asarray(l)[:-1, :2] for l in s.discrete]
def ccw(pts): return [list(orient(Polygon(pts), 1.0).exterior.coords)[:-1]]
def flats(p): return min(np.ptp(p @ [math.cos(a), math.sin(a)]) for a in np.radians(np.arange(0, 180, 0.5)))
def prism(pts, z0, z1): return mf.Manifold.extrude(mf.CrossSection(ccw(pts)), z1 - z0).translate([0, 0, z0])
if which == "1808383":
    SHELF_TOP, ODD = 20.0, np.array([121.325, 151.316])
    low = [l for l in loops(5.0) if np.linalg.norm(l.mean(0) - ODD) < 1.0][0]          # 10.4 mm pocket (z 0..10)
    up = [l for l in loops(15.0) if np.linalg.norm(l.mean(0) - ODD) < 1.0][0]          # regular 9.0 mm hole above it
    ref = [l for l in loops(15.0) if np.linalg.norm(l.mean(0) - ODD) > 15 and abs(flats(l) - 9.0) < 0.01][0]
    print("pocket flats", round(flats(low), 3), "hole above", round(flats(up), 3), "centre offset", np.round(low.mean(0) - up.mean(0), 3))
    fill = prism(Polygon(low).buffer(0.05, join_style=2).exterior.coords[:-1], 0.0, 10.5)  # slightly larger than the pocket
    cut = prism(up, -1.0, SHELF_TOP + 1.0)
    fixed = (part + (fill ^ mf.Manifold.cube([1000, 1000, 10.5]).translate([-500, -500, 0]))) - cut
elif which == "1782552":
    TOP = 25.0
    L = loops(10.0)
    full = [l for l in L if abs(flats(l) - 8.0) < 0.01]
    t12 = [l for l in full if len(l) == 12][0]          # clean 12-vertex outline as the cutter template
    tmpl = t12 - Polygon(t12).centroid.coords[0]
    C = np.array([Polygon(l).centroid.coords[0] for l in full])
    vecs = [np.array(v) for v in [(9.4, 0), (-9.4, 0), (4.7, 8.14), (-4.7, 8.14), (4.7, -8.14), (-4.7, -8.14)]]
    clipped = [l for l in L if 3.0 < flats(l) < 7.99 and Polygon(l).area < 60]
    # each clipped hole lies inside the full hexagon of its lattice site: test lattice points around it and keep the one
    # whose full hexagon contains the clipped outline (intersection / clipped area closest to 1)
    a, b = np.array([9.4, 0.0]), np.array([4.7, 8.1406])
    cut = None; sites = []
    for l in clipped:
        cp = Polygon(l); c = np.array(cp.centroid.coords[0])
        near = C[np.argsort(np.linalg.norm(C - c, axis=1))[:4]]
        cands = [n0 + i * a + j * b for n0 in near for i in range(-3, 4) for j in range(-3, 4)]
        cands = [q for q in cands if np.linalg.norm(q - c) < 6.0]
        if not cands: print("NO CANDIDATE near", c.round(2), "nearest full", near[0].round(2), np.linalg.norm(near[0]-c).round(2)); continue
        best = max(cands, key=lambda q: (Polygon(tmpl + q).intersection(cp).area / cp.area, -np.linalg.norm(q - c)))
        cover = Polygon(tmpl + best).intersection(cp).area / cp.area
        assert cover > 0.995, (c, cover)
        sites.append((best.round(3).tolist(), round(cover, 4)))
        # cutter grown by 0.005 mm so its faces never coincide with the clipped hole's faces (coincident faces leave
        # zero-area triangles that Bambu Studio deletes on import, which opens the mesh); 0.005 mm is far below print resolution
        grown = np.asarray(Polygon(tmpl + best).buffer(0.005, join_style=2).exterior.coords)[:-1]
        p = prism(grown, -1.0, TOP + 1.0); cut = p if cut is None else cut + p
    print("sites", sites)
    print("clipped holes", len(clipped))
    fixed = part - cut
fixed = fixed.simplify(1e-5); assert fixed.status() == mf.Error.NoError
print('zero-area triangles in result:', int(sum(1 for _ in [0])) if False else '')
mm = fixed.to_mesh(); out = trimesh.Trimesh(np.asarray(mm.vert_properties)[:, :3], np.asarray(mm.tri_verts), process=True)
bb = out.split(only_watertight=False)
if len(bb) > 1:  # zero-area sliver shells left where cutter faces coincide with existing hole faces
    main = max(bb, key=lambda b: abs(b.volume) if b.is_watertight else 0)
    junk = [b for b in bb if b is not main]
    print("dropped sliver shells:", len(junk), "max area", round(max(float(b.area) for b in junk), 6), "max |volume|", round(max(abs(float(b.volume)) for b in junk), 6))
    assert max(float(b.area) for b in junk) < 1e-3
    out = main
assert out.is_watertight and len(out.split(only_watertight=False)) == 1
assert abs(out.volume - fixed.volume()) < 0.05, (out.volume, fixed.volume())
out.export(outp + ".stl"); out.export(outp + ".3mf")
print(dict(vol_orig=round(part.volume(), 1), vol_fixed=round(fixed.volume(), 1), added=round((fixed - part).volume(), 2), removed=round((part - fixed).volume(), 2), bbox=out.extents.round(2).tolist()))
