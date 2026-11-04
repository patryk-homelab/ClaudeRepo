#!/bin/bash
# usage: slice.sh model.stl tag [support]  -> /root/bbs/out/<tag>/
in="$1"; tag="$2"; proc=/root/bbs/prof/process_flat.json; [ "$3" = "support" ] && proc=/root/bbs/prof/process_flat_support.json
o=/root/bbs/out/$tag; mkdir -p $o; cp "$in" $o/model.stl
timeout 900 dbus-run-session -- flatpak run --command=bambu-studio com.bambulab.BambuStudio --debug 2 --arrange 1 --orient 0 --allow-rotations --slice 0 \
  --load-settings "/root/bbs/prof/machine_flat.json;$proc" --load-filaments "/root/bbs/prof/filament_flat.json" \
  --outputdir $o --export-3mf sliced.3mf $o/model.stl > $o/log.txt 2>&1
rc=$?
g=$o/plate_1.gcode
sup=$(grep -c -E "^; FEATURE: Support" $g 2>/dev/null); ov=$(grep -c "^; FEATURE: Overhang wall" $g 2>/dev/null); br=$(grep -c "^; FEATURE: Bridge" $g 2>/dev/null)
w=$(grep -m1 "^; total filament weight" $g 2>/dev/null); ft=$(grep -m1 "^; filament_type =" $g); es=$(grep -m1 "^; enable_support =" $g); err=$(python3 -c "import json;print(json.load(open('$o/result.json'))['error_string'])" 2>/dev/null)
t=$(python3 -c "import json;d=json.load(open('$o/result.json'));print(round(d['sliced_plates'][0]['main_predication']/3600,2),'h')" 2>/dev/null)
echo "$tag rc=$rc result='$err' support_features=$sup overhang_wall=$ov bridge=$br | $w | $ft | $es | time $t"
