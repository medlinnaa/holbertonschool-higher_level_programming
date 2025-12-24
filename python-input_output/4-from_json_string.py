#!/usr/bin/python3
"""
This module provides a function that converts a JSON string
into a Python data structure.
"""

import json


def from_json_string(my_str):
    """
    Return a Python object represented by a JSON string.
    """
    return json.loads(my_str)
