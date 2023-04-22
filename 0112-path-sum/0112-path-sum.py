# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, val):
            if not node:
                return False
            
            val += node.val
            if not node.left and not node.right:
                return val == targetSum
            
            return dfs(node.left, val) or dfs(node.right, val)
        
        return dfs(root, 0)