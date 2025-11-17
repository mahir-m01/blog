---
title: Defensive Security
date: 2025-11-17
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - Defense
---
**Note:** 

- This is a combined writeup for the Defensive Security module.
- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.


# Defensive Security Intro


## Task  1 - Introduction to Defensive Security

No answer needed

---
## Task  2 - Areas of Defensive Security

#### 1) What would you call a team of cyber security...?

**Ans:** `Security Operations Center`

#### 2) What does DFIR stand for?

**Ans:** `Digital Forensics and Incident Response`

#### 3) Which kind of malware requires the user to...?

**Ans:** `ransomeware`


---
## Task  3 - Practical Example of Defensive Security

#### 1) What is the flag that you obtained by following along?

*The malicious IP obtained from the is:*

`143.110.250.149`

*Now, we'll escalate it to the `SOC Team Lead`*

*Following that, we'll add the IP address to the firewall's black list*

**Ans:** `THM{THREAT-BLOCKED}`

---
# SOC Fundamentals 


## Task  1 - Introduction to SOC

#### 1) What does the term SOC stand for?

**Ans:** `Security Operations Center`

---
## Task  2 - Purpose and Components

#### 1) The SOC team discovers an unauthorized user is...?

**Ans:** `Detection`

#### 2) What are the three pillars of a SOC?

**Ans:** `People, Process, Technology`

---
## Task  3 - People

#### 1) Alert triage and reporting is the responsibility of?

**Ans:** `SOC Analyst (Level 1)`

#### 2) Which role in the SOC team allows you to work dedicatedly...?

**Ans:** `Detection Engineer`

---
## Task  4 - Process

#### 1) At the end of the investigation, the SOC team found...?

**Ans:** `Who`

#### 2) The SOC team detected a large amount of data exfiltration...?

**Ans:** `What`

---
## Task  5 - Technology

#### 1) Which security solution monitors the incoming...?

**Ans:** `Firewall`

#### 2) Do SIEM solutions primarily focus on detecting..?

**Ans:** `yea`

---
## Task  6 - Practical Exercise of SOC

### Scenario

You are the Level 1 Analyst of your organization’s SOC team. You receive an alert that a port scanning activity has been observed on one of the hosts in the network. You have access to the SIEM solution, where you can see all the associated logs for this alert. You are tasked to view the logs individually and answer the question to the 5 Ws given below.

#### 1) What: Activity that triggered the alert?

*From the scenario we know that it was a port scan.*

**Ans:** `Port Scan`

#### 2) When: Time of the activity?

*Looking at the latest SIEM alert we can find the time.*

**Ans:** `June 12, 2024 17:24`

#### 3) Where: Destination host IP?

*Acknowledge the alert and open it to view more details. Observe the `Destination IP` column.*

**Ans:** `10.0.0.3`

#### 4) Who: Source host name?

*Observe the `Source Host Name` column.*

**Ans:** `Nessus`

#### 5) Why: Reason for the activity? Intended/Malicious

*Based on the data, this activity looks normal and is therefore intended.*

**Ans:** `Intended`

#### 6) Additional Investigation Notes: Has any response been sent...?

*Yes, this was flagged as a `False Positive`*

**Ans:** `yea`

#### 7) What is the flag found after closing the alert?

*Close the alert and you should see the flag.*

**Ans:** `THM{000_INTRO_TO_SOC}`

---
# Digital Forensics Fundamentals 


## Task  1 - Introduction to Digital Forensics

#### 1) Which team was handed the case by law enforcement?

**Ans:** `digital forensics`

---
## Task  2 - Digital Forensics Methodology

#### 1) Which phase of digital forensics is concerned with correlating...?

**Ans:** `Analysis`

#### 2) Which phase of digital forensics is concerned with extracting...?

**Ans:** `Examination`

---
## Task  3 - Evidence Acquisition

#### 1) Which tool is used to ensure data integrity during the collection?

**Ans:** `write blocker`

#### 2) What is the name of the document that has all...?

**Ans:** `chain of custody`

---
## Task  4 - Windows Forensics

#### 1) Which type of forensic image is taken to...?

**Ans:** `Memory Image`

---
## Task  5 - Practical Example of Digital Forensics

#### 1) Using `pdfinfo`, find out the author of the attached PDF file, `ransom-letter.pdf`.

*Ensure you are in the right room's directory and then run the following command: (I am using the Attack Box)*


```bash
pdfinfo ransom-letter.pdf
```


```bash
Title:          Pay NOW
Subject:        We Have Gato
Author:         Ann Gree Shepherd
Creator:        Microsoft® Word 2016
Producer:       Microsoft® Word 2016
CreationDate:   Wed Feb 23 09:10:36 2022 GMT
ModDate:        Wed Feb 23 09:10:36 2022 GMT
Tagged:         yes
UserProperties: no
Suspects:       no
Form:           none
JavaScript:     no
Pages:          1
Encrypted:      no
Page size:      595.44 x 842.04 pts (A4)
Page rot:       0
File size:      71371 bytes
Optimized:      no
PDF version:    1.7

```

**Ans:** `Ann Gree Shepherd`

#### 2) Using `exiftool` or any similar tool, try to find where the kidnappers...?

*Run the following command:*

```bash 
exiftool letter-image.jpg
```

```
GPS Latitude                    : 51 deg 30' 51.90" N
GPS Longitude                   : 0 deg 5' 38.73" W
Date/Time Created               : 2022:02:15 17:23:40-17:23
Digital Creation Date/Time      : 2021:11:05 14:06:13+03:00
Circle Of Confusion             : 0.043 mm
Depth Of Field                  : 0.06 m (0.76 - 0.82 m)
Field Of View                   : 54.9 deg
Focal Length                    : 50.0 mm (35 mm equivalent: 34.6 mm)
GPS Position                    : 51 deg 30' 51.90" N, 0 deg 5' 38.73" W
Hyperfocal Distance             : 20.58 m
Light Value                     : 7.9
Lens ID                         : Canon EF 50mm f/1.8 STM
```

*Converting the GPS location to the right format:*

`51°30'51.9"N, 0°05'38.7"W`

*Using Google Maps; the street associated with the coordinates was `Milk Street`.*

**Ans:** `Milk Street`

#### 3) What is the model name of the camera used to take this photo?

*Since the output is too large, let's use `grep`:*

```bash
exiftool letter-image.jpg | grep -i "model"
```

```bash
Camera Model Name               : Canon EOS R6
Lens Model                      : EF50mm f/1.8 STM
Device Model                    : 
Device Model Desc               : sRGB
```

**Ans:** `Canon EOS R6`

---
# Incident Response Fundamentals 


## Task  1 - Introduction to Incident Response

No answer needed

---
## Task  2 - What are Incidents ? 

#### 1) What is triggered after an event or group of events...?

**Ans:** `Alert`

#### 2) If a security solution correctly identifies a harmful activity..?

**Ans:** `True Positive`

#### 3) If a fire alarm is triggered by smoke after cooking, is it...?

**Ans:** `False Positive`

---
## Task  3 - Types of Incidents

#### 1) A user's system got compromised after downloading a file...?

**Ans:** `malware infection`

#### 2) What type of incident aims to disrupt the availability of an application?

**Ans:** `Denial of service`

---
## Task  4 - Incident Response Process

#### 1) The Security team disables a machine's internet...?

**Ans:** `containment`

#### 2) Which phase of NIST corresponds with the lessons...?

**Ans:** `Post Incident Activity`

---
## Task  5 - Incident Response Techniques

#### 1) Step-by-step comprehensive guidelines for incident response are known as?

**Ans:** `Playbooks`

---
## Task 6 - Lab Work Incident 

**Scenario:** In this task, you will initiate an incident by downloading an attachment from a phishing email. The attachment is malware. Once you download the file, an incident begins. You will now start investigating the incident. The first phase is to see how many hosts are infected with this same file, as there are many chances that a single phishing campaign targets multiple employees within the same organization. You will see some hosts on which this file was executed after getting downloaded and some hosts on which this file was only downloaded. You will perform the necessary actions on all these hosts and see a detailed timeline of events in the infected host.

#### 1) What was the name of the malicious email sender?

*The so-called payslip instructions from Jeff Johnson got flagged as malware.*

**Ans:** `Jeff Johnson`

#### 2) What was the threat vector?

**Ans:** `Email Attachment`

#### 3) How many devices downloaded the email attachment?

*Observe the dashboard. There appears to be 3 devices that dowloaded the attachment.*

**Ans:** `3`

#### 4) How many devices executed the file?

*Observe the dashboard. There appears to be 1 device that executed the file.*

**Ans:** `3`

#### 5) What is the flag found at the end of the exercise?

*Continue the Incident Response and finish the task.*

**Ans:** `THM{My_First_Incident_Response}`

---
# Logs Fundamentals


## Task  1 - Introduction to Incident Response

#### 1) Where can we find the majority of attack traces in a digital system?

**Ans:** `Logs`

---
## Task  2 - What are Incidents ? 

#### 1) Which type of logs contain information regarding the incoming...?

**Ans:** `Network Logs`

#### 2) Which type of logs contain the authentication and authorization events?

**Ans:** `Security Logs`

---
## Task  3 - Windows Event Logs Analysis

#### 1) What is the name of the last user account created on this system?

*Open `Event Viewer` -> `Windows Logs` -> `Security` and filter by Event ID `4720`.*

*Then, open the first event and head over to the `Details` tab and notice the `TargetUserName` field*

**Ans:** `hacked`

#### 2) Which user account created the above account?

*Notice the `SubjectUserName` field*

**Ans:** `Administrator`

#### 3) On what date was this user account enabled? Format: M/D/YYYY

*Filter by Event ID `4722` and verifying that this was indeed the  `Hacked` user account we can note down the date.*

**Ans:** `6/7/2024`

#### 4) Did this account undergo a password reset as well? Format: Yes/No

*Filter by Event ID `4724` and verifying that this was indeed the  `Hacked` user account we can verify that it underwent a password reset.*

**Ans:** `Yes`

---
## Task  4 - Web Server Access Logs Analysis

#### 1) What is the IP which made the last GET request to URL: “/contact”?

*Ensure you are in the right directory (I'm using the Attack Box), and run the following command:*

```bash
grep "GET /contact" access.log
```

```bash
10.0.0.1 - - [06/Jun/2024:13:54:44] "GET /contact HTTP/1.1" 500 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
```

**Ans:** `10.0.0.1`

#### 2) When was the last POST request made by IP: “172.16.0.1”?

*Run the following command:*

```bash
grep "POST /contact" access.log
```

```bash
172.16.0.1 - - [06/Jun/2024:13:55:44] "POST /contact HTTP/1.1" 500 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
```

**Ans:** `06/Jun/2024:13:55:44`

#### 3) Based on the answer from question number 2...?

**Ans:** `/contact`

---

