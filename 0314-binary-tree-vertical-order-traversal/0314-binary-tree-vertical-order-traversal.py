# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lowest = [0]
        highest = [0]
        save = defaultdict(list)
        
        def dfs(node, r, c):
            if not node:
                return
            
            save[c].append([r, node.val])
            lowest[0] = min(lowest[0], c - 1)
            highest[0] = max(highest[0], c + 1)
            dfs(node.left, r + 1, c - 1)
            dfs(node.right, r + 1, c + 1)
        
        dfs(root, 0, 0)
        res = []
        
        while lowest < highest:
            if lowest[0] in save:
                save[lowest[0]].sort(key = lambda x : x[0])
                tmp = []
                for r, v in save[lowest[0]]:
                    tmp.append(v)
                res.append(tmp)
            lowest[0] += 1
        
        return res