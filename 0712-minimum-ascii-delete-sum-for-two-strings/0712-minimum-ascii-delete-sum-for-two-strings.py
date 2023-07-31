class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        for i in range(len(s1)-1,-1,-1):
            for j in range(len(s2)-1,-1,-1):
                if s1[i] == s2[j]:
                    dp[i][j] = ord(s1[i]) + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])                    
        total = 0
        for c in s1:
            total += ord(c)
        for c in s2:
            total += ord(c)
        return total - dp[0][0]*2