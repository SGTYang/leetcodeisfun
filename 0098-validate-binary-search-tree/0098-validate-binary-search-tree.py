# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder
        
        output = []
        
        def dfs(node, output):
            if not node:
                return
            
            dfs(node.left, output)
            output += [node.val]
            dfs(node.right, output)
            
            return
        
        dfs(root, output)
        
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False
        return True