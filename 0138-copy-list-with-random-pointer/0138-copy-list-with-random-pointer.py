"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache = {None:None}
        
        curr = head
        while curr:
            cache[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            cache[curr].next = cache[curr.next]
            cache[curr].random = cache[curr.random]
            curr = curr.next
        
        return cache[head]