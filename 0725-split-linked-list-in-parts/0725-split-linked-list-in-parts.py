# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next
        
        base, remainder = length // k, length % k
        res = []
        curr = head
        
        for i in range(k):
            res.append(curr)
            for j in range(base + (1 if remainder else 0) - 1):
                if not curr:
                    break
                curr = curr.next
            if curr:
                tmp = curr.next
                curr.next = None
                curr = tmp
            remainder -= 1 if remainder else 0
        
        return res