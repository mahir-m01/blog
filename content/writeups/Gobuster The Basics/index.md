---
title: "Gobuster: The Basics"
date: 2025-11-10
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - Gobuster
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task  1 & 2 

No answer needed

---
## Task  2 - Gobuster: Introduction 

#### 1) What flag do we use to specify the target URL?

**Ans:** `-u`
#### 2) What **command** do we use for the subdomain enumeration mode?

**Ans:** `dns`


---
## Task  3 - Javascript Overview 

#### 1) What is the code output if the value of x is changed to 10?

**Ans:** `The result is: 20`
#### 2) What term describes registering domain names that are misspelt ?

**Ans:** `Interpreted`

---

## Task 4 - Use Case: Directory and File Enumeration

#### 1) Which flag do we have to add to our command to skip the TLS verification?

**Ans:** `--no-tls-validation`
#### 2) Which directory catches your attention?

*Run the following command:*

```bash
gobuster dir -u www.offensivetools.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -r -t 64
```

**Ans:** `/secret`

#### 3) What is the flag found in this file?

*Run the following command:*

```bash
gobuster dir -u www.offensivetools.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -r -t 256 -x .js
```

*You should get the file - `flag.js`*

```
curl http://www.offensivetools.thm/secret/flag.js
```

**Ans:** `THM{ReconWasASuccess}`

---
## Task 5 - Use Case: Subdomain Enumeration

#### 1) Apart from the dns keyword and the -w flag...?

**Ans:** `-d`
#### 2) How many subdomains are configured for the offensivetools.thm domain?

*Run the following command:*

```bash
gobuster dns -d www.offensivetools.com -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -t 128
```

**Ans:** `4`

---
## Task 6 - Use Case: Vhost Enumeration

#### 1) How many vhosts on the offensivetools.thm domain reply with a status code 200?

*First, start a server to listen to:*

```bash
python3 -m http.server 8080
```

*Now, run the command:*

```bash
gobuster vhost -u "http://10.48.101.39:8080" --domain offensivetools.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain -t 128 -s 200

```

**Ans:** `4`

---