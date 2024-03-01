#!/bin/bash
# Upload a file
curl -s -X POST -F "@$2" "$1"
