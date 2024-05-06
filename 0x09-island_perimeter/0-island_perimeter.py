#!/usr/bin/python3
"""module"""


def island_perimeter(grid):
    """function that returns the perimeter of
    the given island"""
    perimeter = 0
    for row in grid + list(map(list, zip(*grid))):
        for x1, x2 in zip([0] + row, row + [0]):
            perimeter += int(x1 != x2)
    return perimeter
