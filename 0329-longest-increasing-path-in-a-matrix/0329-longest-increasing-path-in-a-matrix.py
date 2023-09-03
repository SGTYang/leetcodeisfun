class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = {}
        
        def dfs(r, c, prev):
            if r < 0 or c < 0 or r == m or c == n or matrix[r][c] <= prev:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = max(
                dfs(r + 1, c, matrix[r][c]),
                dfs(r - 1, c, matrix[r][c]),
                dfs(r, c + 1, matrix[r][c]),
                dfs(r, c - 1, matrix[r][c])) + 1
            
            dp[(r, c)] = res
            return dp[(r, c)]
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(dfs(i, j, -1), res)
        
        return res
                