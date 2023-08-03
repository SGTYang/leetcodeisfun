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
        res = []
        history = {}
        def dfs_parent(node, prev):
            if not node:
                return
            history[node] = prev
            
            dfs_parent(node.left, node)
            dfs_parent(node.right, node)
        
        visited = set()
        def dfs_dist(node, distance):
            if not node or node in visited:
                return
            if distance == k:
                res.append(node.val)
            visited.add(node)
            
            dfs_dist(node.left, distance + 1)
            dfs_dist(node.right, distance + 1)
            dfs_dist(history[node], distance +1)
            
        dfs_parent(root, None)
        dfs_dist(target, 0)
        
        return res