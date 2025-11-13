@echo off
setlocal
echo ▶ Running baseline (requests)...

REM === Створюємо папку для виводу ===
if not exist out\baseline mkdir out\baseline

REM === Вимірюємо час роботи ===
echo Measuring time...
powershell -Command "Measure-Command { poetry run python lab_4_perf\src\main.py }" > out\baseline\time_verbose.txt

REM === Профілювання та створення FlameGraph напряму ===
echo Running py-spy (direct SVG output)...
poetry run py-spy record -f flamegraph -o out\baseline\flamegraph.svg -- python lab_4_perf\src\main.py

echo ✅ Baseline complete! Results saved to out\baseline\
pause
endlocal