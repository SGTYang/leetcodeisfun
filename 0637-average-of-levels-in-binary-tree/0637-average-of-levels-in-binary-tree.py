# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        que = deque([])
        que.append([root])
        
        while que:
            node_list = que.popleft()
            temp = []
            val_sum = 0
            for node in node_list:
                val_sum += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if len(temp) != 0:
                que.append(temp)
            res.append(val_sum/len(node_list))
        
        return res