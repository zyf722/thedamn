#========================================================
# TheDamnInstaller
#--------------------------------------------------------
# A Tool that helps you to install and configure TheDamn.
#========================================================

#========================================================
# Import libs
#--------------------------------------------------------
import os
#========================================================

print("[+] \033[1;33mTheDamn Installer\033[0m")

#========================================================
# Main Part
#--------------------------------------------------------

# Install python requirements packages
print("[+] Install requirements packages...")
os.system("pip install fuzzywuzzy")
os.system("pip install python-Levenshtein")

# Adding TheDamn directory to PATH
print("[+] Adding the current directory to PATH...")
if "TheDamn" not in os.environ["path"]:
	os.system("wmic ENVIRONMENT where \"name='path' and username='<system>'\" set VariableValue=\"%path%;%CD%\"")
	print("[!] \033[1;33mDone.\033[0m")
else:
	print("[!] \033[1;31mYou've already installed TheDamn!\033[0m")
	
#========================================================