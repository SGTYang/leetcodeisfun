# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, length = head, 0
        while curr:
            curr = curr.next
            length = length + 1
            
        if length == n : return head.next
        
        curr = head
        
        for i in range(1, length-n):
            curr = curr.next
        curr.next = curr.next.next
        return head
