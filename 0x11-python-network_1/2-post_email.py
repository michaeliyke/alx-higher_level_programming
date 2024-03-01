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
    request = urllib.request.Request(sys.argv[1], data.encode('ascii'))

    with urllib.request.urlopen(request) as res:
        out = res.read().decode("utf-8")
        print(out)
