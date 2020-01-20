#!/usr/bin/python3
"""class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square"""

    def __init__(self, size):
        """init"""
        super().integer_validator("size", size)
        super().__init__(size, size)
