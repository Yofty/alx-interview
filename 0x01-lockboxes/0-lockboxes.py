#!/usr/bin/python3
"""return n number"""


def canUnlockAll(boxes):
    """determines if yopu can open all the lockboxes"""
    unlocked = set()

    for box_id, box in enumerate(boxes):
        if len(box) == 0 or box_id == 0:
            unlocked.add(box_id)
        for key in box:
            if key < len(boxes) and key != box_id:
                unlocked.add(key)
        if len(unlocked) == len(boxes):
            return True
    return False
