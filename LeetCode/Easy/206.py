from hashlib import new
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        # If the head is not available or head is the only node 
        if head is None or head.next is None:
            return head

        previous_node = head
        current_node = head.next

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node

        head.next = None
        head = previous_node
        return head

sl = Solution()
newNode = sl.reverseList(ListNode(1, ListNode(2, (ListNode(3)))))
print(newNode.val)