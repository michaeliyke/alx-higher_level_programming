#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import urllib.error

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        html = res.read()
        print("Body response:")
        print("    - type: {}".format(type(html)))
        print("    - content: {}".format(html))
        print("   - utf8 content: {}".format(html.decode("utf-8")))
