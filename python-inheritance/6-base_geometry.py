#!/usr/bin/python3
"""Defines a BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """Represents a base geometry class."""

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
