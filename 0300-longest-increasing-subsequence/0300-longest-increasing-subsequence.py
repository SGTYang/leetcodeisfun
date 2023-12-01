class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Time: O(n^2)
        # Space: O(n)
        dp = [1] * len(nums)
        dp[-1] = 1
        
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)   
        
        return max(dp)