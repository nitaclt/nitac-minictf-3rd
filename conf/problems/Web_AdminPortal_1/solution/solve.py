import requests
import random
import re

url = "http://0.0.0.0:8001"

data = {"username": "guest_{}".format(random.randrange(0, 1<<32)),
        "password": "guest"}
r = requests.post("{}/register.php".format(url), data)

r = requests.post("{}/login.php".format(url), data)
print(re.findall("(NITAC\{.+\})", r.text))
