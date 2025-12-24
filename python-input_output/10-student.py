#!/usr/bin/python3
"""
This module defines a Student class with a method to return
a filtered dictionary representation of the instance.
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
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__
