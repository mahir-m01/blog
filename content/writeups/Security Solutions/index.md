---
title: Security Solution Module
date: 2025-11-18
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - Defense
  - Vulnerability
---
**Note:** 

- This is a combined writeup for the Security Solutions Module.
- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.


# Introduction to SIEM


## Task  1 - Introduction
#### 1) What does SIEM stand for?

**Ans:** `Security Information and Event Management system`

---
## Task  2 - Logs Everywhere, Answers Nowhere

#### 1) Is Registry-related activity host-centric or network-centric?

**Ans:** `host-centric`

#### 2) Is VPN-related activity host-centric or network-centric?

**Ans:** `network-centric`

---
## Task  3 - Why SIEM

No answer needed.

---
## Task  4 -  Log Sources and Ingestion

#### 1) In which location within a Linux environment are HTTP logs stored?

**Ans:** `/var/log/httpd`

#### 2) Is VPN-related activity host-centric or network-centric?

**Ans:** `network-centric`

---
## Task  5 -  Alerting Process and Analysis

#### 1) Which Event ID is generated when event logs are removed?

**Ans:** `104`

#### 2) What type of alert may require tuning?

**Ans:** `False Positive`

---
## Task  6 -  Lab Work

In the static lab attached, a sample dashboard and events are displayed. When a suspicious activity happens, an Alert is triggered, which means some events match the condition of some rule already configured. Complete the lab and answer the following questions.

#### 1) After clicking on the *Start Suspicious Activity button*...?

*After clicking on the button we get an alert for a potential `crypto miner`.*

**Ans:** `cudominer.exe`

#### 2) Find the event that caused the alert and...?

*Looking through the events list we can see that its id is `0xd21aef` and the user `chris` initiated it.*

**Ans:** `chris`

#### 3) What is the hostname of the suspect user?

*Observe the `HostName` field*

**Ans:** `HR_02`

#### 4) Examine the rule and the suspicious process...?

*Analysing the rule gives us the following and we can tell it got flagged because of the `miner` term.*

`Alert "Potential CryptoMiner Activity" If EventID = 4688 AND Log_Source = WindowsEventLogs AND ProcessName = (*miner* OR *crypt*)`

**Ans:** `miner`

#### 4) Which option best represents the event?

*This is a serious event and can cause damage and cannot be ignored, hence it is a `True Positive`.*

**Ans:** `True Positive`

#### 5) Selecting the right ACTION will display the FLAG. What is the FLAG?

**Ans:** `THM{000_SIEM_INTRO}`

---
# Firewall Fundamentals


## Task  1 - What Is the Purpose of a Firewall

#### 1) Which security solution inspects the incoming...?

**Ans:** `Firewall`

---
## Task  2 - Types of Firewalls

#### 1) Which type of firewall maintains the state of connections?

**Ans:** `stateful firewall`

#### 2) Which type of firewall offers heuristic analysis for the traffic?

**Ans:** `next-generation firewall`

#### 3) Which type of firewall inspects the traffic coming to an application?

**Ans:** `proxy firewall`

---
## Task  3 - Rules in Firewalls

#### 1) Which type of action should be defined in a rule to permit any traffic?

**Ans:** `allow`

#### 2) What is the direction of the rule that is created for the traffic leaving our network?

**Ans:** `outbound`

---
## Task  4 - Windows Defender Firewall

#### 1) What is the name of the rule that was created to...?

*Open `Windows Defender Firewall with Advanced Security` on the windows machine and head over to the `Inbound Rules` tab.*

*You can check for `Block` actions, I ended up clicking on the `Action` field to sort it. Look for port `22` as that is the `SSH` port.*

**Ans:** `Core Op`

#### 2) A rule was created to allow SSH from one single IP address...?

*Again you could sort the `Action` and the`Local Port` fields or just filter for it. The allowed `Remote Address` is `192.168.13.7`*

**Ans:** `Infra team`

#### 3) Which IP address is allowed under this rule?

*This was already found as a part of question 2.*

**Ans:** `192.168.13.7`

---
## Task  5 - Linux iptables Firewall

#### 1) Which Linux firewall utility is considered to be the successor of "iptables"?

**Ans:** `nftables`

#### 2) What rule would you issue with ufw to deny all..? 

**Ans:** `ufw default deny outgoing`

---
# IDS Fundamentals

## Task  1 - What is an IDS

#### 1) Can an intrusion detection system (IDS) prevent...?

**Ans:** `Nay`

#### 2) What rule would you issue with ufw to deny all..? 

**Ans:** `ufw default deny outgoing`

---
## Task  2 - Types of IDS

#### 1) Which type of IDS is deployed to detect threats throughout the network?

**Ans:** `Network Intrusion Detection System`

#### 2) Which IDS leverages both signature-based...?

**Ans:** `Hybrid IDS`

---
## Task  3 - IDS Example: Snort

#### 1) Which mode of Snort helps us to log the network traffic in a PCAP file?

**Ans:** `Packet Logging Mode`

#### 2) What is the primary mode of Snort called?

**Ans:** `Network Intrusion Detection System Mode`

---
## Task  4 - Snort Usage

#### 1) Where is the main directory of Snort that stores its files?

**Ans:** `/etc/snort`

#### 2) Which field in the Snort rule indicates the revision number of the rule?

**Ans:** `rev`

#### 3) Which protocol is defined in the sample rule created in the task?

**Ans:** `icmp`

#### 4) What is the file name that contains custom rules for Snort?

**Ans:** `local.rules`

---
## Task  5 - Practical Lab

#### 1) What is the IP address of the machine that tried to...?

*Run the following command (ensure you are in the right directory):*

```bash
sudo snort -q -l /var/log/snort -r Intro_to_IDS.pcap -A console -c /etc/snort/snort.conf | grep "SSH"
```

```bash
07/18-12:52:59.337559  [**] [1:1000002:1] SSH Connection Detected [**] [Priority: 0] {TCP} 10.11.90.211:54334 -> 10.10.161.151:22
```

*I've also mentioned what each parameter does:*

|                            |                          |                                                                 |
| -------------------------- | ------------------------ | --------------------------------------------------------------- |
| `-q`                       | quiet mode               | Hides banner + startup info (clean output)                      |
| `-r Intro_to_IDS.pcap`     | read PCAP file           | Tells Snort to read packets from a PCAP instead of live network |
| `-l /var/log/snort`        | log directory            | Where Snort should save logs / alerts                           |
| `-A console`               | output alerts to console | Prints alerts directly on the screen                            |
| `-c /etc/snort/snort.conf` | configuration file       | Uses your Snort rules + settings from this file                 |


**Ans:** `10.11.90.211`

#### 2) What other rule message besides the SSH message...?

*Run the following command (ensure you are in the right directory):*

```bash
sudo snort -q -l /var/log/snort -r Intro_to_IDS.pcap -A console -c /etc/snort/snort.conf | grep -v "SSH"
```

```bash
07/18-12:53:16.954348  [**] [1:1000001:1] Ping Detected [**] [Priority: 0] {ICMP} 10.11.90.211 -> 10.10.161.151
07/18-12:53:17.956812  [**] [1:1000001:1] Ping Detected [**] [Priority: 0] {ICMP} 10.11.90.211 -> 10.10.161.151
07/18-12:53:18.972925  [**] [1:1000001:1] Ping Detected [**] [Priority: 0] {ICMP} 10.11.90.211 -> 10.10.161.151
```

**Ans:** `rev`

#### 3) What is the sid of the rule that detects SSH?

*Run the following command (ensure you are in the right directory):*

```bash 
sudo cat rules/local.rules
```

```bash
# $Id: local.rules,v 1.11 2004/07/23 20:15:44 bmc Exp $
# ----------------
# LOCAL RULES
# ----------------
# This file intentionally does not come with signatures.  Put your local
# additions here.
alert icmp any any -> $HOME_NET any (msg:"Ping Detected"; sid:1000001; rev:1;)
alert tcp any any -> $HOME_NET 22 (msg:"SSH Connection Detected"; sid:1000002; rev:1;)
```

**Ans:** `1000002`

---
# Vulnerability Scanner Overview

## Task  1 - What Are Vulnerabilities?

#### 1) What is the process of fixing the vulnerabilities called?

**Ans:** `Patching`

---
## Task  2 - Vulnerability Scanning

#### 1) Which type of vulnerability scans require the credentials of the target host?

**Ans:** `Authenticated`

#### 2) Which type of vulnerability scan focuses on identifying the vulnerabilities...?

**Ans:** `External`

---
## Task  3 - Tools for Vulnerability Scanning

#### 1) Is Nessus currently an open-source vulnerability scanner? (Yea/Nay)

**Ans:** `Nay`

#### 2) Which company developed the Nexpose vulnerability scanner?

**Ans:** `Rapid7`

#### 3) What is the name of the open-source vulnerability...?

**Ans:** `Openvas`

---
## Task  4 - CVE & CVSS

#### 1) CVE stands for?

**Ans:** `Common Vulnerabilities and Exposures`

#### 2) Which organization developed CVE?

**Ans:** `MITRE Corporation`

#### 3) What would be the severity level of the vulnerability with a score of 5.3?

**Ans:** `Medium`

---
## Task  5 - OpenVAS

*The answeres to these questions can be found in the images given in the task.*

#### 1) What is the IP address of the machine scanned in this task?

**Ans:** `10.10.154.44`

#### 2) How many vulnerabilities were discovered on this host?

**Ans:** `13`

---
## Task  6 - Practical Exercise 

#### 1) What is the score of the single high-severity vulnerability found in the scan?

*Open the report file.*

```
High (CVSS: 10.0)
NVT: OpenVAS / Greenbone Vulnerability Manager Default Credentials (OID: 1.3.6.1.4.1.25623.1.0.108554) 
```

**Ans:** `10`

#### 2) What is the solution suggested by OpenVAS for this vulnerability?

```
Solution
Solution type: Workaround
Change the password of the mentioned account(s).
```

**Ans:** `Change the password of the mentioned account(s).`

---

