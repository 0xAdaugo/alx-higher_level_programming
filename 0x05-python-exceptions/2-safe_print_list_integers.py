#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0  # Initialize the count of successfully printed integers
    for index in range(x):  # Loop through the given range
        try:
            print("{:d}".format(my_list[index]), end="")  # Try to print an integer
            printed_count += 1  # Increase the count of successfully printed integers
        except (ValueError, TypeError):  # If there's an error, like a non-integer value
            pass  # Just continue to the next iteration
    print()  # Print a newline after printing all integers
    return printed_count  # Return the count of successfully printed integers

