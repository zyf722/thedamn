#========================================================
# TheDamn v0.3
#--------------------------------------------------------
# A magnificent app for Windows CMD, inspired by TheFuck,
# that corrects errors in previous console commands.
#--------------------------------------------------------
# v0.3.2 Add new option for monochrome output
# v0.3.1 Fixed bugs about output colors
# v0.3   1) New Feature: check sub-commands like "git clone"
#        2) Optimize directory structure
#        3) Now we have a config file
# v0.2.2 Fixed bugs about reading the previous command
# v0.2.1 Updated fuzzywuzzy scorer to optimize candicates
# v0.2   1) Renamed keywords.db and some variables
#        2) New Feature: Multi-candicates to choose
#        3) Optimize code comments
# v0.1   First commit
#========================================================



#========================================================
# Import libs
#--------------------------------------------------------
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from colorama import Fore,Style
import os, json
#========================================================



#========================================================
# Load Config
#--------------------------------------------------------
config = json.loads(open(os.path.dirname(__file__)+"\\config.json",encoding='utf-8').read())
#========================================================



#========================================================
# Define methods
#--------------------------------------------------------

#--------------------------------------------------------
### Read CMD commands from keywords.db
#--------------------------------------------------------
def ReadCommands():
	with open(os.path.dirname(__file__)+"\\data\\keywords.db", "r") as cmd_tempfile:
		cmd_list = cmd_tempfile.readlines()
	for file in os.listdir(os.path.dirname(__file__)+"\\data\\subcmds"):
		with open(os.path.dirname(__file__)+"\\data\\subcmds\\"+file, "r") as cmd_tempfile:
			cmd_sub_list = cmd_tempfile.readlines()
			cmd_list += [file.split('.')[0]+ " " + c for c in cmd_sub_list]
	for i in range(0,len(cmd_list)):
		cmd_list[i] = cmd_list[i].strip('\n')
	return cmd_list

#--------------------------------------------------------
### Replace and correct the command
#--------------------------------------------------------
def CorrectCommand(cmd_p,cmd_k,cmd_c,cmd_ci):
	return cmd_p.replace(cmd_k,cmd_c[cmd_ci][0])
	
#========================================================



#========================================================
# Main Part
#--------------------------------------------------------

# Read CMD Input History
with open(os.path.dirname(__file__)+"\\cmd_history.log", "r") as cmd_tempfile:
	cmd_cache = cmd_tempfile.readlines()

# Delete '\n' in cmd_cache
for i in range(0,len(cmd_cache)):
	cmd_cache[i] = cmd_cache[i].strip('\n')

# Get CMD commands and previous command
cmd_list = ReadCommands()
if len(cmd_cache) >= 2:
	cmd_previous = cmd_cache[-2]
else:
	exit(1)

# Get candicates list and initialize cmd_keyword
cmd_keyword = ""
cmd_candicates = []

# Get the cmd_keyword
for i in range(len(cmd_previous.split(' '))):
	
	cmd_keyword += cmd_previous.split(' ')[i]+" "
	cmd_candicates = process.extract(cmd_keyword,cmd_list,scorer=fuzz.ratio)
	
	if cmd_candicates[0][1] != 100:
		cmd_keyword = cmd_keyword[0:len(cmd_keyword)-1]
		break

# Use the prime candicate as a default correction
cmd_candicate_index = 0
cmd_correct = CorrectCommand(cmd_previous,cmd_keyword,cmd_candicates,cmd_candicate_index)

# Wait for confirmation
while cmd_candicate_index < len(cmd_candicates)-1:
	
	if config["require_confirmation"] == True:
		if config["monochrome_mode"] == False:
			print(Style.NORMAL+"\n[+] Did you mean: "+Style.BRIGHT+Fore.YELLOW+cmd_correct
																	+Style.NORMAL+Fore.WHITE+" ["
																	+Style.BRIGHT+Fore.GREEN+"y"
																	+Style.NORMAL+Fore.WHITE+"/"
																	+Style.BRIGHT+Fore.YELLOW+"c"
																	+Style.NORMAL+Fore.WHITE+"/"
																	+Style.BRIGHT+Fore.RED+"n"
																	+Style.NORMAL+Fore.WHITE+"] "
			, end='')
			print(Style.RESET_ALL)
		else:
			print("\n[+] Did you mean: "+cmd_correct+" [y/c/n] ", end='')
		choice = input().lower()
		if choice == "" or choice == "y":
			print("")
			os.system(cmd_correct)
			break
		elif choice == "c":
			cmd_candicate_index += 1
			cmd_correct = CorrectCommand(cmd_previous,cmd_keyword,cmd_candicates,cmd_candicate_index)
		elif choice == "n":
			
			exit(1)
	else:
		if config["monochrome_mode"] == False:
			print("\n[+] TheDamn Corrected Command: "+Style.BRIGHT+Fore.YELLOW+cmd_correct)
			print(Style.RESET_ALL)
		else:
			print("\n[+] TheDamn Corrected Command: "+cmd_correct)
		os.system(cmd_correct)
		break

#========================================================