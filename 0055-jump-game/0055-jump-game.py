class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal =  i
        return True if goal == 0 else False
        
        dp = [False] * len(nums)
        dp[-1] = True
        
        for i in range(len(nums)-2, -1, -1):
            for j in range(i + 1, i + nums[i] + 1):
                if dp[j]:
                    dp[i] = True
                    break
        
        return dp[0]