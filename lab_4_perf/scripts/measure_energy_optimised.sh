#!/bin/bash
set -e

mkdir -p out/optimised
echo "▶ Measuring energy for optimised (aiohttp)..."


sudo -v


sudo powermetrics --samplers tasks --show-process-gpu --show-process-energy -i 200 > out/optimised/energy_system.txt &
PM_PID=$!


python /Users/admin/Documents/system-programming-labs/lab_4_perf/src/optimized_version.py &
PY_PID=$!
wait $PY_PID


sleep 1
sudo kill -2 $PM_PID 2>/dev/null || true
sleep 0.5
sudo kill -9 $PM_PID 2>/dev/null || true
wait $PM_PID 2>/dev/null || true

echo "✅ Energy log saved to out/optimized/energy_system_optimised.txt"