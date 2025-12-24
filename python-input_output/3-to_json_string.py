#!/usr/bin/python3
"""
This module provides a function that returns the JSON representation
of an object as a string.
"""

import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object as a string.
    """
    return json.dumps(my_obj)
