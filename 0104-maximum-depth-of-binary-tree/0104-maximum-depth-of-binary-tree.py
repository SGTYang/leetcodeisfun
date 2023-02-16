# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        que = deque()
        
        if root:
            que.append([root,1])
        
        while que:
            node, depth = que.popleft()
            res = max(res, depth)
            
            if node.left:
                que.append([node.left, depth+1])
            if node.right:
                que.append([node.right, depth+1])
        
        return res