#!/usr/bin/python3
"""json api"""
import requests
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        data = {'q': ''}
    else:
        data = {'q': '{}'.format(argv[1])}
    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    user = r.json()
    try:
        if user:
            print("[{}] {}".format(user.get('id'), user.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
