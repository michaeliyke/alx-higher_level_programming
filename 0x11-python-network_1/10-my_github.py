#!/usr/bin/python3
"""
Python script that takes Github credentials: username and password
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    import sys

    USER = sys.argv[1]
    TOKEN = sys.argv[2]

    headers = {"Authorization": "token {}".format(TOKEN)}

    res = requests.get(f"https://api.github.com/users/{USER}", headers=headers)
    obj = res.json()
    if obj:
        print(obj.get("id"))
