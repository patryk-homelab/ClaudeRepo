import sys, trimesh, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
path, out = sys.argv[1], sys.argv[2]
title = sys.argv[3] if len(sys.argv) > 3 else path.split("/")[-1]
m = trimesh.load(path, force="mesh")
m.apply_translation(-m.bounds[0])
if len(m.faces) > 60000:
    m = m.simplify_quadric_decimation(face_count=60000) if hasattr(m, "simplify_quadric_decimation") else m
views = [("iso", 30, -60), ("raised", 60, -60), ("top", 90, -90), ("front", 0, -90), ("side", 0, 0), ("below", -45, -60)]
fig = plt.figure(figsize=(18, 11))
light = np.array([0.3, -0.5, 0.8]); light /= np.linalg.norm(light)
shade = 0.35 + 0.65 * np.clip(m.face_normals @ light, 0, 1)
cols = np.c_[np.outer(shade, [0.30, 0.55, 0.85]), np.ones(len(shade))]
for i, (name, el, az) in enumerate(views):
    ax = fig.add_subplot(2, 3, i + 1, projection="3d")
    pc = Poly3DCollection(m.triangles, facecolors=cols, edgecolor="none")
    ax.add_collection3d(pc)
    e = m.extents; c = e / 2; r = e.max() / 2
    ax.set_xlim(c[0]-r, c[0]+r); ax.set_ylim(c[1]-r, c[1]+r); ax.set_zlim(c[2]-r, c[2]+r)
    ax.set_box_aspect((1, 1, 1)); ax.view_init(el, az); ax.set_title(f"{name} (el {el}, az {az})")
    ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
fig.suptitle(f"{title}  bbox {m.extents.round(1)} mm", fontsize=13)
plt.tight_layout(); plt.savefig(out, dpi=70)
