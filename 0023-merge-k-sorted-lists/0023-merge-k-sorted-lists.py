# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        def merge(l1, l2):
            dummy = ListNode(0)
            curr = dummy

            while l1 or l2:
                l1_val = l1.val if l1 else float('inf')
                l2_val = l2.val if l2 else float('inf')
                if l1_val > l2_val:
                    curr.next = l2
                    l2 = l2.next if l2 else None
                else:
                    curr.next = l1
                    l1 = l1.next if l1 else None
                curr = curr.next
            
            return dummy.next
        
        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_list.append(merge(l1, l2))
            
            lists = merged_list
        
        return lists[0]
            