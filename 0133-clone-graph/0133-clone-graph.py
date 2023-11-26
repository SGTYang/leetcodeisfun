"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Time: O(n)
        # Space:
        visited = {}
        def dfs(root):
            if root in visited:
                return visited[root]
            
            curr = Node(root.val)
            visited[root] = curr
            
            neighbor = []
            for nei in root.neighbors:
                neighbor.append(dfs(nei))
            
            curr.neighbors = neighbor
            
            return curr
        
        return dfs(node) if node else None
        