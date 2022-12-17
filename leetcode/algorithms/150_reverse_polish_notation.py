import unittest
from typing import List
from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque([])
        for el in tokens:
            print(stack)
            if el.replace('-', '').isdigit():
                stack.append(el)
            else:
                y = stack.pop()
                x = stack.pop()
                print(f'{x} {el} {y}')
                z = int(eval(f'{x} {el} {y}'))
                stack.append(str(z))
        print(stack)
        return int(stack[-1])


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.evolution = Solution()

    def test_1_case(self):
        test1 = self.evolution.evalRPN(["2", "1", "+", "3", "*"])
        self.assertEqual(test1, 9)

    def test_2_case(self):
        test2 = self.evolution.evalRPN(["4", "13", "5", "/", "+"])
        self.assertEqual(test2, 6)

    def test_3_case(self):
        test3 = self.evolution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
        self.assertEqual(test3, 22)


if __name__ == '__main__':
    unittest.main()
