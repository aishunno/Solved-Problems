from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left, right = dummy, head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete 
        left = left.next.next

        return dummy.next

s = Solution()
print(s.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2))