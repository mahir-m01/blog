---
title: MITRE
date: 2026-01-07
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - MITRE
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task 1 - Introduction

No answer needed

---
## Task 2 - ATT&CK® Framework

#### 1) What Tactic does the Hide Artifacts technique belong to in the ATT&CK Matrix?

*The matrix is available [here](https://attack.mitre.org/matrices/). I just used the search box to search for the technique and used the left column view to identify the Tactic.*

**Ans:** `Defense Evasion`

#### 2) Which ID is associated with the Create Account technique?

*Search for the `Create Account` Technique.*

**Ans:** `T1136`

---
## Task 3 - ATT&CK in Operation

#### 1) In which country is Mustang Panda based?

*A simple google search should suffice.*

**Ans:** `China`

#### 2) Which ATT&CK technique ID maps to Mustang Panda’s Reconnaissance tactics?

*Since they primarily use `Phishing` , I looked at the `Phishing for Information ` tactic*

**Ans:** `T1598`

#### 3) Which software is Mustang Panda known to use for Access Token Manipulation?

*This is hard to find through the navigator so I ended up searching for it [here]([)](https://attack.mitre.org/groups/G0129/)*

**Ans:** `Cobalt Strike`

---
## Task 4 - ATT&CK for Threat Intelligence

#### 1) Which APT group has targeted the aviation sector...?

*I searched for `aviation` on the webpage.*

**Ans:** `APT33`

#### 2) Which ATT&CK sub-technique used by this group is a key area of concern...?

*I clicked on the group to find more details and searched for `365`*

**Ans:** `Cloud Accounts`

#### 3) According to ATT&CK, what tool is linked to the APT group...?

**Ans:** `Ruler`

#### 4) Which mitigation strategy advises removing inactive or unused accounts to...?

*I clicked on `Cloud Accounts` for the detailed view and headed over to `Mitigation Techniques`.*

**Ans:** `User Account Management`

#### 5) What Detection Strategy ID would you implement to detect abused...?

*I looked at the `Detection Strategies` for `Cloud Accounts`.*

**Ans:** `DET0546`

---
## Task 5 - Cyber Analytics Repository (CAR)

#### 1) Which ATT&CK Tactic is associated with [CAR-2019-07-001](https://car.mitre.org/analytics/CAR-2019-07-001/)?

*This is under  the `Tactics(s)` field.*

**Ans:** `Defense Evasion`

#### 2) What is the Analytic Type for Access Permission Modification?

*This is available in the small information box on the top-right.*

**Ans:** `Situational Awareness`

---
## Task 6 - MITRE D3FEND Framework

#### 1) Which sub-technique of [User Behavior Analysis](https://d3fend.mitre.org/technique/d3f:UserBehaviorAnalysis/) would you use to analyze...?

*Searching for `geolocation` highlights the sub-tactic* 

**Ans:** `User Geolocation Logon Pattern Analysis`

#### 2) Which digital artifact does this sub-technique rely on analyzing?

*I checked the `Artifact Relationships` section.*

**Ans:** `Network Traffic`

---
## Task 7 - Other MITRE Projects

*Its on the right of the webpage where there is an overview of the techniques.* 

#### 1) What technique ID is associated with [Scrape Blockchain Data](https://aadapt.mitre.org/techniques/ADT3025)...?

**Ans:** `ADT3025`

#### 2) Which tactic does [LLM Prompt Obfuscation](https://atlas.mitre.org/techniques/AML.T0068) belong...?

**Ans:** `Defense Evasion`

---



