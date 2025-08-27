@echo off
cd /d "%~dp0"
python tempmail_gui.py
if %errorlevel% neq 0 (
    echo.
    echo Failed to start the application.
    echo Make sure Python is installed and added to your PATH.
    echo.
    pause
)