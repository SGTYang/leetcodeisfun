class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Greedy
        goal = len(nums)-1
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i]+i >= goal:
                goal = i
        
        return True if goal == 0 else False
            
        #DP
        dp = [False]*len(nums)
        dp[-1] = True
        
        for i in range(len(nums)-2, -1, -1):
            for j in range(i,nums[i]+i+1):
                if dp[j]:
                    dp[i] = True
                    break
        
        return dp[0]