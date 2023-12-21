# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = head
        n = 0
        
        while curr:
            n += 1
            curr = curr.next
            
        n = n//2
        curr = dummy
        while n:
            head = head.next
            curr = curr.next
            n -= 1
        
        curr.next = head.next
        
        return dummy.next