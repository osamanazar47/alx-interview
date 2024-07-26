#!/usr/bin/python3
"""Module for the UTF-8 validation project"""


def validUTF8(data):
    """Returns True if data is a valid UTF-8 encoding, else return False"""
    num_bytes = 0

    for num in data:
        # Convert number to 8-bit binary string
        byte = f"{num:08b}"

        if num < 0 or num > 255:
            return False

        if num_bytes == 0:
            # Determine the number of bytes for this character
            if byte.startswith('0'):
                num_bytes = 0
            elif byte.startswith('110'):
                num_bytes = 1
            elif byte.startswith('1110'):
                num_bytes = 2
            elif byte.startswith('11110'):
                num_bytes = 3
            else:
                return False
        else:
            # For continuation bytes, the prefix must be '10'
            if not byte.startswith('10'):
                return False
            num_bytes -= 1

    return num_bytes == 0
