from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        
        # Find the middle of the linked list
        mid = self.find_middle(head)

        # Reverse the second half of the linked list
        reversed_second_half = self.reverse_list(mid.next)
        mid.next = None

        # Merge the two halves 
        self.merge_lists(head, reversed_second_half)

    def find_middle(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
        return prev

    def merge_lists(self, l1: ListNode, l2: ListNode) -> None:
        while l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2

s = Solution()
s.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))