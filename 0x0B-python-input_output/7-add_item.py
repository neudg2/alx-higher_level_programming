#!/usr/bin/python3
import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if __name__ == "__main__":
    try:
        data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []

    data.extend(sys.argv[1:])

    save_to_json_file(data, "add_item.json")

