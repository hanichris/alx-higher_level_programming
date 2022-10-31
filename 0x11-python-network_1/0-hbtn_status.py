#!/usr/bin/python3
"""Script that fetches data from a particular url."""
import urllib.request


req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    _type = f"    - type: {type(the_page)}\n"
    _cxt = f"    - content: {the_page}\n"
    _utf = f"    - utf8 content: {the_page.decode('utf-8')}"
    print(f"Body response:\n{_type}{_cxt}{_utf}")
