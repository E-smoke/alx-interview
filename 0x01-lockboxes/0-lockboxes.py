#!/usr/bin/python3
"""Locked boxes module"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened or not
    Returns:
        True: if all boxes can be opened
        False: otherwise
    """
    max_idx = len(boxes) - 1
    keys = [0] + boxes[0]
    opened = [0]
    
    while keys:
        if keys[0] in opened:
            keys.remove(keys[0])
        elif keys[0] > max_idx:
            keys.remove(keys[0])
        else:
            keys += boxes[keys[0]]
            opened.append(keys[0])
            keys.remove(keys[0])
    
    if len(opened) == max_idx + 1:
        return True
    return False
