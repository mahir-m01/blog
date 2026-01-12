---
title: Secure Network Architecture
date: 2026-01-08
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - Networking
---
**Note:** 
- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

# Secure Network Architecture

## Task 1 - Introduction

No answer needed

---
## Task 2 - Network Segmentation 

#### 1) How many trunks are present in this configuration?

```bash
/ # ovs-vsctl show
87c2a3ee-5374-435a-81c2-e8aafa96e3b9
    Bridge br2
        datapath_type: netdev
        Port br2
            Interface br2
                type: internal
    Bridge br1
        datapath_type: netdev
        Port br1
            Interface br1
                type: internal
    Bridge br0
        datapath_type: netdev
        Port eth9
            tag: 30
            Interface eth9
        Port br0
            Interface br0
                type: internal
        Port eth13
            tag: 30
            Interface eth13
        Port eth14
            tag: 30
            Interface eth14
        Port eth15
            tag: 30
            Interface eth15
        Port eth2
            tag: 10
            Interface eth2
        Port eth8
            tag: 30
            Interface eth8
        Port eth3
            tag: 20
            Interface eth3
        Port eth7
            tag: 30
            Interface eth7
        Port eth4
            tag: 20
            Interface eth4
        Port eth10
            tag: 30
            Interface eth10
        Port eth5
            tag: 20
            Interface eth5
        Port eth6
            tag: 30
            Interface eth6
        Port eth12
            tag: 30
            Interface eth12
        Port eth0
            Interface eth0
        Port eth11
            tag: 30
            Interface eth11
        Port eth1
            tag: 10
            Interface eth1
    Bridge br3
        datapath_type: netdev
        Port br3
            Interface br3
                type: internal
```

*Since there are 4 bridges there are 4 trunks.*

**Ans:**  `4`

#### 2) What is the VLAN tag ID for interface eth12?

```bash
Port eth12
            tag: 30
            Interface eth12
```

**Ans:**  `30`

---
## Task 3 - Common Secure Network Architecture

#### 1) From the above table, what zone would a user connecting to a public web server be in?

**Ans:**  `External`

#### 2) From the above table, what zone would a public web server be in?

**Ans:**  `DMZ`
#### 3) From the above table, what zone would a core domain controller be placed in?

**Ans:**  `Restricted`

---
## Task 4 - Network Security Policies and Controls

#### 1) According to the corresponding ACL policy, will the first packet result in a drop or accept?

*The packet is valid and should be accepted.*

**Ans:**  `External`

#### 2) According to the corresponding ACL policy, will the second packet result in a drop or accept?

```bash
 Destination Port: 2
```

*This is an invalid port and hence it will be dropped.*

**Ans:**  `drop`

---
## Task 5 - Zone-Pair Policies and Filtering

#### 1) What is the flag found after filling in all blanks on the static site?

*Here is the rules table:*

| Command Scope | Zone / Firewall Name | Parameter         | Value   |
| ------------- | -------------------- | ----------------- | ------- |
| zone-policy   | DMZ                  | default-action    | drop    |
| zone-policy   | DMZ                  | interface         | Eth0.10 |
| zone-policy   | LAN                  | default-action    | drop    |
| zone-policy   | LAN                  | interface         | Eth0.20 |
| firewall      | dmz-lan              | description       | dmz-lan |
| firewall      | dmz-lan              | default-action    | drop    |
| firewall      | dmz-lan              | rule 100 action   | accept  |
| firewall      | dmz-lan              | rule 100 protocol | http    |

**Ans:**  `THM{M05tly_53cure}`

---
## Task 6 - Validating Network Traffic

>SSL/TLS inspection uses an **SSL proxy** to intercept protocols, including HTTP, POP3, SMTP, or other SSL/TLS encrypted traffic. Once intercepted, the proxy will decrypt the traffic and send it to be processed by a **UTM** (**U**nified **T**hreat **M**anagement) platform. UTM solutions will employ deep SSL inspection, feeding the decrypted traffic from the proxy into other UTM services, including but not limited to web filters or **IPS** (**I**ntrusion **P**revention **S**ystem), to process the information.

#### 1) Does SSL inspection require a man-in-the-middle proxy? (Y/N)

**Ans:**  `Y`

#### 2) What platform processes data sent from an SSL proxy?

**Ans:**  `Unified Threat Management `

---
## Task 7 - Addressing Common Attacks

#### 1) Where does DHCP snooping store leased IP addresses from untrusted hosts?

>The switch will store untrusted hosts with leased IP addresses in a **DHCP Binding Database**.

**Ans:**  `DHCP Binding Database`

#### 2) Will a switch drop or accept a DHCPRELEASE packet?

Below is a list of conditions the protocol will inspect to determine if a DHCP packet should be dropped.

- Any DHCP packet is received from outside of the network.
- The source MAC address and DHCP client hardware address do not match.
- A `DHCPRELEASE` or `DHCPDECLINE` packet is received on an untrusted interface that does not match an interface that the source address already has registered.
- A DHCP packet that includes a relay agent address that is not `0.0.0.0`

**Ans:**  `drop`

#### 3) Does dynamic ARP inspection use the DHCP binding database? (Y/N)

**Ans:**  `Y`

#### 4) Dynamic ARP inspection will match an IP address and what other packet detail?

**Ans:**  `MAC Address`

---


