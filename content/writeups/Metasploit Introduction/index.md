---
title: "Metasploit: Introduction"
date: 2025-10-31
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - Metasploit
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task  1 - Introduction

No answer needed

---

## Task  2 - Main Components of Metasploit

>  **Adapters:** An adapter wraps single payloads to convert them into different formats. For example, a normal single payload can be wrapped inside a Powershell adapter, which will make a single powershell command that will execute the payload.  
>  
>  **Singles:** Self-contained payloads (add user, launch notepad.exe, etc.) that do not need to download an additional component to run.
>  
>  **Stagers:** Responsible for setting up a connection channel between Metasploit and the target system. Useful when working with staged payloads. “Staged payloads” will first upload a stager on the target system then download the rest of the payload (stage). This provides some advantages as the initial size of the payload will be relatively small compared to the full payload sent at once.
>  
>  **Stages:** Downloaded by the stager. This will allow you to use larger sized payloads.
#### 1) Name of the code taking advantage of a flaw on the target system?

**Ans:** `Exploit`

#### 2) Code that runs on the target system to achieve the attacker's goal?

**Ans:** `Payload`

#### 3) What are self-contained payloads called?

**Ans:** `Singles`

#### 4) Is windows/x64/pingback_reverse_tcp" among singles or staged ?

**Ans:** `Singles`

> It is an inline (or single) payload, as indicated by the  `_`
---

## Task  3 - Msfconsole

#### 1) How would you search for a module related to Apache?

**Ans:** `search apache`

#### 2) Who provided the auxiliary/scanner/ssh/ssh_login module?

*We can use the `search` functionality and then use `info`  to get the required details*

```bash
msf6 > search  type:auxiliary ssh_login

Matching Modules
================

   #  Name                                    Disclosure Date  Rank    Check  Description
   -  ----                                    ---------------  ----    -----  -----------
   0  auxiliary/scanner/ssh/ssh_login         .                normal  No     SSH Login Check Scanner
   1  auxiliary/scanner/ssh/ssh_login_pubkey  .                normal  No     SSH Public Key Login Scanner
```

```bash
msf6 > info 0

       Name: SSH Login Check Scanner
     Module: auxiliary/scanner/ssh/ssh_login
    License: Metasploit Framework License (BSD)
       Rank: Normal

Provided by:
  todb <todb@metasploit.com>

Check supported:
  No

Basic options:
  Name              Current Setting  Required  Description
  ----              ---------------  --------  -----------
  ANONYMOUS_LOGIN   false            yes       Attempt to login with a blan
                                               k username and password
  BLANK_PASSWORDS   false            no        Try blank passwords for all
                                               users
  BRUTEFORCE_SPEED  5                yes       How fast to bruteforce, from
                                                0 to 5
  CreateSession     true             no        Create a new session for eve
                                               ry successful login
  DB_ALL_CREDS      false            no        Try each user/password coupl
                                               e stored in the current data
                                               base
  DB_ALL_PASS       false            no        Add all passwords in the cur
                                               rent database to the list
  DB_ALL_USERS      false            no        Add all users in the current
                                                database to the list
  DB_SKIP_EXISTING  none             no        Skip existing credentials st
                                               ored in the current database
                                                (Accepted: none, user, user
                                               &realm)
  PASSWORD                           no        A specific password to authe
                                               nticate with
  PASS_FILE                          no        File containing passwords, o
                                               ne per line
  RHOSTS                             yes       The target host(s), see http
                                               s://docs.metasploit.com/docs
                                               /using-metasploit/basics/usi
                                               ng-metasploit.html
  RPORT             22               yes       The target port
  STOP_ON_SUCCESS   false            yes       Stop guessing when a credent
                                               ial works for a host
  THREADS           1                yes       The number of concurrent thr
                                               eads (max one per host)
  USERNAME                           no        A specific username to authe
                                               nticate as
  USERPASS_FILE                      no        File containing users and pa
                                               sswords separated by space,
                                               one pair per line
  USER_AS_PASS      false            no        Try the username as the pass
                                               word for all users
  USER_FILE                          no        File containing usernames, o
                                               ne per line
  VERBOSE           false            yes       Whether to print output for
                                               all attempts

Description:
  This module will test ssh logins on a range of machines and
  report successful logins.  If you have loaded a database plugin
  and connected to a database this module will record successful
  logins and hosts so you can track your access.

References:
  https://nvd.nist.gov/vuln/detail/CVE-1999-0502


View the full module info with the info -d command.


```

*I've added the entire output for convenience.*

**Ans:** `todb`

---

## Task 4 - Working with modules

#### 1) How would you set the LPORT value to 6666?

**Ans:** `set LPORT 6666`

#### 2) Set the global value for RHOSTS  to 10.10.19.23 ?

**Ans:** `setg RHOSTS 10.10.19.23`

#### 3) Command  to clear a set payload?

**Ans:** `unset PAYLOAD`

#### 4) Command to proceed with the exploitation phase?

**Ans:** `exploit`

---
