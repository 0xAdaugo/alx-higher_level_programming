#!/usr/bin/python3

"""Define a custom Square class."""

class Square:
    """Represent a custom square."""

    def __init__(self, size=0):
        """Initialize a new custom square.
        Args:
            size (int): The size of the new custom square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the custom square."""
        return self.__size  

    @size.setter
    def size(self, value):
        if not isinstance(value, int):  # Check if 'value' is an integer
            raise TypeError("Size must be an integer")
        elif value < 0:  # Check if 'value' is non-negative
            raise ValueError("Size must be >= 0")
        self.__size = value  # Store 'value' as '__size'

    def calculate_area(self):
        """Calculate and return the area of the custom square."""
        return self.__size * self.__size

