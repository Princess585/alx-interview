#!/usr/bin/python3
"""
The module that used to add two arrays
"""


def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    opened_boxes = set([0])
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and key not in opened_boxes:
                opened_boxes.add(key)
                queue.append(key)

    return len(opened_boxes) == n
