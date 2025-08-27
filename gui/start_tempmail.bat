@echo off
cd /d "%~dp0"
cd ..
python -m gui.tempmail_gui
if %errorlevel% neq 0 (
    echo.
    echo Failed to start the application.
    echo Make sure Python is installed and added to your PATH.
    echo.
    pause
)