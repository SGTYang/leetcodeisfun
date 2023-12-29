class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        l = len(jobDifficulty)
        if l < d: return -1

        dp = [[float('inf')]*l+[0] for _ in range(d+1)]

        for day in range(1,d+1):
            right = l - day + 1
            for cut in range(right):
                maxsofar = 0
                ans = float('inf')
                for j in range(cut, right):
                    maxsofar = max(maxsofar, jobDifficulty[j])
                    ans = min(ans, maxsofar+dp[day-1][j+1])
                dp[day][cut] = ans
        
        return dp[d][0]