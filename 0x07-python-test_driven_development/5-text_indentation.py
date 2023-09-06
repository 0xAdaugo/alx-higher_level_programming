#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string, otherwise raise a TypeError
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    # Skip leading spaces in the text
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")  # Print two new lines after '.', '?', and ':'
            c += 1
            # Skip spaces after punctuation or new line
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1

