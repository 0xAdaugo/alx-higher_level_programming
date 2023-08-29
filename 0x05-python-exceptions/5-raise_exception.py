#!/usr/bin/python3

def raise_exception():
    raise CustomTypeError("Custom exception raised")  # Raise a custom exception

class CustomTypeError(Exception):
    pass  # Define a custom exception class

