#!/usr/bin/python3
"""
Python script that takes Github credentials: username and password
"""

if __name__ == "__main__":
    import requests
    import sys

    data = {"q": sys.argv[1]} if len(sys.argv) > 1 else {"q": ""}
    res = requests.post("http://0.0.0.0:5000/search_user", params=data)

    try:
        obj = res.json()  # Will raise ValueError if not JSON

        if obj:
            print("[{}] {}".format(obj.get("id"), res.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
