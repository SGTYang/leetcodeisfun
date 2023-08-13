class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n! * n)
        # Space: O(n!)
        res = []
        visited = set()
        curr = []
        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    curr.append(num)
                    dfs()
                    visited.remove(num)
                    curr.pop()
        dfs()
        
        return res
            
            