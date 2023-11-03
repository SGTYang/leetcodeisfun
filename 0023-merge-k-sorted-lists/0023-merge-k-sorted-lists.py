# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1, l2):
            dummy = ListNode()
            curr = dummy
            
            while l1 or l2:
                l1_val = l1.val if l1 else float('inf')
                l2_val = l2.val if l2 else float('inf')
                
                if l1_val > l2_val:
                    curr.next = l2
                    l2 = l2.next
                else:
                    curr.next = l1
                    l1 = l1.next
                
                curr = curr.next
            
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            
            return dummy.next
        
        while len(lists) > 1:
            dummy_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                dummy_list.append(merge(l1, l2))
            
            lists = dummy_list
        
        return lists[0] if lists else None