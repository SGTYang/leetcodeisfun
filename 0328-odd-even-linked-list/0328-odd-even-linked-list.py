# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = ListNode()
        curr = dummy
        odd = prev
        n = 1
        
        while head:
            if n % 2 == 0:
                odd.next = head
                odd = odd.next
            else:
                curr.next = head
                curr = curr.next
            head = head.next
            n += 1
            
        odd.next = None
        curr.next = prev.next
        
        return dummy.next