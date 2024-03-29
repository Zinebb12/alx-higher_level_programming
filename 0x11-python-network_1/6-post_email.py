#!/usr/bin/python3
"""description"""

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    r = requests.post(url, data=value)
    print(r.text)
