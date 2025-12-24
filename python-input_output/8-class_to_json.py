#!/usr/bin/python3
"""
This module provides a function that returns the dictionary
representation of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Return the dictionary description of an object.
    """
    return obj.__dict__
