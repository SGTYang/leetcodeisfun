# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        prev = {}

        def find_start(node):
            if not node:
                return 

            if node.val == start:
                return node
            
            prev[node.left] = node
            prev[node.right] = node

            left = find_start(node.left)
            right = find_start(node.right)

            return left or right

        start = find_start(root)

        que = deque([])
        visited = set()
        que.append(start)
        visited.add(start.val)
        res = -1

        while que:
            n = len(que)
            for _ in range(n):
                node = que.popleft()
                visited.add(node.val)

                if node.left and node.left.val not in visited:
                    que.append(node.left)
                if node.right and node.right.val not in visited:
                    que.append(node.right)
                if node in prev and prev[node].val not in visited:
                    que.append(prev[node])
            
            res += 1
        
        return res