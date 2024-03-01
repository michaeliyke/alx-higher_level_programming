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

    data = urllib.parse.urlencode({'email': sys.argv[2]})
    opts = tuple(url=sys.argv[1], data=data.encode('ascii'), method="POST")
    request = urllib.request.Request(*opts)

    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.read())
