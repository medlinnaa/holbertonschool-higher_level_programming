#!/usr/bin/python3
"""
This module defines a Student class that can be serialized to a
dictionary and reloaded from a dictionary.
"""


class Student:
    """
    Represents a student with basic personal information.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes listed in attrs
        are included in the returned dictionary.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance using a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
