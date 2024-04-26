#!/usr/bin/python3
""" technical interview prep """
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    commits_url = (
        f"https://api.github.com/repos/{owner_name}/{repo_name}/commits")

    r = requests.get(commits_url)
    commits = r.json()

    for commit in commits:
        commit_sha = commit.get('sha')
        author_name = commit['commit']['author'].get('name')
        print(f"{commit_sha}: {author_name}")
