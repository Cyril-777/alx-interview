#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    num_bytes = 0

    for byte in data:
        # Check if the byte is a valid UTF-8 start byte
        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False  # Invalid start byte
        else:
            # Check if the byte is a valid UTF-8 continuation byte
            if (byte >> 6) != 0b10:
                return False

            num_bytes -= 1

    # If there are remaining bytes, it's an incomplete character
    return num_bytes == 0
