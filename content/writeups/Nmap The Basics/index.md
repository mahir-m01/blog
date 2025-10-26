---
title: "Nmap: The Basics"
date: 2025-10-26
draft: false
tags:
  - Nmap
  - TryHackMe
  - Cybersecurity
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task  1 - Introduction

No answer needed

---

## Task  2 - Host Discovery

#### 1)  last IP address - scan target is `192.168.0.1/27`?

*Run the following command:*

```bas
nmap -sL 192.168.0.1/27
```

**Ans:** `192.168.0.31`

---

## Task  3 - Port Scanning 

#### 1) TCP ports open on the target  `10.48.157.161`?

*Run the following command:*

```bash
nmap -sT 10.48.157.161
```

```bash
Nmap scan report for 10.48.157.161
Host is up (0.00058s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE
7/tcp    open  echo
9/tcp    open  discard
13/tcp   open  daytime
17/tcp   open  qotd
22/tcp   open  ssh
8008/tcp open  http
```

**Ans:** `6`

#### 2) Web server on `10.48.157.161` - What is the flag ?

*From the previous scan we know that a `http` server runs on port `8008`. We can `curl` the web-server to retrieve the information.*

```bash
curl 10.48.157.161:8008
```

```html
h1>Flag</h1>   
		<div class="coffee-type">
			<span style="font-size: 24px;"><code>THM{SECRET_PAGE_38B9P6}</code></span>
		</div>

```

**Ans:** `THM{SECRET_PAGE_38B9P6}`

---

## Task 4 - Version Detection

#### 1)  Name and detected version of the web server  ?

*By running the following command:*

```bash
nmap -A -p8008 10.48.157.161
```

```bash
PORT     STATE SERVICE VERSION
8008/tcp open  http    lighttpd 1.4.74
```

**Ans:** `lighttpd 1.4.74`

---

## Task 5 - Timing

#### 1) Non-numeric equivalent of `-T4`?

**Ans:** `-T aggressive`

---
## Task 6 - Output

#### 1) Option to enable debugging?

**Ans:** `-d`

---
## Task 7 - Conclusion and Summary

#### 1) Scan - Nmap uses with local user privileges?

**Ans:** `Connect Scan`
