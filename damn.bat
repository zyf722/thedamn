::======================
:: TheDamn Additional Script v0.2
::======================
@echo off
set DR=%CD%
cd /d %~dp0
doskey /HISTORY > cmd_history.log
cd /d %DR%
damn.py
cd /d %~dp0
del cmd_history.log /f /q
cd /d %DR%