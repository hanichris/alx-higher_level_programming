#!/usr/bin/python3
"""Script to send a request to the provided url.
   On receiving the response, pick out the header with the name
`  X-Request-Id`.
"""
import sys
import urllib.request


req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    print(response.getheader('X-Request-Id'))
