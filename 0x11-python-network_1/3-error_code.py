#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import urllib.error
    import sys

    request = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(request) as res:
            out = res.read().decode("utf-8")
            print(out)
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
