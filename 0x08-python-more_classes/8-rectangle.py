#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """pass"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """property"""
        return self.__width

    @property
    def height(self):
        """property"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter"""
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        if(value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter"""
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        if(value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area"""
        area = self.__height * self.__width
        return area

    def perimeter(self):
        """perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        perimeter = (self.__height * 2) + (self.__width * 2)
        return perimeter

    def __str__(self):
        """print"""
        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.width):
                rectangle += str(self.print_symbol)
            if i < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """repr"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """del"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not(isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not(isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2