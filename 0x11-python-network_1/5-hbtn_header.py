#!/usr/bin/python3
"""Make a GET request and obtain the value of the header X-Request-Id"""
import requests
import sys


if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    print(res.headers['X-Request-Id'])
