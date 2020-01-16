# The Damn ![GitHub](https://img.shields.io/github/license/zyf722/thedamn)

*The Damn* is a magnificent app for Windows CMD, inspired by [*The Fuck*](https://github.com/nvbn/thefuck),
that corrects errors in previous console commands.

![example.gif](https://i.loli.net/2020/01/16/5K8opFnLYrWCqxm.gif)

## Requirements

- Python 3
- pip
- fuzzywuzzy

## Installation
```
git clone https://github.com/zyf722/thedamn.git
cd thedamn
InstallTheDamn.bat
```
PS: This will add the directory of *The Damn* to the environment variable PATH, in order to run it with the command ```damn```.

## Usage
When you type a wrong command and want to fix it, just type ```damn``` like this:
```
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\SysWOW64>peng localhost
'peng' is not recognized as an internal or external command,
operable program or batch file.

C:\Windows\SysWOW64>damn

[+] Did you mean: ping localhost [y/n] y

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

## License
[The MIT License](https://github.com/zyf722/thedamn/blob/master/LICENSE)
