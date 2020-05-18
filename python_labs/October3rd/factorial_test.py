import unittest
from factorial import *

class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(6), 720)

if __name__ == '__main__':
    unittest.main()
