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
        if root == None:
            return None

        head = prev = None

        def in_order(curr):
            if curr == None:
                return
            
            nonlocal prev, head
            
            in_order(curr.left)
            
            if not prev:
                head = curr
                
            else:
                prev.right = curr
                curr.left = prev
                
            prev = curr
            in_order(curr.right)

        in_order(root)
        prev.right = head
        head.left = prev
        return head