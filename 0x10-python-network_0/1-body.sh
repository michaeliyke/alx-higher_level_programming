#!/bin/bash
# conditionally sends a GET request to the URL, and displays the body of the response
if [[ $(curl -sL -w "%{http_code}" -o /dev/null "$1") == 200 ]]; then curl -sL "$1"; fi
