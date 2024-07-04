#!/usr/bin/python3


def canUnlockAll(boxes):
    listOfKeys = [0]  # Start with the first key
    keys = set([0])   # A set to keep track of all unique keys
    
    for i in listOfKeys:
        for key in boxes[i]:
            if key not in keys and key < len(boxes):
                keys.add(key)
                listOfKeys.append(key)

    return len(keys) == len(boxes)
