#!/usr/bin/python3
"""Script that fetches data from a particular url."""
import urllib.request


req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    _type = f"\t- type: {type(the_page)}\n"
    _cxt = f"\t- content: {the_page}\n"
    _utf = f"\t- utf8 content: {the_page.decode('utf-8')}"
    print(f"Body response:\n{_type}{_cxt}{_utf}")
