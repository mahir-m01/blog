---
title: SQL Fundamentals
date: 2025-11-05
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - SQL
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task  1 - Introduction

No answer needed

---
## Task  2 - Databases 101

#### 1) What type of database should you consider...?

**Ans:** `Non-relational database`
#### 2) What type of database should you consider...?

**Ans:** `relational database`

#### 3) In our example, once a record of a book...?

**Ans:** `row`

#### 4) Which type of key provides a link from one table to another?

**Ans:** `foreign key`

#### 5) which type of key ensures a record is unique within a table?

**Ans:** `primary key`

---

## Task  3 - SQL

#### 1) What serves as an interface between a database and an end user?

**Ans:** `DBMS`
#### 2) What query language can be used to interact with a relational database?

**Ans:** `SQL`

---

## Task  4 - Database and Table Statements

#### 1) Using the statement you've learned to list all databases...?

*Make sure you have logged in to mysql.*

```mysql
show databses;
```

```mysql
+-----------------------------------------------+
| Database                                      |
+-----------------------------------------------+
| THM{575a947132312f97b30ee5aeebba629b723d30f9} |
| information_schema                            |
| mysql                                         |
| performance_schema                            |
| sys                                           |
| task_4_db                                     |
| thm_books                                     |
| thm_books2                                    |
| tools_db                                      |
+-----------------------------------------------+
9 rows in set (0.00 sec)
```

**Ans:** `THM{575a947132312f97b30ee5aeebba629b723d30f9}`

#### 2) In the list of available databases, you should...?

*Run the following queries.*

```mysql
use task_4_db;
```

```mysql
show tables;
```

```mysql
+-----------------------------------------------+
| Tables_in_task_4_db                           |
+-----------------------------------------------+
| THM{692aa7eaec2a2a827f4d1a8bed1f90e5e49d2410} |
+-----------------------------------------------+
1 row in set (0.00 sec)
```

**Ans:** `THM{692aa7eaec2a2a827f4d1a8bed1f90e5e49d2410}`

---

## Task  5 - CRUD Operations

*Run the following queries.*

```mysql
use tools_db;
```

```mysql
select * from hacking_tools;
```

```mysql
+----+------------------+----------------------+-------------------------------------------------------------------------+--------+
| id | name             | category             | description                                                             | amount |
+----+------------------+----------------------+-------------------------------------------------------------------------+--------+
|  1 | Flipper Zero     | Multi-tool           | A portable multi-tool for pentesters and geeks in a toy-like form       |    169 |
|  2 | O.MG cables      | Cable-based attacks  | Malicious USB cables that can be used for remote attacks and testing    |    180 |
|  3 | Wi-Fi Pineapple  | Wi-Fi hacking        | A device used to perform man-in-the-middle attacks on wireless networks |    140 |
|  4 | USB Rubber Ducky | USB attacks          | A USB keystroke injection tool disguised as a flash drive               |     80 |
|  5 | iCopy-XS         | RFID cloning         | A tool used for reading and cloning RFID cards for security testing     |    375 |
|  6 | Lan Turtle       | Network intelligence | A covert tool for remote access and network intelligence gathering      |     80 |
|  7 | Bash Bunny       | USB attacks          | A multi-function USB attack device for penetration testers              |    120 |
|  8 | Proxmark 3 RDV4  | RFID cloning         | A powerful RFID tool for reading, writing, and analyzing RFID tags      |    300 |
+----+------------------+----------------------+-------------------------------------------------------------------------+--------+
8 rows in set (0.00 sec)
```

#### 1) Using the `tools_db` database, what is the total number...?

**Ans:** `Wi-Fi Pineapple`

#### 2) Using the `tools_db` database, what is the shared category...?

**Ans:** `USB attacks`

---
## Task  6 - Clauses

*We can use the table display from our previous queries for convenience.*
#### 1) Using the `tools_db` database, what is the total number...?

*Run the following query.*

```mysql
select count(distinct category) from hacking_tools;
```

```mysql
+--------------------------+
| count(distinct category) |
+--------------------------+
|                        6 |
+--------------------------+
1 row in set (0.00 sec)
```

**Ans:** `6`

#### 2) Using the `tools_db` database, what is the first tool...? 

*Run the following query.*

```mysql
select name from hacking_tools order by name asc;
```

```mysql
+------------------+
| name             |
+------------------+
| Bash Bunny       |
| Flipper Zero     |
| iCopy-XS         |
| Lan Turtle       |
| O.MG cables      |
| Proxmark 3 RDV4  |
| USB Rubber Ducky |
| Wi-Fi Pineapple  |
+------------------+
8 rows in set (0.00 sec)
```

**Ans:** `Bash Bunny`

#### 3) Using the `tools_db` database, what is the first tool...? 

*This would just be the last entry from our previous query.*

**Ans:**  `Wi-Fi Pineapple`

---

## Task  7 - Operators

#### 1) Using the `tools_db` database, which tool falls...?

*Run the following query.*

```mysql
select * from hacking_tools where category = 'Multi-Tool';
```

```mysql
+----+--------------+------------+-------------------------------------------------------------------+--------+
| id | name         | category   | description                                                       | amount |
+----+--------------+------------+-------------------------------------------------------------------+--------+
|  1 | Flipper Zero | Multi-tool | A portable multi-tool for pentesters and geeks in a toy-like form |    169 |
+----+--------------+------------+-------------------------------------------------------------------+--------+
1 row in set (0.00 sec)
```

**Ans:** `Flipper Zero`

#### 2) Using the `tools_db` database, what is the category of tools...? 

*Run the following query.*

```mysql
select category from hacking_tools where amount >= 300;
```

```mysql
+--------------+
| category     |
+--------------+
| RFID cloning |
| RFID cloning |
+--------------+
2 rows in set (0.01 sec)
```

**Ans:** `RFID Cloning`

#### 3) Using the `tools_db` database, which tool falls under...? 

*Run the following query.*

```mysql
select name from hacking_tools where category = 'Network intelligence' and amount < 100;
```

```mysql
+------------+
| name       |
+------------+
| Lan Turtle |
+------------+
1 row in set (0.00 sec)
```

**Ans:** `Lan Turtle`

---

## Task 8 - Functions

#### 1) Using the `tools_db` database, what is the tool...?

*Run the following query.*

```mysql
select name, length(name) from hacking_tools order by length(name) desc;
```

```mysql
+------------------+--------------+
| name             | length(name) |
+------------------+--------------+
| USB Rubber Ducky |           16 |
| Wi-Fi Pineapple  |           15 |
| Proxmark 3 RDV4  |           15 |
| Flipper Zero     |           12 |
| O.MG cables      |           11 |
| Lan Turtle       |           10 |
| Bash Bunny       |           10 |
| iCopy-XS         |            8 |
+------------------+--------------+
8 rows in set (0.00 sec)
```

**Ans:** `USB Rubber Ducky`

#### 2) Using the `tools_db` database, what is the total sum of all tools?

*Run the following query.*

```mysql
select sum(amount) from hacking_tools;
```

```mysql
+-------------+
| sum(amount) |
+-------------+
|        1444 |
+-------------+
1 row in set (0.00 sec)
```

**Ans:** `1444`

#### 3) Using the `tools_db` database, what are the tool names where...?

*Run the following query.*

```mysql
select group_concat(name separator " & ") from hacking_tools where amount not like '%0';
```

```mysql
+------------------------------------+
| group_concat(name separator " & ") |
+------------------------------------+
| Flipper Zero & iCopy-XS            |
+------------------------------------+
1 row in set (0.00 sec)
```

**Ans:** `Flipper Zero & iCopy-XS`

---
