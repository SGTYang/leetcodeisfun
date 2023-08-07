# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy
        
        def get_kth(node, k):
            while node and k > 0:
                k -= 1
                node = node.next
            
            return node
        
        while True:
            kth = get_kth(tail, k)
            if not kth:
                break
            nxt = kth.next
            curr = tail.next
            prev = kth.next
            
            while curr != nxt:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = tail.next
            tail.next = kth
            tail = tmp
        
        return dummy.next
            