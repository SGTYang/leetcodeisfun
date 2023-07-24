class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Time: O(2^n)
        # Space: O(n)
        nums.sort()
        res = []
        
        def dfs(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset += [nums[i]]
            dfs(i + 1, subset)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                
            dfs(i + 1, subset)
            
        dfs(0, [])
        return res