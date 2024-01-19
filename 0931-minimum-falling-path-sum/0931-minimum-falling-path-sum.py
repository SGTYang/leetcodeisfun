class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        dp[0] = matrix[0].copy()
        for i in range(1,ROWS):
            for j in range(COLS):
                if j == 0:
                    dp[i][j] = matrix[i][j]+min(dp[i-1][j], dp[i-1][j+1])
                elif j == COLS-1:
                    dp[i][j] = matrix[i][j]+min(dp[i-1][j], dp[i-1][j-1])
                else:
                    dp[i][j] = matrix[i][j]+min(dp[i-1][j], dp[i-1][j+1], dp[i-1][j-1])
        
        return min(dp[-1])