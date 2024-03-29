#!/usr/bin/python3
"""
interpreter used.
"""
import sys


def print_funct(total_size, status_code):
    """
    function to print file size and status code
    """
    print("File size: {}".format(total_size))
    for key, value in sorted(status_code.items()):
        if value != 0:
            print("{}: {}".format(key, value))


def main():
    """
    Main function containing status code etc.
    """
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
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            line = line.rsplit(None, 2)
            if len(line) < 2:
                continue
            status, byte = line[1], line[2]
            if status in status_code:
                status_code[status] += 1
            try:
                total_size += int(byte)
            except ValueError:
                continue
            if count % 10 == 0:
                print_funct(total_size, status_code)
        print_funct(total_size, status_code)

    except KeyboardInterrupt:
        print_funct(total_size, status_code)
        raise


if __name__ == "__main__":
    main()
