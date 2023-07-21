# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que = deque([(root, 0)])
        res = 0
        
        while que:
            n = len(que)
            nodes = []
            
            for _ in range(n):
                node, idx = que.popleft()
                nodes.append(idx)
                
                if node.left:
                    que.append((node.left, 2*idx + 1))
                
                if node.right:
                    que.append((node.right, 2*idx + 2))
            
            res = max(res, max(nodes)-min(nodes)+1)
        return res
