class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n! * n)
        # Space: O(n!)
        res = []
        visited = set()
        
        def dfs(idx, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    curr.append(nums[i])
                    dfs(i, curr)
                    curr.pop()
                    visited.remove(i)
            
            return
        
        dfs(0, [])
        return res