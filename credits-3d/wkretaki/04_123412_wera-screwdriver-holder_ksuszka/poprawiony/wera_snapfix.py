"""Snap fix for 'Wera Screwdriver Holder' by ksuszka (Printables 123412, CC BY), applied to each published holder STL.
Adds a 1 mm relief slot (native coords: y 3 -> 12 mm from the back face, z -13..-12, full width) so the bottom snap foot
bends over ~10.5 mm instead of ~5.75 mm. Same cut as `snap_relief_end_y = 12` in wera_screwdriver_holder_v3_snapfix.scad.
STL files are in the author's print orientation: STL = rotate([90,0,0]) * native, i.e. STL (x, -z_n, y_n).
usage: wera_snapfix.py OUTDIR file1.stl file2.stl ..."""
import sys, os, json, numpy as np, trimesh, manifold3d as mf
from shapely.geometry import Polygon, LineString
outdir = sys.argv[1]; files = sys.argv[2:]
RELIEF_END_Y, Z0, Z1 = 12.0, -13.0, -12.0
def man(m): return mf.Manifold(mf.Mesh(vert_properties=np.asarray(m.vertices, np.float32), tri_verts=np.asarray(m.faces, np.uint32)))
box = mf.Manifold.cube([60, 1, 1]).translate([-30, 3, Z0])
cyl = mf.Manifold.cylinder(60, 0.5, 0.5, 24).transform([[0, 0, 1, -30], [0, 1, 0, 0], [1, 0, 0, 0]]).translate([0, RELIEF_END_Y - 0.5, Z0 + 0.5])
cut_native = mf.Manifold.hull(box + cyl)
TO_STL = [[1, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0]]
cut = cut_native.transform(TO_STL)
def foot_profile(m):
    s = m.section(plane_origin=[0, 0, 0], plane_normal=[1, 0, 0]); P = None
    for l in s.discrete:
        l = np.asarray(l); q = Polygon(np.c_[l[:, 2], -l[:, 1]]).buffer(0)
        P = q if P is None else P.symmetric_difference(q)
    res = {}
    for y in (5.0, 7.0, 9.0, 11.0, 11.9, 12.5):
        I = P.intersection(LineString([(y, -16), (y, -9)]))
        segs = [I] if I.geom_type == 'LineString' else list(getattr(I, 'geoms', []))
        res[y] = sorted([tuple(sorted((round(g.coords[0][1], 2), round(g.coords[-1][1], 2)))) for g in segs if g.length > 0])
    return res
report = []
for f in files:
    name = os.path.basename(f); m = trimesh.load(f, force='mesh'); A = man(m)
    if A.status() != mf.Error.NoError: report.append(dict(file=name, error=str(A.status()))); continue
    before = foot_profile(m)
    B = A - cut; assert B.status() == mf.Error.NoError   # no simplify: vertex merging after simplify opened edges on 3 files
    mm = B.to_mesh(); out = trimesh.Trimesh(np.asarray(mm.vert_properties)[:, :3], np.asarray(mm.tri_verts), process=True)
    bb = out.split(only_watertight=False)
    if len(bb) > 1:
        main = max(bb, key=lambda b: abs(b.volume) if b.is_watertight else 0)
        assert max(float(b.area) for b in bb if b is not main) < 1e-3; out = main
    ok = bool(out.is_watertight and len(out.split(only_watertight=False)) == 1)
    after = foot_profile(out)
    stem = name[:-4] + "_snapfix"
    out.export(os.path.join(outdir, stem + ".stl")); out.export(os.path.join(outdir, stem + ".3mf"))
    # check the files as written (reloaded the way a slicer would merge them)
    for ext in (".stl", ".3mf"):
        r = trimesh.load(os.path.join(outdir, stem + ext), force="mesh")
        ok = ok and bool(r.is_watertight and len(r.split(only_watertight=False)) == 1 and abs(r.volume - B.volume()) < 0.05)
    report.append(dict(file=name, width=round(float(m.extents[0]), 1), removed_mm3=round(A.volume() - B.volume(), 2),
                       added_mm3=round((B - A).volume(), 3), watertight_one_body=ok, foot_before=before, foot_after=after))
json.dump(report, open(os.path.join(outdir, "snapfix_report.json"), "w"), indent=0)
import collections
print("files", len(report), "ok", sum(1 for r in report if r.get('watertight_one_body')), "errors", [r for r in report if 'error' in r][:3])
print("removed per mm width:", collections.Counter(round(r['removed_mm3'] / r['width'], 2) for r in report if 'removed_mm3' in r))
