import unittest
from matrixman import *

class TestSequenceFunctions(unittest.TestCase):
    def test_fill(self):
        a = fill(2, 2, 2.0)
        self.assertEqual(a, [[2.0, 2.0],[2.0, 2.0]])

    def test_identity(self):
        a = identity(2)
        self.assertEqual(a, [[1.0, 0.0],[0.0, 1.0]])

    def test_add(self):
        a = [[1.0]*2 for _ in range(2)]
        b = [[2.0]*2 for _ in range(2)]
        self.assertEqual(add(a, b), [[3.0, 3.0],[3.0, 3.0]])

        a = [[1.0, 2.0],[3.0, 4.0]]
        b = [[2.0, 3.0],[4.0, 5.0]]
        self.assertEqual(add(a, b), [[3.0, 5.0],[7.0, 9.0]])

    def test_sub(self):
        a = [[1.0]*2 for _ in range(2)]
        b = [[2.0]*2 for _ in range(2)]
        self.assertEqual(sub(a, b), [[-1.0, -1.0],[-1.0, -1.0]])

        a = [[1.0, 2.0],[3.0, 4.0]]
        b = [[3.0, 2.0],[1.0, 0.0]]
        self.assertEqual(sub(a, b), [[-2.0, 0.0],[2.0, 4.0]])

    def test_transpose(self):
        a = [[1.0, 2.0],[3.0, 4.0]]
        self.assertEqual(transpose(a), [[1.0, 3.0],[2.0, 4.0]])

if __name__ == '__main__':
    unittest.main()
