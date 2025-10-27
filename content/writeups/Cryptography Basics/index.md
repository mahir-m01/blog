---
title: Cryptography Basics
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

## Task  2 - Common Use of Asymmetric Encryption

#### 1) what real object is analogous to the public key?

**Ans:** `PCI DSS`

---

## Task  3 - Plaintext to Ciphertext

#### 1) What do you call the encrypted plaintext?

**Ans:** `ciphertext`

#### 2) What do you call the process that returns the plaintext?

**Ans:** `decryption`

---

## Task 4 - Historical Ciphers

#### 1) `XRPCTCRGNEI` - Caesar Cipher, what is the plaintext?

*To decrypt this we can bruteforce multiple key shifts to the left. The one that works is 15. That is key = 15.*

**Ans:** `ICANENCRYPT`

---

## Task 5 - Types of Encryption

#### 1) Should you trust DES? (Yea/Nay)?

**Ans:** `Nay`

> **DES** was adopted as a standard in 1977 and uses a 56-bit key. With the advancement in computing power, in 1999, a DES key was successfully broken in less than 24 hours, motivating the shift to 3DES.

#### 2) When was AES adopted as an encryption standard?

**Ans:** `2001`

---

## Task 6 - Basic Math

#### 1) What’s 1001 ⊕ 1010?

*Follow the basic rules of XOR and apply it to numbers individually.*

**Ans:** `0011`
#### 2) What’s 118613842%9091?

*Its best to use an online python compiler. It makes calculation easier.*

```python
print(118613842%9091)
```

**Ans:** `3565`

#### 3) What’s 60%12?

*Its best to use an online python compiler. It makes calculation easier.*

```python
print(60%12)
```

**Ans:** `0`