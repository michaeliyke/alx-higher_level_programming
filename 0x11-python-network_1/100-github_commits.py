#!/usr/bin/python3
"""Interview question"""
if __name__ == "__main__":
    import sys
    import requests
    OWNER = sys.argv[1]
    REPO = sys.argv[2]

    url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
    res = requests.get(url, params={"per_page": 10})
    commits = res.json()
    if not commits:
        exit(0)

    for obj in commits:
        sha = obj.get("sha")
        c = obj.get("commit")
        if not c:
            continue
        author = c.get("author")
        if not author:
            continue
        # date = author.get("date")
        name = author.get("name")
        print("{}: {}".format(sha, name))
