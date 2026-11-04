"""Fix for Printables 1825701 'Large bit holder (wall mounted)' by Jirka (CC0).
Mesh-level edit of the original STL with manifold3d (no STEP published; see report for why not a full rebuild).
1) Front row: 16 pockets are clipped by the pattern boundary at y=82.0 (6.439 mm instead of 6.65 mm across flats).
   Cut the full standard pocket (template copied from the other 304 pockets) at the grid position y = row1 - pitch.
2) Screw holes (3x, d 4.2 mm along Y, z = 32): add a 45-degree teardrop roof so the slicer needs no support.
usage: fix_1825701.py IN.stl OUT_PREFIX"""
import sys, math, numpy as np, trimesh, manifold3d as mf
from shapely.geometry import Polygon
from shapely.geometry.polygon import orient
def ccw(pts):
    return [list(orient(Polygon(pts), 1.0).exterior.coords)[:-1]]
src, outp = sys.argv[1], sys.argv[2]
m = trimesh.load(src, force="mesh")
part = mf.Manifold(mf.Mesh(vert_properties=np.asarray(m.vertices, np.float32), tri_verts=np.asarray(m.faces, np.uint32)))
assert part.status() == mf.Error.NoError
# --- parameters measured from the original mesh (section z=6 / y=171, see report) ---
FLOOR_Z, TOP_Z = 2.0, 12.0
ROW1_Y, ROW_PITCH = 88.96, 3.85           # first full row centre, staggered row pitch
FRONT_Y = ROW1_Y - ROW_PITCH               # 85.11, grid position of the clipped row
TEMPLATE = [(-1.9197, -3.325), (-3.0715, -1.33), (-3.8394, 0.0), (-2.6876, 1.995), (-1.9197, 3.325), (0.3839, 3.325),
            (1.9197, 3.325), (3.0715, 1.33), (3.8394, 0.0), (2.6876, -1.995), (1.9197, -3.325), (-0.3839, -3.325)]
HOLE_R, HOLE_Z, HOLE_X = 2.1, 32.0, (24.982, 127.982, 230.982)
HOLE_Y0, HOLE_Y1 = 160.0, 182.0            # beyond both faces of the back wall (y 165..177)
# 90-degree countersink on the front face: d 7.59 at y 165.5, d 5.59 at y 166.5 -> apex (r = 0) at y 169.295
CS_APEX_Y, CS_FACE_Y = 169.295, 164.5
# front-row x positions: the 16 clipped pockets found in the section at z = 6
sec = m.section(plane_origin=[0, 0, 6], plane_normal=[0, 0, 1])
xs = []
for loop in sec.discrete:
    p = np.asarray(loop)[:-1, :2]
    if np.ptp(p[:, 0]) < 9 and np.ptp(p[:, 1]) < 6.5:
        xs.append(float((p[:, 0].min() + p[:, 0].max()) / 2))
xs = sorted(xs); assert len(xs) == 16, xs
cut = None
for x in xs:
    cs = mf.CrossSection(ccw([(x + a, FRONT_Y + b) for a, b in TEMPLATE]))
    assert cs.area() > 30, cs.area()
    pr = mf.Manifold.extrude(cs, TOP_Z + 1.0 - FLOOR_Z).translate([0, 0, FLOOR_Z])
    cut = pr if cut is None else cut + pr
# teardrop roof: triangle from the 45-degree tangent points to the apex at r*sqrt(2); polygon in XZ, extruded along Y
c45 = HOLE_R * math.cos(math.radians(45))
for x in HOLE_X:
    tri = [(x - c45, HOLE_Z + c45 - 0.4), (x + c45, HOLE_Z + c45 - 0.4), (x + c45, HOLE_Z + c45), (x, HOLE_Z + HOLE_R * math.sqrt(2)), (x - c45, HOLE_Z + c45)]
    cs = mf.CrossSection(ccw(tri))
    assert cs.area() > 1, cs.area()
    pr = mf.Manifold.extrude(cs, HOLE_Y1 - HOLE_Y0)          # along local Z
    # rotation about X by +90 deg (det +1): local y -> world z, local z (extrusion) -> world -y, then shift to HOLE_Y1
    M = [[1, 0, 0, 0], [0, 0, -1, HOLE_Y1], [0, 1, 0, 0]]
    pr = pr.transform(M)
    cut = cut + pr
# countersink: cone with a teardrop base = hull(apex point, teardrop outline just outside the front face)
for x in HOLE_X:
    r = CS_APEX_Y - CS_FACE_Y
    pts = [(x, CS_APEX_Y, HOLE_Z)]
    for t in np.linspace(0, 2 * math.pi, 96, endpoint=False):
        pts.append((x + r * math.cos(t), CS_FACE_Y, HOLE_Z + r * math.sin(t)))
    pts.append((x, CS_FACE_Y, HOLE_Z + r * math.sqrt(2)))
    cut = cut + mf.Manifold.hull_points(pts)
fixed = part - cut
assert fixed.status() == mf.Error.NoError, fixed.status()
mm = fixed.to_mesh()
out = trimesh.Trimesh(vertices=np.asarray(mm.vert_properties)[:, :3], faces=np.asarray(mm.tri_verts), process=True)
# drop zero-area sliver triangles (collinear edges left by the boolean), then require a closed single body
out.update_faces(out.nondegenerate_faces(height=1e-7)); out.remove_unreferenced_vertices()
assert out.is_watertight and len(out.split(only_watertight=False)) == 1, (out.is_watertight, len(out.split(only_watertight=False)))
assert abs(out.volume - fixed.volume()) < 0.01, (out.volume, fixed.volume())
out.export(outp + ".stl"); out.export(outp + ".3mf")
removed = part.volume() - fixed.volume(); added = (fixed - part).volume()
print(dict(front_row_x=[round(x, 2) for x in xs], front_y=FRONT_Y, vol_orig=round(part.volume(), 2), vol_fixed=round(fixed.volume(), 2),
           removed_mm3=round(removed, 3), added_mm3=round(added, 4), removed_by_pockets=round((part ^ (cut)).volume(), 3)))
