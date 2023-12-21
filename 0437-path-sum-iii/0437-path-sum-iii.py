# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(node, s):
            if not node:
                return 0
            
            cnt = 0
            for i in range(len(s)):
                s[i] += node.val
                if s[i] == targetSum:
                    cnt += 1
            
            if node.val == targetSum:
                cnt += 1
            
            left = dfs(node.left, s + [node.val])
            right = dfs(node.right, s + [node.val])
            
            return left + right + cnt
        
        return dfs(root, [])