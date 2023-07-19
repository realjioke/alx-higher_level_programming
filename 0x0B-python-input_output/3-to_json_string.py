#!/usr/bin/python3
""" to json module

    Returns:
        object: json object
    """
import json


def to_json_string(my_obj):
    """ to json function

    Args:
        my_obj (object): object arg

    Returns:
        object: json object
    """
    return json.dumps(my_obj)
