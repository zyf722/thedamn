@echo off
echo [+] Install requirements packages...
pip install fuzzywuzzy
echo [+] Adding the current directory to PATH...
wmic ENVIRONMENT where "name='path' and username='<system>'" set VariableValue="%path%;%CD%"
pause > nul