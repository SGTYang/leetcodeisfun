# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        node = preorder[0]
        node_index = inorder.index(node)
        
        root = TreeNode(node)
        root.left = self.buildTree(preorder[1:node_index + 1], inorder[:node_index])
        root.right = self.buildTree(preorder[node_index + 1:], inorder[node_index + 1:])
        
        return root