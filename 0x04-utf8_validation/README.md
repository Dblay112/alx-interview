This module provides a function validUTF8(data) to check if a given byte sequence represents a valid UTF-8 encoding.

Functionality:

    Analyzes a list of integers representing bytes.
    Ensures each byte adheres to UTF-8 encoding rules.
    Handles single-byte (ASCII) and multi-byte characters (2-4 bytes).
    Detects invalid continuation bytes and incomplete character sequences.

Usage:
Python

import utfvalidation

data = [65]  # 'A' (single byte)
print(utfvalidation.validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]  # "Simple text!"
print(utfvalidation.validUTF8(data))  # True

data = [229, 65, 127, 256]  # Invalid byte sequence
print(utfvalidation.validUTF8(data))  # False

Benefits:

    Ensures data integrity when working with UTF-8 encoded text.
    Helps prevent errors caused by invalid byte sequences.
    Simple and easy-to-use function.

Note:

    This module focuses on basic UTF-8 validation.
    For advanced validation or character decoding, consider using external libraries.

