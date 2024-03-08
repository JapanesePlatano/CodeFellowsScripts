# Script Name:                  Ops Challenge - Windows Batch Scripting
# Author:                       Gilbert Collado
# Date of latest revision:      02/28/2024
# Purpose:                      Create a batch script that robocopies files to another folder via powershell
# Source1:                      https://g.co/gemini/share/166aeefee93f
# Source2:                      https://www.makeuseof.com/tag/use-windows-batch-file-commands-automate-repetitive-tasks/

@echo off
setlocal enabledelayedexpansion

REM Prompt user for source folder path
set /p "sourcePath=Enter the source folder path: "

REM Prompt user for destination folder path
set /p "destPath=Enter the destination folder path: "

REM Validate source folder path
if not exist "!sourcePath!\" (
    echo Source folder does not exist.
    goto :EndScript
)

REM Validate destination folder path
if not exist "!destPath!\" (
    mkdir "!destPath!" 2>nul
    if errorlevel 1 (
        echo Unable to create destination folder.
        goto :EndScript
    )
)

REM Use ROBOCOPY to copy files and subdirectories
robocopy "!sourcePath!" "!destPath!" /E
if errorlevel 1 (
    echo Error occurred during copying.
) else (
    echo File copy completed successfully.
)

:EndScript
endlocal
