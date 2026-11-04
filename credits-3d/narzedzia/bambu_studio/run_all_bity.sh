#!/bin/bash
# Bambu Studio 2.8.2 X2D batch for bit holders: slice with auto supports (tree, 30 deg); if supports appear, slice again with
# supports from the build plate only; then export a project with the variant chosen (none / support_bp if it gives the same support / support).
B="$1"; cd "$B"; : > results.tsv
for f in stl/*.stl; do
  t=$(basename "$f" .stl)
  a=$(bash /root/bbs/slice.sh "$B/$f" "bits_${t}_sup" support)
  ns=$(echo "$a" | sed -n 's/.*support_features=\([0-9]*\).*/\1/p'); nb=""; mode=""
  if [ "${ns:-0}" -gt 0 ]; then
    b=$(bash /root/bbs/slice.sh "$B/$f" "bits_${t}_bp" support_bp); nb=$(echo "$b" | sed -n 's/.*support_features=\([0-9]*\).*/\1/p')
    if [ "$nb" = "$ns" ]; then mode=support_bp; else mode=support; fi
  fi
  if [ "${ns:-0}" -eq 0 ]; then c=$(bash /root/bbs/slice.sh "$B/$f" "bits_${t}_nosup"); else c="$a"; fi
  printf "%s\t%s\t%s\t%s\t%s\t%s\n" "$t" "$ns" "$nb" "${mode:-none}" "$a" "$c" >> results.tsv
  case "$t" in o*) ;; *) bash /root/bbs/project.sh "$B/$f" "$B/proj/${t#*_}_X2D_PETG.3mf" $mode >> proj.log 2>&1 ;; esac
done
echo DONE > done.flag
