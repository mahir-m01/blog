---
title: "Tcpdump: The Basics"
date: 2025-10-24
draft: false
tags:
  -
---

**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task  1 - Introduction

#### 1) Library that is associated with `tcpdump`?

**Ans:** `libpcap`

---

## Task  2 - Basic Packet Capture

#### 1) Display addresses only in numeric format?

**Ans:** `-n`

---

## Task  3 - Filtering Expressions

#### 1) How many packets in `traffic.pcap` use ICMP ?

*By running the following command in the terminal:*

```bash
tcpdump -r traffic.pcap icmp -n | wc
```

```bash
26 358 2722
```

*We are interested in the first number* 

**Ans:** `26`

#### 2) IP address of the host that asked for... ?

*We can find the ip by filtering for arp and the specific dest address*

```bash
tcpdump -r traffic.pcap arp and dst 192.168.124.137
```

```bash
reading from file traffic.pcap, link-type EN10MB (Ethernet) 07:18:29.940761 ARP, Request who-has ip-192-168-124-137.ap-south-1.compute.internal tell ip-192-168-124-148.ap-south-1.compute.internal, length 28
```

**Ans:** `192.168.124.148`

#### 3) What hostname appears in the first DNS query?

*Filtering for only dns packets:* 

```bash
tcpdump -r traffic.pcap udp port 53
```

```bash
reading from file traffic.pcap, link-type EN10MB (Ethernet) 07:18:24.058626 IP ip-192-168-124-137.ap-south-1.compute.internal.33672 > ip-192-168-124-1.ap-south-1.compute.internal.domain: 39913+ A? mirrors.rockylinux.org. (40)
```

**Ans:** `mirrors.rockylinux.org`

---

## Task 4 - Advanced Filtering

#### 1) Packets with only TCP Reset (RST) flag set?

*By filtering for reset flag and piping it to wc*

```bash
tcpdump -r traffic.pcap "tcp[tcpflags] == tcp-rst" -n | wc
```

```bash
57 741 5975
```

**Ans:** `57`

#### 2) IP that sent packets larger than 15000 bytes?

*We can filter for greater than 1500 bytes with domain mapping disabled*

```bash
tcpdump -r traffic.pcap greater 15000 -n
```

```bash
reading from file traffic.pcap, link-type EN10MB (Ethernet) 07:18:24.967023 IP 185.117.80.53.80 > 192.168.124.137.60518: Flags [.], seq 2140876081:2140896901, ack 74199.], 1605, win 235, options [nop,nop,TS val 2226566282 ecr 3054280184], length 20820: HTTP
```

**Ans:** `185.117.80.53`

---

## Task 5 - Displaying Packets

#### 1) MAC address of the host that sent an ARP request?

*We can filter for arp and give the appropriate option to show MAC addresses*

```bash
tcpdump -r traffic.pcap arp -e
```

```bash
reading from file traffic.pcap, link-type EN10MB (Ethernet).],07:18:29.940761 52:54:00:7c:d3:5b (oui Unknown) > Broadcast, ethertype ARP (0x0806), length 42: Request who-has ip-192-168-124-137.ap-south-1.compute.internal tell ip-192-168-124-148.ap-south-1.compute.internal, leng.], th 28
```

**Ans:** `52:54:00:7c:d3:5b`

---
