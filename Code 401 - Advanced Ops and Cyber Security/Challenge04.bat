# Script Name:                  CIS Benchmark Script
# Author:                       Gilbert Collado
# Date of latest revision:      05/02/2024
# Purpose:                      PowerShell script to configure CIS benchmarks 1.1.5 (L1) and 18.4.3 (L1)
# Source1:                      https://g.co/gemini/share/9897a6650969
# Source2:                     
# Function to set the minimum password length
function Set-MinPasswordLength {
    param (
        [int]$length = 14
    )
    # Load the appropriate DLL for accessing advanced password policies
    Add-Type -AssemblyName System.Security
    try {
        # Set minimum password length policy
        secedit /export /cfg "$env:TEMP\secpol.cfg"
        (Get-Content -Path "$env:TEMP\secpol.cfg" -Raw) -replace "MinimumPasswordLength = \d+", "MinimumPasswordLength = $length" | Set-Content -Path "$env:TEMP\secpol.cfg"
        secedit /import /cfg "$env:TEMP\secpol.cfg" /db secedit.sdb /verbose
        Remove-Item -Path "$env:TEMP\secpol.cfg"
        Write-Host "Minimum password length set to $length characters successfully."
    } catch {
        Write-Error "Failed to set the minimum password length. Error: $_"
    }
}

# Function to disable SMB v1 client driver
function Disable-SMBv1Client {
    # Path to the SMBv1 client driver registry key
    $smbv1ClientKey = "HKLM:\SYSTEM\CurrentControlSet\Services\mrxsmb10"
    
    try {
        # Check if the registry path exists
        if (Test-Path $smbv1ClientKey) {
            # Set the 'Start' registry key to 4 (disabled)
            Set-ItemProperty -Path $smbv1ClientKey -Name "Start" -Value 4
            Write-Host "SMB v1 client driver has been disabled successfully."
        } else {
            Write-Warning "SMB v1 client driver registry key does not exist."
        }
    } catch {
        Write-Error "Failed to disable SMB v1 client driver. Error: $_"
    }
}

# Execute the functions
Set-MinPasswordLength -length 14
Disable-SMBv1Client

# Additional instructions for the script
Write-Host "Please restart the server for all changes to take effect fully."
