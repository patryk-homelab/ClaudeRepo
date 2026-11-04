import sys, numpy as np, trimesh, manifold3d as mf
from build123d import import_brep, export_stl, Mesher
brp, stl = sys.argv[1], sys.argv[2]
s = import_brep(brp)
bb = s.bounding_box()
print("BREP solids", len(s.solids()), "volume", round(s.volume, 2), "bbox", [round(v, 3) for v in (bb.size.X, bb.size.Y, bb.size.Z)], "min", [round(v, 3) for v in (bb.min.X, bb.min.Y, bb.min.Z)])
m = trimesh.load(stl, force="mesh")
print("STL volume", round(m.volume, 2), "bbox", m.extents.round(3).tolist(), "min", m.bounds[0].round(3).tolist())
# tessellate BREP finely and compare by boolean symmetric difference (after aligning bbox minima)
tmp = sys.argv[3]
export_stl(s, tmp, tolerance=0.002, angular_tolerance=0.05)
b = trimesh.load(tmp, force="mesh")
b.apply_translation(m.bounds[0] - b.bounds[0])
def man(t): return mf.Manifold(mf.Mesh(vert_properties=np.asarray(t.vertices, np.float32), tri_verts=np.asarray(t.faces, np.uint32)))
A, B = man(b), man(m)
print("aligned by bbox min; BREP-only volume", round((A - B).volume(), 3), "STL-only volume", round((B - A).volume(), 3), "BREP tess vol", round(b.volume, 2))
