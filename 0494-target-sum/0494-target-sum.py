class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def backtrack(idx, total):
            if idx == len(nums):
                return 1 if total == target else 0
            if (idx, total) in dp:
                return dp[(idx, total)]
            
            dp[(idx, total)] = (backtrack(idx+1, total+nums[idx]) + 
                               backtrack(idx+1, total-nums[idx]))
            
            return dp[(idx, total)]
        
        return backtrack(0,0)
    
        res = [0]
        
        def backtrack(idx, total):
            if idx == len(nums) and total == target:
                res[0] += 1
                return
            if idx >= len(nums):
                return
            
            backtrack(idx+1, total+nums[idx])
            backtrack(idx+1, total-nums[idx])

        backtrack(0,0)
        return res[0]