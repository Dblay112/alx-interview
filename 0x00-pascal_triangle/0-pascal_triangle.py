#!/usr/bin/python3
"""
0-pascal_triangle task
"""


def pascal_triangle(n):
    """
    function that returns a list of integers
    representing the Pascal Triangle of n
    """
    k = []
    if n <= 0:
        return k
    k = [[1]]
    for i in range(1, n):
        tri = [1]
        for j in range(len(k[i - 1]) - 1):
            curr = k[i - 1]
            tri.append(k[i - 1][j] + k[i - 1][j + 1])
        tri.append(1)
        k.append(tri)
    return k
