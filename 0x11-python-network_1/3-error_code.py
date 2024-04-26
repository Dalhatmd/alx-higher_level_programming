#!/usr/bin/python3
"""Handles error in HTTP response """
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    r = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(r) as response:
        try:
            print(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
