# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        if length == n:
            return head.next
        
        target = length - n
        curr = head
        cnt = 1
        
        while curr:
            if cnt == target:
                curr.next = curr.next.next
                break
            curr = curr.next
            cnt += 1
        return head