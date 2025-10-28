---
title: "John the Ripper: The Basics"
date: 2025-10-28
draft: false
tags:
  - TryHackMe
  - Hashing
  - Cybersecurity
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task  1 - Introduction

No answer needed

---

## Task  2 - Basic Terms

#### 1) What is the most popular extended version of John the Ripper?

**Ans:** `Jumbo John`

---

## Task  3 - Setting Up Your System

#### 1) Which website’s breach was the `rockyou.txt` wordlist created from?

**Ans:** `rockyou.com`

---

## Task 4 - Cracking Basic Hashes

#### 1) What type of hash is hash1.txt?

*We can paste the hash in `hashed.com` to identify the type of hash.*

**Ans:** `md5`
#### 2) What is the cracked value of hash1.txt?

*Run the following command to crack the hash:*

```bash
 john --format=raw-md5 --wordlist /usr/share/wordlists/rockyou.txt hash1.txt
```

*Run the following command to display the cracked hash:*

```bash
john --show --format=Raw-MD5 hash1.txt
?:biscuit
```

**Ans:** `biscuit`

#### 3) What type of hash is hash2.txt?

*We can paste the hash in `hashed.com` to identify the type of hash*

**Ans:** `SHA1`

#### 4) What is the cracked value of hash2.txt?

*Run the following command to crack the hash:*

```bash
 john --format=raw-SHA1 --wordlist /usr/share/wordlists/rockyou.txt hash2.txt
```

*Run the following command to display the cracked hash.*

```bash
john --show --format=Raw-SHA1 hash2.txt
?:kangeroo
```

**Ans:** `kangeroo`

#### 5) What type of hash is hash3.txt?

*We can paste the hash in `hashed.com` to identify the type of hash.*

**Ans:** `SHA256`

#### 6) What is the cracked value of hash3.txt?

*Run the following command to crack the hash:*

```bash
 john --format=raw-SHA256 --wordlist /usr/share/wordlists/rockyou.txt hash3.txt
```

*Run the following command to display the cracked hash:*

```bash
john --show --format=Raw-SHA256 hash3.txt
?:microphone
```

**Ans:** `microphone`

#### 7) What type of hash is hash4.txt?

*Its hard to find this one online you'll have to use the recommended python tool `hash-id` to be able to get suggestions for the possible hash type.*

**Ans:** `whirlpool`

#### 8) What is the cracked value of hash3.txt?

*Run the following command to crack the hash:*

```bash
 john --format=whirlpool --wordlist /usr/share/wordlists/rockyou.txt hash4.txt
```

*Run the following command to display the cracked hash:*

```bash
john --show --format=whirlpool hash4.txt
?:colossal
```

**Ans:** `colossal`

---

## Task 5 - Cracking Windows Authentication Hashes

*For the following questions, you can typically find the details on the internet by searching around and on websites like `Hashcat`.*

#### 1) What do we need to set the `--format` flag ?

*We can find this by using the following command:*

```bash
john --list=formats | grep -iF "ntlm"
mysql, net-ah, nethalflm, netlm, netlmv2, net-md5, netntlmv2, netntlm, 
netntlm-naive, net-sha1, nk, notes, md5ns, nsec3, NT, NT-long, o10glogon, 
430 formats (151 dynamic formats shown as just "dynamic_n" here)
```

**Ans:** `NT`

#### 2) What is the cracked value of this password?

*Run the following command to crack the hash:*

```bash
 john --format=NT --wordlist /usr/share/wordlists/rockyou.txt ntlm.txt
```

*Run the following command to display the cracked hash:*

```bash
john --show --format=NT ntlm.txt
?:mushroom
```

**Ans:** `mushroom`

---

## Task 6 - Cracking /etc/shadow Hashes

#### 1) What is the root password?

*We first need to create `unshadowed.txt` and then use `john` to crack it.*

```bash
unshadow local_passwd local_shadow > unshadowed.txt
```

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt unshadowed.txt
```

```bash
john --show unshadowed.txt 
root:1234:0:0::/root:/bin/bash
```

**Ans:** `1234`

---

## Task 7 -  Single Crack Mode

#### 1) What is Joker’s password?

*The hash is of the `md5` format. We also need to append the user's name in front of the hash before cracking it.*

`Joker:7bf6d9bb82bed1302f331fc6b816aada`

```bash
john --single --format=Raw-md5 hash07.txt
```


```bash
john --show --format=Raw-md5 hash07.txt
```

**Ans:** `Jok3r`

---

## Task 8 - Custom Rules

#### 1) What do custom rules allow us to exploit?

**Ans:** `Password complexity predictability`

#### 2) What rule would we use to add all capital letters to the end of the word?

**Ans:** `Az"[A-Z]"`

#### 3) What flag would we use to call a custom rule called `THMRules`?

**Ans:** `--rule=THMRules`

---

## Task 9 - Cracking Password Protected Zip Files

#### 1) What is the password for the secure.zip file?

*In order to get the password we first need to convert the zip to a hash using `zip2john` and the crack the hash as usual.*

```bash
zip2john secure.zip > hash.txt
```

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

```bash
john --show hash.txt
secure.zip/zippy/flag.txt:pass123:zippy/flag.txt:secure.zip::secure.zip
```

**Ans:** `pass123`

#### 2) What is the contents of the flag inside the zip file?

*We can use `unzip` to extract the file and then discover the contents of the flag*

```bash
unzip secure.zip
```

**Ans:** `THM{w3ll_d0n3_h4sh_r0y4l}`

---
## Task 10 - Cracking Password-Protected RAR Archives

#### 1) What is the password for the secure.rar file?

*In order to get the password we first need to convert the zip to a hash using `rar2john` and the crack the hash as usual.*

```bash
rar2john secure.rar > hash.txt
```

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

```bash
john --show hash.txt
secure.rar:password
```

**Ans:** `password`

#### 2) What are the contents of the flag inside the zip file?

*We can use `unrar` to extract the file and then discover the contents of the flag*

```bash
unrar x secure.rar
```

**Ans:** `THM{w3ll_d0n3_h4sh_r0y4l}`

---

## Task 11 - Cracking Password-Protected RAR Archives

#### 1) What is the password for the secure.rar file?

*In order to get the password we first need to convert `id_rsa` to a hash using `ssh2john.py` and the crack the hash as usual.*

```bash
/opt/john/ssh2john.py id_rsa > hash.txt
```

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

```bash
john --show hash.txt
id_rsa:mango
```

**Ans:** `mango`

---

