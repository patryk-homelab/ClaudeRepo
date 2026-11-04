#!/bin/bash
# usage: slice.sh in.stl out_prefix
in="$1"; o="$2"
prusa-slicer --export-gcode --support-material --support-material-auto --nozzle-diameter 0.4 --filament-diameter 1.75 --layer-height 0.2 \
  --bed-shape 0x0,256x0,256x256,0x256 --max-print-height 260 --center 128,128 -o "$o.gcode" "$in" > "$o.log" 2>&1
rc=$?
sup=$(grep -c ';TYPE:Support material$' "$o.gcode" 2>/dev/null); iface=$(grep -c ';TYPE:Support material interface$' "$o.gcode" 2>/dev/null)
fil=$(grep -m1 -E '^; filament used \[cm3\]' "$o.gcode" 2>/dev/null); t=$(grep -m1 -E '^; estimated printing time \(normal mode\)' "$o.gcode" 2>/dev/null)
echo "$(basename "$in") rc=$rc support_blocks=$sup interface_blocks=$iface | $fil | $t"
