import collections
import unittest


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        looking_length = len(s1)
        s1_counts = sorted(s1)

        for i, char in enumerate(s2):
            if char in s1_counts:
                print(f's2 string: {sorted(s2[i:i+looking_length])}')
                print(f's1 string: {s1_counts}')
                if sorted(s2[i:i+looking_length]) == s1_counts:
                    return True

        return False


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.check_inclusion = Solution()

    def test_1_case(self):
        test_1 = self.check_inclusion.checkInclusion("ab", "eidbaooo")
        self.assertEqual(test_1, True)

    def test_2_case(self):
        test_2 = self.check_inclusion.checkInclusion("ab", "eidboaoo")
        self.assertEqual(test_2, False)

    def test_3_case(self):
        test_3 = self.check_inclusion.checkInclusion("adc", "dcda")
        self.assertEqual(test_3, True)
