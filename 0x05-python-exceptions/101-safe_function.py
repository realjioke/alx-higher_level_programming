#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as error:
        result = None
        print("Exception: {}".format(error), file=sys.stderr)
    finally:
        return result
