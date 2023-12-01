#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
"""
import urllib.request
import sys

def get_request_id(url):
    with urllib.request.urlopen(url) as response:
        header_info = response.info()
        request_id = header_info.get('X-Request-Id')
        if request_id:
            print(f"The value of X-Request-Id: {request_id}")
        else:
            print("X-Request-Id not found in the header")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_url = sys.argv[1]
        get_request_id(input_url)
    else:
        print("Please provide a URL as an argument")

