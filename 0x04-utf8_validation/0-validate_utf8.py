#!/usr/bin/python3
"""
utf validator module
"""


def validUTF8(data):
    """
    function to validate if data is valid utf-8 encoding
    """
    if len(data) == 0:
        return True

    length = len(data)
    byte = 0
    num = data[0]
    while byte < 4:
        shift = 7 - byte
        bit = num >> shift & 1
        if not bit:
            break
        byte += 1
    shift = 7 - byte
    bit = num >> shift & 1
    if byte == 1 or byte > length or bit:
        return False
    if byte == 0:
        return validUTF8(data[1:])

    for i in range(1, byte):
        num = data[i]
        shift = 7 - 1
        if not (num >> 7 & 1) or (num >> shift & 1):
            return False
    return validUTF8(data[i + 1:])
