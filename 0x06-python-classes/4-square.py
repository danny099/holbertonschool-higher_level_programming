#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """init
        Description: init size
        Args:
             arg1 (size): size of square"""
        self.size = size

    def area(self):
        """Return area"""
        return self.__size * self.__size

    @property
    def size(self):
        """property"""
        return self.__size

    @size.setter
    def size(self, value):
        if not(isinstance(value, int)):
            raise TypeError("size must be an integer")
        if(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
