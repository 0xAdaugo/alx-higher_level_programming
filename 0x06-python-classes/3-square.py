#!/usr/bin/python3

"""Define a custom Square class."""

class Square:
    """Represent a custom square."""

    def __init__(self, size=0):
        """Initialize a new custom square.
        Args:
            size (int): The size of the new custom square.
        """
        if not isinstance(size, int):  # Check if size is an integer
            raise TypeError("Size must be an integer")
        elif size < 0:  # Check if size is non-negative
            raise ValueError("Size must be >= 0")
        self.__size = size  # Store the size as a private attribute

    def calculate_area(self):
        """Calculate and return the area of the custom square."""
        return self.__size * self.__size  # Calculate area as size * size

