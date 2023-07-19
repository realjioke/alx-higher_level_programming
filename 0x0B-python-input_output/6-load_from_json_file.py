#!/usr/bin/python3
""" load from json file  module
"""

import json


def load_from_json_file(filename):
    """ load file from json

    Args:
        filename (str): filename

    Returns:
        json: json file
    """
    with open(filename, encoding="utf-8") as fd:
        return json.load(fd)
