#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file
"""
import json
import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


filname = "add_item.json"


try:
    data = load(filename=filname)
except FileNotFoundError:
    data = []

data += sys.argv[1:]
save(data, filename=filname)
