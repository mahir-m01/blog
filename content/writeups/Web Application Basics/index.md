---
title: Web Application Basics
date: 2025-11-04
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - Web
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task  1 - Introduction

No answer needed

---
## Task  2 - Web Application Overview

#### 1) What is responsible for hosting and delivering content for web applications?

**Ans:** `web server`
#### 2) Which tool is used to access and interact with web applications?

**Ans:** `web browser`

#### 3) Which component acts as a protective layer...?

**Ans:** `web application firewall`

>**WAF** (Web Application Firewall) is an optional component for web applications. It helps filter out dangerous requests away from the Web Server and provides an element of protection. 

---

## Task  3 - Uniform Resource Locator

#### 1) Which protocol provides encrypted communication...?

**Ans:** `HTTPS`
#### 2) What term describes registering domain names that are misspelt ?

**Ans:** `Typesquatting`

> From a security standpoint, look for domain names that appear almost like real ones but have small differences (this is called **typosquatting**). These fake domains are often used in phishing attacks to trick people into giving up sensitive info.

#### 3) What part of a URL is used to pass additional information ?

**Ans:** `Query String`

>The **query string** is the part of the URL that starts with a question mark (?). It’s often used for things like search terms or form inputs. Since users can modify these query strings, it’s important to handle them securely to prevent attacks like **injections**, where malicious code could be added.

---

## Task  4 - HTTP Messages

#### 1) Which HTTP message is returned by the web server...?

**Ans:** `HTTP Response`
#### 2) What follows the headers in an HTTP message? ?

**Ans:** `Empty Line`

---

## Task  5 - HTTP Request: Request Line and Methods

#### 1) Which HTTP protocol version became widely adopted...?

**Ans:** `HTTP/1.1`

>Brought persistent connections, chunked transfer encoding, and better caching. It’s still widely used today.

#### 2) Which HTTP request method describes the communication options...? 

**Ans:** `OPTIONS`

#### 3) In an HTTP request, which component specifies the specific resource...? 

**Ans:** `URL Path`

---

## Task  6 - HTTP Request: Headers and Body

#### 1) Which HTTP request header specifies the domain name...?

**Ans:** `Host`

#### 2) What is the default content type for form submissions...? 

**Ans:** `application/x-www-form-urlencoded`

*This is how the message looks like*

```http
POST /profile HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 33

name=Aleksandra&age=27&country=US
```
#### 3) Which part of an HTTP request contains additional information...? 

**Ans:** `Request Headers`

---

## Task  7 - HTTP Response: Status Line and Status Codes

#### 1) What part of an HTTP response provides the HTTP version...?

**Ans:** `Status Line`

The first line in every HTTP response is called the **Status Line**. It gives you three key pieces of info:

1. **HTTP Version**: This tells you which version of HTTP is being used.
2. **Status Code**: A three-digit number showing the outcome of your request.
3. **Reason Phrase**: A short message explaining the status code in human-readable terms.

#### 2) Which category of HTTP response codes indicates...? 

**Ans:** `Server Error Responses`

#### 3) Which HTTP status code indicates that the requested resource...? 

**Ans:** `404`

>**404 (Not Found)**  
The server couldn’t find the resource at the given URL. Double-check that you’ve got the right address.

---

## Task  8 - HTTP Response: Headers and Body

#### 1) Which HTTP response header can reveal information...?

**Ans:** `Server`

> This header shows what kind of server software is handling the request. It’s good for debugging, but it can also reveal server information that might be useful for attackers, so many people remove or obscure this one.

#### 2) Which flag should be added to cookies in the Set-Cookie HTTP...? 

**Ans:** `Secure`

#### 3) Which flag should be added to cookies in the Set-Cookie HTTP...? 

**Ans:** `HttpOnly`

>   This header sends cookies from the server to the client, which the client then stores and sends back with future requests. To keep things secure, make sure cookies are set with the `HttpOnly` flag (so they can’t be accessed by JavaScript) and the `Secure` flag (so they’re only sent over HTTPS).

---

## Task  9 - Security Headers

#### 1) In a Content Security Policy (CSP) configuration, which property...?

**Ans:** `script-src`

>  It specifics the policy for where scripts can be loaded from, which is self along with scripts hosted on `https://cdn.tryhackme.com`

#### 2) When configuring the Strict-Transport-Security (HSTS)...? 

**Ans:** `includeSubDomains`

> It is an optional setting that instructs the browser to also apply this setting to all subdomains.

#### 3) Which HTTP header directive is used to prevent browsers...? 

**Ans:** `nosniff`

---

## Task  10 - Practical Task: Making HTTP Requests

*This is very similar to `Postman` - if you have used it for testing.*
#### 1) Make a **GET** request to `/api/users`. What is the flag ?

```
https://tryhackme.com/api/users
```

```html
HTTP/1.1 200 Ok

Server: nginx/1.15.8

Tue, 4 Nov 2025 19 6 48 GMT

Content-Type: text/html; charset=utf-8

Content-Length: 633

Last-Modified: Tue, 4 Nov 2025 19 6 48 GMT

  
<html>  
<head>  
    <title>TryHackMe</title>  
</head>  
<body>  
    <table class="table-auto"><thead><tr class="bg-gray text-white"><th class="w-20">Name</th><th class="w-20">Age</th><th class="w-20">Country</th><th>Flag</th></tr></thead><tbody><tr><td class="text-center">Alice</td><td class="text-center">28</td><td class="text-center">US</td><td class="text-center"></td></tr><tr><td class="text-center">Bob</td><td class="text-center">34</td><td class="text-center">UK</td><td class="text-center"></td></tr><tr><td class="text-center">Charlie</td><td class="text-center">25</td><td class="text-center">CA</td><td class="text-center">THM{YOU_HAVE_JUST_FOUND_THE_USER_LIST}</td></tr></tbody></table>  
</body>  
</html>
```

**Ans:** `THM{YOU_HAVE_JUST_FOUND_THE_USER_LIST}

#### 2) Make a **POST** request to `/api/user/2` and update...? 

*Okay, so this one was unnecessarily frustrating,  make sure you have an extra blank key-value pair box otherwise it doesn't add the query parameters correctly.*

`country=US`

**Ans:** `THM{YOU_HAVE_MODIFIED_THE_USER_DATA}`
#### 3) Make a **DELETE** request to `/api/user/1` to delete the user...? 

```
https://tryhackme.com/api/user/1
```

**Ans:** `THM{YOU_HAVE_JUST_DELETED_A_USER}`

---
