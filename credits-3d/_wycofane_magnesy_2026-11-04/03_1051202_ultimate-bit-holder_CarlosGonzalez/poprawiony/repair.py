"""Mesh repair for Printables 1051202 parts: keep closed bodies with real volume, drop zero-volume junk and
internal zero-thickness sheets, boolean-union the rest into one solid (manifold3d), export STL + 3MF.
usage: repair.py IN OUT_PREFIX"""
import sys, numpy as np, trimesh, manifold3d as mf
src, outp = sys.argv[1], sys.argv[2]
m = trimesh.load(src, force="mesh")
bodies = m.split(only_watertight=False)
keep, drop = [], []
for b in bodies:
    (keep if (b.is_watertight and abs(b.volume) > 1.0) else drop).append(b)
acc = None
for b in keep:
    if b.volume < 0: b.invert()
    mb = mf.Manifold(mf.Mesh(vert_properties=np.asarray(b.vertices, np.float32), tri_verts=np.asarray(b.faces, np.uint32)))
    assert mb.status() == mf.Error.NoError, mb.status()
    acc = mb if acc is None else acc + mb
mm = acc.to_mesh()
out = trimesh.Trimesh(vertices=np.asarray(mm.vert_properties)[:, :3], faces=np.asarray(mm.tri_verts), process=True)
out.update_faces(out.nondegenerate_faces(height=1e-7)); out.remove_unreferenced_vertices()
assert out.is_watertight and len(out.split(only_watertight=False)) == 1
out.export(outp + ".stl"); out.export(outp + ".3mf")
print(dict(src=src, bodies_in=len(bodies), kept=len(keep), dropped=[(len(d.faces), round(float(d.area), 4)) for d in drop],
           sum_kept_volume=round(sum(b.volume for b in keep), 2), union_volume=round(acc.volume(), 2), out_faces=len(out.faces)))
