---
title: Public Key Cryptography Basics
date: 2025-10-26
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - Cryptography
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task  1 - Introduction

No answer needed

---

## Task  2 - Importance of Cryptography

#### 1) Standard required for handling credit card information?

**Ans:** `Lock`

---

## Task  3 - RSA

#### 1) Knowing that _p_ = 4391 and _q_ = 6659. What is _n_?

_n_ = _p_ _x_ _q_

**Ans:** `29239669`

#### 2) Knowing that _p_ = 4391 and _q_ = 6659. What is _ϕ_(_n_)?

_ϕ_(_n_) = _n_ - _p_ - _q_ + 1

**Ans:** `29228620`

---

## Task 4 - Diffie-Hellman Key Exchange

#### 1) Consider _p_ = 29, _g_ = 5, _a_ = 12. What is _A_?

*A = g^a mod p*

**Ans:** `7`

#### 2) Consider _p_ = 29, _g_ = 5, _b_ = 17. What is _B_?

*B = g^b mod p*

**Ans:** `9`

#### 3) What is the key calculated by Bob? 

*key = B^a mod p*

**Ans:** `24`

#### 4) what is the key calculated by Alice? 

*key = A^b mod p*

**Ans:** `24`

---

## Task 5 - SSH

#### 1) What algorithm does the key use?

*We can `ls` the directory and the type is in the name of they key.*

**Ans:** `RSA`

---

## Task 6 - Digital Signatures and Certificates

#### 1) What does a remote web server use to prove itself to the client?

**Ans:** `Certificate`
#### 2)  What would you use to get a free TLS certificate for your website?

**Ans:** `Let's Encrypt`

---

## Task 7 - PGP and GPG

#### 1) What secret word does the message hold?

*We first import the key and the decrypt the message.*

```bash
user@ip-10-48-173-106:~/Public-Crypto-Basics/Task-7$ ls
message.gpg  tryhackme.key
user@ip-10-48-173-106:~/Public-Crypto-Basics/Task-7$ gpg --import tryhackme.key 
gpg: /home/user/.gnupg/trustdb.gpg: trustdb created
gpg: key FFA4B5252BAEB2E6: public key "TryHackMe (Example Key)" imported
gpg: key FFA4B5252BAEB2E6: secret key imported
gpg: Total number processed: 1
gpg:               imported: 1
gpg:       secret keys read: 1
gpg:   secret keys imported: 1
user@ip-10-48-173-106:~/Public-Crypto-Basics/Task-7$ gpg --decrypt message.gpg 
gpg: encrypted with rsa1024 key, ID 2A0A5FDC5081B1C5, created 2020-06-30
      "TryHackMe (Example Key)"
You decrypted the file!
The secret word is Pineapple.
```

**Ans:** `Pineapple`