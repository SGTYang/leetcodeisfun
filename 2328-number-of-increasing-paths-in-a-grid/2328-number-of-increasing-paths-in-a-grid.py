class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        d = []
        for i in range(m):
            for j in range(n):
                d.append((grid[i][j],i,j))

        d = sorted(d)
        dp = [[1]*n for i in range(m)]
        ans = 0
        m1 = 10**9+7
        for (key,i,j) in d:
            if (i-1>=0):
                if grid[i][j] > grid[i-1][j]:
                    dp[i][j] += dp[i-1][j]
            if j-1>=0:
                if grid[i][j] > grid[i][j-1]:
                    dp[i][j] += dp[i][j-1]
            if i+1<m:
                if grid[i][j] > grid[i+1][j]:
                    dp[i][j] += dp[i+1][j]
            if j+1<n:
                if grid[i][j] > grid[i][j+1]:
                    dp[i][j] += dp[i][j+1]
            ans = (ans+dp[i][j])%m1
        return ans