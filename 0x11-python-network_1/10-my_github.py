#!/usr/bin/python3
""" Displays Id using the Github API """
from requests.auth import HTTPBasicAuth
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = "https://api.github.com/user"

    payload = HTTPBasicAuth(user, passwd)
    r = requests.get("https://api.github.com/user", auth=payload)
    user_data = r.json()
    print(user_data.get('id'))
