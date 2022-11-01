#!/usr/bin/python3
"""Interview challenge."""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    res = requests.get(url)
    if res.status_code == 200:
        for elem in res.json()[:10]:
            sha = elem.get('sha')
            name = elem.get('commit').get('author').get('name')
            print(f"{sha}: {name}")
    else:
        print(f'Error code: {res.status_code}')
