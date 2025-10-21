---
title: "Wireshark: The Basics"
date: 2025-10-20
draft: false
tags:
  - TryHackMe
  - Wireshark
---
**Note:** The questions are shortened for a cleaner view

## Task 1 - Introduction

The answers are already provided by THM.

#### 1) File used to **simulate** the screenshots?
**Ans:** `http1.pcapng`

#### 2) File used to **answer** the questions?
**Ans:** `Exercise.pcapng`

---

## Task 2 - Tool Overview

*Looking at Statistics -> Capture File Properties*

#### 1) What is the flag?
**Ans:** `TryHackMe_Wireshark_Demo`

#### 2) Total number of packets?
**Ans:** `58620`

####  3) **SHA256 hash** value ?
**Ans:** `f446de335565fb0b0ee5e5a3266703c778b2f3dfad7efeaeccb2da5641a6d6eb`

---

## Task 3 - Packet Dissection

*Looking at the Application Data:*

#### 1) Markup Language used?
**Ans:** `eXtensible Markup Language`

#### 2) Arrival date of the packet?  
*(Answer format: Month/Day/Year)*  

*Looking at the Frame:*

**Ans:** `05/13/2004`

####  3) TTL value?

*Looking at IPv4:*

**Ans:** `47`

####  4) TCP payload size?

*Looking at Protocol:*

**Ans:** `424`

####  5) e-tag value?

*Looking at Hypertext Transfer Protocol:*

**Ans:** `9a01a-4696-7e354b00`

> *The HTTP `ETag` (entity tag) is an identifier for a specific version of a resource, used for caching efficiency and avoiding mid-air collisions.*

---

## Task 4 - Packet Navigation

#### 1) Name of artist 1?
**Ans:** `r4w8173`

#### 2) Go to packet 12. What is the answer?

*Getting the md5 sum of the image:*

**Ans:** `911cd574a42865a956ccde2d04495ebf`

####  3) Alien's name?

*Exporting Packet Bytes of Line-based text data and viewing the file we get:*

**Ans:** `PACKETMASTER`

#### 4) Number of warnings?

*Looking at Analyze -> Expert Infromation*

**Ans:** `1636`

---

## Task 5 - Packet Filtering

#### 1)  Filter query?
**Ans:** `http`

#### 2) Number of displayed packets?

*Looking at the displayed packets with the filter* `http`*

**Ans:** `1089`

#### 3) Total number of artists?

```html
<div id="content">
  <div class='story'>
    <a href='artists.php?artist=1'><h3>r4w8173</h3></a>
    <p><a href='#' onClick="window.open('./comment.php?aid=1','comment','width=500,height=400')">comment on this artist</a></p>
  </div>
  <div class='story'>
    <a href='artists.php?artist=2'><h3>Blad3</h3></a>
    <p><a href='#' onClick="window.open('./comment.php?aid=2','comment','width=500,height=400')">comment on this artist</a></p>
  </div>
  <div class='story'>
    <a href='artists.php?artist=3'><h3>lyzae</h3></a>
    <p><a href='#' onClick="window.open('./comment.php?aid=3','comment','width=500,height=400')">comment on this artist</a></p>
  </div>	
</div>
```

*We get the above code block by searching for the term* `artist`  

**Ans:** `3`

#### 4) Name of the second artist?

**Ans:** `Blad3`

----

