#!/bin/bash
# sends a request to a URL, and displays the size of the body of the response
curl -Is -X OPTIONS "$1" | grep 'Allow:' | cut -d ':' -f2 | sed 's/^[[:space:]]*//'
