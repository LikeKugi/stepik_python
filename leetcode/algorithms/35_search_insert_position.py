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
            return start


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.binary_search = Solution()

    def test_1_case(self):
        first_case = self.binary_search.search([1, 3, 5, 6], 5)
        self.assertEqual(first_case, 2)

    def test_2_case(self):
        second_case = self.binary_search.search([1, 3, 5, 6], 2)
        self.assertEqual(second_case, 1)

    def test_3_case(self):
        third_case = self.binary_search.search([1, 3, 5, 6], 7)
        self.assertEqual(third_case, 4)


if __name__ == '__main__':
    unittest.main()
