#!/usr/bin/python3
"""interpreter used/location"""
import sys


def print_func(total_size, status_code):
    """
    function to print file size,total size and
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
    count = 0 #keep track of inputs in stdin

    try:
      for word in sys.stdin
      count += 1
      word = word.rplit(None, 2)
      if len(word) < 2:
        continue
      status, byte = word[1], word[2]
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


if __name__ == "__main__":
    main()
