"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        que = deque([root])
        res = []
        
        while que:
            prev = []
            for _ in range(len(que)):
                node = que.popleft()
                
                if len(prev) != 0:
                    prev_node = prev.pop()
                    prev_node.next = node
                    
                prev.append(node)
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            node.next = None
        
        return root