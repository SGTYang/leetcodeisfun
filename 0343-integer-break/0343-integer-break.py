class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for num in range(4, n + 1):
            max_num = 0
            for sub_num in range(1, num // 2 + 1):
                max_num = max(max_num, dp[sub_num] * dp[num - sub_num])
            dp[num] = max_num

        return dp[n]