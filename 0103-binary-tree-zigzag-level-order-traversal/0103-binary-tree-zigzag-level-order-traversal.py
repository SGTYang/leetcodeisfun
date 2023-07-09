# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        que = deque([root])
        left_to_right = True
        
        while que:
            curr = []
            
            for _ in range(len(que)):
                node = que.popleft()
                
                if left_to_right:
                    curr.append(node.val)
                else:
                    curr = [node.val] + curr
                    
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                    
            left_to_right = not left_to_right
            res.append(curr)    
        
        return res
        