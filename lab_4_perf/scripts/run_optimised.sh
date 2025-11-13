#!/bin/bash
set -e

mkdir -p out/optimized
echo "▶ Running optimized (aiohttp)..."

/usr/bin/time -lp python lab_4_perf/src/optimized_version.py \
  2> out/optimized/time_verbose.txt

sudo -E py-spy record --format raw --output out/optimized/profile.raw -- \
  python /Users/admin/Documents/system-programming-labs/lab_4_perf/src/optimized_version.py

cat out/optimized/profile.raw | flamegraph.pl > out/optimized/flamegraph.svg

echo "✅ Optimized version complete! Results saved to out/optimized/"