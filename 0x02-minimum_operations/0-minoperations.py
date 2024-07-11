#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n: int) -> int:
    '''minOperations'''
    count = 2
    no_H = 2
    paste = 1
    if n <= 1:
        return 0
    while no_H != n:
        if n % no_H == 0:
            paste = no_H
            count += 2
            no_H *= 2
        else:
            count += 1
            no_H += paste
    return count
