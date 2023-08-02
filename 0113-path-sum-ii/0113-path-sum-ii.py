# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        
        def dfs(node, total, history):
            if not node:
                return
            
            if total + node.val == targetSum and not node.left and not node.right :
                res.append(history + [node.val])
                return
            
            dfs(node.left, total + node.val, history + [node.val])
            dfs(node.right, total + node.val, history + [node.val])
            
        dfs(root, 0, [])
        return res