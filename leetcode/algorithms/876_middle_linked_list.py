from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        middle_node = 0
        current_pointer = 0
        middle_pointer = 0
        while current_node:
            current_node = current_node.next
            # print(current_node)
            current_pointer += 1
            # print(current_pointer)
            middle_pointer = current_pointer // 2
            # print(f'middle: {middle_pointer}')

        middle_node = head
        for _ in range(middle_pointer):
            middle_node = middle_node.next
        return middle_node


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.middle_node = Solution()

    def test_1_case(self):
        head = [1, 2, 3, 4, 5]
        test_1 = self.middle_node.middleNode(head)
        self.assertEqual(test_1, [[3, 4, 5]])

    def test_2_case(self):
        head = [1, 2, 3, 4, 5, 6]
        test_2 = self.middle_node.middleNode(head)
        self.assertEqual(test_2, [4, 5, 6])

