import unittest
from fish import solution


class testSolution(unittest.TestCase):
    def test(self):
        arrA = [4, 3, 2, 1, 5, 6]
        arrB = [0, 1, 0, 0, 1, 0]
        res = solution(arrA, arrB)
        self.assertEqual(res, 2)


if __name__ == '__main__':
    unittest.main()
