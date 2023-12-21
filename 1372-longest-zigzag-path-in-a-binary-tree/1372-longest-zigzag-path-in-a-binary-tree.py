# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(node, curr, is_right):
            if not node:
                return 
            
            res[0] = max(res[0], curr)
            
            if is_right:
                dfs(node.left, curr + 1, False)
                dfs(node.right, 1, True)
            else:
                dfs(node.left, 1, False)
                dfs(node.right, curr + 1, True)
                
        dfs(root.right, 1, True)
        dfs(root.left, 1, False)
        return res[0]