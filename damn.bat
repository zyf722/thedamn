@echo off
set DR=%CD%
cd /d %~dp0
doskey /HISTORY > cmd.tmp
damn.py
del cmd.tmp /f /q
cd /d %DR%