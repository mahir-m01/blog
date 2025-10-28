---
title: Hashing Basics
date: 2025-10-27
draft: false
tags:
  - Cryptography
  - TryHackMe
  - Hashing
  - Cybersecurity
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task  1 - Introduction

No answer needed

---

## Task  2 - Hash Functions

#### 1) What is the SHA256 hash of the `passport.jpg`

*Run the following command to view the hash:*

```bash
user@ip-10-48-180-74:~/Hashing-Basics/Task-2$ sha256sum passport.jpg 
77148c6f605a8df855f2b764bcc3be749d7db814f5f79134d2aa539a64b61f02 passport.jpg
```

**Ans:** `77148c6f605a8df855f2b764bcc3be749d7db814f5f79134d2aa539a64b61f02`

#### 2) What is the output size of the MD5 hash function?

**Ans:** `16`

>The MD5 hash function produces a fixed output size of **128 bits**, which equals **16 bytes** because each byte consists of 8 bits. Although MD5 hashes are typically displayed as a 32-character hexadecimal string, that format is just a readable representation - each hexadecimal character represents 4 bits, meaning two hex characters equal one byte. Therefore, the 32-character hex string corresponds to a 16-byte binary value.

#### 3) 8-bit hash output, how many possible hash values ?

*We can find this by calculating 2^8*

**Ans:** `256`

---

## Task  3 - Insecure Password Storage for Authentication

#### 1) What is the 20th password in `rockyou.txt`?

*Do NOT just `cat` it , be smart and only output the first 20 lines.*

```bash
 cat rockyou.txt | head -n 20
```

**Ans:** `qwerty`

---

## Task 4 - Using Hash for Secure Password Storage

#### 1) Manually check the hash using the rainbow table above.

**Ans:** `inS3CyourP4$$`

#### 2) Crack the hash using an online tool.

*I ended up using `hashes.com` for this*

`5b31f93c09ad1d065c0491b764d04933:tryhackme:MD5`

**Ans:** `tryhackme`

#### 3) Should you encrypt passwords in password-verification systems?

**Ans:** `Nay`

>The reason is that even if we select a secure hashing algorithm to encrypt the passwords before storing them, we still need to store the used key. Consequently, if someone gets the key, they can easily decrypt all the passwords.

---

## Task 5 - Recognising Password Hashes

*For the following questions, you can typically find the details on the internet by searching around and on websites like `Hashcat`*

#### 1) What is the hash size in yescrypt?

**Ans:** `256`

#### 2) What’s the Hash-Mode listed for Cisco-ASA MD5?

**Ans:** `2410`

#### 3) What hashing algorithm is used in Cisco-IOS if it starts with `$9$`?

**Ans:** `scrypt`

---

## Task 6 - Password Cracking

#### 1) Use `hashcat` to crack the hash...

*A little bit of research by breaking down the hash by its parts (`$2a$`) tells us that that this is a `bcrypt` hash. Knowing this we can execute the following command:*

>`$2a$` corresponds to `bcrypt` and the mode is `3200`

```bash
hashcat -m 3200 -a 0 hash1.txt /usr/share/wordlists/rockyou.txt 
```

*We can show the actual password by running the following command once cracked:*

```bash
hashcat -m 3200 -a 0 hash1.txt /usr/share/wordlists/rockyou.txt --show
```

**Ans:** `85208520`

#### 2)  Use `hashcat` to crack the SHA2-256 hash

>`SHA2-256` - mode is `1400`

```bash
 hashcat -m 1400 -a 0 hash2.txt /usr/share/wordlists/rockyou.txt
```

*We can show the actual password by running the following command once cracked:*

```bash
 hashcat -m 1400 -a 0 hash2.txt /usr/share/wordlists/rockyou.txt --show
```

**Ans:** `halloween`

#### 3)  Use `hashcat` to crack the hash...

>`$6$` corresponds to `sha512crypt` and the mode is `1800`

```bash
 hashcat -m 1800 -a 0 hash3.txt /usr/share/wordlists/rockyou.txt
```

*We can show the actual password by running the following command once cracked:*

```bash
 hashcat -m 1800 -a 0 hash3.txt /usr/share/wordlists/rockyou.txt --show
```

**Ans:** `spaceman`

#### 4)  Crack the hash...

*Since it is not really possible to determine the type of hash used, its best to use an online rainbow table. I decided to go with `hashes.com` as  usual -*

`b6b0d451bbf6fed658659a9e7e5598fe:funforyou`

**Ans:** `funforyou`

---

## Task 7 -  Hashing for Integrity Checking

#### 1) What is SHA256 hash of `libgcrypt-1.11.0.tar.bz2` ?

*Run the following command to get the hash:*

```bash
sha256sum libgcrypt-1.11.0.tar.bz2 
```

**Ans:** `09120c9867ce7f2081d6aaa1775386b98c2f2f246135761aae47d81f58685b9c`

#### 2) What’s the hashcat mode number ?

*Searching for the mode number `$pass` for `HMAC-SHA512` in hashcat we get:*

**Ans:** `1750`

---

## Task 8 - Conclusion

#### 1) Use `base64` to decode `RU5jb2RlREVjb2RlCg==`.

*Run the following command to decode the text*

```bas
base64 -d decode-this.txt
```

**Ans:** `ENcodeDEcode`

---
