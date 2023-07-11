# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def recursive(num_list):
            nums_dict = {v:i for i, v in enumerate(num_list)}
            if not num_list:
                return None
            root = max(num_list)
            tree = TreeNode(root)
            
            tree.left = recursive(num_list[:nums_dict[root]])
            tree.right = recursive(num_list[nums_dict[root]+1:])
            
            return tree
        
        return recursive(nums)