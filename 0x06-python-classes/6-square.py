#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size  # Initialize the size attribute
        self.position = position  # Initialize the position attribute

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

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)  # Return the private __position attribute

    @position.setter
    def position(self, value):
        # Check if value is a valid tuple of 2 positive integers
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Store the value as the private __position attribute

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)  # Calculate and return the area

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:  # If size is 0, print a newline and return
            print("")
            return

        [print("") for i in range(0, self.__position[1])]  # Print newlines for vertical offset
        for i in range(0, self.__size):  # Loop through each row of the square
            [print(" ", end="") for j in range(0, self.__position[0])]  # Print spaces for horizontal offset
            [print("#", end="") for k in range(0, self.__size)]  # Print # for each column of the square
            print("")  # Print a newline after each row

