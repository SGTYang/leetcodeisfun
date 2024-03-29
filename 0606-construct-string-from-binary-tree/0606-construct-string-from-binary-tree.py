# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):            
            res.append(str(node.val))
            
            if node.left:
                res.append("(")
                dfs(node.left)
                res.append(")")
            elif not node.left and node.right:
                res.append("()")
                
            if node.right:
                res.append("(")
                dfs(node.right)
                res.append(")")
                
        
        dfs(root)
        return "".join(res)
            