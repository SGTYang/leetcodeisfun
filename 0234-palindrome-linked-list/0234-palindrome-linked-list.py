# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev, fast, slow = None, head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow, prev, prev.next = slow.next, slow, prev
            
        tail = slow.next if fast else slow
        
        while prev:
            if tail.val != prev.val:
                return False
            tail = tail.next
            prev = prev.next
        
        return True