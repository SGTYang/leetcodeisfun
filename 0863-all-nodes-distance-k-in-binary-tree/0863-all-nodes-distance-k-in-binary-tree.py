# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        
        history = {}
        res = []
        visited = set()
        
        def dfs_parent(node, parent):
            if not node:
                return
            
            history[node] = parent
            
            dfs_parent(node.left, node)
            dfs_parent(node.right, node)
            
        def dfs_dist(node, distance):
            if not node or node.val in visited:
                return
            visited.add(node.val)
            
            if distance == k:
                res.append(node.val)
            
            dfs_dist(node.left, distance+1)
            dfs_dist(node.right, distance+1)
            dfs_dist(history[node], distance+1)
            
            return
        
        dfs_parent(root, None)
        dfs_dist(target, 0)
        
        return res
                