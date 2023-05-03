# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left, right)
        
    def getMid(self, node):
        slow, fast = node, node.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
    
    def merge(self, left, right):
        dummy = ListNode(0)
        curr = dummy
        
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            
            curr = curr.next
        
        if left:
            curr.next = left

        if right:
            curr.next = right
            
        return dummy.next