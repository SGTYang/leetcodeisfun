class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (-1, -2), (-2, -1), (1, -2), (-2, 1)] 
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp_prev = [[0 for _ in range(n)] for _ in range(n)]
        dp_prev[row][column] = 1

        for step in range(k):
            for r in range(n):
                for c in range(n):
                    dp[r][c] = 0
                    for dr, dc in moves:
                        prev_r, prev_c = r - dr, c - dc
                        if 0 <= prev_r < n and 0 <= prev_c < n:
                            dp[r][c] += dp_prev[prev_r][prev_c] / 8.0
            dp, dp_prev = dp_prev, dp 

        total_probability = sum(sum(dp_prev[r][c] for c in range(n)) for r in range(n))
        return total_probability