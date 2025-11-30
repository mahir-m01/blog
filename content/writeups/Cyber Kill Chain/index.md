---
title: Cyber Kill Chain
date: 2025-11-30
draft: false
tags:
  - Cybersecurity
  - TryHackMe
  - Framework
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task 1 - Introduction

#### 1) How many phases comprise the Cyber Kill Chain?

1. **Reconnaissance**: In the first stage, the attacker gathers information about the target
2. **Weaponisation**: Once proper reconnaissance is conducted, the attacker creates a deliverable payload or modifies an existing one based on the target system’s vulnerabilities
3. **Delivery**: Once ready, the attacker sends the weaponised payload to the target
4. **Exploitation**: Once executed, the payload exploits a vulnerability in the target’s system
5. **Installation**: The exploitation enables the attacker to install a backdoor or malware to maintain persistence in the target’s environment
6. **Command & Control (C2)**: Using the installed backdoor, the attacker can control the compromised system
7. **Actions on Objectives**: Reaching this far, the attacker can now carry out further actions such as data exfiltration or other systems’ exploitation

**Ans:** `7`

---
## Task  2 - Reconnaissance 

#### 1) What is the term for using search engines to reveal sensitive information...?

**Ans:** `Google Dorking`

#### 2) What type of reconnaissance is it where the attacker checks...?

*When carrying out **passive reconnaissance**, the attacker performs their activities without making any “noise,” for example, using open-source intelligence (OSINT).*

**Ans:** `passive reconnaissance`


---
## Task  3 - Weaponisation

#### 1) What technique is mentioned to evade detection by making it...?

**Ans:** `Obfuscation`
#### 2) What built-in feature makes creating a malicious MS Office document possible?

*A macro executes a saved set of instructions when the document is opened.*

**Ans:** `Macro`

---
## Task  4 - Delivery

#### 1) What method involves showing advertisements on legitimate websites...?

**Ans:** `Malvertising`

#### 2) What phishing attack sends text messages with malicious links...?

**Ans:** `Smishing`

- **Malvertising**: The attackers show advertisements on legitimate websites to redirect users to the malicious page.
- **SMS Phishing (Smishing)**: The attacker sends text messages with malicious links or instructions to download malware.

---
## Task  5 - Exploitation

#### 1) What type of exploit is used before the vendor...?

*Sometimes, an exploit is made available before the vendor becomes aware that a vulnerability exists in their product; in this case, it is called a zero-day exploit.*

**Ans:** `Zero-day exploit`

#### 2) What technology is mentioned to prevent an attacker...?

**Ans:** `MFA`

---
## Task  6 - Installation

#### 1) What tactic allows attackers to execute operating system commands...?

**Ans:** `web shell`

- A web shell is a small script written in a programming language that is supported by the exploited server; it allows the attacker to execute operating system commands on the target via a web browser interface.

#### 2) What technique is mentioned to prevent the execution of unauthorised...?

**Ans:** `allowlisting`

---
## Task  7 - Command and Control (C2)

#### 1) What is the name of the tactic where data is hidden within DNS queries?

**Ans:** `DNS tunnelling`
#### 2) What protocol would the attacker use to smuggle his data as encrypted web traffic?

**Ans:** `HTTPS`

---
## Task  8 - Action on Objectives

#### 1) What is the term for stealing sensitive files from a target network?

**Ans:** `Data Exfiltration`

#### 2) What principle limits who can access sensitive systems and...?

**Ans:** `principle of least privilege`

#### 3) What type of attack involves encrypting files and demanding payment...?

**Ans:** `ransomeware`


---
## Task  9  - Conclusion

#### 1) What is the flag after you complete the static site?

*Since this is randomized, I can't show all the possible questions. Just follow what you have learnt in the room to finish this task.*

**Ans:** `THM{CKC_NJHERDX327}`

---
