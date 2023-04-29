#!/usr/bin/python3

import requests

url = "https://alx-intranet.hbtn.io/status"
response = requests.get(url)

print("Body response:")
print("\t- type: {}".format(type(response.content)))
print("\t- content: {}".format(response.content))
print("\t- utf8 content: {}".format(response.text))

