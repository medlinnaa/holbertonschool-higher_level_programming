#!/usr/bin/python3
"""Defines a MyList class that extends list with a sorted print method."""


class MyList(list):
    """Represents a list with a method to print it sorted."""

    def print_sorted(self):
        """Print the list elements in ascending sorted order."""
        print(sorted(self))
