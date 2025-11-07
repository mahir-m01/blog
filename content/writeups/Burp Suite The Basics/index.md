---
title: "Burp Suite: The Basics"
date: 2025-11-07
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - BurpSuite
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task  1 - Introduction

No answer needed

---
## Task  2 - What is Burp Suite

#### 1) Which edition of Burp Suite runs on a server...?

**Ans:** `burp suite enterprise`

#### 2) Burp Suite is frequently used when attacking...?

**Ans:** `mobile`

---
## Task  3 - Features of Burp Community

#### 1) Which Burp Suite feature allows us to intercept...?

**Ans:** `Proxy`

#### 2) Which Burp tool would we use to brute-force a login form?

**Ans:** `Intruder`

---
## Task  4 - Installation

No answer needed

---
## Task  5 - The Dashboard

#### 1) What menu provides information about the actions performed...?

**Ans:** `Event log`

> The Event log provides information about the actions performed by Burp Suite, such as starting the proxy, as well as details about connections made through Burp.

---
## Task  6 - Navigation

#### 1) Which tab **Ctrl + Shift + P** will switch us to?

**Ans:** `Proxy tab`

---
## Task  7 - Options

#### 1) In which category can you find a reference to a "Cookie jar"?

*Search for `Cookie Jar` in the search bar under the `Settings` menu.*

**Ans:** `Sessions`

#### 2) In which base category can you find the "Updates"...?

*Search for `Updates` in the search bar under the `Settings` menu.*

**Ans:** `Suite`

#### 3) What is the name of the sub-category which allows...?

*Search for `key` in the search bar under the `Settings` menu.*

**Ans:** `Hotkeys`

#### 4) If we have uploaded Client-Side TLS certificates...?

**Ans:** `yea`

> Project settings are specific to the current project and apply only during the session.

---
## Task  8 

No answer needed

---
## Task 9 Connecting through the Proxy (FoxyProxy)

No answer needed

*Upon intercepting traffic for `10.49.146.170` we get*

```http
GET / HTTP/1.1
Host: 10.49.146.170
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Priority: u=0, i
```

---
## Task  10 - Site Map and Issue Definitions 

#### 1) What is the flag you receive after visiting the unusual endpoint?

*The general procedure is to go ahead and visit every link you can find so as to let the tool scrape as many endpoints as possible.*

*Upon close inspection, it seems that the browser makes a `GET` request to `http://10.49.146.170/5yjR2GLcoGoij2ZK` when the `/ticket` endpoint is visited.*

*The `Target` view will show this once you intercept the endpoint.*

`http://10.49.146.170/5yjR2GLcoGoij2ZK`

*Visiting the endpoint should give you the flag.*

**Ans:** `THM{NmNlZTliNGE1MWU1ZTQzMzgzNmFiNWVk}`

Further tasks do not require any answers.

---
