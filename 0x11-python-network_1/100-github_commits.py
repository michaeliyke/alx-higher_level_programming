#!/usr/bin/env python3
if __name__ == "__main__":
    import sys
    import requests
    OWNER = sys.argv[1]
    REPO = sys.argv[2]

    u = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
    params = {"per_page": 10, "sort": "author-date-asc"}
    res = requests.get(u, params=params)
    o = res.json()
    if o:
        for e in o:
            print("{}: {}".format(e.get("sha"), e.get(
                "commit").get("author").get("name")))
