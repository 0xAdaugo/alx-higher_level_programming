#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size  # Initialize the size attribute

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)  # Return the private __size attribute

    @size.setter
    def size(self, value):
        if not isinstance(value, int):  # Check if value is an integer
            raise TypeError("size must be an integer")
        elif value < 0:  # Check if value is non-negative
            raise ValueError("size must be >= 0")
        self.__size = value  # Store the value as the private __size attribute

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)  # Calculate and return the area

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):  # Loop through each row
            [print("#", end="") for j in range(self.__size)]  # Print # for each column
            print("")  # Print a newline after each row
        if self.__size == 0:  # If the size is 0, print a newline
            print("")

