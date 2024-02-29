#!/bin/bash
# Scripts that displays only the response code
curl -sL -w "%{http_code}" -o /dev/null "$1"
