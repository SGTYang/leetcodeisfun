# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        cnt = 0
        while curr:
            cnt += 1
            curr = curr.next
        
        if cnt == n:
            return head.next
        
        curr = head
        for i in range(cnt - n - 1):
            curr = curr.next
        curr.next = curr.next.next
        return head