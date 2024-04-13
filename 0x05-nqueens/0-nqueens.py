#!/usr/bin/python3
"""
<<<<<<< HEAD
Module.
=======
Module solve n quens problem
>>>>>>> bee732e297dd696b056fc13a75ec1792b269bea3
"""
import sys


def is_valid(board, col):
    """
    Checks is the given board is valid till column col
    """
    row = board[col]
    for i in range(col):
        if board[i] == row or col - i == abs(row - board[i]):
            return False
    return True


def main(n):
    """
    Print every possible solution for the n quens problem
    """
    board = [-1 for _ in range(n)]

    board[0] = 0
    i = 0
    while True:
        if is_valid(board, i):
            if i == n - 1:
                lst = [[i, n] for i, n in enumerate(board)]
                print(lst)
                board[i] = -1
                i -= 1
            else:
                i += 1
        else:
            if board[i] >= n - 1:
                board[i] = -1
                i -= 1
        while board[i] >= n - 1 and i > 0:
            board[i] = -1
            i -= 1
        if board[i] >= n - 1 and i == 0:
            break
        board[i] += 1


if __name__ == "__main__":
    argv = sys.argv
    min_size = 4

    if (len(argv) != 2):
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(argv[1])
        if n < min_size:
            print("N must be at least 4")
            sys.exit(1)
        main(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
