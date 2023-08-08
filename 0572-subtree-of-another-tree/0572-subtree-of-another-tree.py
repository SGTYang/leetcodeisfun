# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(node, sub):
            if not node and not sub:
                return True
            if node and sub and node.val == sub.val:
                return is_same(node.left, sub.left) and is_same(node.right, sub.right)
            return False
        
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if is_same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)