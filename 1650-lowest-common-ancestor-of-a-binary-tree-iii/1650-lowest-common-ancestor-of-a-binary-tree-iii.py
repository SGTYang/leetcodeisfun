"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        def get_depth(p):
            depth = 0
            while p:
                p = p.parent
                depth += 1
            
            return depth
        
        p_depth = get_depth(p)
        q_depth = get_depth(q)
        
        for i in range(p_depth - q_depth):
            p = p.parent
        
        for i in range(q_depth - p_depth):
            q = q.parent
        
        while p != q:
            p = p.parent
            q = q.parent
        
        return p