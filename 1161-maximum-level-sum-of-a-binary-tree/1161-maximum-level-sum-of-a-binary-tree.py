# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        que = deque([root])
        max_val = float('-inf')
        min_x = 0
        level = 1
        
        while que:
            n = len(que)
            curr = 0
            for _ in range(n):
                node = que.popleft()
                curr += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            if max_val < curr:
                min_x = level
                max_val = curr
            level += 1
        
        return min_x