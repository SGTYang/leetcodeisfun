class Solution:
    def rob(self, nums: List[int]) -> int:
        # [rob1, rob2, n, n+1, ...]
        l = len(nums)
        if l < 3: return max(nums)
        dp = [0]*l
        dp[0], dp[1], dp[2] = nums[0], nums[1],  nums[0]+nums[2]

        for i in range(3,l):
            dp[i] = max(dp[i-3], dp[i-2])+nums[i]
        
        return max(dp[-1], dp[-2])