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
    stack = [0]

    for id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in stack and key != id:
                stack.append(key)
    if len(stack) == len(boxes):
        return True
    return False
