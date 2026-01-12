---
title: 100 Days of DevOps Complete Writeup
date: 2026-01-07
draft: false
tags:
  -
---
- This is/will be a complete writeup of the 100 Days of DevOps program from KodeKloud.
- The KodeKloud platform uses various users, servers etc within their infrastructure for challenges. I will be writing a guide based on the content I get for the challenges and yours may be different. As a result, Day 1 has a writeup of a general command blocks for understanding. Should you wish to follow along, change the details as need be.

## Day 1: Linux User Setup with Non-Interactive Shell

### Solution

SSH into the server:

```bash
ssh user@server
```

Create the user using the command:

```bash
sudo useradd -m -s /usr/sbin/nologin username
```

- `-m` creates a home directory

>The `**nologin**` **shell** is a special type of shell in Linux designed to prevent a user from logging in interactively .

---
## Day 2: Temporary User Setup with Expiry

### Task:

Create a user named `jim` on `App Server 1` in Stratos Datacenter. Set the expiry date to `2024-02-17`, ensuring the user is created in lowercase as per standard protocol.

### Solution 
1
SSH into the server:

```bash
ssh tony@stapp01.stratos.xfusioncorp.com
```

Create the user: 

```bash
sudo useradd -m -e 2024-02-17 jim
```

Verify the entry:

```bash
cat /etc/passwd
```

---
## Day 3: Temporary User Setup with Expiry

### Task:

Following security audits, the `xFusionCorp Industries` security team has rolled out new protocols, including the restriction of direct root SSH login.  
Your task is to disable direct SSH root login on all app servers within the `Stratos Datacenter`.

### Solution 

SSH into the server:

```bash
ssh tony@stapp01.stratos.xfusioncorp.com
```

Change `PermitRootLogin` to `no`:

**1. Open the file:**

```bash
sudo vi /etc/ssh/sshd_config
```

**2. Find the line you need:**

- Press `/`
- Type `PermitRootLogin`
- Press Enter

**3. Enter edit mode:**

- Press `i` (insert mode)

**4. Edit the text:**

- Use arrow keys to move around
- Delete characters with Backspace
- Change `yes` to `no`

**5. Exit edit mode:**

- Press Escape

**6. Save and quit:**

- Type `:wq` (colon, w, q)
- Press Enter

Then restart SSH:

```bash
sudo systemctl restart sshd
```

*Repeat the process for the other 2 App Servers*

---

