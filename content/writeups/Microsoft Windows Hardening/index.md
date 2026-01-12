---
title: Microsoft Windows Hardening
date: 2026-01-12
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - Windows
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task 1 - Introduction

No answer needed

---
## Task 2 - Understanding General Concepts

#### 1) What is the startup type of App Readiness service in the services panel?

*Search for `services` in the search box and open it. Double click on `App Readiness` to know more.*

**Ans:** `Manual`
#### 2) What is the default value of the key?

*Search for `registry` in the search box and open it. `Ctrl + F` to open the search box and search for `tryhackme`.*

**Ans:** `{THM_REG_FLAG}`
#### 3) Can you find the flag?

*The flag is in the following location: `C:\ProgramData\Microsoft\Diagnosis\flag.txt.txt`. Its not possible to open it as is, so open `Notepad` with admin privileges and then open the file.*

**Ans:** `{THM_REG_FLAG}`

---
## Task 3 - Identity & Access Management

#### 1) Find the name of the Administrator Account of the attached VM.

*Go to `Control Panel > User Accounts`*

**Ans:** `Harden`
#### 2) What is the default level of Notification?

*To access UAC, go to `Control Panel -> User Accounts` and click on `Change User Account Control Setting`.*

**Ans:** `Always Notify`

#### 3) How many standard accounts are created in the VM?

*There is only 1 admin account, no standard accounts.*

**Ans:** `0`

---
## Task 4 - Network Management

#### 1) Which of the following profiles is active?

*For me it was showing that the `Public Profile is Active` so I'm not really sure why the answer is `Private`...*

**Ans:** `Private`
#### 2) How many standard accounts are created in the VM?

*Run, the following command in `command prompt` or `powershell`.*

```powershell
type C:\Windows\System32\Drivers\etc\hosts
```

**Ans:** `0`
#### 3) What is the Physical address for the IP address 255.255.255.255?

```powershell
C:\Users\Harden>arp -a

Interface: 10.49.186.172 --- 0x5
  Internet Address      Physical Address      Type
  10.49.128.1           0a-8d-9c-ee-ea-81     dynamic
  10.49.191.255         ff-ff-ff-ff-ff-ff     static
  169.254.169.254       0a-8d-9c-ee-ea-81     dynamic
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static
```

**Ans:** `ff-ff-ff-ff-ff-ff`

---
## Task 5 - Application Management

#### 1) What is the extension?

*Go to `Virus and Threat Protection -> Exclusions`.*

**Ans:** `.ps`

#### 2) Is it best practice to open it immediately on your personal computer ?

**Ans:** `nay`

#### 3) What is the flag you received after executing the Office Hardening Batch file?

**Ans:** `{THM_1101110}`

---
## Task 6 - Storage Management

#### 1) Can you read the last six digits of the recovery key?

*The recovery key can be found in the `Documents` folder.*

```txt
Recovery Key:

	132858-327525-689172-680790-354607-080454-642268-377564
```

**Ans:** `377564`

#### 2) How many characters does the BitLocker recovery key have...?

*I used python to find the length:*

```python
print(len("132858327525689172680790354607080454642268377564"))
```

**Ans:** `48`

#### 3) What is the extension of that file?

**Ans:** `.bkf`

---
## Task 7 - Updating Windows

#### 1) What is the CVE score for the vulnerability CVE ID CVE-2022-32230?

*You can find more information about the `cve` [here](https://www.cvedetails.com/cve/CVE-2022-32230/).*

>Microsoft Windows SMBv3 suffers from a null pointer dereference in versions of Windows prior to the April, 2022 patch set. By sending a malformed FileNormalizedNameInformation SMBv3 request over a named pipe, an attacker can cause a Blue Screen of Death (BSOD) crash of the Windows kernel. For most systems, this attack requires authentication, except in the special case of Windows Domain Controllers, where unauthenticated users can always open named pipes as long as they can establish an SMB session. Typically, after the BSOD, the victim SMBv3 server will reboot.

**Ans:** `7.8`

---
