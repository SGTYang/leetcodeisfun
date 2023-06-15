# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = defaultdict(int)
        que = deque([(root, 1)])
        res = 0 
        while que:
            node, level = que.popleft()
            
            level_sum[level] += node.val
            
            if node.left:
                que.append([node.left, level+1])
            if node.right:
                que.append([node.right, level+1])
        
        max_val = float("-inf")
        
        for level, val_sum in level_sum.items():
            print(level, val_sum)
            if max_val < val_sum:
                res = level
                max_val = val_sum
        
        return res