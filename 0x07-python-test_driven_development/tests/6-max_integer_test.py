#!/usr/bin/python3
"""
Using unit test to find max int
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TextMaxInteger(unittest.TestCase):

    def text_ismax(self):
        self.assertEqual(max_integer([5, 12, 2, -6]), 12)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([12]), 12)
        self.assertEqual(max_integer([12, 1, 2, -6]), 12)
        self.assertEqual(max_integer(5, 1, 2, 12]), 12)
        self.assertEqual(max_integer([-5, -12, -2, -6]), -2)

    def test_isint(self):
        self.assertIsInstance(max_integer([5, 7, 3, -1]), int)
        self.assertIs(max_integer([]), None)

    if __name__ == "__main__":
        unittest.main()
