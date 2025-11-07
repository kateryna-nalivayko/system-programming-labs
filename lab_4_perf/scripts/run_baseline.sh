#!/bin/bash
set -e


mkdir -p out/baseline
echo "▶ Running baseline (requests)..."

/usr/bin/time -lp poetry run python lab_4_perf/src/main.py \
  2> out/baseline/time_verbose.txt


poetry run py-spy record flamegraph --output out/baseline/flamegraph.svg -- python lab_4_perf/src/main.py

echo "✅ Baseline complete! Results saved to out/baseline/"