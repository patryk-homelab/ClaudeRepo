#!/bin/bash
# usage: project.sh model.stl out.3mf [support] [rot45|rot90] : Bambu Studio 2.8.2 project with X2D 0.4 + 0.20mm Standard + Bambu PETG Basic, Textured PEI
in="$1"; out="$2"; proc=/root/bbs/prof/process_flat.json; [ "$3" = "support" ] && proc=/root/bbs/prof/process_flat_support.json; [ "$3" = "support_bp" ] && proc=/root/bbs/prof/process_flat_support_bp.json
o=$(mktemp -d /root/bbs/out/proj.XXXX)
python3.13 -I -c "
import trimesh, numpy as np
m=trimesh.load('$in', force='mesh')
if '$4'=='rot90': m.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[0,0,1]))
if '$4'=='rot45': m.apply_transform(trimesh.transformations.rotation_matrix(np.pi/4,[0,0,1]))
c=(m.bounds[0]+m.bounds[1])/2; m.apply_translation([128-c[0],128-c[1],-m.bounds[0][2]]); m.export('$o/$(basename "${in%.*}").stl')"
timeout 900 dbus-run-session -- flatpak run --command=bambu-studio com.bambulab.BambuStudio --debug 2 --arrange 0 --orient 0 \
  --load-settings "/root/bbs/prof/machine_flat.json;$proc" --load-filaments "/root/bbs/prof/filament_flat.json" \
  --outputdir $o --export-3mf project.3mf "$o/$(basename "${in%.*}").stl" > $o/log.txt 2>&1
cp $o/project.3mf "$out" && echo "$(basename "$out") $(stat -c %s "$out") bytes" || (echo FAIL; tail -5 $o/log.txt)
