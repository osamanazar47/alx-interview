#!/usr/bin/python3
"""Module for task (finding the minimum number of coins)"""


def makeChange(coins, total):
    """A function that returns the minimum num of coins"""
    if total <= 0:
        return 0
    coins = sorted(coins)
    coins.reverse()
    count = 0
    for coin in coins:
        if total < coin:
            return -1
        while coin <= total:
            count += 1
            total -= coin
            if total == 0:
                return count

    return count
