# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(nums):
            if not nums:
                return
            max_value = max(nums) # O(n)
            max_index = nums.index(max_value) # O(n)
            
            root = TreeNode(max_value)
            root.left = build_tree(nums[0:max_index])
            root.right = build_tree(nums[max_index + 1:len(nums)])
            
            return root
        
        return build_tree(nums)