#!/usr/bin/python3
""" class to json module
"""


def class_to_json(obj):
    """ class to json

    Args:
        obj (object): object instance

    Returns:
        dict: class dict
    """
    return obj.__dict__
