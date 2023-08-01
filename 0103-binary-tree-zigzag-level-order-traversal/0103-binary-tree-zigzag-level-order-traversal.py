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
        que = deque([(root, 1)])
        while que:
            n = len(que)
            level_node = []
            for _ in range(n):
                node, level = que.popleft()
                level_node.append(node.val)
                if node.left:
                    que.append((node.left, level + 1))
                if node.right:
                    que.append((node.right, level + 1))
            
            if level % 2 == 0:
                res.append(level_node[::-1])
            else:
                res.append(level_node)
        
        return res