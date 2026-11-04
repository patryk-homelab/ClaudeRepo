import sys, numpy as np, trimesh, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
mode, a, b, out = sys.argv[1:5]
A = trimesh.load(a, force='mesh'); B = trimesh.load(b, force='mesh')
if mode == 'holes':   # z-section hole map
    z = float(sys.argv[5]); xl = [float(v) for v in sys.argv[6].split(',')]
    fig, axs = plt.subplots(1, 2, figsize=(16, 7))
    for ax, m, t in zip(axs, [A, B], ['oryginał', 'poprawiony']):
        s = m.section(plane_origin=[0, 0, z], plane_normal=[0, 0, 1])
        for l in s.discrete: l = np.asarray(l); ax.plot(l[:, 0], l[:, 1], 'k-', lw=0.6)
        ax.set_xlim(xl[0], xl[1]); ax.set_ylim(xl[2], xl[3]); ax.set_aspect('equal'); ax.set_title(f'{t}: przekrój z = {z} mm'); ax.grid(True, alpha=0.3)
elif mode == 'xz':    # vertical section at y
    y = float(sys.argv[5]); xl = [float(v) for v in sys.argv[6].split(',')]
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    for ax, m, t in zip(axs, [A, B], ['oryginał', 'poprawiony']):
        s = m.section(plane_origin=[0, y, 0], plane_normal=[0, 1, 0])
        for l in s.discrete: l = np.asarray(l); ax.plot(l[:, 0], l[:, 2], 'k-', lw=0.8)
        ax.set_xlim(xl[0], xl[1]); ax.set_ylim(xl[2], xl[3]); ax.set_aspect('equal'); ax.set_title(f'{t}: przekrój pionowy y = {y} mm'); ax.grid(True, alpha=0.3)
elif mode == 'wera':  # snap profile at x=0, STL orientation -> native
    fig, ax = plt.subplots(figsize=(7, 8))
    for m, c, t in [(A, '0.55', 'oryginał'), (B, 'r', 'z poprawką')]:
        s = m.section(plane_origin=[0, 0, 0], plane_normal=[1, 0, 0])
        for i, l in enumerate(s.discrete):
            l = np.asarray(l); ax.plot(l[:, 2], -l[:, 1], color=c, lw=1.4 if c == 'r' else 2.5, label=t if i == 0 else None)
    ax.set_xlim(-1, 16); ax.set_ylim(-16.5, 11); ax.set_aspect('equal'); ax.grid(True, alpha=0.3); ax.legend()
    ax.set_xlabel('głębokość od ściany [mm]'); ax.set_ylabel('wysokość [mm]'); ax.set_title('Zatrzask uchwytu na szynie (przekrój x = 0)')
plt.tight_layout(); plt.savefig(out, dpi=70)
