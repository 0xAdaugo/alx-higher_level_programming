#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request, and displays
the value of the X-Request-Id variable found in the header
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else input("Enter URL: ")
    with urllib.request.urlopen(url) as response:
        request_id = response.getheader('X-Request-Id')
        if request_id:
            print(f"The value of X-Request-Id: {request_id}")
        else:
            print("X-Request-Id not found in the header")

