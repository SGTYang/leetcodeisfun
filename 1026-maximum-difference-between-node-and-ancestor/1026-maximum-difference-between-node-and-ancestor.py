# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(node, min_v, max_v):
            if not node:
                return
            
            curr = max(abs(min_v - node.val), abs(max_v - node.val))
            
            res[0] = max(res[0], curr)
            
            dfs(node.left, min(min_v, node.val), max(max_v, node.val))
            dfs(node.right, min(min_v, node.val), max(max_v, node.val))
        
        dfs(root, root.val, root.val)
        
        return res[0]