import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        else:
            return -1


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.binary_search = Solution()

    def test_1_case(self):
        first_case = self.binary_search.search([-1, 0, 3, 5, 9, 12], 9)
        self.assertEqual(first_case, 4)

    def test_2_case(self):
        second_case = self.binary_search.search([-1, 0, 3, 5, 9, 12], 2)
        self.assertEqual(second_case, -1)

    def test_3_case(self):
        third_case = self.binary_search.search([5], 5)
        self.assertEqual(third_case, 0)

    def test_4_case(self):
        fourth_case = self.binary_search.search([2, 5], 5)
        self.assertEqual(fourth_case, 1)


if __name__ == '__main__':
    unittest.main()
