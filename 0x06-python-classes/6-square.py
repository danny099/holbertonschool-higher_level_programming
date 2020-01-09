#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """init
        Description: init size
        Args:
             arg1 (size): size of square
             arg2 (position): position square"""
        self.size = size
        self.position = position

    def area(self):
        """Return area"""
        return self.__size * self.__size

    @property
    def size(self):
        """property"""
        return self.__size

    @property
    def position(self):
        """property"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        if not(isinstance(value, int)):
            raise TypeError("size must be an integer")
        if(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print square with #"""
        sz = self.__size
        ps = self.__position
        if sz == 0:
            print("")
            return

        for r in range(ps[1]):
            print("")
        for i in range(sz):
            for spc in range(ps[0]):
                print(" ", end="")
            for j in range(sz):
                print("#", end="")
            print("")
