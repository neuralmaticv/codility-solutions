import unittest
from stoneWall import solution


class testSolution(unittest.TestCase):
    def test(self):
        arr = [8, 8, 5, 7, 9, 8, 7, 4, 8]
        res = solution(arr)
        self.assertEqual(res, 7)


if __name__ == '__main__':
    unittest.main()