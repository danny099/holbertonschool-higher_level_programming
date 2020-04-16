#!/usr/bin/python3
"""heraders"""
import requests
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    header = requests.get(url)
    print(header.headers.get('X-Request-Id'))
