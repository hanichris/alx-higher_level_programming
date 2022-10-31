#!/usr/bin/python3
"""Display the status code of a response if it was >= 400."""
import sys
import requests


if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
