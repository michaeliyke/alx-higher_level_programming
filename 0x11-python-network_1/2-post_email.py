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
    request = urllib.request.Request(
        url=sys.argv[1], data=data.encode('ascii'), method="POST"
    )

    with urllib.request.urlopen(request) as res:
        byte_arr = res.read()
        str_ = byte_arr.decode("utf-8")
        print(str)
