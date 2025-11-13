@echo off
setlocal enabledelayedexpansion

echo ▶ Measuring energy for baseline (requests)...

if not exist out\baseline mkdir out\baseline

rem === Start CPU monitoring via WMI ===
echo Collecting CPU load...
powershell -Command " $cpu = Get-WmiObject Win32_Processor | Select-Object -ExpandProperty LoadPercentage; $time = Get-Date -Format 'yyyy-MM-dd_HH-mm-ss'; [PSCustomObject]@{Timestamp=$time; CPU_Load=$cpu} | Export-Csv -Path 'out\baseline\energy_system.csv' -NoTypeInformation -Encoding utf8 "

rem === Run target Python program ===
echo Running Python program...
python lab_4_perf\src\main.py > out\baseline\main_output.log 2>&1

echo ✅ Energy log saved to out\baseline\energy_system.csv
pause