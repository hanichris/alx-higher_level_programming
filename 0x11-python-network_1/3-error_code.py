#!/usr/bin/python3
"""Script to send a GET request and handles the HTTPError if present."""
import sys
import urllib.request
from urllib.error import HTTPError


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print(f'Error code: {e.code}')
