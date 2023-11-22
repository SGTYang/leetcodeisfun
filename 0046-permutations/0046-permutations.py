class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n! * n)
        # Space: O(n!)
        res = []
        def dfs(idx, curr, visited):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if i not in visited:
                    curr.append(nums[i])
                    visited.add(i)
                    dfs(i, curr, visited)
                    curr.pop()
                    visited.remove(i)
        
        dfs(0, [], set())
        
        return res