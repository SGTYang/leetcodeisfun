class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n*2^n) -> n for subset.copy()
        # Space: O(n)
        nums.sort()
        res = []
        curr = []
        def dfs(idx):
            if idx == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[idx])
            dfs(idx + 1)
            curr.pop()
            
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            dfs(idx + 1)
        
        dfs(0)
        return res 