#!/usr/bin/python3
"""Display id of GitHub credentials using the GitHub API."""
import sys
import requests


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = f'https://api.github.com/users/{user}'
    res = requests.get(url, auth=(user, passwd))
    print(res.json().get('id'))
