#!/usr/bin/python3

"""Module that write a script that adds all arguments to a
Python list and then save them to a file"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    json_list = load_from_json_file("add_item.json")
except Exception:
    json_list = []

for argm in sys.argv[1:]:
    json_list.append(argm)
save_to_json_file(json_list, "add_item.json")
