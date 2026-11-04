import json, os, sys, glob
base = "/root/bbs/BBL"
idx = {}
for kind in ("machine", "process", "filament"):
    for f in glob.glob(f"{base}/{kind}/**/*.json", recursive=True):
        try: d = json.load(open(f))
        except Exception: continue
        if "name" in d: idx[(kind, d["name"])] = d
def flat(kind, name):
    d = idx[(kind, name)]; chain = [d]
    while d.get("inherits"):
        d = idx[(kind, d["inherits"])]; chain.append(d)
    out = {}
    for d in reversed(chain): out.update(d)
    out.pop("inherits", None); out["from"] = "system"; out["name"] = name; out["instantiation"] = "true"
    return out, [c["name"] for c in chain]
for kind, name, fn, extra in [("machine", "Bambu Lab X2D 0.4 nozzle", "machine_flat.json", {}),
                              ("process", "0.20mm Standard @BBL X2D", "process_flat.json", {}),
                              ("process", "0.20mm Standard @BBL X2D", "process_flat_support.json", {"enable_support": "1"}),
                              ("filament", "Bambu PETG Basic @BBL X2D 0.4 nozzle", "filament_flat.json", {})]:
    o, ch = flat(kind, name); o.update(extra)
    json.dump(o, open(f"/root/bbs/prof/{fn}", "w"), indent=1)
    print(fn, "chain:", ch, {k: o.get(k) for k in ("enable_support", "support_type", "support_threshold_angle", "wall_loops", "sparse_infill_density", "filament_type", "filament_density", "compatible_printers", "nozzle_temperature") if k in o})
