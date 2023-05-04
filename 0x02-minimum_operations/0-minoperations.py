#!/usr/bin/python3
""" minimum operation challenge"""


def minOperations(n):
    """calculate the lowest number of operation needed"""
    no_of_chars = 1  # number of characters in the file
    counter = 0     # number of operation performed
    no_of_copy = 0  # number of 'H's copied

    while no_of_chars < n:
        if no_of_copy == 0:
            no_of_copy = no_of_chars
            counter += 1

        if no_of_chars == 1:
            no_of_chars += no_of_copy
            counter += 1
            continue

        remaining = n - no_of_chars
        if remaining < no_of_copy:
            return 0

        if remaining % no_of_chars != 0:
            no_of_chars += no_of_copy
            counter += 1
        else:
            no_of_copy = no_of_chars
            no_of_chars += no_of_copy
            counter += 2

    if no_of_chars == n:
        return counter
    else:
        return 0
