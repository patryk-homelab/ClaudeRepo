import sys, re, json, collections, numpy as np
o = sys.argv[1]
res = json.load(open(o + '/result.json'))
try: ob = res['sliced_plates'][0]['objects'][0]['bbox']
except Exception:
    import trimesh; mm = trimesh.load(o + '/model.stl'); ob = {'x': float(mm.bounds[0][0]), 'y': float(mm.bounds[0][1]), 'note': 'model.stl placed bounds'}
z = 0; feat = None; P = []
for line in open(o + '/plate_1.gcode'):
    if line.startswith('; Z_HEIGHT:'): z = float(line.split(':')[1])
    elif line.startswith('; FEATURE:'): feat = line.split(':', 1)[1].strip()
    elif feat and feat.startswith('Support') and line.startswith('G1') and ' E' in line:
        mx = re.search(r'X([-\d.]+)', line); my = re.search(r'Y([-\d.]+)', line)
        if mx and my: P.append((float(mx.group(1)), float(my.group(1)), z, feat))
print('object bbox on plate', ob)
if not P: print('no support extrusion'); sys.exit()
A = np.array([p[:3] for p in P]); A[:, 0] -= ob['x']; A[:, 1] -= ob['y']
print('support moves', len(A), collections.Counter(p[3] for p in P))
print('model-relative x %.1f..%.1f y %.1f..%.1f z %.2f..%.2f' % (A[:,0].min(), A[:,0].max(), A[:,1].min(), A[:,1].max(), A[:,2].min(), A[:,2].max()))
c = collections.Counter((round(a[0] / 10) * 10, round(a[1] / 10) * 10, round(a[2] / 5) * 5) for a in A)
for k, v in sorted(c.items(), key=lambda x: -x[1])[:15]: print('  cell x,y,z', k, v)
