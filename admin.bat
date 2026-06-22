@echo off
title Portfolio Admin
cd /d "%~dp0"
venv\Scripts\python.exe manage.py createsuperuser
pause
