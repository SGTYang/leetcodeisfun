# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = defaultdict(int)
        odd = [0]
        def dfs(node):
            if not node:
                return 0
            
            count[node.val] += 1
            if count[node.val] % 2 != 0:
                odd_change = 1
            else:
                odd_change = -1
            odd[0] += odd_change
            
            if not node.left and not node.right:
                if odd[0] == 1 or odd[0] == 0:
                    res = 1
                else:
                    res = 0
            else:
                res = dfs(node.left) + dfs(node.right)
            
            odd[0] -= odd_change
            count[node.val] -= 1
            
            return res
        
        return dfs(root)