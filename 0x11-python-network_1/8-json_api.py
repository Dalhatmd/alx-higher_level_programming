#!/usr/bin/python3
""" doc """
import requests
import sys


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    value = {'q': letter}
    r = requests.post(url, data=value)

    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
