#!/usr/bin/python3
"""interpreter used/location."""
import sys


def print_func(total_size, status_code):
    """
    function to print file size, total size, and
    status code
    """
    print("File size: {}".format(total_size))
    for key, value in sorted(status_code.items()):
        if value != 0:
            print("{}: {}".format(key, value))


def main():
    """main function to use, contains status code etc"""
    status_code = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    total_size = 0
    count = 0  # keep track of inputs in stdin

    try:
        for word in sys.stdin:
            count += 1
            word = word.rstrip().rsplit(None, 2)  # Fix typo here: rsplit instead of rplit
            if len(word) < 3:  # Changed to 3, since we want at least IP, status, and byte
                continue
            status, byte = word[-2], word[-1]  # Changed to use negative indices for correct extraction
            if status in status_code:
                status_code[status] += 1
            try:
                total_size += int(byte)
            except ValueError:
                continue
            if count % 10 == 0:
                print_func(total_size, status_code)
        print_func(total_size, status_code)

    except KeyboardInterrupt:
        print_func(total_size, status_code)
        raise
