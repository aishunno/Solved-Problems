class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeLists(l1, l2):
        dummy = ListNode()
        node = dummy

        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        if l1:
            node.next = l1
        if l2:
            node.next = l2

        return dummy.next   

mergeLists(ListNode(1, ListNode(4, ListNode(5, None))), ListNode(1, ListNode(3, ListNode(4, None))))  