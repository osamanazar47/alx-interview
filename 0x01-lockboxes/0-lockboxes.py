#!/usr/bin/python3
""" A function to determine if all the boxes can be unlocked or not """
def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of list of int): A list of boxes, each containing a list of keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.

    Example:
        >>> canUnlockAll([[1], [2], [3], []])
        True
        >>> canUnlockAll([[1, 2], [3], [4], []])
        False
    """
    # Start with the first key
    listOfKeys = [0]
    # A set to keep track of all unique keys
    keys = set([0])

    # Iterate over each key in listOfKeys
    for i in listOfKeys:
        # Check each key in the current box
        for key in boxes[i]:
            # If the key is new and within the range of boxes, add it to the set and list
            if key not in keys and key < len(boxes):
                keys.add(key)
                listOfKeys.append(key)

    # Return True if the number of unique keys equals the number of boxes
    return len(keys) == len(boxes)
