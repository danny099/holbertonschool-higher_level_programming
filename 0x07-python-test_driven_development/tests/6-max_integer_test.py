#!/usr/bin/python3
"""Unittest
.
.
.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class Test(unittest.TestCase):
    """unittest
    .
    ."""

    def test1(self):
        self.assertEqual(max_integer([9, -2, 30, -4]), 30)
        self.assertEqual(max_integer([55]), 50)
        self.assertEqual(max_integer([0, -45, -60]), 0)
        self.assertEqual(max_integer([1, 2, 4, 10]), 10)
        self.assertEqual(max_integer([1, 3, 40, 20]), 40)
        self.assertEqual(max_integer([-2, -6, -8, -4]), -2)

    def test2(self):
        self.assertEqual(max_integer([1, 2, 3, float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, 2, 30, float('nan')]), 30)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer("string"), 't')
        self.assertEqual(max_integer((1, 2, 3, 40)), 40)

if __name__ == '__main__':
    unittest.main()
