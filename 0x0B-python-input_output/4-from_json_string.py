#!/usr/bin/python3
"""from json module
"""

import json


def from_json_string(my_str):
    """ Setsstrings tojson

    Args:
        my_str (str): String object

    Returns:
        json: json data
    """
    return json.loads(my_str)
