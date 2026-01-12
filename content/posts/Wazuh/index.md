---
title: Installing Wazuh on Proxmox
date: 2026-01-11
draft: false
tags:
  - Proxmox
  - Cybersecurity
  - Wazuh
---
# Installing Wazuh on Proxmox

This is a personal documentation and guide to install Wazuh on Proxmox and is a part of a series of guides for my personal Proxmox Lab build.

I decided to install Wazuh on a container to be resource friendly. If you are going to have it on strict isolated lab then obviously it is better to install it on a VM for the kernel level isolation. 

---
## OPNsense Prep and Architecture

In order to manage and isolate Wazuh better, I'll be creating a seperate VLAN for tools (VLAN 100) and adding the container to this VLAN. 

Here are the required ports mentioned in the [architecture](https://documentation.wazuh.com/current/getting-started/architecture.html) of Wazuh documentation:

![Screenshot 2026-01-11 at 12.13.54 PM.png](/images/Screenshot%202026-01-11%20at%2012.13.54%20PM.png)

**Ports 9200, 9300-9400** - Internal between Wazuh components (indexer), not exposed externally. These stay inside the VM.

This will be the configuration I'll be setting up in OPNsense:
### Aliases 

**Firewall → Aliases**1

- Name: `Wazuh_Agent_Ports`
- Ports: 1514, 1515

### Inbound Rules (To VLAN100)

1. **Allow Agent Traffic**
    - Action: Pass | Protocol: TCP | Source: any | Dest: VLAN100 net | Dest Port: 1514, 1515
2. **Allow Web UI Access**
    - Action: Pass | Protocol: TCP | Source: any | Dest: VLAN100 net | Dest Port: 443
3. **Allow API (Optional)**
    - Action: Pass | Protocol: TCP | Source: any | Dest: VLAN100 net | Dest Port: 55000

### Outbound Rules (From VLAN100)

4. **Allow All Outbound**
    - Action: Pass | Protocol: any | Source: VLAN100 net | Dest: any

![Screenshot 2026-01-11 at 1.21.33 PM.png](/images/Screenshot%202026-01-11%20at%201.21.33%20PM.png)

*Right now the source is undefined so any IP is accepted which is a little insecure. In the future, I'll probably restrict it to specific VLANs and subnets.*

---
## Installation

### Create an LXC

To get started, I created a standard debian 13 LXC container as base system to install Wazuh and ran a few basic post-install commands:

```bash
apt update && apt upgrade -y && apt install curl sudo -y
```

**Options:**

 Since this is not going to be used heavily it is okay to cut down on resources mentioned in the wazuh documentation found [here](https://documentation.wazuh.com/current/getting-started/index.html).

- 4 cores
- 4096 MB (4GB) of RAM
- 25 GB storage
- Configured static IP `10.200.100.10` and VLAN tag `100` on `vmbr1`

**If required, you can always allocate more resources later.**

### Installing Wazuh

I used the installation assistant:

```bash
curl -sO https://packages.wazuh.com/4.14/wazuh-install.sh && sudo bash ./wazuh-install.sh -a
```

Once the installation is complete, take a note of the temporary password, as you'll need it to log into the dashboard. 

If you forgot to take a note of it (like me) just run the following command to list all the users and their passwords:

```bash
tar -O -xvf wazuh-install-files.tar wazuh-install-files/wazuh-passwords.txt
```

Login with the username `admin` and the temporary password. Don't forget to change the password once logged in :

The passwords tool is embedded in the Wazuh indexer under `/usr/share/wazuh-indexer/plugins/opensearch-security/tools/`. You can use the embedded version or download it with the following command:

```bash
curl -so wazuh-passwords-tool.sh https://packages.wazuh.com/4.14/wazuh-passwords-tool.sh
```

```bash
bash wazuh-passwords-tool.sh -u admin -p <mypassword>
```

and of course...
#### Dark Theme:

Wazuh developers have done a pretty good job at hiding this setting not going to lie. This could have been way simpler but here is a [guide](https://dev.to/sivolko/missing-dark-mode-in-wazuh--2k5f) I found online

### Wazuh Twingate Access

In order to save my sanity and make life easier, I created a new resource and network in twingate and added a twingate connector to the wazuh container for ease of access and management. 

You can configure port forwarding, even more firewall rules, static routes etc but it gets complicated really quickly.

### Wazuh Agents

Use the official [documentation](https://documentation.wazuh.com/current/installation-guide/wazuh-agent/wazuh-agent-package-linux.html) to add the agents. This one is specific to linux. Make sure to follow the right guide for the right OS.

---
