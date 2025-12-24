#!/usr/bin/python3
"""
This module defines a Student class with a method to return
its dictionary representation.
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

    def to_json(self):
        """
        Return the dictionary representation of the Student instance.
        """
        return self.__dict__
