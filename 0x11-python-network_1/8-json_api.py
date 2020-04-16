#!/usr/bin/python3
"""json api"""
import requests
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        letter = argv[1]
    else:
        letter = ''
    r = requests.post('http://0.0.0.0:5000/search_user',
                      data={'q': '{}'.format(letter)})
    user = r.json()
    try:
        if user:
            print("[{}] {}".format(user.get('id'), user.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
