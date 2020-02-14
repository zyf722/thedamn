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

print("[+] TheDamn Installer")

#========================================================
# Main Part
#--------------------------------------------------------

# Install python requirements packages
print("[+] Installing requirements packages...\n")
os.system("pip install -r requirements.txt")

# Adding TheDamn directory to PATH
print("[+] Adding the current directory to PATH...\n")
if "TheDamn" not in os.environ["path"]:
	os.system("wmic ENVIRONMENT where \"name='path' and username='<system>'\" set VariableValue=\"%path%;%CD%\"")
	print("\n[!] Done.")
else:
	print("\n[!] You've already installed TheDamn!")
	
#========================================================