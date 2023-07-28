# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left, right = head, self.get_mid(head)
        tmp = right.next 
        right.next = None
        right = tmp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left, right)
    
    # Split
    def get_mid(self, node):
        slow, fast = node, node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
        
    def merge(self, node1, node2):
        dummy = ListNode()
        curr = dummy

        while node1 and node2:
            if node1.val > node2.val:
                curr.next = node2
                curr = curr.next
                node2 = node2.next
            else:
                curr.next = node1
                curr = curr.next
                node1 = node1.next

        if node1:
            curr.next = node1
        if node2:
            curr.next = node2

        return dummy.next