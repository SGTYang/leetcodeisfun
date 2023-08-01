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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        que = deque([root])
        while que:
            n = len(que)
            level_node = []
            for i in range(n):
                node = que.popleft()
                if len(level_node) != 0:
                    prev = level_node.pop()
                    prev.next = node
                    
                level_node.append(node)
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            node.next = None
        
        return root