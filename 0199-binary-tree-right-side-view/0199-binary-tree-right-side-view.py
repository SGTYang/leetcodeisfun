# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        que = deque([root])
        
        while que:
            n = len(que)
            for _ in range(n):
                node = que.popleft()
                side = node.val
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                    
            res.append(side)
        
        return res