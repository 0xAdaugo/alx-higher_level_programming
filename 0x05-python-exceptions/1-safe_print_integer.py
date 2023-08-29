#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # Try to print the value as an integer
        printed = True  # If successful, set printed to True
    except Exception:  # If there's an error, like a non-integer value
        printed = False  # Set printed to False
    return printed  # Return whether the integer was printed successfully or not

