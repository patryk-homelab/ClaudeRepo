"""Hex-bit pocket fit check on an STL (projekt-3d-druk section 4 a/b).
Bit: ISO 1173 hex 6.3, cross-section = hexagon (flats s) intersected with circle (diameter e).
a) radial sweep + min gap: 2D, bit centred in every pocket section along the prismatic zone.
b) insertion: 3D (manifold3d), worst-case bit moved along the pocket axis from 40 mm outside in 0.25 mm steps;
   first contact = seat; seat must be within 4.5 mm of the floor/stop measured at the pocket centre.
usage: sweep2.py STL '[ax,ay,az]' '[section depths from global top]' OUT.json [wall=0|1] [gap=0.10]"""
import sys, json, math, trimesh, numpy as np, manifold3d as mf
from shapely.geometry import Polygon
path, axis, depths, out = sys.argv[1], np.array(json.loads(sys.argv[2]), float), json.loads(sys.argv[3]), sys.argv[4]
wall = len(sys.argv) > 5 and sys.argv[5] == "1"
GAP = float(sys.argv[6]) if len(sys.argv) > 6 else 0.10
axis /= np.linalg.norm(axis)
m = trimesh.load(path, force="mesh")
part = mf.Manifold(mf.Mesh(vert_properties=np.asarray(m.vertices, np.float32), tri_verts=np.asarray(m.faces, np.uint32)))
assert part.status() == mf.Error.NoError
zmin = m.bounds[0][2]
if wall:  # the wall the part is screwed to (part's z=min face) acts as the stop for through tubes
    lo, hi = m.bounds
    part = part + mf.Manifold.cube([hi[0] - lo[0] + 200, hi[1] - lo[1] + 200, 20]).translate([lo[0] - 100, lo[1] - 100, zmin - 20])
top = (m.vertices @ axis).max()
tmp = np.array([1.0, 0, 0]) if abs(axis[0]) < 0.9 else np.array([0, 1.0, 0])
u = np.cross(axis, tmp); u /= np.linalg.norm(u); v = np.cross(axis, u)
S_ = [6.292, 6.311, 6.330, 6.350]; E_ = [7.11, 7.145, 7.18]
def bitpoly(s, e, th, c=(0, 0)):
    a = np.radians(th + np.arange(6) * 60); R = s / math.sqrt(3)
    hx = Polygon(np.c_[R * np.cos(a) + c[0], R * np.sin(a) + c[1]])
    return hx.intersection(Polygon([(c[0] + e / 2 * math.cos(t), c[1] + e / 2 * math.sin(t)) for t in np.linspace(0, 2 * math.pi, 192, endpoint=False)]))
pockets = {}
for d in depths:
    sec = m.section(plane_origin=axis * (top - d), plane_normal=axis)
    if sec is None: continue
    for loop in sec.discrete:
        p3 = np.asarray(loop)
        if np.allclose(p3[0], p3[-1]): p3 = p3[:-1]
        p2 = np.c_[p3 @ u, p3 @ v]
        ws = [np.ptp(p2 @ [math.cos(a), math.sin(a)]) for a in np.radians(np.arange(0, 180, 0.25))]
        fl, co = min(ws), max(ws)
        if not (6.2 < fl < 7.6 and co < 9.0): continue
        poly = Polygon(p2)
        if not poly.is_valid or poly.area < 25: continue
        c2 = np.array(poly.centroid.coords[0])
        r = np.linalg.norm(p2 - c2, axis=1); th = math.degrees(math.atan2(*(p2[r.argmax()] - c2)[::-1])) % 60
        # same pocket = centre within 1.5 mm in the plane perpendicular to the axis (pockets are >= 7.5 mm apart)
        key = next((k for k in pockets if math.hypot(k[0] - c2[0], k[1] - c2[1]) < 1.5), (float(c2[0]), float(c2[1])))
        pk = pockets.setdefault(key, dict(c2=c2.tolist(), th=th, secs=[], d0=d))
        pk["secs"].append(dict(d=d, flats=round(fl, 3), corners=round(co, 3), area=poly.area, poly=poly))
P = list(pockets.values())
print("pockets", len(P))
# a) radial sweep + min gap per pocket (only sections whose area is within 2% of the pocket's median: prismatic zone)
rad = []
for p in P:
    # prismatic zone only: sections equal to the pocket's modal section (area within 0.1 %, flats and corners within
    # 0.01 mm); sections that clip the entry chamfer or an inclined floor are excluded
    med = np.median([s["area"] for s in p["secs"]])
    fm = np.median([s["flats"] for s in p["secs"]]); cm = np.median([s["corners"] for s in p["secs"]])
    secs = [s for s in p["secs"] if abs(s["area"] - med) / med < 0.001 and abs(s["flats"] - fm) < 0.01 and abs(s["corners"] - cm) < 0.01]
    p["n_secs_used"] = len(secs)
    p["flats"] = min(s["flats"] for s in secs); p["corners"] = min(s["corners"] for s in secs)
    # bit self-aligns: pick the rotation (0.5 deg grid over 60 deg) that maximises the worst-case gap
    sc_ref = secs[len(secs) // 2]; cref = sc_ref["poly"].centroid.coords[0]; best_th = None
    for th in np.arange(0, 60, 0.5):
        b = bitpoly(6.35, 7.18, th, cref)
        g = sc_ref["poly"].exterior.distance(b) if sc_ref["poly"].contains(b) else -b.difference(sc_ref["poly"]).area
        if best_th is None or g > best_th[0]: best_th = (g, th)
    p["th"] = float(best_th[1])
    worst = None
    for s in S_:
        for e in E_:
            for sc in secs:
                b = bitpoly(s, e, p["th"], sc["poly"].centroid.coords[0])
                g = sc["poly"].exterior.distance(b) if sc["poly"].contains(b) else -b.difference(sc["poly"]).area
                if worst is None or g < worst[0]: worst = (g, s, e, sc["d"])
    p["min_gap_worst"] = round(worst[0], 3); rad.append(worst)
fails_interf = [p for p in P if p["min_gap_worst"] < 0]
fails_gap = [p for p in P if p["min_gap_worst"] < GAP]
# b) insertion + seat (3D), worst-case bit 6.35 / 7.18, L = 25
def bit3d(p, s, e, L, t):
    a = np.radians(p["th"] + np.arange(6) * 60); R = s / math.sqrt(3)
    cs = mf.CrossSection([np.c_[R * np.cos(a), R * np.sin(a)].tolist()]) ^ mf.CrossSection.circle(e / 2, 96)
    c = p["c2"][0] * u + p["c2"][1] * v + axis * t
    return mf.Manifold.extrude(cs, L).transform(np.c_[u, v, axis, c].tolist())
ins = []
for p in P:
    c3 = p["c2"][0] * u + p["c2"][1] * v
    # stop under the pocket centre (ray along -axis from inside the pocket)
    o = c3 + axis * (top - p["d0"])
    hit, _, _ = m.ray.intersects_location([o], [-axis], multiple_hits=False)
    t_floor = float(hit[0] @ axis) if len(hit) else (zmin - o[2]) / axis[2] * 1.0 + float(o @ axis) if wall else None
    # rim: rays at radius e/2+0.8 around the pocket from 60 mm outside
    rim = []
    for k in range(12):
        ang = math.radians(p["th"] + 15 + 30 * k); q = c3 + (4.4) * (math.cos(ang) * u + math.sin(ang) * v) + axis * (top + 60)
        h, _, _ = m.ray.intersects_location([q], [-axis], multiple_hits=False)
        if len(h): rim.append(float(h[0] @ axis))
    t = top + 40.0; contact = None
    t_end = (t_floor if t_floor is not None else top - 80) - 6
    # local copy of the part around the whole insertion path (bit swept from t_end to top+40+90) for speed
    sweep_vol = mf.Manifold.hull(bit3d(p, 8.5, 8.5, 1.0, t_end) + bit3d(p, 8.5, 8.5, 1.0, top + 40.0 + 90.0))
    lp = part ^ sweep_vol
    while t > t_end:
        if (lp ^ bit3d(p, 6.35, 7.18, 25.0, t)).volume() > 1e-3:
            contact = t; break
        t -= 0.25
    seat = None if contact is None else contact + 0.25
    rec = dict(pocket=p["c2"], t_floor=t_floor, rim_low=min(rim) if rim else None, rim_high=max(rim) if rim else None, seat=seat)
    rec["seat_above_floor"] = None if (seat is None or t_floor is None) else round(seat - t_floor, 2)
    rec["blocked"] = seat is None or t_floor is None or (seat - t_floor) > 4.5
    if seat is not None and rim:
        rec["protrusion_25"] = round(seat + 25 - max(rim), 2)
        rec["depth_in_pocket"] = round(min(rim) - seat, 2)
        long = {}
        for L in (50.0, 70.0, 90.0):
            long[L] = round((lp ^ bit3d(p, 6.35, 7.18, L, seat)).volume(), 3)
        rec["long_bit_interference_mm3"] = long
    ins.append(rec)
res = dict(file=path, axis=axis.round(4).tolist(), tilt_deg=round(math.degrees(math.acos(min(1, axis[2]))), 2), wall_stop=wall, pockets=len(P),
           grid=dict(s=S_, e=E_, note="s grid 0.019 mm incl. both ISO 1173 limits; e grid 0.035 mm incl. both limits"),
           pocket_flats=sorted({p["flats"] for p in P}), pocket_corners=sorted({p["corners"] for p in P}),
           radial_interference_pockets=len(fails_interf), min_gap_required=GAP, below_min_gap_pockets=len(fails_gap),
           min_gap_per_side_range=[min(p["min_gap_worst"] for p in P), max(p["min_gap_worst"] for p in P)],
           sections_per_pocket=[min(p["n_secs_used"] for p in P), max(p["n_secs_used"] for p in P)],
           below_min_gap_detail=[(round(p["c2"][0], 1), round(p["c2"][1], 1), p["flats"], p["min_gap_worst"]) for p in fails_gap][:40],
           insertion_blocked=sum(r["blocked"] for r in ins),
           seat_above_floor_range=[min(r["seat_above_floor"] for r in ins if r["seat_above_floor"] is not None), max(r["seat_above_floor"] for r in ins if r["seat_above_floor"] is not None)] if ins else None,
           depth_in_pocket_range=[min(r.get("depth_in_pocket", 99) for r in ins), max(r.get("depth_in_pocket", -99) for r in ins)],
           protrusion_25mm_range=[min(r.get("protrusion_25", 99) for r in ins), max(r.get("protrusion_25", -99) for r in ins)],
           long_bits_colliding={L: sum(1 for r in ins if r.get("long_bit_interference_mm3", {}).get(L, 0) > 1e-3) for L in (50.0, 70.0, 90.0)})
# control: the 2D check must flag a bit 0.2 mm bigger than the largest pocket, the 3D check must flag a bit pushed 1 mm past its seat
fm = max(p["flats"] for p in P); p0 = P[0]; sc0 = p0["secs"][0]
b = bitpoly(fm + 0.2, (fm + 0.2) * 1.1547, p0["th"], sc0["poly"].centroid.coords[0])
res["control_2d_oversize_flagged"] = not sc0["poly"].contains(b)
r0 = ins[0]
res["control_3d_past_seat_flagged"] = r0["seat"] is not None and (part ^ bit3d(p0, 6.35, 7.18, 25.0, r0["seat"] - 1.0)).volume() > 1e-3
res["per_pocket"] = ins
json.dump(res, open(out, "w"), indent=1, default=float)
print(json.dumps({k: v for k, v in res.items() if k != "per_pocket"}, default=float))
