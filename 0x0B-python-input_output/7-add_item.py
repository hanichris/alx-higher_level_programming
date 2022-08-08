#!/usr/bin/python3
"""Script to add all command line arguments to a list and
save the list object to a file.
"""
import json
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if __name__ == "__main__":
    try:
        my_list = load_from_json_file('add_item.json')
    except Exception:
        if len(sys.argv) == 1:
            save_to_json_file([], 'add_item.json')
        else:
            save_to_json_file(sys.argv[1:], 'add_item.json')
    else:
        for element in sys.argv:
            if element != './7-add_item.py':
                my_list.append(element)
        save_to_json_file(my_list, 'add_item.json')
