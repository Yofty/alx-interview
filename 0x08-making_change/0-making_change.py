#!/usr/bin/python3
"""A function to determine the fewest number of coins needed"""


def makeChange(coins, total):
    """this function will take list of coins and calculate total"""
    if total <= 0:
        return 0
    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
