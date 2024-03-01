#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header of the
response"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import urllib.error
    import sys

    with urllib.request.urlopen(sys.argv[1]) as res:
        # This is different for all requests
        h = res.getheader("X-Request-Id")
        print(h)
