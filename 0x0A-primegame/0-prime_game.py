#!/usr/bin/python3
"""Module for the prime game problem"""


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_up_to(n):
    primes = []
    for i in range(2, n + 1):
        if isPrime(i):
            primes.append(i)
    return primes

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = primes_up_to(n)
        turns = len(primes)

        # Maria wins if turns is odd, Ben wins if turns is even
        if turns % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
