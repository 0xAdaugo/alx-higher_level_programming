#!/usr/bin/python3
# 4-print_square.py
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): The height/width of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    # Check if size is an integer, otherwise raise a TypeError
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    # Check if size is greater than or equal to 0, otherwise raise a ValueError
    if size < 0:
        raise ValueError("size must be >= 0")

    # Loop through rows and columns to print the square
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

