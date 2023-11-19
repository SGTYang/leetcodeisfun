# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_k(node, k):
            while node and k:
                k -= 1
                node = node.next
            return node
            
        dummy = ListNode(0, head)
        tail = dummy
        
        while True:
            k_node = get_k(tail, k)
            if not k_node:
                break
            
            nxt = k_node.next
            prev = k_node.next
            curr = tail.next
            
            while curr != nxt:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = tail.next
            tail.next = k_node
            tail = tmp
        
        return dummy.next