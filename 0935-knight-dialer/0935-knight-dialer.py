class Solution:
    def knightDialer(self, n: int) -> int:
        dp = {}
        MOD = 10**9 + 7
        dial = [
            [1, 2, 3], 
            [4, 5, 6],
            [7, 8, 9],
            ["*", 0, "#"],
        ]
        rows, cols = len(dial), len(dial[0])
        
        def dfs(i, j, cnt):
            if i < 0 or j < 0 or i >= rows or j >= cols or dial[i][j] in ["*", "#"]:
                return 0
            
            if cnt == n:
                return 1
            
            if (i, j, cnt) in dp:
                return dp[(i, j, cnt)]
            
            dp[(i, j, cnt)] = (((((((dfs(i + 2, j + 1, cnt + 1) +
                         dfs(i + 2, j - 1, cnt + 1)) % MOD +
                         dfs(i - 2, j + 1, cnt + 1)) % MOD +
                         dfs(i - 2, j - 1, cnt + 1)) % MOD +
                         dfs(i + 1, j + 2, cnt + 1)) % MOD +
                         dfs(i + 1, j - 2, cnt + 1)) % MOD +
                         dfs(i - 1, j + 2, cnt + 1)) % MOD +
                         dfs(i - 1, j - 2, cnt + 1)) % MOD
                    
            return dp[(i, j, cnt)]
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                res = (res + dfs(r, c, 1)) % MOD

        return res