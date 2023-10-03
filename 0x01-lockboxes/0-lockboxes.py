#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes
"""


def canUnlockAll(boxes):
    """
    A method that determines if all the boxes can be opened
    """
    n = len(boxes)  # Number of boxes
    opened = [False] * n  # Initialize all boxes as unopened
    opened[0] = True

    stack = [0]
    while stack:
        currBox = stack.pop()
        for key in boxes[currBox]:
            if not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)