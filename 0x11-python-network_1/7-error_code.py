#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""

if __name__ == "__main__":
    import requests
    import sys

    res = requests.post(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: ".format(res.status_code))
    else:
        print(res.text)
