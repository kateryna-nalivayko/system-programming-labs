@echo off
setlocal
echo ▶ Running optimised (requests, aiohttp)...

REM === Створюємо папку для виводу ===
if not exist out\optimised mkdir out\optimised

REM === Вимірюємо час роботи ===
echo Measuring time...
powershell -Command "Measure-Command { poetry run python lab_4_perf\src\optimized_version.py }" > out\optimised\time_verbose.txt

REM === Профілювання та створення FlameGraph напряму ===
echo Running py-spy (direct SVG output)...
poetry run py-spy record -f flamegraph -o out\optimised\flamegraph.svg -- python lab_4_perf\src\optimized_version.py

echo ✅ optimised complete! Results saved to out\optimised\
pause
endlocal