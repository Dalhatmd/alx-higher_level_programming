#!/usr/bin/python3
""" Doc """
import urllib.request


req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    page = response.read()
    print("Body response:")
    print(f"\t- type: {type(page)}")
    print(f"\t- content: {page}")
    print(f"\t- utf8 content: {page.decode('utf-8')}")
