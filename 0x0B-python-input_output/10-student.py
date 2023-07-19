#!/usr/bin/python3
"""Student module
"""


class Student:

    """ Studen class
    """

    def __init__(self, first_name: str, last_name: str, age: str) -> None:
        """Summary

        Args:
            first_name (str): first name
            last_name (str): last name
            age (str): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None) -> dict:
        """to json method

        Returns:
            dict: return data
        """
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
