---
title: Linux System Hardening
date: 2026-01-09
draft: false
tags:
  - Cybersecurity
  - TryHackMe
  - Linux
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task 1 - Introduction

No answer needed

---
## Task 2 - Physical Security

#### 1) What command can you use to create a password for the GRUB bootloader?

**Ans:** `grub2-mkpasswd-pbkdf2`

#### 2) What does PBKDF2 stand for?

>PBKDF2 (Password-Based Key Derivation Function 2) is ==a cryptographic standard that securely turns a password or passphrase into a long, strong cryptographic key, primarily by applying a pseudorandom function (like HMAC) iteratively with a unique salt and a high number of rounds (iterations)==. Its purpose is to make [brute-force attacks](https://www.google.com/search?sca_esv=b04cb06c25fa1fe2&sxsrf=ANbL-n5aXI4yXdtvvK9u9FZLuGnXP-9-4Q%3A1767971561952&q=brute-force+attacks&sa=X&ved=2ahUKEwjz9bCn3_6RAxXdR2wGHUp5MTgQxccNegQILBAB&mstk=AUtExfCe6yPdgkD1nfNQvFIpVNbMmn_8rQ8qUKHFC-dxSHNKELYVTKyXOxgX0k47eqWrq7w8dRuVV3Z0SgUFZ22JD1T-LzHDpQYEqNzfOxhz1wXjrcu3-fXAauOe1-C05AeclQPKVT1FG4kAGpe_NKSZp8yleP2jeT_xb7CFDbtzeZPW9kOCd0sv89IhCzjSEQKgYdVh8ujKQtus7xcEleqJremwuf7xgLX3jMZ687DDAlADA-ja_FXLFFTPel6yXHSLFiBTd9yVXGII1CRPjJHqdyKN&csui=3) computationally expensive and slow, protecting stored passwords and creating encryption keys, and is defined in [RFC 2898](https://www.google.com/search?sca_esv=b04cb06c25fa1fe2&sxsrf=ANbL-n5aXI4yXdtvvK9u9FZLuGnXP-9-4Q%3A1767971561952&q=RFC+2898&sa=X&ved=2ahUKEwjz9bCn3_6RAxXdR2wGHUp5MTgQxccNegQILBAC&mstk=AUtExfCe6yPdgkD1nfNQvFIpVNbMmn_8rQ8qUKHFC-dxSHNKELYVTKyXOxgX0k47eqWrq7w8dRuVV3Z0SgUFZ22JD1T-LzHDpQYEqNzfOxhz1wXjrcu3-fXAauOe1-C05AeclQPKVT1FG4kAGpe_NKSZp8yleP2jeT_xb7CFDbtzeZPW9kOCd0sv89IhCzjSEQKgYdVh8ujKQtus7xcEleqJremwuf7xgLX3jMZ687DDAlADA-ja_FXLFFTPel6yXHSLFiBTd9yVXGII1CRPjJHqdyKN&csui=3).

**Ans:** `Password-Based Key Derivation Function 2`

---
## Task 3 - Filesystem Partitioning and Encryption

#### 1) What does LUKS stand for?

**Ans:** `Linux Unified Key Setup`

#### 2) What is the flag in the secret vault?

##### Step 1: Decrypt/Open the Encrypted Image with cryptsetup

Use `cryptsetup` to decrypt the image file. 

```bash
sudo cryptsetup open /home/tryhackme/secretvault.img myvault
```

- **`open`**: Opens/decrypts the LUKS container
- **`/home/tryhackme/secretvault.img`**: The encrypted file
- **`myvault`**: The name for the decrypted device mapping
- When prompted, enter the password: `2N9EdZYNkszEE3Ad`

After this command, the decrypted device will be available at `/dev/mapper/myvault`

##### Step 2: Mount the Decrypted Device

Now mount the decrypted device 

```bash
sudo mount /dev/mapper/myvault myvault
```
##### Step 3: Access the Files

Now you can read the files:

```bash
ls myvault
```

**Ans:** `THM{LUKS_not_LUX}`

---
## Task 4 - Firewall

#### 1) It is allowing another TCP port; what is it?

*Run the following command:*

```bash
sudo ufw status
```

```bash
Status: active

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere                  
14298/udp                  ALLOW       Anywhere                  
12526/tcp                  ALLOW       Anywhere                  
22/tcp (v6)                ALLOW       Anywhere (v6)             
14298/udp (v6)             ALLOW       Anywhere (v6)             
12526/tcp (v6)             ALLOW       Anywhere (v6) 
```

**Ans:** `12526`

#### 2) What is the allowed UDP port?

**Ans:** `14298`

---
## Task 5 - Remote Access

#### 1)  What flag is hidden in the `sshd_config` file?

*I used `grep` to search through the file to make it easier:*

```bash
grep "THM" /etc/ssh/sshd_config
# THM{secure_SEA_shell}
```

**Ans:** `THM{secure_SEA_shell}`

---
## Task 6 - Securing User Accounts

#### 1) What is the suggested value to use for the shell?

**Ans:** `/sbin/nologin`

#### 2) What is the name of the RedHat and Fedora systems sudoers group?

**Ans:** `wheel`

#### 3) What is the name of the sudoers group on Debian and Ubuntu systems?

**Ans:** `sudo`

#### 4) Other than `tryhackme` and `ubuntu`, what is the username...?

*The following command lists all users in `sudo` group:*

```bash
getent group sudo
```

**Ans:** `blacksmith`

---
## Task 7 - Software and Services

#### 1) Besides FTPS, what is another secure replacement for TFTP and FTP?

>Instead of Telnet, the SSH protocol is now widely available. For example, the Secure File Transfer Protocol (SFTP) protocol provides a great alternative to the TFTP protocol. The critical point is that a secure alternative is selected and used.

**Ans:** `SFTP`

---
## Task 8 - Update and Upgrade Policies

#### 1) What command would you use to update an older Red Hat system?

**Ans:** `yum update`

#### 2) What command would you use to update a modern Fedora system?

**Ans:** `dnf update`

#### 3) What two commands are required to update a Debian system?

**Ans:** `apt update && apt upgrade`

#### 4) What does `yum` stand for?

**Ans:** `Yellowdog Updater, Modified`

#### 5) What does `dnf` stand for?

**Ans:** `Dandified YUM`

#### 6) What flag is hidden in the `sources.list` file?

*For some reason there was no flag when I was doing the room but this command would have worked:*

```bash
grep "THM" /etc/apt/sources.list
```

**Ans:** `THM{not_Advanced_Persistent_Threat}`

---
## Task 9 - Audit and Log Configuration

#### 1) What command can you use to display the last 15 lines of `kern.log`?

**Ans:** `tail -n 15 kern.log`

#### 2) What command can you use to display the lines containing...?

**Ans:** `grep denied secure`

---
