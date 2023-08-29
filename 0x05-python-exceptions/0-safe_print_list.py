#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_count = 0  # Initialize the count of printed items
    try:
        for index in range(x):  # Loop through the given range
            print("{}".format(my_list[index]), end='')  # Print the item
            printed_count += 1  # Increase the count of printed items
    except Exception:  # If there's an error, don't worry
        pass
    finally:
        print()  # Print a newline after the loop
    return printed_count  # Return the total number of printed items

