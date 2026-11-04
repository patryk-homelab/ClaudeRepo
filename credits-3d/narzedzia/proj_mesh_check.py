"""Load the mesh(es) stored in a Bambu project 3MF and report faces, watertightness, bodies, volume vs source mesh.
usage: proj_mesh_check.py PROJECT.3mf SOURCE_MESH"""
import sys, zipfile, re, numpy as np, trimesh
z = zipfile.ZipFile(sys.argv[1]); src = trimesh.load(sys.argv[2], force='mesh')
tot_f = 0; parts = []
for n in z.namelist():
    if not n.endswith('.model'): continue
    x = z.read(n).decode()
    for obj in re.findall(r'<mesh>(.*?)</mesh>', x, re.S):
        v = re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', obj); t = re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', obj)
        m = trimesh.Trimesh(np.array(v, float), np.array(t, int), process=True); parts.append(m); tot_f += len(t)
m = trimesh.util.concatenate(parts) if len(parts) > 1 else parts[0]
print(sys.argv[1].split('/')[-1], 'faces', tot_f, '(source', len(src.faces), ', degenerate in source', int((src.area_faces < 1e-12).sum()), ') watertight', m.is_watertight, 'bodies', m.body_count,
      'vol', round(m.volume, 2), 'source vol', round(src.volume, 2))
