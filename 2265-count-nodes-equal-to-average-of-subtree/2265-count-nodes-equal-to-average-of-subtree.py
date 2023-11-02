# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(node):
            if not node:
                return (0, 0)
            
            left_total_sum, left_total_cnt = dfs(node.left) 
            right_total_sum, right_total_cnt = dfs(node.right)
            
            total = left_total_sum + right_total_sum + node.val 
            cnt = left_total_cnt + right_total_cnt + 1
            
            if node.val == total//cnt:
                res[0] += 1
            
            return (total, cnt)
        
        dfs(root)
        return res[0]