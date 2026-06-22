@echo off
title Portfolio Admin
cd /d "%~dp0"

set "PYTHON=venv\Scripts\python.exe"
"%PYTHON%" --version >nul 2>&1
if errorlevel 1 (
    set "PYTHON=C:\Users\Admin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
    set "PYTHONPATH=%CD%\venv\Lib\site-packages"
)

if not exist "%PYTHON%" (
    echo Python could not be found. Recreate the virtual environment and try again.
    pause
    exit /b 1
)

"%PYTHON%" manage.py createsuperuser
pause
