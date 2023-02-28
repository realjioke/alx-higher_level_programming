#!/usr/bin/python3
""" save to json module
"""

import json


def save_to_json_file(my_obj, filename):
    """ saves file to json

    Args:
        my_obj (str object): Object arg
        filename (str): Filename
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
