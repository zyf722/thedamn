# TheDamn v0.3 ![GitHub](https://img.shields.io/github/license/zyf722/thedamn)

*The Damn* is a magnificent app for Windows CMD, inspired by [*The Fuck*](https://github.com/nvbn/thefuck),
that corrects errors in previous console commands.

![example_default](https://i.loli.net/2020/02/09/6TRoUFS7BqtpnJz.gif)

![example_candicates](https://i.loli.net/2020/02/09/gM7VBuTsLzNfR1O.gif)

![example_second_command](https://i.loli.net/2020/02/12/oWLUHqflmxcj98B.gif)

## Features
- Automatically correct wrong commands *(Only supports correcting the **unknown command error** now)*
-  Multi-candicates to choose
- **(New!)** Correct sub-commands

## Requirements

- Python 3
- pip
- fuzzywuzzy
- python-Levenshtein
- colorama

## Installation
```
git clone https://github.com/zyf722/thedamn.git
cd thedamn
install
```
This will add the directory of *TheDamn* to the environment variable PATH, in order to run it with the command ```damn```.

## Usage
When you type a wrong command and want to fix it, just type ```damn``` like this:
```
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\SysWOW64>peng localhost
'peng' is not recognized as an internal or external command,
operable program or batch file.

C:\Windows\SysWOW64>damn

[+] Did you mean: ping localhost [y/c/n] y

Pinging THEDAMN [::1] with 32 bytes of data:
Reply from ::1: time<1ms
Reply from ::1: time<1ms
Reply from ::1: time<1ms
Reply from ::1: time<1ms

Ping statistics for ::1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```
You can enter *y* or simply press the enter key to confirm.

If you want to choose another candicate, you can enter *c* to change.

If you're not afraid of running corrected commands without confirmation, the ```require_confirmation``` option can be set to ```false``` in ```config.json```.

## Customization
### New commands
To add your own command, you can add new keywords to the file ```data/keywords.db```.

### New Sub-commands
If you want to add sub-commands for your new command, you can create a new file named as your command in the ```data/subcmds/``` directory, then add sub-commands for it.

The folder structure should be like this:
```
thedamn
│  config.json
│  damn.bat
│  damn.py
│  install.py
│  LICENSE
│  README.md
│  requirements.txt
│  
├─data
│  │  keywords.db
│  │  
│  └─subcmds
│          your_new_sub_command.db
|          (other files...)
│          
└─presets
        keywords_default.db
        keywords_only_tools.db
```

You can refer to the ```git``` command and its sub-commands.

### Presets
If you need a file that just contains Windows basic commands or other tools, you can find what you want in the ```presets``` directory. You can replace ```data/keywords.db``` with them if you want to. (The default ```data/keywords.db``` is the union of the two files in ```presets/```)

### Configuration
Some of TheDamn settings can be changed in the file ```config.json```:
- ```require_confirmation``` - requires confirmation before running new command, by default ```true```
- ```monochrome_mode``` - print output without any color, by default ```false```

## To-Do
- [x] Support sub-commands
- [ ] Fix more types of error like **argument errors** and **switch errors**.

## License
[The MIT License](https://github.com/zyf722/thedamn/blob/master/LICENSE)
