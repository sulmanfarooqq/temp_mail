@echo off
echo Installing TempMail GUI Application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python 3.7+ and make sure it's added to your PATH.
    echo Download from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Install required packages
echo Installing required packages...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install required packages.
    pause
    exit /b 1
)

REM Create desktop shortcut
echo Creating desktop shortcut...
cd gui
python create_shortcut.py

echo.
echo Setup complete!
echo You can now use the TempMail application by double-clicking the desktop shortcut.
echo.
pause