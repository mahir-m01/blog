---
title: JavaScript Essentials
date: 2025-11-05
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - JavaScript
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task  1 - Introduction

No answer needed

---
## Task  2 - Essential Concepts

#### 1) What term allows you to run a code block multiple times?

**Ans:** `loop`

> Loops allow you to run a code block multiple times as long as a condition is `true`.

---

## Task  3 - Javascript Overview 

#### 1) What is the code output if the value of x is changed to 10?

**Ans:** `The result is: 20`
#### 2) What term describes registering domain names that are misspelt ?

**Ans:** `Interpreted`

> JS is an **interpreted** language, meaning the code is executed directly in the browser without prior compilation.

---

## Task  4 - Integrating JavaScript in HTML

#### 1) Which type of JavaScript integration...?

**Ans:** `Internal`
#### 2) Which method is better for reusing JS across multiple web pages? 

**Ans:** `External`

#### 3) What is the name of the external JS file...?

**Ans:** `thm_external.js`

#### 4) What attribute links an external JS file in the `<script>` tag? 

**Ans:** `src`

---

## Task  5 - Abusing Dialogue Functions

#### 1) In the file **invoice.html**...?

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Hacked</title>
</head>
<body>
    <script>
        for (let i = 0; i < 5; i++) {
            alert("Hacked");
        }
    </script>
</body>
</html>
```

**Ans:** `5`


#### 2) Which of the JS interactive elements should be used to display...? 

**Ans:** `prompt`

#### 3) If the user enters Tesla, what value is stored in the carName...? 

*The entered value is what will be stored*

**Ans:** `Tesla`

---

## Task  6 - Bypassing Control Flow Statements 

#### 1) What is the message displayed if you enter the age less than 18?

```hmtl
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Age Verification</title>
</head>
<body>
    <h1>Age Verification</h1>
    <p id="message"></p>

    <script>
        let age = prompt("What is your age")
        if (age >= 18) {
            document.getElementById("message").innerHTML = "You are an adult.";
        } else {
            document.getElementById("message").innerHTML = "You are a minor.";
        }
    </script>
</body>
</html>
```

**Ans:** `You are a minor.`

#### 2) What is the password for the user admin? 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login Page</title>
</head>
<body>
    <h2>Login Authentication</h2>

    <script>
        let username = prompt("Enter your username:");
        let password = prompt("Enter your password:");

        if (username === "admin" && password === "ComplexPassword") {
            document.write("You are successfully authenticated!");
        } else {
            document.write("Authentication failed. Incorrect username or password.");
        }
    </script>
</body>
</html>
```

**Ans:** `ComplexPassword`

---

## Task  7 - Exploiting Minified Fields

#### 1) What is the alert message shown after running the file **hello.html**?

*Use an online tool, I ended up using `https://obf-io.deobfuscate.io/`*

**Ans:** `Welcome to THM`

#### 2) What is the value of the **age** variable...?

*Step 1: Convert all hex values to decimal:*

0x1 = 1  
0x247e = 9342  
0x35 = 53  
0x2e = 46  
0x1ae3 = 6883  

*Step 2: Substitute and compute:*

age = (1 x 9342) + (53  x -46) + (-6883)  
age = 9342 - 2438 - 6883  
age = 21  

**Ans:** `21`

---

## Task  8 - Best Practices

#### 1) Is it a good practice to blindly include JS in your code from any source?

**Ans:** `nay`

>  If you blindly include a malicious library, you will expose your web application to threats.

---
