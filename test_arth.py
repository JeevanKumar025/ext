import unittest
from arth import *

class ArithmeticTesting(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5,5), 10)
    def test_sub(self):
        self.assertEqual(sub(5,5), 0)
    def test_mul(self):
        self.assertEqual(mul(5,5), 25)

if __name__ == "__main__":
    unittest.main()