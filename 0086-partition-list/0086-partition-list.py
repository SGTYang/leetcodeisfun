# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Quick select
        left = ListNode()
        right = ListNode()
        l_tail, r_tail = left, right
        
        curr = head
        
        while curr:
            if curr.val < x:
                l_tail.next = curr
                l_tail = l_tail.next
            else:
                r_tail.next = curr
                r_tail = r_tail.next
            curr = curr.next
        
        l_tail.next = right.next
        r_tail.next = None
        return left.next
        