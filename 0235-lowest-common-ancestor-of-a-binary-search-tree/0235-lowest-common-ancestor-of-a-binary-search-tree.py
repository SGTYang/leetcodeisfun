# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Using BST
        if not root:
            return None
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p ,q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p ,q)
        else:
            return root
        
        
        # Brute force
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left or right