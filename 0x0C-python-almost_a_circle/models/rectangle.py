#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor"""
        super().__init__(id=id)

        self.validate("width", width)
        self.validate("height", height)
        self.validate("x", x)
        self.validate("y", y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """Converts the rectangle object to a dictionary"""
        return {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "id": self.id,
        }

    def update(self, *args, **kwargs):
        """Updates attributes id, width, height, x and y using args"""
        if not args:
            props = ("id", "width", "height", "x", "y")
            for key, value in kwargs.items():
                if key in props:
                    setattr(self, key, value)
            return

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(end=" ")
            for _ in range(self.width):
                print("#", end="")
            print()

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return self.width * self.height

    def validate(self, name: str, value):
        """Integer validation for width, height, x, y"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name in ("width", "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if name in ("x", "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        return True

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        self.validate("width", width)
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        self.validate("height", height)
        self.__height = height

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self.validate("y", y)
        self.__y = y

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.validate("x", x)
        self.__x = x
