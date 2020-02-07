#========================================================
# TheDamn v0.2
#--------------------------------------------------------
# A magnificent app for Windows CMD, inspired by TheFuck,
# that corrects errors in previous console commands.
#--------------------------------------------------------
# v0.2 1) Renamed keywords.db and some variables
#      2) New Feature: Now you can choose more candicates
#      3) Optimize code comments
# v0.1 First commit
#========================================================



#========================================================
# Import libs
#--------------------------------------------------------
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os
#========================================================



#========================================================
# Define methods
#--------------------------------------------------------

#--------------------------------------------------------
### Read CMD commands from keywords.db
#--------------------------------------------------------
def ReadCommands():
	with open(os.path.dirname(__file__)+"\\keywords.db", "r") as cmd_tempfile:
		cmd_list = cmd_tempfile.readlines()
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
	for i in range(len(cmd_cache)):
		if i != "damn":
			cmd_previous = cmd_cache[-2]
			break
else:
	exit(1)

# Get candicates list
cmd_keyword = cmd_previous.split(' ')[0]
cmd_candicates = process.extract(cmd_keyword,cmd_list)

# Use the prime candicate as a default correction
cmd_candicate_index = 0
cmd_correct = CorrectCommand(cmd_previous,cmd_keyword,cmd_candicates,cmd_candicate_index)

# Wait for confirmation
while cmd_candicate_index < len(cmd_candicates)-1:
	print("\n[+] Did you mean: "+"\033[1;33m"+cmd_correct+"\033[0m [\033[1;32my\033[0m/\033[1;33mc\033[0m/\033[1;31mn\033[0m] ", end='')
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

#========================================================