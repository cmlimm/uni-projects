import unittest
from matrixman import *

class TestSequenceFunctions(unittest.TestCase):
    def test_fill(self):
        a = fill(2, 2, 2.0)
        self.assertEqual(a, [[2.0, 2.0],[2.0, 2.0]])

        self.assertRaises(TypeError, fill, 2.5, 2, 2.0)
        self.assertRaises(TypeError, fill, 2, 2.5, 2.0)

    def test_identity(self):
        a = identity(2)
        self.assertEqual(a, [[1.0, 0.0],[0.0, 1.0]])

        self.assertRaises(TypeError, identity, 2.5)

    def test_add(self):
        a = [[1.0]*2 for _ in range(2)]
        b = [[2.0]*2 for _ in range(2)]
        self.assertEqual(add(a, b), [[3.0, 3.0],[3.0, 3.0]])

        a = [[1.0, 2.0],[3.0, 4.0]]
        b = [[2.0, 3.0],[4.0, 5.0]]
        self.assertEqual(add(a, b), [[3.0, 5.0],[7.0, 9.0]])

        a = [[1.0, 2.0],[3.0, 4.0]]
        b = [[2.0, 3.0],[4.0, 5.0],[4.0, 5.0]]
        self.assertRaises(ValueError, add, a, b)

        a = [["b", 2.0],[3.0, 4.0]]
        b = [[2.0, 3.0],[4.0, 5.0]]
        self.assertRaises(TypeError, add, a, b)

    def test_sub(self):
        a = [[1.0]*2 for _ in range(2)]
        b = [[2.0]*2 for _ in range(2)]
        self.assertEqual(sub(a, b), [[-1.0, -1.0],[-1.0, -1.0]])

        a = [[1.0, 2.0],[3.0, 4.0]]
        b = [[3.0, 2.0],[1.0, 0.0]]
        self.assertEqual(sub(a, b), [[-2.0, 0.0],[2.0, 4.0]])

        a = [[1.0, 2.0],[3.0, 4.0]]
        b = [[2.0, 3.0],[4.0, 5.0],[4.0, 5.0]]
        self.assertRaises(ValueError, sub, a, b)

        a = [["b", 2.0],[3.0, 4.0]]
        b = [[2.0, 3.0],[4.0, 5.0]]
        self.assertRaises(TypeError, sub, a, b)

    def test_transpose(self):
        a = [[1.0, 2.0],[3.0, 4.0]]
        self.assertEqual(transpose(a), [[1.0, 3.0],[2.0, 4.0]])

        a = [["b", 2.0],[3.0, 4.0]]
        self.assertRaises(TypeError, transpose, a)

    def test_mult(self):
        a = [[1.0, 2.0],[3.0, 4.0]]
        self.assertEqual(mult(a, 2.0), [[2.0, 4.0],[6.0, 8.0]])

        a = [["b", 2.0],[3.0, 4.0]]
        self.assertRaises(TypeError, mult, a, 20)

    def test_negative(self):
        a = [[1.0, 2.0],[3.0, 4.0]]
        self.assertEqual(negative(a), [[-1.0, -2.0],[-3.0, -4.0]])

        a = [["b", 2.0],[3.0, 4.0]]
        self.assertRaises(TypeError, negative, a)

    def test_dot(self):
        a = [[1.0, 2.0],[3.0, 4.0]]
        b = [[2.0, 3.0],[4.0, 5.0]]
        self.assertEqual(dot(a, b), [[10.0, 13.0],[22.0, 29.0]])

        a = [[1.0, 2.0],[3.0, 4.0]]
        b = [[2.0, 3.0],[4.0, 5.0],[4.0, 5.0]]
        self.assertRaises(ValueError, dot, a, b)

        a = [["b", 2.0],[3.0, 4.0]]
        b = [[2.0, 3.0],[4.0, 5.0]]
        self.assertRaises(TypeError, dot, a, b)

if __name__ == '__main__':
    unittest.main()
