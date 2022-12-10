import unittest
from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        matrix = [[0] * n for _ in range(m)]
        print(matrix)
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    q = self.find_closest_zero(mat, i, j)
                    print(q)
                    matrix[i][j] = q
        return matrix

    def find_closest_zero(self, mat: List[List[int]], i: int, j: int) -> int:
        m = len(mat)
        n = len(mat[0])
        current = deque([(i, j)])
        next = deque([])
        counter = 0
        used = set()
        while current:

            if current[0]:
                ii, jj = current[0]
                print(current[0])
                if mat[ii][jj] == 0:
                    return counter
            if ii > 0 and (ii - 1, jj) not in used:
                next.append((ii - 1, jj))
            if jj > 0 and (ii, jj - 1) not in used:
                next.append((ii, jj - 1))
            if ii < m - 1 and (ii + 1, jj) not in used:
                next.append((ii + 1, jj))
            if jj < n - 1 and (ii - 1, jj) not in used:
                next.append((ii, jj + 1))
            used.add(current[0])
            current.popleft()

            if not current:
                current.extend(next)
                next.clear()
                counter += 1
            print(current)
        else:
            return -1


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.matrix = Solution()

    def test_1_case(self):
        test_1 = self.matrix.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        self.assertEqual(test_1, [[0, 0, 0], [0, 1, 0], [0, 0, 0]])

    def test_2_case(self):
        test_2 = self.matrix.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
        self.assertEqual(test_2, [[0, 0, 0], [0, 1, 0], [1, 2, 1]])
