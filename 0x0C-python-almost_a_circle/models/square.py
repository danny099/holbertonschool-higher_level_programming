#!/usr/bin/python3

"""
is a Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """is a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init a square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """property function"""
        return self.__width

    @size.setter
    def size(self, value):
        """setter function"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value
        self.__width = value

    def __str__(self):
        """str function"""
        w = self.__width
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, w)

    def update(self, *args, **kwargs):
        """str function"""
        i = 0
        for arg in args:
            i += 1
            if i == 1:
                self.id = arg
            if i == 2:
                self.__width = arg
            if i == 3:
                self.x = arg
            if i == 4:
                self.y = arg

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "size":
                self.__width = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value

    def to_dictionary(self):
        """to dictionary function"""
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["size"] = self.width
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
