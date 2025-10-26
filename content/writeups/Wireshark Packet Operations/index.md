---
title: "Wireshark: Packet Operations"
date: 2025-10-21
draft: false
tags:
  - TryHackMe
  - Wireshark
  - Cybersecurity
---
**Note:** The questions are shortened for a cleaner view

## Task 1 - Introduction

There's no answer needed

## Task 2 - Statistics | Summary

#### 1) IP address of the hostname starts with "bbc"?

*Statistics -> Resolved Addresses and search for `bbc`*

**Ans:** `199.232.24.81`

#### 2) Number of IPv4 conversations?

*Statistics -> Conversations*

**Ans:** `435`

#### 3) Bytes (k) transferred from the "Micro-St" MAC address?

*Statistics -> Endpoints; Name resolution -> Checked*

**Ans:** `7474`

#### 4) IP addresses linked with "Kansas City"?

*Statistics -> Endpoints*

**Ans:** `4`

#### 5) IP address  linked with "Blicnet" AS Organisation?

*Statistics -> Endpoints; Sort `AS Organisation `column*

**Ans:** `188.246.82.7`

---

## Task 3 - Statistics | Protocol Details:


#### 1) Most used IPv4 destination address?

*Statistics -> IPv4 Statistics -> All Addresses; Sort `Count` column*

**Ans:** `10.100.1.33`

> The actual answer is supposed to be `10.10.57.178 `according to statistical sorting in descending order. However THM seems to accept only the second highest.

#### 2) Max service request-response time of the DNS packets?

*Statistics -> DNS; Sort `Max val` column; Observe Service Stats -> `request-response time (secs)`*

**Ans:** `0.467897`

#### 3) HTTP Requests accomplished by "rad[.]msn[.]com?

*Statistics -> HTTP; Sort `Topic / Item` column*

**Ans:** `39`

---

## Task 4 - Packet Filtering | Principles

There's no answer needed

---

## Task 5 - Packet Filtering | Principles 

#### 1) Number of IP packets?

*Set display filter: `ip`; Observe `Displayed` at the bottom*

**Ans:** `81420`

#### 2) Packets with a "TTL value less than 10"?

*Set display filter: `1p.ttl < 10`; Observe `Displayed` at the bottom*

**Ans:** `66`

#### 3) Packets which uses "TCP port 4444"?

*Set display filter: `tcp.port == 4444`; Observe `Displayed` at the bottom*

**Ans:** `632`

#### 4) "HTTP GET" requests sent to port "80"?

*Set display filter: `http.request.method == "GET" && tcp.port == 80`; Observe `Displayed` at the bottom*

**Ans:** `527`

#### 5) Number of "type A DNS Queries"?

*Set display filter: `dns.qry.type == 1 && dns.flags.response == 1`; Observe `Displayed` at the bottom*

**Ans:** `51`

> Yes, THM did not explicitly mention that it had to be `DNS Responses`, had to figure this one out by playing around with different filters

---

## Task 6 - Advanced Filtering

#### 1) Microsoft IIS Servers. Packets not from port 80 ?

*Set display filter: `http.server matches "microsoft" && !(tcp.srcport == 80)`; Observe `Displayed` at the bottom*

**Ans:** `21`

#### 2) Microsoft IIS Servers. Packets that have "version 7.5" ?

*Set display filter: `http.server matches "microsoft" && http.server matches "7.5" `; Observe `Displayed` at the bottom*

**Ans:** `71`

#### 3) Packets that use ports 3333, 4444 or 9999?

*Set display filter: `tcp.port in {3333 4444 9999}`; Observe `Displayed` at the bottom*

**Ans:** `2235`

#### 4) Packets with "even TTL numbers"?

*Set display filter: `string(ip.ttl) matches "[02468]$"`; Observe `Displayed` at the bottom*

**Ans:** `2235`

> We use the `string` function because `ip.ttl` expects a type of `integer`

#### 5) Number of "Bad TCP Checksum" packets?

*Set display filter: `tcp.checksum.status == 0`; Observe `Displayed` at the bottom*

**Ans:** `34185`

#### 6) Number of displayed packets?

*Use the `gif/jpeg with http-200`  button *

**Ans:** `261`

---


