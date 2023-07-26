class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0:1}
        
        for i in range(1, target + 1):
            total = 0
            for num in nums:
                total += dp.get(i - num, 0)
            dp[i] = total
        
        return dp[target]