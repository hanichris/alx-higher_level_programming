#!/usr/bin/python3
"""Script to send a `POST` request to the passed url."""
import sys
import urllib.request
import urllib.parse


if __name__ == '__main__':
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
