# Script Name:                  Ops Challenge -Automated Endpoint Configuration
# Author:                       Gilbert Collado
# Date of latest revision:      0203/4/2024
# Purpose:                      Enable File and Printer Sharing, Allow ICMP traffic, Enable Remote management, Remove bloatware, Enable Hyper-V, Disable SMBv1, an insecure protocol
# Source1:                      https://g.co/gemini/share/1f69781668a8
# Source2:                      https://github.com/codefellows/seattle-ops-201d12/blob/main/class-11/challenges/DEMO.md

@echo off


powershell -Command "Enable-NetFirewallRule -DisplayGroup 'File and Printer Sharing'"


powershell -Command "New-NetFirewallRule -DisplayName 'ICMPv4' -Direction Inbound -Protocol ICMPv4 -Enabled True -Profile Any -Action Allow"
powershell -Command "New-NetFirewallRule -DisplayName 'ICMPv6' -Direction Inbound -Protocol ICMPv6 -Enabled True -Profile Any -Action Allow"


powershell -Command "Enable-PSRemoting -Force"


set appsToRemove="3DBuilder" "Getstarted" "MicrosoftOfficeHub" "MicrosoftSolitaireCollection" "OneNote" "Sway" "OneConnect" "People" "Print3D" "SkypeApp" "Wallet" "Photos" "Alarms" "Calculator" "Camera" "windowscommunicationsapps" "Maps" "WindowsPhone" "WindowsSoundRecorder" "WindowsStore" "XboxApp" "ZuneMusic" "ZuneVideo"
for %%i in (%appsToRemove%) do (
    powershell -Command "Get-AppxPackage -Name %%i | Remove-AppxPackage"
)


powershell -Command "Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All"


powershell -Command "Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol -NoRestart"

:: Display a message indicating completion
echo Configuration completed successfully.
pause

# Enable File and Printer Sharing
# Allow ICMP traffic
# Enable Remote management
# Remove bloatware
# Enable Hyper-V
# Disable SMBv1
# Display a message indicating completion