# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Time: O(n^2)
        # Space: O(n)
        res = [0]
        
        def dfs(node, history):
            if not node:
                return
            
            for i in range(len(history)):
                history[i] += node.val
                if history[i] == targetSum:
                    res[0] += 1
                    
            if node.val == targetSum:
                res[0] += 1
                
            dfs(node.left, history + [node.val])
            dfs(node.right, history + [node.val])
        
        dfs(root, [])
        
        return res[0]
            