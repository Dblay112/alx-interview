#!/usr/bin/python3
"""
module
"""


def makeChange(coins, total):
    """ makeChange method"""
    if total <= 0:
        return 0
    dyn_prog = [0] + [float("inf")] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            dyn_prog[i] = min(dyn_prog[i], dyn_prog[i - coin] + 1)
    return dyn_prog[-1] if dyn_prog[-1] != float("inf") else -1
