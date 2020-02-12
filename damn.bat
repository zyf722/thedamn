::======================
:: TheDamn Additional Script v0.3
::======================
@echo off
doskey /HISTORY > %~dp0cmd_history.log
damn.py
del %~dp0cmd_history.log /f /q