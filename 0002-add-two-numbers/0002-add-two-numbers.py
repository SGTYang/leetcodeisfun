# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        successor = 0
        
        while l1 or l2 or successor:
            if l1:
                left = l1.val
            else:
                left = 0
                
            if l2:
                right = l2.val
            else:
                right = 0
                
            s = left + right + successor
            
            successor = s // 10
            rest = s % 10
            
            curr.next = ListNode(rest)
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        
        return dummy.next
            