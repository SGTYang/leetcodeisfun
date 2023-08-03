# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def tree(preo, ino):
            if not preo or not ino:
                return None
            mid = ino.index(preo[0])
            root = TreeNode(preo[0])
            root.left = tree(preo[1:mid + 1], ino[:mid])
            root.right = tree(preo[mid + 1:], ino[mid + 1:])
            
            return root
        
        return tree(preorder, inorder)