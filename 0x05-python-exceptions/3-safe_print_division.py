#!/usr/bin/python3

def safe_print_division(a, b):
    division_result = None  # Initialize the division result variable
    try:
        division_result = a / b  # Try to perform the division
    except:  # If there's an error, like division by zero
        pass  # Ignore the error and continue
    finally:
        print("Calculated result: {}".format(division_result))  # Print the result, even if it's None
    return division_result  # Return the division result, even if it's None

