import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        start_pointer = 0
        max_len = 0

        for i, char in enumerate(s):
            # print(characters)
            # print(char)
            # print(start_pointer)
            if char in characters:
                print(f'Repeated: {char} index: {i} start {start_pointer}')
                print(characters)
                if (l := i-start_pointer) > max_len:
                    max_len = l
                for j in range(start_pointer, i):
                    print(characters)
                    print(f'lf: {char} removing: {s[j]}')
                    characters.remove(s[j])
                    start_pointer += 1
                    if s[j] == char:

                        print(f'out: {characters}')
                        break
            characters.add(char)
            print(s)
            print(f'Start = {start_pointer}, Current = {i}')
            print('/------------------------------------------/')
        else:
            if (l := len(s) - start_pointer) > max_len:
                max_len = l

        print(max_len)
        return max_len


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.length_longest = Solution()

    def test_1_case(self):
        test_1 = self.length_longest.lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(test_1, 3)

    def test_2_case(self):
        test_2 = self.length_longest.lengthOfLongestSubstring("bbbbb")
        self.assertEqual(test_2, 1)

    def test_3_case(self):
        test_3 = self.length_longest.lengthOfLongestSubstring("pwwkew")
        self.assertEqual(test_3, 3)

    def test_4_case(self):
        test_4 = self.length_longest.lengthOfLongestSubstring(" ")
        self.assertEqual(test_4, 1)


if __name__ == '__main__':
    unittest.main()
