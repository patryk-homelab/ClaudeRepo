"""Fix for Printables 146076 'Hex Bit Holder' by GUZ_prints (CC0), file hex_bit_holder.stl (v1).
Problem (Printables comment 2022-06-03): no screw holes, part twists and bows when screwed through a cell.
Fix: two flat mounting ears on the back (print bed side) at both ends of the tube-tilt direction (= top and bottom
on the wall), each with a d4.5 hole and a 90-degree countersink on the visible side. Ears are cut by the tube
cavities so all 144 tubes stay open to the wall. Mesh-level edit with manifold3d.
usage: fix_146076.py IN.stl OUT_PREFIX"""
import sys, math, numpy as np, trimesh, manifold3d as mf
from shapely.geometry import Polygon
from shapely.geometry.polygon import orient
src, outp = sys.argv[1], sys.argv[2]
EAR_T = 5.0        # ear thickness on the bed
EAR_W = 26.0       # ear width (across the part)
EAR_OUT = 22.0     # how far the ear sticks out past the part (hole centre = EAR_OUT - EAR_W/2 beyond the part)
EAR_IN = 14.0      # how far the ear reaches under the honeycomb (merges with the cell walls)
HOLE_D = 4.5       # clearance for a 4 mm wood screw
CSK_D = 9.5        # countersink diameter at the top face (90 degrees); heads of 4 mm wood screws are 7.0-8.9 mm (DIN 7997, SPAX, Wurth ASSY)
AXIS = np.array([0.6428, 0.0, 0.766]); AXIS /= np.linalg.norm(AXIS)
m = trimesh.load(src, force="mesh")
m.apply_translation([0, 0, -m.bounds[0][2]])          # put the back face on z = 0
part = mf.Manifold(mf.Mesh(vert_properties=np.asarray(m.vertices, np.float32), tri_verts=np.asarray(m.faces, np.uint32)))
assert part.status() == mf.Error.NoError
(x0, y0, _), (x1, y1, _) = m.bounds
yc = (y0 + y1) / 2
def ccw(pts): return [list(orient(Polygon(pts), 1.0).exterior.coords)[:-1]]
# tube cavities: closed hole loops from sections at several heights (outermost tubes are trimmed at the back and only
# close higher up), deduplicated by their position projected along the tube axis, each swept along the axis (shear in x)
a = AXIS[0] / AXIS[2]
cav = None; seen = {}
for z_ref in (0.5, 2.0, 4.0, 7.0, 10.0, 13.0):
    sec = m.section(plane_origin=[0, 0, z_ref], plane_normal=[0, 0, 1])
    for loop in sec.discrete:
        p = np.asarray(loop)[:-1, :2]
        if np.ptp(p[:, 0]) > 12 or np.ptp(p[:, 1]) > 12: continue      # outer outline, not a tube
        cs = mf.CrossSection(ccw([tuple(q) for q in p]))
        if cs.area() < 20: continue
        c = p.mean(0); key = (round(c[0] - a * z_ref), round(c[1]))
        if any(abs(key[0] - k[0]) <= 1 and abs(key[1] - k[1]) <= 1 for k in seen): continue
        seen[key] = z_ref
        pr = mf.Manifold.extrude(cs, EAR_T + 4.0 + 20).translate([0, 0, -2.0 - 10])
        pr = pr.transform([[1, 0, a, -a * z_ref], [0, 1, 0, 0], [0, 0, 1, 0]])
        cav = pr if cav is None else cav + pr
nholes = len(seen)
ears = None
for side in (-1, 1):
    xe = x0 - EAR_OUT if side < 0 else x1 + EAR_OUT          # outer end of the ear
    xi = x0 + EAR_IN if side < 0 else x1 - EAR_IN            # inner end (under the honeycomb)
    xh = xe + side * -1 * (EAR_W / 2)                         # hole centre = centre of the rounded end
    lo, hi = min(xi, xh), max(xi, xh)
    box = mf.Manifold.cube([hi - lo, EAR_W, EAR_T]).translate([lo, yc - EAR_W / 2, 0])
    rnd = mf.Manifold.cylinder(EAR_T, EAR_W / 2, EAR_W / 2, 96).translate([xh, yc, 0])
    ear = box + rnd
    hole = mf.Manifold.cylinder(EAR_T + 2, HOLE_D / 2, HOLE_D / 2, 64).translate([xh, yc, -1])
    csk_h = (CSK_D - HOLE_D) / 2
    csk = mf.Manifold.cylinder(csk_h + 0.01, HOLE_D / 2, CSK_D / 2 + 0.01, 64).translate([xh, yc, EAR_T - csk_h])
    ear = ear - hole - csk
    ears = ear if ears is None else ears + ear
ears = ears - cav
fixed = part + ears
print('CHECK inside tubes after union (mm3):', round(((fixed - part) ^ cav).volume(), 4), ' ears alone:', round(ears.volume(), 1), ' ears outside part:', round((ears - part).volume(), 1))
fixed_raw = fixed
assert fixed.status() == mf.Error.NoError, fixed.status()
_mm = fixed.to_mesh()          # round-trip through float32 (as in the STL) so that near-collinear slivers become exactly degenerate
fixed = mf.Manifold(mf.Mesh(vert_properties=np.asarray(_mm.vert_properties, np.float32)[:, :3].copy(), tri_verts=np.asarray(_mm.tri_verts, np.uint32)))
fixed = fixed.simplify(1e-4)   # collapse sliver triangles (with 1e-5, 2 zero-area triangles stayed on the back face and
                               # Bambu Studio dropped them on import, leaving the mesh open); changes the shape by < 0.01 mm3
print('CHECK simplify changed (mm3): +', round((fixed - fixed_raw).volume(), 4), ' -', round((fixed_raw - fixed).volume(), 4))
assert fixed.status() == mf.Error.NoError
mm = fixed.to_mesh()
out = trimesh.Trimesh(vertices=np.asarray(mm.vert_properties)[:, :3], faces=np.asarray(mm.tri_verts), process=False)
from trimesh.grouping import group_rows
print("DIAG raw: wt", out.is_watertight, "open", len(group_rows(out.edges_sorted, require_count=1)), "deg", int((out.area_faces < 1e-12).sum()))
out = trimesh.Trimesh(vertices=np.asarray(mm.vert_properties)[:, :3], faces=np.asarray(mm.tri_verts), process=True)
print("DIAG processed: wt", out.is_watertight, "open", len(group_rows(out.edges_sorted, require_count=1)))
print('DIAG after simplify: degenerate faces', int((out.area_faces < 1e-12).sum()))
bb = out.split(only_watertight=False)
if not (out.is_watertight and len(bb) == 1):
    print("DIAG wt", out.is_watertight, "bodies", [(len(b.faces), round(float(b.area), 4), b.bounds.round(2).tolist()) for b in bb][:8]); sys.exit(1)
assert abs(out.volume - fixed.volume()) < 0.01
assert int((out.area_faces < 1e-9).sum()) == 0, 'zero-area triangles left'
out.export(outp + ".stl"); out.export(outp + ".3mf")
print(dict(tube_cavities_cut=nholes, vol_orig=round(part.volume(), 1), vol_fixed=round(fixed.volume(), 1), added=round((fixed - part).volume(), 1),
           removed=round((part - fixed).volume(), 4), bbox=[round(v, 2) for v in out.extents], hole_x=[round(x0 - EAR_OUT + EAR_W / 2, 2), round(x1 + EAR_OUT - EAR_W / 2, 2)]))
