# Script Name:                  Ops Challenge -Log Retrieval via Powershell 
# Author:                       Gilbert Collado
# Date of latest revision:      02/29/2024
# Purpose:                      Retrieve logs, extract specific events, print selected amount
# Source1:                      https://g.co/gemini/share/694efd03f47d
# Source2:                      https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/?view=powershell-5.1

@echo off

echo Running Get-WinEvent -LogName System -FilterXPath "*[System[TimeCreated[timediff(@SystemTime) <= 86400000]]]"...
PowerShell.exe -NoProfile -ExecutionPolicy Bypass -Command "Get-WinEvent -LogName System -FilterXPath '*[System[TimeCreated[timediff(@SystemTime) <= 86400000]]]' | Out-File -FilePath 'C:\Users\gilbertcollado\Desktop\last_24.txt'"

echo Running Get-WinEvent -LogName System -FilterXPath "*[System[Level=2]]"...
PowerShell.exe -NoProfile -ExecutionPolicy Bypass -Command "Get-WinEvent -LogName System -FilterXPath '*[System[Level=2]]' | Out-File -FilePath 'C:\Users\gilbertcollado\Desktop\errors.txt'"

echo Running Get-WinEvent -LogName System -FilterXPath "*[System[EventID=16]]"...
PowerShell.exe -NoProfile -ExecutionPolicy Bypass -Command "Get-WinEvent -LogName System -FilterXPath '*[System[EventID=16]]' | Format-Table -AutoSize"

echo Running Get-WinEvent -LogName System -MaxEvents 20...
PowerShell.exe -NoProfile -ExecutionPolicy Bypass -Command "Get-WinEvent -LogName System -MaxEvents 20 | Format-Table -AutoSize"

echo Running Get-WinEvent -LogName System -MaxEvents 500...
PowerShell.exe -NoProfile -ExecutionPolicy Bypass -Command "Get-WinEvent -LogName System -MaxEvents 500 | ForEach-Object { Write-Host $_.ProviderName + ': ' + $_.Message }"

echo Done!


Operation 1: Get all events from the System log in the last 24 hours and output to file

Operation 2: Get all events of type "Error" from the System log and output to file

Operation 3: Print all events with ID 16 from the System log to the console

Operation 4: Print the most recent 20 entries from the System log to the console

Operation 5: Print all unique sources of the 500 most recent entries from the System log (without truncation)

