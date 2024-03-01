# Script Name:                  Ops Challenge -System Process Commands
# Author:                       Gilbert Collado
# Date of latest revision:      02/29/2024
# Purpose:                      Sort processes, Inedexing processes, starting and stoping processes
# Source1:                      https://chat.openai.com/share/bc69ee75-f727-4471-b8b4-2e914b52d256
# Source2:                      https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/?view=powershell-5.1

@echo off


echo Running Get-Process | Sort-Object CPU -Descending | Format-Table Name, CPU


echo Running Get-Process | Sort-Object Id -Descending | Format-Table Name, Id


echo Running Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5 | Format-Table Name, @{Name="WS (KB)";Expression={$_.WorkingSet / 1KB}}


echo Running Start-Process "microsoft-edge:" -ArgumentList "https://owasp.org/www-project-top-ten/"


echo Running for ($i = 0; $i -lt 10; $i++) {
  Start-Process "notepad.exe"
}

echo Running Get-Process notepad | Stop-Process

echo Running Stop-Process -Id 2880

# Get all active processes and sort them by CPU time (descending)
# Get all active processes and sort them by PID (descending)
# Get the top 5 processes sorted by Working Set (WS)
# Start Notepad 10 times using a for loop
# Close all Notepad instances
# Open OWASP website in a browser
# Kill a process by PID


