#!/usr/bin/python3
"""json"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    obj = load_from_json_file("add_item.json")
except FileNotFoundError:
    save_to_json_file([], "add_item.json")
    obj = load_from_json_file("add_item.json")

for i in range(1, len(sys.argv)):
    obj.append(str(sys.argv[i]))
save_to_json_file(obj, "add_item.json")
