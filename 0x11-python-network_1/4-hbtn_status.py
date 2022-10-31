#!/usr/bin/python3
"""Using the `requests` module instead of `urllib`."""
import requests


if __name__ == '__main__':
    res = requests.get('https://alx-intranet.hbtn.io/status')
    _type = f'\t- type: {type(res.text)}\n'
    _cxt = f'\t- content: {res.text}'
    print(f"Body response:\n{_type}{_cxt}")
