#!/usr/bin/python3

"""
module for Reactangle class
"""


from models.base import Base


class Rectangle(Base):
    """one base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init a base"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """property function"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """property function"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter function"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """property function"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter function"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property function"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter function"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area function"""
        return self.__width * self.__height

    def display(self):
        """display function"""
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """str function"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """update function"""
        i = 0
        for arg in args:
            i += 1
            if i == 1:
                self.id = arg
            if i == 2:
                self.__width = arg
            if i == 3:
                self.__height = arg
            if i == 4:
                self.__x = arg
            if i == 5:
                self.__y = arg

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "width":
                self.__width = value
            if key == "height":
                self.__height = value
            if key == "x":
                self.__x = value
            if key == "y":
                self.__y = value

    def to_dictionary(self):
        """to dictionary function"""
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["width"] = self.width
        dictionary["height"] = self.height
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
