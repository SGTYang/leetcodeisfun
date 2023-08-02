# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
        
#         # Wrong answer for some how
#         if not root:
#             return root
#         def dfs(node):
#             if node.val < min(p.val, q.val):
#                 dfs(node.right)
#             elif node.val > max(p.val, q.val):
#                 dfs(node.left)
#             else:
#                 return node
        
#         return dfs(root)