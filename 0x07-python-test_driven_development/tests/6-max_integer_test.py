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

    mensaje = "'>' not supported between instances of 'str' and 'int'"

    def test_std(self):
        a = [1, 3, 5]
        self.assertEqual(max_integer(a), 5)

    def negatives(self):
        self.assertEqual(max_integer([-4, 5, -5]), 5)

    def floats(self):
        self.assertEqual(max_integer([5.65, 3, 8.493]), 8.493)

    def lists(self):
        a = [1, 2, 3]
        b = [1, 9, 3]
        c = [4, 2, 1]
        d = [a, b, c]
        self.assertEqual(max_integer(d), [4, 2, 1])

    def tuples(self):
        self.assertEqual(max_integer((14, 7, 12)), 14)

    def test_wrong_type(self):
        a = [6, 4, 'd', 6]
        with self.assertRaises(TypeError, msg=self.mensaje):
            max_integer(a)
