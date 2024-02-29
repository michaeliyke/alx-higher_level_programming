#!/usr/bin/bash
# sends a request to a URL, and displays the size of the body of the response
curl "$1" -I -s | grep 'Content-Length' | tr -d ' ' | cut -d ':' -f2
