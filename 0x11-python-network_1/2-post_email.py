#!/usr/bin/python3
"""post email"""
import urllib.parse
import urllib.request
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    values = {'email': '{}'.format(argv[2])}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        email = response.read()
    print(email.decode('utf-8'))
