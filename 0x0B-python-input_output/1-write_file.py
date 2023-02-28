#!/usr/bin/python3
""" Write file module
    """


def write_file(filename="", text="") -> int:
    """ write to a file

    Args:
        filename (str, optional): filename to write to. Defaults to "".
        text (str, optional): text to write. Defaults to "".

    Returns:
        int: _description_
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
