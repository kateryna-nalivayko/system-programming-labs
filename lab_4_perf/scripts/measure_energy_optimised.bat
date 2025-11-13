@echo off
setlocal enabledelayedexpansion

echo ▶ Measuring energy for optimised (requests)...

if not exist out\optimised mkdir out\optimised

rem === Start CPU monitoring via WMI ===
echo Collecting CPU load...
powershell -Command " $cpu = Get-WmiObject Win32_Processor | Select-Object -ExpandProperty LoadPercentage; $time = Get-Date -Format 'yyyy-MM-dd_HH-mm-ss'; [PSCustomObject]@{Timestamp=$time; CPU_Load=$cpu} | Export-Csv -Path 'out\optimised\energy_system.csv' -NoTypeInformation -Encoding utf8 "

rem === Run target Python program ===
echo Running Python program...
python lab_4_perf\src\optimised_version.py > out\optimised\main_output.log 2>&1

echo ✅ Energy log saved to out\optimised\energy_optimised_system.csv
pause