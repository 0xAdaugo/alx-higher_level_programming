#!/usr/bin/python3

"""Define a custom Square class."""

class Square:
    """Represent a custom square."""

    def __init__(self, size=0):
        """Initialize a new custom square.
        Args:
            size (int): The size of the new custom square.
        """
        # Check if the provided size is an integer
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        # Check if the provided size is non-negative
        elif size < 0:
            raise ValueError("Size must be >= 0")
        # Store the size as a private attribute
        self.__size = size

