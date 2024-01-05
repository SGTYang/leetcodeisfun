class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Time: O(n^2)
        # Space: O(n)
        
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)