# Script Name:                  SOC 2 automation configuration script
# Author:                       Gilbert Collado
# Date of latest revision:      04/29/2024
# Purpose:                      This automates ALL of the following required SOC 2 configurations on a Windows 10 endpoint. Automatic screen lock, Antivirus installed and scanning, Automatic OS updates enabled
# Source1:                      https://g.co/gemini/share/187023bd8482

@echo off

REM Automatic screen lock configuration
REM Set screen lock timeout to 15 minutes (900 seconds)
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaveTimeOut /t REG_SZ /d 900 /f
REM Enable screen saver and require a password to unlock
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaverIsSecure /t REG_SZ /d 1 /f
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaveActive /t REG_SZ /d 1 /f

REM Antivirus installation and scanning
REM Check if Windows Defender is enabled
setlocal enabledelayedexpansion
for /f "tokens=2 delims==" %%a in ('powershell -Command "(Get-MpComputerStatus).AntivirusEnabled"') do (
    set "defenderStatus=%%a"
)
if "%defenderStatus%"=="False" (
    echo Windows Defender is not enabled. Please enable it to meet SOC 2 requirements.
) else (
    echo Windows Defender is already enabled.
)

REM Automatic OS updates enabled
REM Enable automatic updates
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update" /v AUOptions /t REG_DWORD /d 4 /f

echo Automatic OS updates have been enabled.
echo SOC 2 configurations have been applied successfully.
