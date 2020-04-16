#!/usr/bin/python3
"""last 10 commits"""
import requests
from sys import argv
if __name__ == "__main__":
    r = requests.get(
        """
        https://api.github.com/repos/{}/{}/commits?per_page=10
        """.format(argv[2], argv[1]))
    for i in r.json():
        print("{}: {}".format(i.get('sha'), i.get(
            'commit').get('author').get('name')))
