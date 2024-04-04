#!/usr/bin/python3
"""utf-8 validator module"""


def validUTF8(data):
  """function that determines if a given
  data set represents a valid UTF-8 encoding"""
  i = 0
  for num in data:
    byte = num & 0xFF
    if i > 0 and (byte & 0xC0) != 0x80:
      return False
    if (byte & 0x80) == 0:
      i = 0
    elif (byte & 0xE0) == 0xC0:
      i = 1
    elif (byte & 0xF0) == 0xE0:
      i = 2
    elif (byte & 0xF8) == 0xF0:
      i = 3
    else:
      return False
    if i > 0 and i < data.index(byte) + 1 - len(data):
      return False
  return i == 0
