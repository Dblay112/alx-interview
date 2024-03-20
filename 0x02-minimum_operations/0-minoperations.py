#!/usr/bin/python3

"""interpreter usage"""


def minOperations(n):
    """function that calculates the  number of operations
    needed to give a result of exactly n H characters.
    """

    if n <= 1:
        return 0

    min_num = 0
    even_number = 2

    while even_number <= n:
        if n % even_number == 0:
            min_num += even_number
            n = n // even_number
        else:
            even_number += 1

    return min_num
