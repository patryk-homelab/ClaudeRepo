import sys, glob, trimesh, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
files = sys.argv[2:]; out = sys.argv[1]
cols = 5; rows = (len(files) + cols - 1) // cols
fig = plt.figure(figsize=(4 * cols, 4 * rows))
light = np.array([0.3, -0.5, 0.8]); light /= np.linalg.norm(light)
for i, f in enumerate(files):
    m = trimesh.load(f, force="mesh"); m.apply_translation(-m.bounds[0])
    ax = fig.add_subplot(rows, cols, i + 1, projection="3d")
    sh = 0.35 + 0.65 * np.clip(m.face_normals @ light, 0, 1)
    ax.add_collection3d(Poly3DCollection(m.triangles, facecolors=np.c_[np.outer(sh, [0.3, 0.55, 0.85]), np.ones(len(sh))], edgecolor="none"))
    e = m.extents; c = e / 2; r = e.max() / 2
    ax.set_xlim(c[0]-r, c[0]+r); ax.set_ylim(c[1]-r, c[1]+r); ax.set_zlim(c[2]-r, c[2]+r); ax.set_box_aspect((1, 1, 1)); ax.view_init(45, -60)
    ax.set_title(f.split("/")[-1][:38] + f"\n{e.round(0)}", fontsize=8); ax.set_axis_off()
plt.tight_layout(); plt.savefig(out, dpi=55)
