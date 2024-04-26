#!/usr/bin/python3
""" Posts an email to a url """
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = {"emal": "umarmd709@gmail.com"}
    post_data = urllib.parse.urlencode(data)
    post_data = post_data.encode('ascii')

    r = urllib.request.Request(sys.argv[1], post_data)
    with urllib.request.urlopen(r) as response:
        page = response.read()

    print("Your email is: {}".format(page))
