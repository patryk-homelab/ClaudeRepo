import sys, math, json, trimesh, numpy as np
BED = (256, 256, 260)
res = []
for path in sys.argv[1:]:
    try:
        m = trimesh.load(path, force="mesh")
    except Exception as e:
        res.append({"file": path, "error": repr(e)}); continue
    ext = m.extents
    bodies = m.split(only_watertight=False)
    o, n = m.triangles_center, m.face_normals
    sampled = 0
    try:
        walls = []
        idx = np.arange(len(o)) if len(o) <= 12000 else np.random.default_rng(0).choice(len(o), 12000, replace=False)
        sampled = len(idx)
        for a in range(0, len(idx), 2000):
            oo, nn = o[idx[a:a+2000]], n[idx[a:a+2000]]
            loc, ri, _ = m.ray.intersects_location(oo - nn * 0.01, -nn, multiple_hits=False)
            walls.append(np.linalg.norm(loc - (oo[ri] - nn[ri] * 0.01), axis=1))
        wall = np.concatenate(walls)
        wmin = float(wall.min()); w01 = float(np.percentile(wall, 1))
    except Exception as e:
        wmin = w01 = None
    # overhang relative to min z (as-oriented in file)
    down = (n[:, 2] < -math.cos(math.radians(45))) & (o[:, 2] > m.bounds[0][2] + 0.2)
    fits = sorted(ext[:2]) <= sorted(BED[:2]) and ext[2] <= BED[2]
    res.append({"file": path.split("/dl/")[-1], "faces": len(m.faces), "watertight": bool(m.is_watertight),
        "bodies": len(bodies), "volume_cm3": round(float(m.volume)/1000, 2) if m.is_watertight else None,
        "bbox_mm": [round(float(x), 2) for x in ext], "min_z": round(float(m.bounds[0][2]), 3),
        "min_wall": None if wmin is None else round(wmin, 3), "wall_p1": None if w01 is None else round(w01, 3), "wall_faces_sampled": f"{sampled}/{len(o)}",
        "overhang45_mm2": round(float(m.area_faces[down].sum()), 1), "fits_X2D": bool(fits)})
for r in res: print(json.dumps(r, ensure_ascii=False))
