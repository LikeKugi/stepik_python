import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word[::-1] for word in s.split()]
        return ' '.join(words)


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.reverse_words = Solution()

    def test_1_case(self):
        first_test = self.reverse_words.reverseWords("Let's take LeetCode contest")
        self.assertEqual(first_test, "s'teL ekat edoCteeL tsetnoc")

    def test_2_case(self):
        second_test = self.reverse_words.reverseWords("God Ding")
        self.assertEqual(second_test, "doG gniD")


if __name__ == '__main__':
    unittest.main()
