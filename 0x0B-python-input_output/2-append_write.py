#!/usr/bin/python3
""" append write module
    """


def append_write(filename="", text="") -> int:
    """ Write append

    Args:
        filename (str, optional): filename to append to. Defaults to "".
        text (str, optional): text to append. Defaults to "".

    Returns:
        int: len of text appended
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
