#!/usr/bin/python3

def raise_exception_msg(custom_message=""):
    raise CustomNameError(custom_message)  # Raise a custom error with a given message

class CustomNameError(NameError):
    pass  # Define a custom error class based on NameError

