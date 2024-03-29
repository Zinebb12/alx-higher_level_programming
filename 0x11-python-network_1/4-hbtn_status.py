#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status."""

import requests

r = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:")
print("\t- type: {}".format(type(str(r))))
print("\t- content: {}".format(r.text))
