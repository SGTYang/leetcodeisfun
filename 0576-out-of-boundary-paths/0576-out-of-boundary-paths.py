class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        
        dp = {}
        
        def dfs(r, c, move):
            if (r, c, move) in dp:
                return dp[(r, c, move)]
            
            if move > maxMove:
                return 0
            
            if r < 0 or c < 0 or r == m or c == n:
                return 1

            res = (dfs(r + 1, c, move + 1) % MOD +
                    dfs(r - 1, c, move + 1) % MOD +
                    dfs(r, c + 1, move + 1) % MOD +
                    dfs(r, c - 1, move + 1) % MOD)
            
            dp[(r, c, move)] = res % MOD
            return dp[(r, c, move)]
        
        return dfs(startRow, startColumn, 0)