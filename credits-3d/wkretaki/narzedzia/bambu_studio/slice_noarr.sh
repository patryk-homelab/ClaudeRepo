#!/bin/bash
# usage: slice_noarr.sh model.stl tag [support] [rot90] : centre the model on the 256x256 plate, no auto-arrange
in="$1"; tag="$2"; proc=/root/bbs/prof/process_flat.json; [ "$3" = "support" ] && proc=/root/bbs/prof/process_flat_support.json
o=/root/bbs/out/$tag; mkdir -p $o
python3.13 -I -c "
import trimesh, numpy as np, sys
m=trimesh.load('$in', force='mesh')
if '$4'=='rot90': m.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[0,0,1]))
if '$4'=='rot45': m.apply_transform(trimesh.transformations.rotation_matrix(np.pi/4,[0,0,1]))
c=(m.bounds[0]+m.bounds[1])/2; m.apply_translation([128-c[0],128-c[1],-m.bounds[0][2]]); m.export('$o/model.stl'); print('placed', m.bounds.round(2).tolist())"
timeout 900 dbus-run-session -- flatpak run --command=bambu-studio com.bambulab.BambuStudio --debug 2 --arrange 0 --orient 0 --slice 0 \
  --load-settings "/root/bbs/prof/machine_flat.json;$proc" --load-filaments "/root/bbs/prof/filament_flat.json" \
  --outputdir $o --export-3mf sliced.3mf $o/model.stl > $o/log.txt 2>&1
rc=$?; g=$o/plate_1.gcode
sup=$(grep -c -E "^; FEATURE: Support" $g 2>/dev/null); ov=$(grep -c "^; FEATURE: Overhang wall" $g 2>/dev/null); br=$(grep -c "^; FEATURE: Bridge" $g 2>/dev/null)
w=$(grep -m1 "^; total filament weight" $g 2>/dev/null); err=$(python3 -c "import json;print(json.load(open('$o/result.json'))['error_string'])" 2>/dev/null)
t=$(python3 -c "import json;d=json.load(open('$o/result.json'));print(round(d['sliced_plates'][0]['main_predication']/3600,2),'h')" 2>/dev/null)
echo "$tag rc=$rc result='$err' support_features=$sup overhang_wall=$ov bridge=$br | $w | time $t"
