#!/usr/bin/python3
""" A unittest module"""

import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class BaseTestCase(unittest.TestCase):
    """ base test class """
    def reset(self):
        Base.__Base__nb_objects = 0

    def test_task_one(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        b3 = Base()

        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

        b4 = Base()
        b5 = Base(16)
        b6 = Base()

        self.assertEqual(b4.id, 4)
        self.assertEqual(b5.id, 16)
        self.assertEqual(b6.id, 5)

if __name__ == "__main__":
    unittest.main()

