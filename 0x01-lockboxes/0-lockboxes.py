#!/usr/bin/python3

"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
    - boxes (list of lists): Each box is represented as a list of keys that can
      open other boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """

    # Correct indentation for the function body
    v_boxes = [False] * len(boxes)  # Create a list to track visited boxes
    v_boxes[0] = True  # Mark the first box as visited

    queued_boxes = [0]  # Initialize a queue with the first box

    while queued_boxes:
        c_box = queued_boxes.pop(0)  # Get the next box from the queue

        for key in boxes[c_box]:
            if not v_boxes[key]:  # If the box hasn't been visited yet
                v_boxes[key] = True  # Mark it as visited
                queued_boxes.append(key)  # Add it to the queue for exploration

    return all(v_boxes)  # Check if all boxes have been visited
