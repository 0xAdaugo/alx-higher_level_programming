#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
"""
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            request_id = response.getheader('X-Request-Id')
            if request_id:
                print(f"The value of X-Request-Id: {request_id}")
            else:
                print("X-Request-Id not found in the header")
    else:
        print("Please provide a URL as an argument")

