class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m=len(group)
        dp=[[[0]*(minProfit+1) for _ in range(n+1)] for _ in range(m+1)]
        for j in range(n+1):
            dp[m][j][0]=1

        for i in range(m-1,-1,-1):
            for j in range(n+1):
                for k in range(minProfit+1):
                    dp[i][j][k]=dp[i+1][j][k]
                    if group[i]<=j:
                        dp[i][j][k]+=dp[i+1][j-group[i]][max(0,k-profit[i])]
                    dp[i][j][k]%=10**9+7

        return dp[0][n][minProfit]