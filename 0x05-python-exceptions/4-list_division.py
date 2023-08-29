#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []  # Initialize the list to store division results
    try:
        for i in range(list_length):  # Loop through the given range
            division_result = 0  # Initialize the division result variable
            try:
                division_result = my_list_1[i] / my_list_2[i]  # Try to perform division
            except TypeError:  # If there's a type error (e.g., dividing strings)
                print("Incorrect data type")
            except ZeroDivisionError:  # If there's a division by zero
                print("Division by zero")
            else:  # If no errors occurred
                pass  # Do nothing special
            finally:
                result_list.append(division_result)  # Append the result to the result list
    except IndexError:  # If index goes out of range
        print("Index out of range")
    else:  # If no errors occurred in the outer loop
        pass  # Do nothing special
    return result_list  # Return the list of division results

