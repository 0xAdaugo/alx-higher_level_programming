#!/usr/bin/python3
# 3-say_my_name.py
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.

    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    # Check if first_name and last_name are strings, otherwise raise a TypeError
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    # Print the formatted name
    print("My name is {} {}".format(first_name, last_name))

