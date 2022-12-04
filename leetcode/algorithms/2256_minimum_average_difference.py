import math
import unittest
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        min_index = 0
        n = len(nums)
        current_sum = 0
        current_min_average = math.inf

        for i in range(n):
            current_sum += nums[i]

            left_sum_average = current_sum // (i+1)
            right_sum_average = (total_sum - current_sum) // (n - i - 1) if i != n-1 else 0

            if current_min_average > (cd:= abs(left_sum_average - right_sum_average)):
                current_min_average = cd
                min_index = i
        return min_index


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.min_average = Solution()

    def test_1_case(self):
        test_1 = self.min_average.minimumAverageDifference([2, 5, 3, 9, 5, 3])
        self.assertEqual(test_1, 3)

    def test_2_case(self):
        test_2 = self.min_average.minimumAverageDifference([0])
        self.assertEqual(test_2, 0)

    def test_3_case(self):
        test_3 = self.min_average.minimumAverageDifference([0, 0, 0, 0, 0])
        self.assertEqual(test_3, 0)

    def test_4_case(self):
        test_4 = self.min_average.minimumAverageDifference([0, 1, 0, 1, 0, 1])
        self.assertEqual(test_4, 0)


if __name__ == '__main__':
    unittest.main()
