#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.

    Args:
        data (dict): Python dictionary to serialize
        filename (str): Name of the JSON file to write to
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a Python dictionary.

    Args:
        filename (str): Name of the JSON file to read from

    Returns:
        dict: Deserialized Python dictionary
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
