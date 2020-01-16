# TheDamn
# A magnificent app for Windows CMD, inspired by TheFuck,
# that corrects errors in previous console commands.

# Import libs
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os

# Define methods

### Read CMD commands from CMDList.db
def ReadCommands():
	with open(os.path.dirname(__file__)+"\\CMDList.db", "r") as cmd_tmp:
		cmd_list = cmd_tmp.readlines()
	for i in range(0,len(cmd_list)):
		cmd_list[i] = cmd_list[i].strip('\n')
	return cmd_list

# Read CMD Logs
with open(os.path.dirname(__file__)+"\\cmd.tmp", "r") as cmd_tmp:
	cmd_cache = cmd_tmp.readlines()

# Delete '\n'
for i in range(0,len(cmd_cache)):
	cmd_cache[i] = cmd_cache[i].strip('\n')

# Get CMD commands and previous command
cmd_list = ReadCommands()
if len(cmd_cache) >= 2:
	cmd_previous = cmd_cache[-2]
else:
	exit(1)

# Get candicates list
cmd_keyword = cmd_previous.split(' ')[0]
cmd_candicates = process.extract(cmd_keyword,cmd_list)

# Correct
cmd_correct = cmd_previous.replace(cmd_keyword,cmd_candicates[0][0])

# Wait for confirmation
print("\n[+] Did you mean: "+"\033[1;33m"+cmd_correct+"\033[0m [\033[1;32my\033[0m/\033[1;31mn\033[0m] ", end='')
choice = input()
if choice == "" or choice.lower() == "y":
	os.system(cmd_correct)
elif choice.lower() == "n":
	exit(1)