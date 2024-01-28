"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        self.head, self.prev = None, None
        
        def in_order(node):
            if not node:
                return None
            
            in_order(node.left)
            
            if not self.prev:
                self.head = node
            else:
                self.prev.right = node
                node.left = self.prev
            
            self.prev = node
            in_order(node.right)
        
        in_order(root)
        self.prev.right = self.head
        self.head.left = self.prev
        
        return self.head
            