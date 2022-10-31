#!/usr/bin/python3
"""Send a POST request and catch any exceptions raised."""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    res = requests.post(url, data={'q': q})
    try:
        json = res.json()
        if len(json) == 0:
            print('No result')
        else:
            print(f'{[json["id"]]} {json["name"]}')
    except ValueError:
        print('Not a valid JSON')
