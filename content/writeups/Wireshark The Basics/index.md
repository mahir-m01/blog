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

#### File is used to **simulate** the screenshots?
**Ans:** `http1.pcapng`

#### File is used to **answer** the questions?
**Ans:** `Exercise.pcapng`

---

## Task 2 - Tool Overview

#### What is the flag?
**Ans:** `TryHackMe_Wireshark_Demo`

#### Total number of packets?
**Ans:** `58620`

####  **SHA256 hash** value ?
**Ans:** `f446de335565fb0b0ee5e5a3266703c778b2f3dfad7efeaeccb2da5641a6d6eb`

---

## Task 3 - Packet Dissection

#### Markup Language used?
**Ans:** `eXtensible Markup Language`

#### Arrival date of the packet?  
*(Answer format: Month/Day/Year)*  
**Ans:** `05/13/2004`

####  TTL value?
**Ans:** `47`

####  TCP payload size?
**Ans:** `424`

####  e-tag value?
**Ans:** `9a01a-4696-7e354b00`

> *The HTTP `ETag` (entity tag) is an identifier for a specific version of a resource, used for caching efficiency and avoiding mid-air collisions.*

---

## Task 4 - Packet Navigation

#### Name of artist 1?
**Ans:** `r4w8173`

#### Go to packet 12. What is the answer?
**Ans:** `911cd574a42865a956ccde2d04495ebf`

####  Alien's name?
**Ans:** `PACKETMASTER`

#### Number of warnings?
**Ans:** `1636`

---

## Task 5 - Packet Filtering

#### Filter query?
**Ans:** `http`

#### Number of displayed packets?
**Ans:** `1089`


#### Total number of artists?

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

From the above code block that we get by searching for the term `artist` we get: 

**Ans:** `3`

#### Name of the second artist?

**Ans:** `Blad3`

----

