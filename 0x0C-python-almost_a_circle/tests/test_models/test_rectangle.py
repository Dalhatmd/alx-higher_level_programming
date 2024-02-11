#!/usr/bin/python3
""" unittests for rectangle class """
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class RectangleTest(unittest.TestCase):
    """ Rectangle test cases """
    def reset(self):
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 5)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)

        with self.assertRaises(ValueError):
            r3 = Rectangle(-1, 5)

        with self.assertRaises(TypeError):
            r4 = Rectangle("4", 5)

        r5 = Rectangle(5, 5)
        self.assertEqual(r5.area(), 25)

if __name__ == "__main__":
    unittest.main
