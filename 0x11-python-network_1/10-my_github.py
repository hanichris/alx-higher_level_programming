#!/usr/bin/python3
"""Display id of GitHub credentials using the GitHub API."""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    basic = HTTPBasicAuth(user, passwd)
    res = requests.get('https://api.github.com/user', auth=basic)
    print(res.json().get('id'))
