#!/usr/bin/python3
"""Module for task (finding the minimum number of coins)"""


def makeChange(coins, total):
    """A function that returns the minimum num of coins"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total >= coin:
            num_coins = total // coin
            count += num_coins
            total -= num_coins * coin
        if total == 0:
            return count

    return -1 if total > 0 else count
