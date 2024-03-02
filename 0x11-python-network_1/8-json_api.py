#!/usr/bin/python3
"""
Python script that takes a letter and sends a post request to
http://0.0.0.0:5000/search_user with the letter as parameter

If the response body JSON, display the id and name like this: [<id>] <name>
Handle invalid JSON
Handle No data
"""

if __name__ == "__main__":
    import requests
    import sys

    q = sys.argv[1] if len(sys.argv) > 1 else ""
    res = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        obj = res.json()  # Will raise ValueError if not JSON

        if obj:
            print("[{}] {}".format(obj.get("id"), obj.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
