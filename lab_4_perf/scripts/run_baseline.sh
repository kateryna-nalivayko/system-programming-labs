#!/bin/bash
set -e


mkdir -p out/baseline
echo "▶ Running baseline (requests)..."

/usr/bin/time -lp python lab_4_perf/src/main.py \
  2> out/baseline/time_verbose.txt

sudo -E py-spy record --format raw --output out/baseline/profile.raw -- \
  python /Users/admin/Documents/system-programming-labs/lab_4_perf/src/main.py

cat out/baseline/profile.raw | flamegraph.pl > out/baseline/flamegraph.svg

echo "✅ Baseline complete! Results saved to out/baseline/"