#!/usr/bin/python3
"""heraders"""
import requests
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    if int(r.status_code) < 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
