#!/usr/bin/python3
""" A rectangle blueprint """


from models.base import Base
class Rectangle(Base):
    """ A rectangle blueprint"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializer """
        self.checks(width, height, x, y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def check_int(self, attr, val):
        """ func doc """
        if not isinstance(val, int):
            raise TypeError(f"{attr} must be an integer")

    def check_positive(self, attr, val):
        """ func doc """
        if val <= 0:
            raise ValueError(f"{attr} must be > 0")

    def check_positive_zero(self, attr, val):
        """ func doc """
        if val < 0:
            raise ValueError(f"{attr} must be >= 0")

    def checks(self, width, height, x, y):
        """ func doc """
        self.check_int("width", width)
        self.check_int("height", height)
        self.check_int("x", x)
        self.check_int("y", y)
        self.check_positive("width", width)
        self.check_positive("height", height)
        self.check_positive_zero("x", x)
        self.check_positive_zero("y", y)

    @property
    def width(self):
        """width getter """
        return self.__width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @property
    def y(self):
        """ y getter"""
        return self.__y
    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Displays a rectangle based on parameters"""
        for i in range(self.__x):
            print('')
        for column in range(self.__height):
            for i in range(self.__x):
                print(' ', end='')
            print("#" * self.__width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Updates the class """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            self.id = kwargs.get("id", self.id)
            self.__width = kwargs.get("width", self.__width)
            self.__height = kwargs.get("height", self.__height)
            self.__x = kwargs.get("x", self.__x)
            self.__y = kwargs.get("y", self.__y)

    def to_dictionary(self):
        return {"id" : self.id, "width" : self.__width, "height" : self.__height, "x" : self.__x, "y" : self.__y}
