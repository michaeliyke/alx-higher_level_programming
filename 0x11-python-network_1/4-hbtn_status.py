#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""

if __name__ == "__main__":
    import requests
    multi = """Body response:\n\t- type: {}\n\t- content: {}"""
    res = requests.get("https://alx-intranet.hbtn.io/status")
    print(multi.format(type(res.text), res.text))
