# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, curr_sum, path):
            if not node:
                return 
            if curr_sum + node.val == targetSum and (not node.left and not node.right):
                res.append(path+[node.val])
            
            dfs(node.left, curr_sum+node.val, path+[node.val])
            dfs(node.right, curr_sum+node.val, path+[node.val])

        dfs(root, 0, [])
        return res