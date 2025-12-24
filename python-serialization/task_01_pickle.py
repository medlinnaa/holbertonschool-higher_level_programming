#!/usr/bin/python3
"""
task_01_pickle.py
Serialize/deserialize a custom class using pickle.
"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.
        Returns None if an error occurs.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError, AttributeError, TypeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a pickle file.
        Returns the object, or None if the file doesn't exist or is malformed.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            # Optional safety check: ensure it's the right type
            if not isinstance(obj, cls):
                return None
            return obj
        except (OSError, EOFError, pickle.UnpicklingError, pickle.PickleError):
            return None
